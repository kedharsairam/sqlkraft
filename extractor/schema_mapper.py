"""
schema_mapper.py — Content Collection Markdown Generator

Transforms extracted page data into Astro Content Collection Markdown files
with validated frontmatter schemas. This is the bridge between raw PDF
extraction and the Astro rendering engine.

For each extracted content item (DMV, wait type, function, etc.):
  1. Parse structured JSON from page_extractor batches
  2. Map fields to content collection schema
  3. Generate frontmatter (YAML) + markdown body
  4. Write to site/src/content/<collection>/<slug>.md
  5. Validate against Zod schema rules
"""

import json
import re
import os
from pathlib import Path
from typing import Any, Optional
from datetime import datetime


# Map page_extractor output to content collection fields
FIELD_MAPPING = {
    "dmv": {
        "title": "title",
        "name": "name",          # sys.dm_exec_requests
        "description": "description",
        "category": "category",
        "tags": "tags",
        "permissions": "permissions",
    },
    "wait_statistics": {
        "name": "name",
        "title": "title",
        "category": "category",   # baseline, triage, top-consumer, latency, blocking, memory, scheduling, io
        "severity": "severity",
        "description": "description",
        "tags": "tags",
        "related_scripts": "relatedScripts",
    },
}


# Regex pattern to detect DMV names
DMV_NAME_PATTERN = re.compile(r"(sys\.dm_[a-z_0-9]+)", re.IGNORECASE)
# Filter for lines that look like actual DMV or other reference names
REFERENCE_NAME_PATTERN = re.compile(r"(sys\.(dm_|sp_|fn_|xp_))", re.IGNORECASE)


def is_valid_dmv_name(text: str) -> bool:
    """Check if text looks like a valid DMV/reference object name."""
    return bool(DMV_NAME_PATTERN.match(text.strip()))


def extract_dmv_name_from_lines(paragraphs: list[dict]) -> str:
    """Search paragraphs for DMV names when headings don't contain them."""
    for p in paragraphs:
        text = p["text"].strip()
        match = DMV_NAME_PATTERN.search(text)
        if match:
            return match.group(1)
    return ""


def parse_dmv_from_headings(headings: list[dict]) -> dict[str, Any]:
    """Extract DMV metadata from heading structure."""
    dmv = {
        "name": "",
        "title": "",
        "description": "",
        "category": "execution",
        "tags": [],
        "permissions": "",
    }

    for h in headings:
        text = h["text"].strip()
        if h["level"] == 2 and not dmv["name"]:
            dmv["name"] = text
            dmv["title"] = text
        elif h["level"] == 3:
            tl = text.lower()
            if "permission" in tl:
                dmv["permissions"] = text

    # Infer category from name prefix — only if name looks valid
    name = dmv["name"]
    if is_valid_dmv_name(name):
        if name.startswith("sys.dm_exec_"):
            dmv["category"] = "execution"
        elif name.startswith("sys.dm_os_"):
            dmv["category"] = "os"
        elif name.startswith("sys.dm_db_index_") or name.startswith("sys.dm_db_missing_index"):
            dmv["category"] = "index"
        elif name.startswith("sys.dm_io_"):
            dmv["category"] = "io"
        elif name.startswith("sys.dm_tran_"):
            dmv["category"] = "transactions"
        elif name.startswith("sys.dm_db_xtp_"):
            dmv["category"] = "in-memory"
        elif name.startswith("sys.dm_hadr_") or name.startswith("sys.dm_os_cluster"):
            dmv["category"] = "availability"

        # Generate tags from name keywords
        dmv["tags"] = [dmv["category"]]
        for kw in ["requests", "sessions", "connections", "sql_text", "query_stats",
                   "wait_stats", "locks", "transactions", "memory", "schedulers",
                   "workers", "tasks", "threads", "index", "io", "buffer",
                   "databases", "log", "space"]:
            if kw in name.lower():
                dmv["tags"].append(kw)

    return dmv


def build_frontmatter(fields: dict[str, Any], collection_type: str) -> str:
    """Build YAML frontmatter string from fields dict."""
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
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for k, v in value.items():
                lines.append(f"  {k}: {v}")
        else:
            # String — wrap in quotes if contains special chars
            sv = str(value)
            if any(c in sv for c in [":", "#", "{", "}", "[", "]", ">", "|", '"', "'", "\n"]):
                lines.append(f'{key}: "{sv}"')
            else:
                lines.append(f"{key}: {sv}")
    lines.append("---")
    return "\n".join(lines)


def build_markdown_body(
    paragraphs: list[dict],
    code_blocks: list[str],
) -> str:
    """Build Markdown body from extracted page content."""
    body_parts = []
    in_code = False

    for p in paragraphs:
        text = p["text"].strip()
        if not text:
            continue

        # Detect potential headings in paragraph text
        if len(text) < 100 and any(text.startswith(prefix) for prefix in
                                   ["Syntax", "Arguments", "Returns", "Remarks",
                                    "Permissions", "Examples", "Best Practice"]):
            if in_code:
                body_parts.append("```\n")
                in_code = False
            body_parts.append(f"\n## {text}\n")
        else:
            body_parts.append(text + "\n\n")

    # Append code blocks
    for cb in code_blocks:
        body_parts.append(f"```sql\n{cb}\n```\n\n")

    return "".join(body_parts).strip() or "*(Content pending extraction)*"


def generate_slug(title: str) -> str:
    """Generate URL-safe slug."""
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


def write_content_file(
    output_dir: str,
    collection: str,
    slug: str,
    frontmatter: str,
    body: str,
) -> str:
    """Write a single content collection markdown file."""
    collection_dir = Path(output_dir) / collection
    collection_dir.mkdir(parents=True, exist_ok=True)

    filepath = collection_dir / f"{slug}.md"
    content = frontmatter + "\n\n" + body + "\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return str(filepath)


def process_dmv_batch(
    batch_file: str,
    content_output_dir: str,
) -> list[dict[str, Any]]:
    """
    Process a single batch JSON file and generate markdown content files.

    Args:
        batch_file: Path to page_extractor batch JSON
        content_output_dir: Target directory for .md files

    Returns:
        List of records generated (for search index)
    """
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

        # Scan paragraphs for DMV names (headings may not contain them)
        dmv_name_from_body = extract_dmv_name_from_lines(paragraphs)

        for h in headings:
            # H2 starts a new DMV entry
            if h["level"] == 2:
                # Flush previous DMV if exists
                if current_dmv.get("name"):
                    rec = _flush_dmv(
                        current_dmv, current_paragraphs, current_code,
                        content_output_dir
                    )
                    if rec:
                        records.append(rec)
                    current_paragraphs = []
                    current_code = []

                current_dmv = parse_dmv_from_headings([h])

                # If heading didn't yield a valid name, try the body text
                if not is_valid_dmv_name(current_dmv.get("name", "")):
                    found = extract_dmv_name_from_lines(paragraphs)
                    if found:
                        current_dmv["name"] = found
                        current_dmv["title"] = found

            elif h["level"] == 3:
                current_paragraphs.append({
                    "text": f"## {h['text']}",
                    "font": "",
                    "size": 0,
                })

        current_paragraphs.extend(paragraphs)
        current_code.extend(code_blocks)

    # Flush last DMV
    if current_dmv.get("name"):
        rec = _flush_dmv(
            current_dmv, current_paragraphs, current_code,
            content_output_dir
        )
        if rec:
            records.append(rec)

    # Filter out any None entries that slipped through
    return [r for r in records if r is not None]


def _flush_dmv(
    dmv: dict,
    paragraphs: list,
    code_blocks: list,
    output_dir: str,
) -> Optional[dict[str, Any]]:
    """Write a single DMV content file and return search record.

    Returns None if the DMV name is not a valid reference object
    (e.g., table headers or structural UI text).
    """
    name = dmv.get("name", "").strip()
    if not is_valid_dmv_name(name) and not name.startswith("sys."):
        return None  # Skip non-DMV entries

    slug = generate_slug(name)

    # Build frontmatter
    frontmatter_fields = {
        "title": dmv.get("title", ""),
        "name": dmv.get("name", ""),
        "category": dmv.get("category", "execution"),
        "description": dmv.get("description", ""),
        "tags": dmv.get("tags", []),
        "pubDate": datetime.now(),
    }

    # Add optional fields
    if dmv.get("permissions"):
        frontmatter_fields["permissions"] = dmv["permissions"]

    fm = build_frontmatter(frontmatter_fields, "dmv")
    body = build_markdown_body(paragraphs, code_blocks)

    filepath = write_content_file(output_dir, "dmvs", slug, fm, body)

    return {
        "slug": slug,
        "name": dmv.get("name", ""),
        "title": dmv.get("title", ""),
        "category": dmv.get("category", ""),
        "tags": dmv.get("tags", []),
        "description": dmv.get("description", "")[:150],
        "filepath": filepath,
        "collection": "dmvs",
    }


def build_search_index(records: list[dict], output_path: str) -> str:
    """
    Build a metadata-only Fuse.js search index.

    CRITICAL: ONLY contains name, title, slug, category, tags, and
    150-char description. NEVER ingests full body text.
    """
    index = []
    for rec in records:
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
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return str(output_path)


if __name__ == "__main__":
    import sys
    batch_dir = sys.argv[1] if len(sys.argv) > 1 else "output"
    content_dir = sys.argv[2] if len(sys.argv) > 2 else "../site/src/content"

    print(f"[schema_mapper] Processing batch files from {batch_dir}...")

    all_records = []
    batch_files = sorted(Path(batch_dir).glob("system-dmvs_*.json"))

    if not batch_files:
        print("[schema_mapper] No batch files found. Run page_extractor first.")
        sys.exit(1)

    for bf in batch_files:
        print(f"  Processing {bf.name}...")
        records = process_dmv_batch(str(bf), content_dir)
        all_records.extend(records)
        print(f"    -> {len(records)} records extracted")

    # Build search index
    search_path = os.path.join(content_dir, "..", "data", "search-index.json")
    build_search_index(all_records, search_path)

    print(f"\n[schema_mapper] Done. {len(all_records)} content items written.")
    print(f"[schema_mapper] Search index saved to {search_path}")

    # Verification summary
    categories = {}
    for r in all_records:
        cat = r.get("category", "unknown")
        categories[cat] = categories.get(cat, 0) + 1
    print(f"[schema_mapper] Category breakdown: {json.dumps(categories, indent=2)}")
