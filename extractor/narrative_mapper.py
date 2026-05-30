"""
narrative_mapper.py --- v0.4.0 Narrative Content Ingestion Engine

Extracts three types of narrative content from batch JSON files:

  1. Error Severities (p.17659-17665) -> src/content/errors/
  2. XQuery Reference    (p.30181-30465) -> src/content/tsql-reference/
  3. Expanded Architecture (p.2043-4681) -> src/content/architecture/

Uses TOC entries as authoritative section boundaries and maps each to
the correct collection with proper frontmatter.

Usage:
  python narrative_mapper.py [batch_dir] [content_dir]
"""

import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# -- Paths --
BATCH_DIR = Path(__file__).parent / "output"
CONTENT_DIR = Path(__file__).parent.parent / "site" / "src" / "content"
TOC_PATH = BATCH_DIR / "toc_index.json"

# -- Architecture H2 -> topic mapping --
H2_TOPIC_MAP = {
    "hierarchical data": "hierarchical-data",
    "collation": "collation",
    "event notification": None,  # too small, merge into parent
    "filestream, filetable & blob": "filestream",
    "sql graph": "sql-graph",
    "sequence numbers": "service-broker",  # main content is Service Broker
    "spatial data": "spatial-data",
    "tables": "tables",
    "compare change tracking with cdc": "change-data-capture",
    "user-defined functions": None,  # procedural, not architecture
    "views": None,  # procedural, not architecture
    "xml data": "xml-data",
    "code a client program >": None,
    "common language runtime (clr)": "clr-integration",
    "json": "json-data",
    "regular expressions": None,  # too small
}

# Pages that should be skipped (navigation, appends, etc.)
SKIP_PAGE_TITLES = {
    "in this article", "see also", "next steps", "prerequisites",
    "additional resources", "related content", "related tasks",
    "related sections", "feedback", "submit and view feedback for",
}

# -- Helpers --

def slugify(text: str) -> str:
    """Convert heading text to a URL-friendly slug."""
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def make_title(name: str) -> str:
    """Convert a slug or code-style name to a proper title."""
    s = name.replace("-", " ").replace("_", " ")
    return " ".join(w.capitalize() for w in s.split())


def find_batch_files(prefix: str) -> list[Path]:
    """Find all batch JSON files matching a prefix, sorted by page range."""
    files = sorted(BATCH_DIR.glob(f"{prefix}_p*.json"))
    return files


def load_batch_pages(prefix: str) -> list[dict]:
    """Load all pages from batch files with a given prefix."""
    pages = []
    for bf in find_batch_files(prefix):
        with open(bf, "r", encoding="utf-8") as f:
            pages.extend(json.load(f))
    return sorted(pages, key=lambda p: p["page_number"])


def extract_body_text(page: dict) -> str:
    """Extract clean body paragraphs from a page."""
    lines = []
    for p in page.get("paragraphs", []):
        text = p.get("text", "").strip()
        if text and text.lower() not in SKIP_PAGE_TITLES:
            lines.append(text)
    return "\n\n".join(lines)


def extract_code_blocks(page: dict) -> list[str]:
    """Extract code blocks from a page."""
    return page.get("code_blocks", [])


def build_frontmatter(fields: dict) -> str:
    """Build YAML frontmatter with literal block scalars for multi-line values."""
    lines = ["---"]
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, datetime):
            lines.append(f'{key}: {value.strftime("%Y-%m-%d")}')
        elif isinstance(value, list):
            items = "\n".join(f"  - {json.dumps(v)}" for v in value)
            lines.append(f"{key}:\n{items}")
        elif isinstance(value, str) and "\n" in value:
            lines.append(f"{key}: |")
            for line in value.split("\n"):
                lines.append(f"  {line}")
        else:
            lines.append(f"{key}: {json.dumps(value)}")
    lines.append("---")
    return "\n".join(lines)


def write_content_file(filepath: Path, frontmatter: dict, body: str):
    """Write a .md content file with frontmatter + body."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    content = build_frontmatter(frontmatter) + "\n\n" + body.strip()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# ═══════════════════════════════════════════
# 1. ERROR SEVERITIES (p.17659-17665)
# ═══════════════════════════════════════════

def extract_error_severities():
    """Extract Database Engine error severity definitions."""
    print("\n" + "=" * 60)
    print("PHASE 1b: ERROR SEVERITIES (p.17659-17665)")
    print("=" * 60)

    pages = load_batch_pages("errors")
    # Severity definitions span pages 17663-17665
    severity_pages = [p for p in pages if 17663 <= p["page_number"] <= 17665]

    if not severity_pages:
        print("  ERROR: No severity pages found!")
        return []

    # Parse severity levels from page content
    # Format: "Severity level\nDescription\n\nSeverity level\nDescription..."
    severities = []
    current_level = None
    current_desc = []
    in_table = False

    for page in severity_pages:
        for p in page.get("paragraphs", []):
            text = p.get("text", "").strip()
            if not text:
                continue

            # Check for severity number patterns
            sev_match = re.match(r"^(\d+)\s*$", text)
            if sev_match:
                if current_level:
                    severities.append({
                        "level": int(current_level),
                        "description": " ".join(current_desc).strip()
                    })
                current_level = sev_match.group(1)
                current_desc = []
                continue

            # Check for "Severity level" table headers
            if "severity" in text.lower() and ("level" in text.lower() or "description" in text.lower()):
                in_table = True
                continue

            # Severity description or table cell content
            if current_level:
                # Remove table artifacts
                cleaned = re.sub(r"^\d+\s+", "", text).strip()
                if cleaned and cleaned.lower() not in ["severity", "level", "description", ""]:
                    current_desc.append(cleaned)

    # Flush last severity
    if current_level:
        severities.append({
            "level": int(current_level),
            "description": " ".join(current_desc).strip()
        })

    # Write severity files
    errors_dir = CONTENT_DIR / "errors"
    count = 0
    for sev in severities:
        sev_num = sev["level"]
        if sev_num < 1 or sev_num > 25:
            continue

        name = f"severity-{sev_num:02d}"
        title = f"Severity Level {sev_num}"
        desc = sev.get("description", f"Database Engine error severity level {sev_num}.")[:250]

        # Map severity number to our enum
        if sev_num <= 10:
            sev_enum = "info"
        elif sev_num <= 16:
            sev_enum = "low"
        elif sev_num <= 18:
            sev_enum = "medium"
        elif sev_num <= 20:
            sev_enum = "high"
        else:
            sev_enum = "critical"

        frontmatter = {
            "name": name,
            "title": title,
            "errorNumber": sev_num,
            "severity": sev_enum,
            "category": "system",
            "description": desc,
            "tags": ["error-severity", f"level-{sev_num}"],
            "pubDate": datetime(2025, 12, 1),
        }
        body = desc

        fpath = errors_dir / f"{name}.md"
        if not fpath.exists():  # don't overwrite
            write_content_file(fpath, frontmatter, body)
            count += 1

    print(f"  Created {count} severity files")
    return severities


# ═══════════════════════════════════════════
# 2. XQUERY CONTENT (p.30181-30465)
# ═══════════════════════════════════════════

def extract_xquery():
    """Extract XQuery Language Reference into tsql-reference collection."""
    print("\n" + "=" * 60)
    print("PHASE 1a: XQUERY (p.30181-30465)")
    print("=" * 60)

    # Load TOC
    with open(TOC_PATH, "r", encoding="utf-8") as f:
        toc = json.load(f)

    # Find XQuery TOC entries (p.30181-30465)
    xq_toc = [e for e in toc if e.get("page") and 30181 <= e["page"] <= 30465 and e["depth"] >= 2]

    # Load XQuery batch pages
    pages = load_batch_pages("xquery")
    pages_by_num = {p["page_number"]: p for p in pages}

    tsql_dir = CONTENT_DIR / "tsql-reference"
    count = 0
    source_articles = []

    for entry in xq_toc:
        if entry["depth"] < 2:
            continue

        title = entry["title"].strip()
        page_num = entry["page"]
        slug = slugify(title)

        # Skip navigation pages
        if title.lower() in SKIP_PAGE_TITLES:
            continue

        # Get page content
        page = pages_by_num.get(page_num)
        if not page:
            continue

        body_text = extract_body_text(page)
        code_blocks = extract_code_blocks(page)

        # Build article body
        body_parts = []
        if body_text:
            body_parts.append(body_text)
        if code_blocks:
            body_parts.append("\n".join(["```sql"] + code_blocks + ["```"]))

        body = "\n\n".join(body_parts)
        if not body.strip():
            body = f"XQuery language reference for {title}."

        # Generate unique name
        name = f"xquery-{slug}"[:80]

        frontmatter = {
            "name": name,
            "title": f"XQuery - {title}",
            "category": "xquery",
            "description": f"XQuery Language Reference: {title}"[:200],
            "syntax": code_blocks[0] if code_blocks else None,
            "tags": ["xquery", slug],
            "pubDate": datetime(2025, 12, 1),
        }
        # Don't include null/None syntax
        if frontmatter["syntax"] is None:
            del frontmatter["syntax"]

        fpath = tsql_dir / f"{name}.md"
        if not fpath.exists():
            write_content_file(fpath, frontmatter, body)
            count += 1
            source_articles.append(name)

    print(f"  Created {count} XQuery articles")
    return source_articles


# ═══════════════════════════════════════════
# 3. EXPANDED ARCHITECTURE (p.2043-4681)
# ═══════════════════════════════════════════

def extract_architecture():
    """Extract expanded architecture articles from database-design + extra-arch batches."""
    print("\n" + "=" * 60)
    print("PHASE 1c: EXPANDED ARCHITECTURE (p.2043-4681)")
    print("=" * 60)

    # Load TOC
    with open(TOC_PATH, "r", encoding="utf-8") as f:
        toc = json.load(f)

    # Load all architecture-related batch pages
    all_pages = []
    for prefix in ["database-design", "extra-arch"]:
        all_pages.extend(load_batch_pages(prefix))
    pages_by_num = {p["page_number"]: p for p in all_pages}

    # Find TOC entries in the architecture expansion range
    arch_toc = [e for e in toc if e.get("page") and 2043 <= e["page"] <= 4681]
    arch_toc_by_page = {e["page"]: e for e in arch_toc}

    # Group TOC entries by H2 section
    h2_sections = []
    current_h2 = None
    current_h3_list = []
    current_h2_page = None

    for e in arch_toc:
        if e["depth"] == 2:
            if current_h2:
                h2_sections.append((current_h2, current_h2_page, current_h3_list))
            current_h2 = e["title"]
            current_h2_page = e.get("page")
            current_h3_list = []
        elif e["depth"] >= 3 and current_h2:
            current_h3_list.append(e)

    if current_h2:
        h2_sections.append((current_h2, current_h2_page, current_h3_list))

    arch_dir = CONTENT_DIR / "architecture"
    count = 0

    for h2_title, h2_page, h3_entries in h2_sections:
        # Map to topic
        topic = H2_TOPIC_MAP.get(h2_title.lower().strip())
        if topic is None:
            print(f"  SKIP: {h2_title} (no topic mapping)")
            continue

        print(f"\n  H2: {h2_title} -> topic: {topic} ({len(h3_entries)} entries)")

        for h3 in h3_entries:
            title = h3["title"].strip()
            page_num = h3.get("page")
            depth = h3["depth"]

            if not page_num or title.lower() in SKIP_PAGE_TITLES:
                continue

            slug = slugify(title)
            name = slug

            # Get page content
            page = pages_by_num.get(page_num)
            if not page:
                # Try to find nearby pages
                for delta in range(1, 5):
                    page = pages_by_num.get(page_num + delta) or pages_by_num.get(page_num - delta)
                    if page:
                        break
            if not page:
                continue

            body_text = extract_body_text(page)
            code_blocks = extract_code_blocks(page)

            # Build body
            body_parts = []
            if body_text:
                body_parts.append(body_text)
            if code_blocks:
                body_parts.append("\n".join(["```sql"] + code_blocks + ["```"]))

            body = "\n\n".join(body_parts) if body_parts else f"Architecture guide: {title}."

            # Build frontmatter
            frontmatter = {
                "title": title,
                "topic": topic,
                "description": body_text[:200] if body_text else f"SQL Server {topic.replace('-', ' ')} architecture guide for {title}"[:200],
                "tags": [topic, slug],
                "pubDate": datetime(2025, 12, 1),
            }

            fpath = arch_dir / f"{name}.md"
            if not fpath.exists():
                write_content_file(fpath, frontmatter, body)
                count += 1

    print(f"\n  Created {count} architecture articles")
    return count


# ═══════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════

def main():
    print("=" * 60)
    print("NARRATIVE MAPPER --- v0.4.0")
    print("=" * 60)

    # Phase 1b: Error severities (fast)
    severities = extract_error_severities()

    # Phase 1a: XQuery articles
    xq_articles = extract_xquery()

    # Phase 1c: Expanded architecture
    arch_count = extract_architecture()

    # Summary
    print("\n" + "=" * 60)
    print("EXTRACTION SUMMARY")
    print("=" * 60)
    print(f"  Error severities:  {len(severities)} definitions")
    print(f"  XQuery articles:   {len(xq_articles)}")
    print(f"  Architecture:      {arch_count} articles")
    total = len(severities) + len(xq_articles) + arch_count
    print(f"  --------------------------")
    print(f"  TOTAL NEW FILES:   {total}")


if __name__ == "__main__":
    main()
