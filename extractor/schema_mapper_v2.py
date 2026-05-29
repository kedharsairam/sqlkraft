"""
schema_mapper_v2.py — Multi-Type Content Collection Generator

Handles all 9 Astro content collection types:
  - DMVs (existing, improved)
  - Error Codes
  - Catalog Views
  - System Functions
  - Stored Procedures
  - T-SQL Reference
  - Architecture / Narrative
  - Wait Statistics (programmatic)
  - Scripts

For each batch JSON file (from page_extractor Phase B), detects the
content type from the filename prefix and applies the appropriate parser.
"""

import json
import re
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Any, Optional


# ──────────────────────────────────────────────────
# Pattern detection
# ──────────────────────────────────────────────────

# SQL Server object name patterns
CATALOG_VIEW_PATTERN = re.compile(r"(sys\.\w+)", re.IGNORECASE)
ERROR_NUMBER_PATTERN = re.compile(r"(\d{4,5})")
FUNCTION_PATTERN = re.compile(r"(sys\.(?:fn_|sp_))", re.IGNORECASE)

# Heading text blocklist (table headers, structural noise)
HEADING_BLOCKLIST = {
    "expand table", "applies to:", "important", "note", "caution",
    "warning", "tip", "see also", "related content", "required permissions",
    "description", "feedback", "in this article", "prerequisites",
    "next steps", "quickstart", "column name", "data type", "column_name",
    "data_type", "permissions for sql server", "sql", "resource",
    "severity", "error", "event logged", "lock mode", "attribute",
    "wait type", "waiting tasks count", "wait time",
}

# Section → collection name mapping
SECTION_COLLECTION_MAP = {
    "system-dmvs": "dmvs",
    "errors": "errors",
    "system-catalog-views": "catalog-views",
    "system-functions": "functions",
    "architecture": "architecture",
    "tsql-reference": "tsql-reference",
}


# ──────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────

def generate_slug(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


def clean_text(text: str) -> str:
    """Remove non-breaking spaces and normalize whitespace."""
    text = text.replace("\u00a0", " ").replace("\xa0", " ")
    return " ".join(text.split())


def extract_first_paragraph(paragraphs: list[dict], min_len: int = 30, max_len: int = 200) -> str:
    """Extract first meaningful paragraph as description."""
    for p in paragraphs:
        t = clean_text(p.get("text", "")).strip()
        if len(t) >= min_len:
            if len(t) > max_len:
                return t[:max_len - 3] + "..."
            return t
    return ""


def is_heading_noise(text: str) -> bool:
    """Check if heading text should be ignored."""
    tl = text.strip().lower()
    if tl in HEADING_BLOCKLIST:
        return True
    for b in HEADING_BLOCKLIST:
        if tl.startswith(b):
            return True
    return False


def build_frontmatter(fields: dict) -> str:
    """Build YAML frontmatter string."""
    lines = ["---"]
    for key, value in fields.items():
        if value is None or (isinstance(value, (list, dict)) and not value):
            continue
        if isinstance(value, datetime):
            lines.append(f'{key}: {value.strftime("%Y-%m-%d")}')
        elif isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        elif isinstance(value, (int, float)):
            lines.append(f"{key}: {value}")
        elif isinstance(value, list):
            items = json.dumps(value)
            lines.append(f"{key}: {items}")
        else:
            # Use single quotes for YAML strings — avoids escape interpretation
            sv = str(value).replace("'", "''")
            lines.append(f"{key}: '{sv}'")
    lines.append("---")
    return "\n".join(lines)


def build_markdown_body(paragraphs: list[dict], code_blocks: list[str]) -> str:
    """Build markdown body from extracted page content."""
    body_parts = []
    for p in paragraphs:
        text = clean_text(p.get("text", "")).strip()
        if not text:
            continue
        # Detect section headings embedded in paragraphs
        if len(text) < 100 and re.match(
            r"^(Syntax|Arguments|Returns|Remarks|Permissions|Examples|Best Practice|Remarks|Description)",
            text, re.IGNORECASE
        ):
            body_parts.append(f"\n## {text}\n")
        else:
            body_parts.append(text + "\n\n")
    for cb in code_blocks:
        body_parts.append(f"```sql\n{cb}\n```\n\n")
    result = "".join(body_parts).strip()
    return result or "*(Content pending extraction)*"


def write_content_file(output_dir: str, collection: str, slug: str, frontmatter: str, body: str) -> str:
    """Write a single content collection markdown file."""
    collection_dir = Path(output_dir) / collection
    collection_dir.mkdir(parents=True, exist_ok=True)
    filepath = collection_dir / f"{slug}.md"
    content = frontmatter + "\n\n" + body + "\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return str(filepath)


# ──────────────────────────────────────────────────
# DMV Parser (existing, ported from v1)
# ──────────────────────────────────────────────────

DMV_NAME_PATTERN = re.compile(r"(sys\.dm_[a-z_0-9]+)", re.IGNORECASE)

def is_valid_dmv_name(text: str) -> bool:
    return bool(DMV_NAME_PATTERN.match(text.strip()))


def parse_dmv_from_headings(headings: list[dict]) -> dict[str, Any]:
    dmv = {"name": "", "title": "", "description": "", "category": "execution", "tags": [], "permissions": ""}
    for h in headings:
        text = clean_text(h["text"])
        if h["level"] == 2 and not dmv["name"]:
            dmv["name"] = text
            dmv["title"] = text
        elif h["level"] == 3 and "permission" in text.lower():
            dmv["permissions"] = text
    name = dmv["name"]
    if is_valid_dmv_name(name):
        if name.startswith("sys.dm_exec_"):         dmv["category"] = "execution"
        elif name.startswith("sys.dm_os_"):          dmv["category"] = "os"
        elif name.startswith("sys.dm_db_index_") or name.startswith("sys.dm_db_missing_index"): dmv["category"] = "index"
        elif name.startswith("sys.dm_io_"):          dmv["category"] = "io"
        elif name.startswith("sys.dm_tran_"):        dmv["category"] = "transactions"
        elif name.startswith("sys.dm_db_xtp_"):      dmv["category"] = "in-memory"
        elif name.startswith("sys.dm_hadr_") or name.startswith("sys.dm_os_cluster"): dmv["category"] = "availability"
        dmv["tags"] = [dmv["category"]]
        for kw in ["requests", "sessions", "connections", "sql_text", "query_stats",
                    "wait_stats", "locks", "transactions", "memory", "schedulers",
                    "workers", "tasks", "threads", "index", "io", "buffer",
                    "databases", "log", "space"]:
            if kw in name.lower():
                dmv["tags"].append(kw)
    return dmv


def extract_dmv_name_from_lines(paragraphs: list[dict]) -> str:
    for p in paragraphs:
        text = p.get("text", "").strip()
        match = DMV_NAME_PATTERN.search(text)
        if match:
            return match.group(1)
    return ""


def process_dmv_batch(batch_file: str, content_output_dir: str) -> list[dict]:
    """Process DMV batch — identical logic to v1 schema_mapper."""
    with open(batch_file, "r", encoding="utf-8") as f:
        pages = json.load(f)
    records = []
    current_dmv = {}
    current_paragraphs = []
    current_code = []
    for page_data in pages:
        headings = page_data.get("headings", [])
        paragraphs = page_data.get("paragraphs", [])
        code_blocks = page_data.get("code_blocks", [])
        for h in headings:
            if h["level"] == 2:
                if current_dmv.get("name"):
                    rec = _flush_entry(current_dmv, current_paragraphs, current_code, content_output_dir, "dmvs")
                    if rec:
                        records.append(rec)
                    current_paragraphs = []
                    current_code = []
                current_dmv = parse_dmv_from_headings([h])
                if not is_valid_dmv_name(current_dmv.get("name", "")):
                    found = extract_dmv_name_from_lines(paragraphs)
                    if found:
                        current_dmv["name"] = found
                        current_dmv["title"] = found
            elif h["level"] == 3 and not is_heading_noise(h["text"]):
                current_paragraphs.append({"text": f"## {h['text']}", "font": "", "size": 0})
        current_paragraphs.extend(paragraphs)
        current_code.extend(code_blocks)
    if current_dmv.get("name"):
        rec = _flush_entry(current_dmv, current_paragraphs, current_code, content_output_dir, "dmvs")
        if rec:
            records.append(rec)
    return [r for r in records if r is not None]


# ──────────────────────────────────────────────────
# Error Codes Parser
# ──────────────────────────────────────────────────

ERROR_SEVERITY_MAP = {
    10: "info", 11: "low", 12: "low", 13: "low", 14: "low",
    15: "medium", 16: "medium", 17: "high", 18: "high",
    19: "critical", 20: "critical", 21: "critical", 22: "critical", 23: "critical", 24: "critical", 25: "critical",
}

ERROR_CATEGORIES = {
    "deadlock": "deadlock",
    "connection": "connection",
    "corruption": "corruption",
    "disk": "io",
    "io": "io",
    "query": "query-execution",
    "login": "authentication",
    "authentication": "authentication",
    "replication": "replication",
    "system": "system",
}

def map_error_severity(severity_num: int) -> str:
    return ERROR_SEVERITY_MAP.get(severity_num, "medium")


def infer_error_category(text: str) -> str:
    tl = text.lower()
    for keyword, cat in ERROR_CATEGORIES.items():
        if keyword in tl:
            return cat
    return "system"


def parse_error_entry(combined_text: str) -> Optional[dict]:
    """Parse a text block into an error entry.
    
    Error pages typically have rows like:
      Error: 18456  Severity: 14  Event logged: Yes  Description: Login failed...
    or table-like structures.
    """
    entry = {}
    
    # Try to extract error number
    num_match = re.search(r"(\d{4,5})", combined_text)
    if not num_match:
        return None
    
    entry["error_number"] = int(num_match.group(1))
    
    # Try to extract severity
    sev_match = re.search(r"Severity[:\s]+(\d+)", combined_text, re.IGNORECASE)
    if sev_match:
        entry["severity_num"] = int(sev_match.group(1))
        entry["severity"] = map_error_severity(entry["severity_num"])
    else:
        entry["severity"] = "medium"
    
    # Remove noise from the description
    desc = re.sub(r"Error[:\s]+\d+", "", combined_text, flags=re.IGNORECASE)
    desc = re.sub(r"Severity[:\s]+\d+", "", desc, flags=re.IGNORECASE)
    desc = re.sub(r"Event logged[:\s]*(Yes|No)", "", desc, flags=re.IGNORECASE)
    desc = desc.strip().strip(',').strip()
    
    if len(desc) < 10:
        return None
    
    # Use first 200 chars of description
    entry["description"] = desc[:200]
    entry["name"] = str(entry["error_number"])
    entry["title"] = f"Error {entry['error_number']}"
    entry["category"] = infer_error_category(desc)
    entry["tags"] = [entry["category"], f"severity-{entry['severity']}"]
    
    return entry


def process_errors_batch(batch_file: str, content_output_dir: str) -> list[dict]:
    """Process error batch pages — extract individual error entries."""
    with open(batch_file, "r", encoding="utf-8") as f:
        pages = json.load(f)
    
    records = []
    current_entry = None
    current_body = []
    seen_error_numbers = set()
    
    for page_data in pages:
        headings = page_data.get("headings", [])
        paragraphs = page_data.get("paragraphs", [])
        code_blocks = page_data.get("code_blocks", [])
        
        # Combine all text to find error entries
        full_text = ""
        for p in paragraphs:
            full_text += clean_text(p.get("text", "")) + " "
        for h in headings:
            full_text += clean_text(h.get("text", "")) + " "
        
        # Split by error number patterns to find individual entries
        # Error pages have densely packed entries
        error_blocks = re.split(r'(Error\s*:\s*\d{4,5}\s*)', full_text, flags=re.IGNORECASE)
        
        for block in error_blocks:
            entry = parse_error_entry(block)
            if entry and entry["error_number"] not in seen_error_numbers:
                seen_error_numbers.add(entry["error_number"])
                rec = flush_error_entry(entry, content_output_dir)
                if rec:
                    records.append(rec)
    
    return records


def flush_error_entry(entry: dict, output_dir: str) -> Optional[dict]:
    """Write an error entry content file."""
    slug = f"error-{entry['error_number']}"
    en = entry["error_number"]
    
    frontmatter_fields = {
        "name": str(en),
        "title": f"Error {en}",
        "errorNumber": en,
        "severity": entry["severity"],
        "category": entry["category"],
        "description": entry["description"][:200],
        "tags": entry["tags"],
        "pubDate": datetime.now(),
    }
    
    fm = build_frontmatter(frontmatter_fields)
    body = f"""## Description

{entry['description']}

## Severity

{entry['severity'].upper()} (Level {entry.get('severity_num', 'N/A')})

## Troubleshooting

*(Diagnostic content pending full extraction)*
"""
    
    filepath = write_content_file(output_dir, "errors", slug, fm, body)
    
    return {
        "slug": slug,
        "name": str(en),
        "title": entry["title"],
        "category": entry["category"],
        "tags": entry["tags"],
        "description": entry["description"][:150],
        "filepath": filepath,
        "collection": "errors",
    }


# ──────────────────────────────────────────────────
# Catalog Views Parser
# ──────────────────────────────────────────────────

CATEGORY_VIEW_CATEGORIES = {
    "databases": "databases-files", "files": "databases-files", "filegroups": "databases-files",
    "objects": "objects", "tables": "objects", "views": "objects", "columns": "objects",
    "index": "indexes", "indexes": "indexes",
    "partition": "partitions",
    "security": "security", "permissions": "security", "user": "security", "login": "security", "role": "security",
    "query_store": "query-store",
    "service_broker": "service-broker", "broker": "service-broker",
    "fulltext": "full-text", "full_text": "full-text",
    "config": "configuration", "configure": "configuration",
    "xml": "xml",
    "spatial": "spatial",
    "external": "external",
}

CATALOG_VIEW_NAME_PATTERN = re.compile(r"sys\.([a-z_0-9]+)", re.IGNORECASE)


def infer_catalog_category(name: str) -> str:
    name_lower = name.lower()
    for keyword, cat in CATEGORY_VIEW_CATEGORIES.items():
        if keyword in name_lower:
            return cat
    return "objects"


def process_catalog_views_batch(batch_file: str, content_output_dir: str) -> list[dict]:
    """Process catalog views batch — H1 headings are view names."""
    with open(batch_file, "r", encoding="utf-8") as f:
        pages = json.load(f)
    
    records = []
    current_view = {}
    current_paragraphs = []
    current_code = []
    
    for page_data in pages:
        headings = page_data.get("headings", [])
        paragraphs = page_data.get("paragraphs", [])
        code_blocks = page_data.get("code_blocks", [])
        
        for h in headings:
            text = clean_text(h["text"])
            if h["level"] == 1 and not is_heading_noise(text):
                # New view starts
                if current_view.get("name"):
                    rec = _flush_entry(current_view, current_paragraphs, current_code, content_output_dir, "catalog-views")
                    if rec:
                        records.append(rec)
                    current_paragraphs = []
                    current_code = []
                
                # Extract view name — MUST contain sys. prefix
                name_match = CATALOG_VIEW_NAME_PATTERN.search(text)
                if not name_match:
                    # Skip headings that don't reference sys. objects
                    continue
                view_name = f"sys.{name_match.group(1)}"
                
                current_view = {
                    "name": view_name,
                    "title": text.replace(" (Transact-SQL)", "").strip(),
                    "category": infer_catalog_category(view_name),
                    "tags": ["catalog-view", infer_catalog_category(view_name)],
                    "description": "",
                    "pubDate": datetime.now(),
                }
            elif h["level"] == 2 and not is_heading_noise(text):
                current_paragraphs.append({"text": f"## {text}", "font": "", "size": 0})
        
        if not current_view.get("name"):
            for p in paragraphs:
                t = clean_text(p.get("text", ""))
                name_match = CATALOG_VIEW_NAME_PATTERN.search(t)
                if name_match:
                    view_name = f"sys.{name_match.group(1)}"
                    current_view = {
                        "name": view_name,
                        "title": view_name,
                        "category": infer_catalog_category(view_name),
                        "tags": ["catalog-view", infer_catalog_category(view_name)],
                        "description": "",
                        "pubDate": datetime.now(),
                    }
                    break
        
        current_paragraphs.extend(paragraphs)
        current_code.extend(code_blocks)
    
    if current_view.get("name"):
        rec = _flush_entry(current_view, current_paragraphs, current_code, content_output_dir, "catalog-views")
        if rec:
            records.append(rec)
    
    return records


# ──────────────────────────────────────────────────
# Functions Parser
# ──────────────────────────────────────────────────

FUNCTION_NAME_PATTERN = re.compile(r"(sys\.(fn_|sp_))", re.IGNORECASE)

FUNCTION_CATEGORIES = {
    "aggregate": "aggregate", "analytic": "analytic", "conversion": "conversion",
    "crypt": "cryptographic", "encrypt": "cryptographic",
    "date": "date-time", "time": "date-time", "datetime": "date-time",
    "math": "mathematical", "float": "mathematical",
    "metadata": "metadata", "object_id": "metadata",
    "rank": "ranking", "row_number": "ranking",
    "security": "security", "login": "security", "user": "security",
    "string": "string", "char": "string", "nchar": "string", "nvarchar": "string", "varchar": "string",
    "system": "system", "fn_help": "system",
    "statistical": "system-statistical",
    "text": "text-image", "image": "text-image",
    "trigger": "trigger",
    "json": "json",
}


def infer_function_category(name: str) -> str:
    name_lower = name.lower()
    for keyword, cat in FUNCTION_CATEGORIES.items():
        if keyword in name_lower:
            return cat
    return "system"


def process_functions_batch(batch_file: str, content_output_dir: str) -> list[dict]:
    """Process system functions batch — detect functions and SPs by heading pattern."""
    with open(batch_file, "r", encoding="utf-8") as f:
        pages = json.load(f)
    
    records = []
    current_func = {}
    current_paragraphs = []
    current_code = []
    
    for page_data in pages:
        headings = page_data.get("headings", [])
        paragraphs = page_data.get("paragraphs", [])
        code_blocks = page_data.get("code_blocks", [])
        
        for h in headings:
            text = clean_text(h["text"])
            if h["level"] == 1 and not is_heading_noise(text):
                # Flush previous
                if current_func.get("name"):
                    collection = "stored-procedures" if current_func.get("name", "").startswith("sys.sp_") else "functions"
                    rec = _flush_entry(current_func, current_paragraphs, current_code, content_output_dir, collection)
                    if rec:
                        records.append(rec)
                    current_paragraphs = []
                    current_code = []
                
                func_name = text.replace(" (Transact-SQL)", "").strip()
                is_fn = func_name.lower().startswith("sys.fn_")
                is_sp = func_name.lower().startswith("sys.sp_")
                
                # Only accept sys.fn_ or sys.sp_ prefixed names
                if not (is_fn or is_sp):
                    continue
                
                current_func = {
                    "name": func_name,
                    "title": func_name,
                    "category": infer_function_category(func_name),
                    "tags": ["function" if not is_sp else "stored-procedure"],
                    "description": "",
                    "returnType": "",
                    "pubDate": datetime.now(),
                }
                
                if is_sp:
                    current_func["category"] = "general"
                    current_func["tags"] = ["stored-procedure"]
            elif h["level"] == 2:
                tl = text.lower()
                if "return" in tl and not current_func.get("returnType"):
                    current_func["returnType"] = text
                elif not is_heading_noise(text):
                    current_paragraphs.append({"text": f"## {text}", "font": "", "size": 0})
        
        # Set description from first paragraph if empty
        if not current_func.get("description"):
            desc = extract_first_paragraph(paragraphs, min_len=20)
            if desc:
                current_func["description"] = desc
        
        current_paragraphs.extend(paragraphs)
        current_code.extend(code_blocks)
    
    if current_func.get("name"):
        collection = "stored-procedures" if current_func.get("name", "").startswith("sys.sp_") else "functions"
        rec = _flush_entry(current_func, current_paragraphs, current_code, content_output_dir, collection)
        if rec:
            records.append(rec)
    
    return records


# ──────────────────────────────────────────────────
# Architecture / Narrative Parser
# ──────────────────────────────────────────────────

ARCHITECTURE_TOPICS = {
    "query": "query-processing", "execution plan": "query-processing",
    "index": "index-architecture", "indexes": "index-architecture",
    "memory": "memory-management", "buffer": "memory-management",
    "locking": "locking", "lock": "locking",
    "deadlock": "deadlocks",
    "thread": "thread-task", "task": "thread-task", "scheduler": "thread-task",
    "io": "io-fundamentals", "i/o": "io-fundamentals", "disk": "io-fundamentals",
    "log": "transaction-log", "transaction log": "transaction-log",
    "latch": "latch-contention",
    "spinlock": "spinlock-contention",
}


def infer_architecture_topic(text: str) -> str:
    tl = text.lower()
    for keyword, topic in ARCHITECTURE_TOPICS.items():
        if keyword in tl:
            return topic
    return "query-processing"


def process_architecture_batch(batch_file: str, content_output_dir: str) -> list[dict]:
    """Process architecture narrative section.
    
    Architecture is long-form text. We split by major H2 headings into
    individual narrative entries.
    """
    with open(batch_file, "r", encoding="utf-8") as f:
        pages = json.load(f)
    
    records = []
    current_entry = None
    current_paragraphs = []
    current_code = []
    
    for page_data in pages:
        headings = page_data.get("headings", [])
        paragraphs = page_data.get("paragraphs", [])
        code_blocks = page_data.get("code_blocks", [])
        
        for h in headings:
            text = clean_text(h["text"])
            if h["level"] in (1, 2) and not is_heading_noise(text) and len(text) > 5:
                # Flush previous
                if current_entry and current_paragraphs:
                    rec = flush_architecture_entry(current_entry, current_paragraphs, current_code, content_output_dir)
                    if rec:
                        records.append(rec)
                    current_paragraphs = []
                    current_code = []
                
                topic = infer_architecture_topic(text)
                current_entry = {
                    "title": text,
                    "topic": topic,
                    "tags": [topic, "architecture"],
                    "description": "",
                }
            
            elif h["level"] == 3:
                current_paragraphs.append({"text": f"### {text}", "font": "", "size": 0})
        
        current_paragraphs.extend(paragraphs)
        current_code.extend(code_blocks)
    
    # Flush last
    if current_entry and current_paragraphs:
        rec = flush_architecture_entry(current_entry, current_paragraphs, current_code, content_output_dir)
        if rec:
            records.append(rec)
    
    return records


def flush_architecture_entry(entry: dict, paragraphs: list, code_blocks: list, output_dir: str) -> Optional[dict]:
    """Write an architecture content file."""
    title = entry.get("title", "").strip()
    # Filter noise: single words, hex values, very short titles, table noise
    if not title or len(title) < 5:
        return None
    if re.match(r"^[0-9a-fA-Fx]+$", title):
        return None
    if title.lower() in ["description", "details", "overview", "summary", "remarks", "guide"]:
        return None
    
    desc = extract_first_paragraph(paragraphs, min_len=20, max_len=200)
    if desc:
        entry["description"] = desc
    
    slug = generate_slug(entry["title"])
    
    frontmatter_fields = {
        "title": entry["title"],
        "topic": entry["topic"],
        "description": entry.get("description", "")[:200],
        "tags": entry.get("tags", []),
        "pubDate": datetime.now(),
    }
    
    fm = build_frontmatter(frontmatter_fields)
    body = build_markdown_body(paragraphs, code_blocks)
    
    filepath = write_content_file(output_dir, "architecture", slug, fm, body)
    
    return {
        "slug": slug,
        "name": entry["title"],
        "title": entry["title"],
        "category": entry["topic"],
        "tags": entry.get("tags", []),
        "description": entry.get("description", "")[:150],
        "filepath": filepath,
        "collection": "architecture",
    }


# ──────────────────────────────────────────────────
# T-SQL Reference Parser
# ──────────────────────────────────────────────────

TSQL_CATEGORY_KEYWORDS = {
    "statements": [
        "create", "alter", "drop", "grant", "deny", "revoke", "backup",
        "restore", "truncate", "update statistics", "checkpoint", "dbcc",
        "shutdown", "kill", "print", "raiserror", "readtext", "writetext",
        "updatetext", "bulk insert", "return", "waitfor", "goto",
        "execute", "exec", "open", "close", "deallocate", "prepare",
        "reconfigure", "set", "use",
    ],
    "queries": [
        "select", "insert", "update", "delete", "merge", "from", "where",
        "join", "on", "group by", "having", "order by", "union",
        "intersect", "except", "for xml", "for json", "pivot", "unpivot",
        "offset fetch", "output clause", "into", "values", "with",
        "option", "table value constructor", "subquery",
    ],
    "language-elements": [
        "if", "else", "while", "begin", "end", "break", "continue",
        "case", "declare", "goto", "label", "return", "throw",
        "try", "catch", "waitfor", "raiseerror", "print", "nullif",
        "coalesce", "iif", "choose",
    ],
    "data-types": [
        "int", "bigint", "smallint", "tinyint", "decimal", "numeric",
        "float", "real", "money", "smallmoney", "bit", "char", "varchar",
        "nchar", "nvarchar", "text", "ntext", "binary", "varbinary",
        "image", "cursor", "hierarchyid", "geography", "geometry",
        "date", "time", "datetime", "datetime2", "datetimeoffset",
        "smalldatetime", "sql_variant", "table", "rowversion",
        "timestamp", "uniqueidentifier", "xml", "spatial",
        "data type", "alias",
    ],
    "operators": [
        "arithmetic", "+", "-", "*", "/", "%", "modulo", "concatenation",
        "comparison", "=", "!=", "<>", ">", "<", ">=", "<=", "!<", "!>",
        "logical", "and", "or", "not", "bitwise", "&", "|", "^", "~",
        "operator", "unary",
    ],
    "hints": [
        "nolock", "readuncommitted", "readcommitted", "repeatableread",
        "serializable", "snapshot", "readonly", "index", "force seek",
        "forcescan", "table hint", "query hint", "optimizer hints",
        "join hint", "hash", "loop", "merge", "option",
    ],
    "predicates": [
        "exists", "any", "all", "some", "in", "between", "like",
        "is null", "is not null", "freetext", "contains", "full-text",
        "comparison",
    ],
    "transactions": [
        "begin transaction", "begin tran", "commit", "rollback",
        "save transaction", "save tran", "transaction", "set transaction",
        "set implicit_transactions",
    ],
    "variables": [
        "declare @", "set @", "variable", "local variable",
        "cursor variable", "table variable",
    ],
}


def infer_tsql_category(name: str) -> str:
    """Infer T-SQL Reference category from statement/object name."""
    nl = name.lower().strip()
    for cat, keywords in TSQL_CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if nl.startswith(kw) or f" {kw} " in f" {nl} " or nl == kw:
                return cat
    # Fallback: check for common patterns
    if nl.startswith("@") or "variable" in nl:
        return "variables"
    if any(t in nl for t in ["data type", "types", "datetime", "numeric", "string"]):
        return "data-types"
    if "hint" in nl or "table_hint" in nl:
        return "hints"
    return "statements"


def process_tsql_reference_batch(batch_file: str, content_output_dir: str) -> list[dict]:
    """Process T-SQL Reference section.

    Each H1 heading (e.g., 'SELECT (Transact-SQL)', 'CREATE TABLE') is
    treated as a separate reference entry. Sub-headings (Syntax, Arguments,
    Returns, Remarks, Permissions, Examples) structure the body content.
    """
    with open(batch_file, "r", encoding="utf-8") as f:
        pages = json.load(f)

    records = []
    current_entry = {}
    current_paragraphs = []
    current_code = []
    syntax_captured = False
    in_syntax_section = False
    section_headings = {"syntax", "arguments", "returns", "remarks",
                        "permissions", "examples", "description", "best practice"}

    for page_data in pages:
        headings = page_data.get("headings", [])
        paragraphs = page_data.get("paragraphs", [])
        code_blocks = page_data.get("code_blocks", [])

        for h in headings:
            text = clean_text(h["text"])
            if h["level"] == 1 and not is_heading_noise(text) and len(text) > 3:
                # Flush previous entry
                if current_entry.get("name"):
                    rec = _flush_tsql_entry(
                        current_entry, current_paragraphs, current_code,
                        syntax_captured, content_output_dir
                    )
                    if rec:
                        records.append(rec)
                    current_paragraphs = []
                    current_code = []
                    syntax_captured = False
                    in_syntax_section = False

                # Extract T-SQL statement name (strip " (Transact-SQL)" suffix)
                entry_name = text.replace(" (Transact-SQL)", "").strip()
                if not entry_name:
                    continue

                current_entry = {
                    "name": entry_name,
                    "title": entry_name,
                    "category": infer_tsql_category(entry_name),
                    "tags": ["tsql", infer_tsql_category(entry_name)],
                    "description": "",
                    "syntax": "",
                }

            elif h["level"] == 2 and current_entry.get("name"):
                tl = text.lower().strip()
                # Track syntax section for first code block capture
                in_syntax_section = (tl == "syntax")
                if not is_heading_noise(text) and tl not in section_headings:
                    current_paragraphs.append({"text": f"## {text}", "font": "", "size": 0})

            elif h["level"] >= 3 and current_entry.get("name"):
                tl = text.lower().strip()
                if tl not in section_headings:
                    current_paragraphs.append({"text": f"{'#' * h['level']} {text}", "font": "", "size": 0})

        # Capture first code block after Syntax heading as the syntax field
        for cb in code_blocks:
            if in_syntax_section and not syntax_captured and cb.strip():
                current_entry["syntax"] = cb.strip()[:500]
                syntax_captured = True
                break

        # Set description from first meaningful paragraph
        if not current_entry.get("description"):
            desc = extract_first_paragraph(paragraphs, min_len=20, max_len=200)
            if desc:
                current_entry["description"] = desc

        current_paragraphs.extend(paragraphs)
        current_code.extend(code_blocks)

    # Flush last entry
    if current_entry.get("name"):
        rec = _flush_tsql_entry(
            current_entry, current_paragraphs, current_code,
            syntax_captured, content_output_dir
        )
        if rec:
            records.append(rec)

    return records


def _flush_tsql_entry(
    entry: dict, paragraphs: list, code_blocks: list,
    syntax_captured: bool, output_dir: str
) -> Optional[dict]:
    """Write a T-SQL reference content file."""
    name = entry.get("name", "").strip()
    if not name:
        return None

    slug = generate_slug(name)
    desc = entry.get("description", "") or extract_first_paragraph(paragraphs, min_len=20, max_len=200)

    frontmatter_fields = {
        "name": name,
        "title": entry.get("title", name),
        "category": entry.get("category", "statements"),
        "description": desc[:200],
        "tags": entry.get("tags", []),
        "pubDate": datetime.now(),
    }

    if entry.get("syntax"):
        frontmatter_fields["syntax"] = entry["syntax"]

    fm = build_frontmatter(frontmatter_fields)
    body = build_markdown_body(paragraphs, code_blocks)

    filepath = write_content_file(output_dir, "tsql-reference", slug, fm, body)

    return {
        "slug": slug,
        "name": name,
        "title": entry.get("title", name),
        "category": entry.get("category", "statements"),
        "tags": entry.get("tags", []),
        "description": desc[:150],
        "filepath": filepath,
        "collection": "tsql-reference",
    }


# ──────────────────────────────────────────────────
# Generic entry flusher (for DMV, catalog-views, functions)
# ──────────────────────────────────────────────────

# Name validation rules per collection
VALID_NAME_PATTERNS = {
    "dmvs": re.compile(r"^sys\.dm_[a-z_0-9]{3,}$", re.IGNORECASE),
    "catalog-views": re.compile(r"^sys\.[a-z_0-9]{3,}$", re.IGNORECASE),
    "functions": re.compile(r"^sys\.fn_[a-z_0-9]{3,}$", re.IGNORECASE),
    "stored-procedures": re.compile(r"^sys\.sp_[a-z_0-9]{3,}$", re.IGNORECASE),
    "tsql-reference": None,  # Accept any non-empty name
}


def is_valid_name(name: str, collection: str) -> bool:
    """Validate that a name matches the expected pattern for its collection."""
    pattern = VALID_NAME_PATTERNS.get(collection)
    if pattern:
        return bool(pattern.match(name.strip()))
    return bool(name.strip())  # No pattern = accept any non-empty name


def _flush_entry(
    item: dict,
    paragraphs: list,
    code_blocks: list,
    output_dir: str,
    collection: str,
) -> Optional[dict]:
    """Write a generic content file entry."""
    name = item.get("name", "").strip()
    if not name or not is_valid_name(name, collection):
        return None
    
    slug = generate_slug(name)
    desc = item.get("description", "") or extract_first_paragraph(paragraphs, min_len=20, max_len=200)
    return_type = item.get("returnType", "")
    
    frontmatter_fields = {
        "name": name,
        "title": item.get("title", name),
        "category": item.get("category", "general"),
        "description": desc[:200],
        "tags": item.get("tags", []),
        "pubDate": datetime.now(),
    }
    
    # Add type-specific optional fields
    if return_type and collection == "functions":
        frontmatter_fields["returnType"] = return_type
    if item.get("permissions") and collection == "dmvs":
        frontmatter_fields["permissions"] = item["permissions"]
    
    fm = build_frontmatter(frontmatter_fields)
    body = build_markdown_body(paragraphs, code_blocks)
    
    filepath = write_content_file(output_dir, collection, slug, fm, body)
    
    return {
        "slug": slug,
        "name": name,
        "title": item.get("title", name),
        "category": item.get("category", "general"),
        "tags": item.get("tags", []),
        "description": desc[:150],
        "filepath": filepath,
        "collection": collection,
    }


# ──────────────────────────────────────────────────
# Search Index Builder
# ──────────────────────────────────────────────────

def build_search_index(records: list[dict], output_path: str) -> str:
    """
    Metadata-only Fuse.js search index.
    NEVER contains full body text.
    """
    index = []
    for rec in records:
        if not rec:
            continue
        index.append({
            "slug": rec["slug"],
            "name": rec.get("name", ""),
            "title": rec.get("title", ""),
            "category": rec.get("category", ""),
            "tags": rec.get("tags", []),
            "description": rec.get("description", "")[:150],
            "collection": rec.get("collection", ""),
        })
    
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    return str(output_path)


# ──────────────────────────────────────────────────
# Main Processor
# ──────────────────────────────────────────────────

BATCH_PROCESSORS = {
    "system-dmvs": process_dmv_batch,
    "errors": process_errors_batch,
    "system-catalog-views": process_catalog_views_batch,
    "system-functions": process_functions_batch,
    "architecture": process_architecture_batch,
    "tsql-reference": process_tsql_reference_batch,
}


def get_section_prefix(filename: str) -> str:
    """Extract section prefix from batch filename."""
    for prefix in BATCH_PROCESSORS:
        if filename.startswith(prefix):
            return prefix
    return ""


def process_all_batches(batch_dir: str, content_output_dir: str, search_index_path: str) -> dict:
    """Process all batch files and generate content + search index."""
    batch_dir = Path(batch_dir)
    batch_files = sorted(batch_dir.glob("*.json"))
    
    all_records = []
    results = {}
    
    for bf in batch_files:
        if bf.name == "toc_index.json":
            continue
        
        prefix = get_section_prefix(bf.name)
        if not prefix:
            continue
        
        processor = BATCH_PROCESSORS[prefix]
        print(f"  Processing {bf.name} ({prefix})...", end=" ")
        try:
            records = processor(str(bf), content_output_dir)
            collection = SECTION_COLLECTION_MAP.get(prefix, "unknown")
            results[bf.name] = {"records": len(records), "collection": collection}
            all_records.extend(records)
            print(f"{len(records)} records")
        except Exception as e:
            print(f"ERROR: {e}")
            results[bf.name] = {"error": str(e)}
    
    # Build search index
    built_path = build_search_index(all_records, search_index_path)
    print(f"\n  Search index: {built_path} ({len(all_records)} total records)")
    
    # Summary by collection
    collection_counts = {}
    for r in all_records:
        coll = r.get("collection", "unknown")
        collection_counts[coll] = collection_counts.get(coll, 0) + 1
    
    print(f"\n  Collection breakdown:")
    for coll, count in sorted(collection_counts.items()):
        print(f"    {coll}: {count}")
    
    return {
        "total_records": len(all_records),
        "collection_counts": collection_counts,
        "results": results,
    }


if __name__ == "__main__":
    batch_dir = sys.argv[1] if len(sys.argv) > 1 else "output"
    content_dir = sys.argv[2] if len(sys.argv) > 2 else "../site/src/content"
    search_index = sys.argv[3] if len(sys.argv) > 3 else "../site/src/data/search-index.json"
    
    print(f"[schema_mapper_v2] Processing all batches from {batch_dir}...")
    print(f"[schema_mapper_v2] Content output: {content_dir}")
    print(f"[schema_mapper_v2] Search index: {search_index}")
    
    result = process_all_batches(batch_dir, content_dir, search_index)
    
    print(f"\n[schema_mapper_v2] Done. {result['total_records']} content items generated.")
