"""
content_classifier.py — DBA Content Relevance Classifier

Classifies extracted page content into DBA knowledge tiers and
structural content types based on heading patterns and section context.

Each section from the TOC maps to:
  - A DBA tier (1=Daily Toolkit, 2=Performance, 3=BCDR, 4=Admin, 5=Reference)
  - A content type (dmv, function, wait_type, error_code, tsql_command, narrative)
  - Structural sub-types (syntax_block, argument_table, permission_block, example)
"""

import json
import re
from pathlib import Path
from typing import Any, Optional

# Mapping of section keywords to DBA tiers and content types
SECTION_CLASSIFICATION = {
    # Tier 1: Daily DBA Toolkit
    "system dynamic management views": {"tier": 1, "content_type": "dmv", "label": "DMV"},
    "system catalog views": {"tier": 1, "content_type": "catalog_view", "label": "Catalog View"},
    "system compatibility views": {"tier": 1, "content_type": "compatibility_view", "label": "Compat View"},
    "dbcc": {"tier": 1, "content_type": "dbcc_command", "label": "DBCC"},
    "system tables": {"tier": 1, "content_type": "system_table", "label": "System Table"},

    # Tier 2: Performance Tuning
    "query store": {"tier": 2, "content_type": "performance", "label": "Query Store"},
    "execution plans": {"tier": 2, "content_type": "performance", "label": "Execution Plan"},
    "index architecture": {"tier": 2, "content_type": "architecture", "label": "Index Architecture"},
    "query processing": {"tier": 2, "content_type": "architecture", "label": "Query Processing"},
    "lock": {"tier": 2, "content_type": "architecture", "label": "Locking"},
    "memory management": {"tier": 2, "content_type": "architecture", "label": "Memory"},
    "latch contention": {"tier": 2, "content_type": "architecture", "label": "Latch Contention"},
    "spinlock contention": {"tier": 2, "content_type": "architecture", "label": "Spinlock"},
    "statistics": {"tier": 2, "content_type": "performance", "label": "Statistics"},
    "resource governor": {"tier": 2, "content_type": "performance", "label": "Resource Governor"},

    # Tier 3: High Availability & BCDR
    "backup": {"tier": 3, "content_type": "bcdr", "label": "Backup"},
    "restore": {"tier": 3, "content_type": "bcdr", "label": "Restore"},
    "availability group": {"tier": 3, "content_type": "bcdr", "label": "Availability Group"},
    "failover cluster": {"tier": 3, "content_type": "bcdr", "label": "Failover Cluster"},
    "log shipping": {"tier": 3, "content_type": "bcdr", "label": "Log Shipping"},
    "database mirroring": {"tier": 3, "content_type": "bcdr", "label": "Database Mirroring"},

    # Tier 4: Administration & Security
    "security": {"tier": 4, "content_type": "security", "label": "Security"},
    "system stored procedures": {"tier": 4, "content_type": "stored_procedure", "label": "System SP"},
    "system functions": {"tier": 4, "content_type": "function", "label": "System Function"},
    "configuration": {"tier": 4, "content_type": "config", "label": "Configuration"},
    "trace flags": {"tier": 4, "content_type": "config", "label": "Trace Flag"},

    # Tier 5: Reference
    "transact-sql": {"tier": 5, "content_type": "tsql_reference", "label": "T-SQL Reference"},
    "errors & events": {"tier": 5, "content_type": "error", "label": "Error Code"},
    "xquery": {"tier": 5, "content_type": "tsql_reference", "label": "XQuery"},
    "data types": {"tier": 5, "content_type": "tsql_reference", "label": "Data Type"},
    "functions": {"tier": 5, "content_type": "function", "label": "Function"},
    "language elements": {"tier": 5, "content_type": "tsql_reference", "label": "Language Element"},
    "queries": {"tier": 5, "content_type": "tsql_reference", "label": "Query"},
    "statements": {"tier": 5, "content_type": "tsql_reference", "label": "Statement"},

    # Architecture & Narrative
    "internals & architecture": {"tier": 2, "content_type": "narrative", "label": "Architecture"},
    "what is sql server": {"tier": 5, "content_type": "narrative", "label": "Overview"},
}

# Content structure patterns — used to identify sub-sections within pages
STRUCTURE_PATTERNS = {
    "syntax": re.compile(r"^(syntax|arguments?|permissions?|returns?|remarks?|examples?|best practices?)", re.IGNORECASE),
    "argument_table": re.compile(r"^(table|column|argument|parameter)", re.IGNORECASE),
    "permission": re.compile(r"permissions?", re.IGNORECASE),
    "note": re.compile(r"^(note|important|caution|warning|tip)", re.IGNORECASE),
    "see_also": re.compile(r"see also", re.IGNORECASE),
}


def classify_section(section_name: str) -> dict[str, Any]:
    """Classify a section by its name."""
    sn = section_name.lower().strip()
    for keyword, classification in SECTION_CLASSIFICATION.items():
        if keyword in sn:
            return dict(classification)
    return {"tier": 5, "content_type": "unknown", "label": "Unclassified"}


def classify_page_content(
    headings: list[dict[str, Any]],
    code_blocks: list[str],
    page_text: str,
) -> dict[str, Any]:
    """
    Analyze page structure to identify content sub-types.

    Returns:
        Dict with structural flags and detected patterns.
    """
    result = {
        "has_syntax_block": False,
        "has_argument_table": False,
        "has_permission_block": False,
        "has_note_block": False,
        "has_examples": False,
        "structure_type": None,
    }

    # Check headings for structural patterns
    for h in headings:
        text = h["text"].strip()
        for pname, pattern in STRUCTURE_PATTERNS.items():
            if pattern.search(text):
                result[f"has_{pname}_block"] = True

    # Check code blocks for syntax indicators
    for cb in code_blocks:
        first_line = cb.split("\n")[0].strip().upper()
        if any(first_line.startswith(kw) for kw in ["SELECT", "CREATE", "ALTER", "DROP", "INSERT", "UPDATE", "DELETE", "BACKUP", "RESTORE", "DBCC", "SET", "DECLARE", "BEGIN", "EXEC", "GRANT", "DENY", "REVOKE"]):
            result["has_syntax_block"] = True
            break

    # Determine primary structure type
    if result["has_syntax_block"] and result["has_argument_table"]:
        result["structure_type"] = "reference_item"
    elif result["has_note_block"]:
        result["structure_type"] = "best_practice"
    elif result["has_syntax_block"]:
        result["structure_type"] = "syntax_reference"
    else:
        result["structure_type"] = "narrative"

    return result


def generate_description(
    headings: list[dict[str, Any]],
    paragraphs: list[dict[str, Any]],
    max_chars: int = 150,
) -> str:
    """Generate a 150-char excerpt from first meaningful paragraph."""
    # Try H2/H3 text as description foundation
    for h in headings:
        if h["level"] in (2, 3) and len(h["text"]) > 10:
            base = h["text"]
            if len(base) > max_chars:
                return base[:max_chars - 3] + "..."
            return base

    # Fall back to first substantial paragraph
    for p in paragraphs:
        text = p["text"].strip()
        if len(text) > 30:
            if len(text) > max_chars:
                return text[:max_chars - 3] + "..."
            return text

    return ""


def generate_slug(title: str) -> str:
    """Generate a URL-safe slug from a title."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


if __name__ == "__main__":
    # Test classification
    test_sections = [
        "System Dynamic Management Views",
        "System Catalog Views",
        "Backup & Restore",
        "Transact-SQL (T-SQL) Reference",
        "Security",
        "Internals & Architecture",
        "DBCC",
    ]
    print("[content_classifier] Section classification test:")
    for s in test_sections:
        cls = classify_section(s)
        print(f"  {s:>45} -> Tier {cls['tier']} {cls['content_type']:>20} [{cls['label']}]")
