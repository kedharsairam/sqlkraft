"""
schema_mapper_v3.py - TOC-Driven Mass Ingestion Engine

Strategy: Instead of pattern-matching headings, use the PDF's own Table of
Contents (7,783 entries) as the authoritative object checklist. For each TOC
entry that maps to a database object (DMV, catalog view, stored procedure,
function), find matching pages in the batch JSON files and extract full,
untruncated content with:

  - Complete syntax blocks
  - Full arguments list
  - Structured return columns/types matrix
  - Permissions requirements
  - Native example blocks

Usage:
    python schema_mapper_v3.py [batch_dir] [content_dir] [search_index_path]
"""

import json
import re
import os
import sys
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Any, Optional
from collections import defaultdict

# -
# Section - Collection mapping
# -

SECTION_COLLECTION_MAP = {
    "system-dmvs": "dmvs",
    "system-catalog-views": "catalog-views",
    "system-compat-views": "catalog-views",
    "system-tables": "catalog-views",
    "system-functions": "functions",
    "tsql-reference": "tsql-reference",
    "architecture": "architecture",
    "errors": "errors",
}

# -
# TOC Object Extraction
# -

DMV_PATTERN = re.compile(r"(?:sys\.)?dm_[a-z_0-9]+", re.IGNORECASE)
CV_PATTERN = re.compile(r"sys\.([a-z_][a-z_0-9]+)", re.IGNORECASE)
SP_PATTERN = re.compile(r"(?:sys\.)?sp_[a-z_0-9]+", re.IGNORECASE)
FN_PATTERN = re.compile(r"(?:sys\.)?fn_[a-z_0-9]+", re.IGNORECASE)

# Object name - collection mapping via prefix
PREFIX_COLLECTION_MAP = {
    "sys.dm_": "dmvs",
    "sys.sp_": "stored-procedures",
    "sys.fn_": "functions",
}

# Category keyword maps for DMVs
DMV_CATEGORIES = {
    "exec": "execution", "os": "os", "db_index": "index",
    "db_missing_index": "index", "io": "io", "tran": "transactions",
    "db_xtp": "in-memory", "hadr": "availability", "os_cluster": "availability",
    "resource": "resource-governor", "fts": "full-text",
    "audit": "security-audit", "broker": "service-broker",
    "change_feed": "change-tracking", "clr": "clr",
    "column_store": "columnstore", "db_column_store": "columnstore",
    "db_fts": "full-text", "db_log": "log",
    "db_file": "file", "db_database": "database",
    "db_stats": "statistics", "db_partition": "partition",
    "db_query": "query-performance",
}

CATALOG_CATEGORIES = {
    "databases": "databases-files", "files": "databases-files",
    "filegroups": "databases-files", "objects": "objects",
    "tables": "objects", "views": "objects", "columns": "objects",
    "index": "indexes", "indexes": "indexes",
    "partition": "partitions", "security": "security",
    "permissions": "security", "user": "security", "login": "security",
    "role": "security", "query_store": "query-store",
    "service_broker": "service-broker", "broker": "service-broker",
    "fulltext": "full-text", "full_text": "full-text",
    "config": "configuration", "configure": "configuration",
    "xml": "xml", "spatial": "spatial", "external": "external",
    "sys": "compatibility",
}

FUNCTION_CATEGORIES = {
    "aggregate": "aggregate", "analytic": "analytic",
    "conversion": "conversion", "crypt": "cryptographic",
    "encrypt": "cryptographic", "date": "date-time", "time": "date-time",
    "datetime": "date-time", "math": "mathematical", "float": "mathematical",
    "metadata": "metadata", "rank": "ranking", "row_number": "ranking",
    "security": "security", "string": "string", "char": "string",
    "system": "system", "statistical": "system-statistical",
    "text": "text-image", "image": "text-image", "trigger": "trigger",
    "json": "json", "cdc": "change-data-capture",
    "backup": "backup-restore", "hadr": "availability-group",
    "dm_db": "dmv-helper",
}


def infer_dmv_category(name: str) -> str:
    nl = name.lower()
    for k, c in DMV_CATEGORIES.items():
        if k in nl:
            return c
    return "execution"


def infer_catalog_category(name: str) -> str:
    nl = name.lower()
    for k, c in CATALOG_CATEGORIES.items():
        if k in nl:
            return c
    return "objects"


def infer_function_category(name: str) -> str:
    nl = name.lower()
    for k, c in FUNCTION_CATEGORIES.items():
        if k in nl:
            return c
    return "system"


def extract_toc_objects(toc_path: str) -> dict[str, list[dict]]:
    """Extract ALL database objects from TOC.json, classified by collection."""
    with open(toc_path, "r", encoding="utf-8") as f:
        toc = json.load(f)

    objects = {
        "dmvs": [],
        "catalog-views": [],
        "stored-procedures": [],
        "functions": [],
        "tsql-reference": [],
    }

    seen = defaultdict(set)

    # Track section context
    current_section = None
    current_subsection = None

    for entry in toc:
        d = entry["depth"]
        title = entry["title"]
        page = entry.get("page")

        if d == 1:
            current_section = (title or "").lower()
        elif d == 2:
            current_subsection = (title or "").lower()

        section_lower = (current_section or "") + " " + (current_subsection or "")

        # - DMVs -
        m = DMV_PATTERN.search(title)
        if m and ("dmv" in section_lower or "dynamic management" in section_lower):
            name = m.group(0).lower()
            if not name.startswith("sys."):
                name = "sys." + name
            if name not in seen["dmvs"] and not name.startswith("sys.sp_") and not name.startswith("sys.fn_"):
                seen["dmvs"].add(name)
                objects["dmvs"].append({
                    "name": name, "title": title, "page": page,
                    "category": infer_dmv_category(name),
                })

        # - Catalog Views -
        m = CV_PATTERN.search(title)
        if m and ("catalog" in section_lower or "system table" in section_lower or
                   "compatibility" in section_lower or "system" in section_lower):
            name = "sys." + m.group(1).lower()
            if name not in seen["catalog-views"] and not any(
                name.startswith(p) for p in ["sys.dm_", "sys.sp_", "sys.fn_"]
            ):
                seen["catalog-views"].add(name)
                objects["catalog-views"].append({
                    "name": name, "title": title, "page": page,
                    "category": infer_catalog_category(name),
                })

        # - Stored Procedures -
        m = SP_PATTERN.search(title)
        if m and ("stored procedure" in section_lower or "function" in section_lower or
                   "system" in section_lower):
            name = m.group(0).lower()
            if not name.startswith("sys."):
                name = "sys." + name
            if name not in seen["stored-procedures"]:
                seen["stored-procedures"].add(name)
                objects["stored-procedures"].append({
                    "name": name, "title": title, "page": page,
                    "category": "general",
                })

        # - Functions -
        m = FN_PATTERN.search(title)
        if m and ("function" in section_lower or "system" in section_lower):
            name = m.group(0).lower()
            if not name.startswith("sys."):
                name = "sys." + name
            if name not in seen["functions"]:
                seen["functions"].add(name)
                objects["functions"].append({
                    "name": name, "title": title, "page": page,
                    "category": infer_function_category(name),
                })

    return objects


# -
# Batch File Page Index
# -

class BatchPageIndex:
    """Index of all pages from batch JSON files, searchable by object name."""

    def __init__(self, batch_dir: str):
        self.batch_dir = Path(batch_dir)
        self.pages = []                 # All pages flattened
        self.page_map = {}              # page_number -> page_data
        self.name_index = defaultdict(list)  # object_name -> list of page numbers
        self._build_index()

    def _build_index(self):
        """Load all batch JSON files and build searchable index."""
        batch_files = sorted(self.batch_dir.glob("*.json"))
        toc_index_seen = False

        for bf in batch_files:
            if bf.name == "toc_index.json":
                toc_index_seen = True
                continue

            try:
                with open(bf, "r", encoding="utf-8") as f:
                    pages_data = json.load(f)
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                print(f"    [WARN] Skipping {bf.name}: {e}")
                continue

            for page_data in pages_data:
                pn = page_data.get("page_number")
                if not pn:
                    continue

                self.pages.append(page_data)
                self.page_map[pn] = page_data

                # Index all headings + first paragraph text
                page_text = ""
                for h in page_data.get("headings", []):
                    page_text += " " + h.get("text", "")
                for p in page_data.get("paragraphs", [])[:3]:  # First 3 paragraphs
                    page_text += " " + p.get("text", "")
                for cb in page_data.get("code_blocks", [])[:2]:  # First 2 code blocks
                    page_text += " " + cb[:200]

                # Extract all sys. names from the page text
                for pattern_name, regex in [
                    ("dmvs", DMV_PATTERN),
                    ("catalog-views", CV_PATTERN),
                    ("stored-procedures", SP_PATTERN),
                    ("functions", FN_PATTERN),
                ]:
                    for m in regex.finditer(page_text):
                        obj_name = m.group(0).lower()
                        if not obj_name.startswith("sys."):
                            if obj_name.startswith("dm_") or obj_name.startswith("sp_") or obj_name.startswith("fn_"):
                                obj_name = "sys." + obj_name
                            else:
                                continue
                        self.name_index[obj_name].append(pn)

        print(f"  Index built: {len(self.page_map)} pages, {len(self.name_index)} unique object references")

    def find_pages(self, obj_name: str) -> list[dict]:
        """Find all pages that reference an object name."""
        obj_lower = obj_name.lower()
        pns = self.name_index.get(obj_lower, [])
        # Deduplicate
        pns = list(dict.fromkeys(pns))
        return [self.page_map[pn] for pn in pns if pn in self.page_map]

    def get_all_page_numbers(self) -> set:
        return set(self.page_map.keys())


# -
# Content Extraction
# -

def clean_text(text: str) -> str:
    text = text.replace("\u00a0", " ").replace("\xa0", " ")
    return " ".join(text.split())


def generate_slug(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def extract_syntax_from_pages(pages: list[dict]) -> str:
    """Extract the first complete syntax block found after a 'Syntax' heading."""
    for page_data in pages:
        in_syntax = False
        for h in page_data.get("headings", []):
            if h.get("text", "").strip().lower() == "syntax":
                in_syntax = True
            elif in_syntax and h["level"] <= 2:
                in_syntax = False

        if in_syntax:
            for cb in page_data.get("code_blocks", []):
                if cb.strip():
                    return cb.strip()

    # Fallback: return first code block from any page
    for page_data in pages:
        for cb in page_data.get("code_blocks", []):
            if cb.strip() and len(cb) > 20:
                return cb.strip()

    return ""


def extract_arguments(pages: list[dict]) -> list[str]:
    """Extract arguments section text."""
    args = []
    in_arguments = False
    for page_data in pages:
        for h in page_data.get("headings", []):
            tl = h.get("text", "").strip().lower()
            if tl in ("arguments", "parameters", "parameter"):
                in_arguments = True
            elif in_arguments and h["level"] <= 2 and tl not in (
                "arguments", "parameters", "parameter"
            ):
                in_arguments = False

        for p in page_data.get("paragraphs", []):
            if in_arguments:
                t = clean_text(p.get("text", "")).strip()
                if t and len(t) > 10:
                    args.append(t)
    return args


def extract_return_columns(pages: list[dict]) -> list[dict]:
    """Extract return column definitions."""
    columns = []
    in_returns = False
    for page_data in pages:
        for h in page_data.get("headings", []):
            tl = h.get("text", "").strip().lower()
            if tl in ("returns", "return", "return value"):
                in_returns = True
            elif in_returns and h["level"] <= 2 and tl not in ("returns", "return", "return value"):
                in_returns = False

        if in_returns:
            for p in page_data.get("paragraphs", []):
                t = clean_text(p.get("text", "")).strip()
                # Try to extract column definitions (table-like rows)
                col_match = re.match(
                    r"^\s*(\w+(?:_\w+)*)\s+(nvarchar|varchar|int|bigint|smallint|tinyint|"
                    r"decimal|numeric|float|real|money|bit|datetime|datetime2|date|time|"
                    r"uniqueidentifier|varbinary|binary|xml|sql_variant|sysname|hierarchyid|"
                    r"geography|geometry|image|text|ntext|rowversion|timestamp)\b",
                    t, re.IGNORECASE
                )
                if col_match:
                    columns.append({
                        "name": col_match.group(1),
                        "type": col_match.group(2),
                        "description": t
                    })
                elif t and len(t) > 15 and not t.startswith("https"):
                    columns.append({"name": "", "type": "", "description": t})

    return columns


def extract_permissions(pages: list[dict]) -> str:
    """Extract permissions section."""
    in_perms = False
    perm_texts = []
    for page_data in pages:
        for h in page_data.get("headings", []):
            tl = h.get("text", "").strip().lower()
            if "permission" in tl:
                in_perms = True
            elif in_perms and h["level"] <= 2:
                in_perms = False

        for p in page_data.get("paragraphs", []):
            if in_perms:
                t = clean_text(p.get("text", "")).strip()
                if t:
                    perm_texts.append(t)
    return " ".join(perm_texts) if perm_texts else ""


def extract_examples(pages: list[dict]) -> list[str]:
    """Extract example code blocks."""
    examples = []
    in_examples = False
    for page_data in pages:
        for h in page_data.get("headings", []):
            tl = h.get("text", "").strip().lower()
            if "example" in tl:
                in_examples = True
            elif in_examples and h["level"] <= 2:
                in_examples = False

        for cb in page_data.get("code_blocks", []):
            if in_examples and cb.strip():
                examples.append(cb.strip())

    return examples


def extract_description(pages: list[dict]) -> str:
    """Extract full description from first meaningful paragraphs."""
    desc_parts = []
    seen_desc_start = False

    for page_data in pages:
        for h in page_data.get("headings", []):
            tl = h.get("text", "").strip().lower()
            if tl in ("description", "remarks") and h["level"] <= 2:
                seen_desc_start = True
                continue
            if seen_desc_start and h["level"] <= 2 and tl not in ("remarks", "description"):
                seen_desc_start = False

        for p in page_data.get("paragraphs", []):
            t = clean_text(p.get("text", "")).strip()
            if not t or len(t) < 15:
                continue
            if seen_desc_start:
                desc_parts.append(t)
                if len(" ".join(desc_parts)) > 800:
                    break

    if not desc_parts:
        # Fallback: first non-trivial paragraph
        for page_data in pages:
            for p in page_data.get("paragraphs", []):
                t = clean_text(p.get("text", "")).strip()
                if len(t) >= 30:
                    desc_parts.append(t)
                    if len(" ".join(desc_parts)) > 400:
                        break
            if desc_parts:
                break

    return " ".join(desc_parts) if desc_parts else "(Content pending extraction)"


def extract_remarks(pages: list[dict]) -> str:
    """Extract full remarks section."""
    in_remarks = False
    parts = []
    for page_data in pages:
        for h in page_data.get("headings", []):
            tl = h.get("text", "").strip().lower()
            if tl == "remarks":
                in_remarks = True
            elif in_remarks and h["level"] <= 2:
                in_remarks = False

        if in_remarks:
            for p in page_data.get("paragraphs", []):
                t = clean_text(p.get("text", "")).strip()
                if t and len(t) > 10:
                    parts.append(t)

    return "\n\n".join(parts) if parts else ""


# -
# Content File Generation
# -

def build_frontmatter(fields: dict) -> str:
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
            sv = str(value)
            if "\n" in sv or "\r" in sv:
                # Multi-line value: use YAML literal block scalar
                lines.append(f"{key}: |")
                for line in sv.splitlines():
                    lines.append(f"  {line}")
            else:
                sv = sv.replace("'", "''")
                lines.append(f"{key}: '{sv}'")
    lines.append("---")
    return "\n".join(lines)


def write_content_file(output_dir: str, collection: str, slug: str, frontmatter: str, body: str) -> str:
    collection_dir = Path(output_dir) / collection
    collection_dir.mkdir(parents=True, exist_ok=True)
    filepath = collection_dir / f"{slug}.md"
    content = frontmatter + "\n\n" + body + "\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return str(filepath)


def generate_content_record(slug: str, obj: dict, collection: str) -> dict:
    return {
        "slug": slug,
        "name": obj.get("name", ""),
        "title": obj.get("title", obj.get("name", "")),
        "category": obj.get("category", "general"),
        "tags": obj.get("tags", []),
        "description": obj.get("description", "")[:150],
        "collection": collection,
    }


# -
# Object Processor
# -

def process_toc_object(
    obj: dict,
    collection: str,
    page_index: BatchPageIndex,
    content_output_dir: str,
) -> Optional[dict]:
    """Process a single TOC object: find pages, extract content, write file."""
    name = obj["name"]
    pages = page_index.find_pages(name)

    if not pages:
        # Try fuzzy match: search for the base name without sys. prefix
        base_name = name.replace("sys.", "", 1)
        all_pages = page_index.pages
        pages = []
        for p in all_pages:
            page_text = ""
            for h in p.get("headings", []):
                page_text += " " + h.get("text", "")
            if base_name in page_text.lower():
                pages.append(p)
                if len(pages) >= 5:  # Limit to 5 pages
                    break

    if not pages:
        return None

    # Sort pages by proximity to the named page
    target_page = obj.get("page")
    if target_page:
        pages.sort(key=lambda p: abs(p.get("page_number", 0) - target_page))

    # Extract full content
    syntax = extract_syntax_from_pages(pages)
    arguments = extract_arguments(pages)
    return_columns = extract_return_columns(pages)
    permissions = extract_permissions(pages)
    examples = extract_examples(pages)
    description = extract_description(pages)
    remarks = extract_remarks(pages)

    # Category inference
    if collection == "dmvs":
        category = infer_dmv_category(name)
        tags = [category, "dmv"]
    elif collection == "catalog-views":
        category = infer_catalog_category(name)
        tags = [category, "catalog-view"]
    elif collection == "stored-procedures":
        category = "general"
        tags = ["stored-procedure"]
    elif collection == "functions":
        category = infer_function_category(name)
        tags = [category, "function"]
    else:
        category = "general"
        tags = []

    # Build slug
    slug = generate_slug(name)

    # Build frontmatter - NO truncation, full depth
    frontmatter_fields = {
        "name": name,
        "title": obj.get("title", name),
        "category": category,
        "description": description[:400] if description else "(Content pending extraction)",
        "tags": tags,
        "pubDate": datetime.now(),
    }

    if syntax:
        frontmatter_fields["syntax"] = syntax

    # Build body - full content, no summaries
    body_parts = []

    if description:
        body_parts.append(f"## Description\n\n{description}\n")

    if syntax:
        body_parts.append(f"## Syntax\n\n```sql\n{syntax}\n```\n")

    if arguments:
        body_parts.append("## Arguments\n")
        for arg_text in arguments[:50]:  # Cap at 50 argument entries
            body_parts.append(f"{arg_text}\n\n")
        if len(arguments) > 50:
            body_parts.append(f"*(... and {len(arguments) - 50} more arguments)*\n")

    if return_columns:
        body_parts.append("## Return Columns\n")
        body_parts.append("| Column Name | Data Type | Description |\n")
        body_parts.append("|---|---|---|\n")
        for col in return_columns[:40]:
            cn = col.get("name", "") or "-"
            ct = col.get("type", "") or "-"
            cd = (col.get("description", "") or "")[:100]
            body_parts.append(f"| {cn} | {ct} | {cd} |\n")
        if len(return_columns) > 40:
            body_parts.append(f"\n*(... and {len(return_columns) - 40} more columns)*\n")

    if permissions:
        body_parts.append(f"## Permissions\n\n{permissions}\n")

    if remarks:
        body_parts.append(f"## Remarks\n\n{remarks}\n")

    if examples:
        body_parts.append("## Examples\n")
        for i, ex in enumerate(examples[:10], 1):
            body_parts.append(f"### Example {i}\n\n```sql\n{ex}\n```\n")
        if len(examples) > 10:
            body_parts.append(f"\n*(... and {len(examples) - 10} more examples)*\n")

    # Collect all code blocks not already captured
    all_code = []
    for page_data in pages:
        for cb in page_data.get("code_blocks", []):
            t = cb.strip()
            if t and t not in all_code and t != syntax and t not in examples:
                all_code.append(t)

    if all_code and not examples and not syntax:
        body_parts.append("## Code Blocks\n\n")
        for cb in all_code[:5]:
            body_parts.append(f"```sql\n{cb}\n```\n\n")

    body = "\n".join(body_parts).strip()
    if not body:
        body = "*(Content pending full extraction)*"

    fm = build_frontmatter(frontmatter_fields)
    filepath = write_content_file(content_output_dir, collection, slug, fm, body)

    # Update obj with description for search index
    obj["description"] = description[:150]

    return generate_content_record(slug, obj, collection)


# -
# Search Index Builder
# -

def build_search_index(records: list[dict], output_path: str) -> str:
    index = []
    seen = set()
    for rec in records:
        if not rec:
            continue
        slug = rec.get("slug", "")
        if slug in seen:
            continue
        seen.add(slug)
        index.append({
            "slug": slug,
            "name": rec.get("name", ""),
            "title": rec.get("title", ""),
            "category": rec.get("category", ""),
            "tags": rec.get("tags", []),
            "description": (rec.get("description", "") or "")[:150],
            "collection": rec.get("collection", ""),
        })

    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return str(output_path)


# -
# Main Pipeline
# -

def main():
    toc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "toc_index.json")
    batch_dir = sys.argv[1] if len(sys.argv) > 1 else "output"
    content_output_dir = sys.argv[2] if len(sys.argv) > 2 else "../site/src/content"
    search_index_path = sys.argv[3] if len(sys.argv) > 3 else "../site/src/data/search-index.json"

    print("=" * 70)
    print("  SCHEMA_MAPPER_V3 - TOC-Driven Mass Ingestion Engine")
    print("=" * 70)

    # Phase 1: Load TOC objects
    print("\n[Phase 1] Loading TOC object checklist...")
    if not os.path.exists(toc_path):
        print(f"  ERROR: TOC not found at {toc_path}")
        return
    toc_objects = extract_toc_objects(toc_path)
    for coll, objs in toc_objects.items():
        print(f"  {coll}: {len(objs)} objects in TOC")

    # Phase 2: Build page index
    print("\n[Phase 2] Building page index from batch files...")
    page_index = BatchPageIndex(batch_dir)

    # Phase 3: Process each collection
    print("\n[Phase 3] Processing TOC objects...")
    all_records = []
    collection_stats = defaultdict(lambda: {"found": 0, "not_found": 0, "errors": 0})

    for collection in ["dmvs", "catalog-views", "stored-procedures", "functions"]:
        objs = toc_objects.get(collection, [])
        if not objs:
            continue

        print(f"\n  - Processing {collection} ({len(objs)} objects) -")

        # Load existing content names to avoid overwriting
        existing_dir = Path(content_output_dir) / collection
        existing_names = set()
        if existing_dir.exists():
            for f in existing_dir.glob("*.md"):
                existing_names.add(f.stem.lower())

        new_count = 0
        existing_count = 0

        for i, obj in enumerate(objs):
            name = obj["name"]
            slug = generate_slug(name)

            if slug in existing_names:
                existing_count += 1
                continue

            try:
                rec = process_toc_object(obj, collection, page_index, content_output_dir)
                if rec:
                    all_records.append(rec)
                    collection_stats[collection]["found"] += 1
                    new_count += 1
                else:
                    collection_stats[collection]["not_found"] += 1
            except Exception as e:
                collection_stats[collection]["errors"] += 1
                print(f"    [ERROR] {name}: {e}")

            if (i + 1) % 50 == 0:
                print(f"    Progress: {i+1}/{len(objs)} (found {collection_stats[collection]['found']} new)")

        print(f"    Done: {new_count} new, {existing_count} already exist")

    # Phase 4: Preserve existing content (merge, don't replace)
    print("\n[Phase 4] Merging with existing content...")
    existing_records_count = 0
    for collection in ["dmvs", "catalog-views", "stored-procedures", "functions", "architecture",
                        "errors", "tsql-reference", "wait-statistics"]:
        coll_dir = Path(content_output_dir) / collection
        if not coll_dir.exists():
            continue
        for md_file in coll_dir.glob("*.md"):
            slug = md_file.stem
            # Check if already in new records
            if not any(r.get("slug") == slug for r in all_records):
                # Quick frontmatter parse
                content = md_file.read_text(encoding="utf-8")
                name_m = re.search(r"^name:\s+'(.+?)'", content, re.MULTILINE)
                title_m = re.search(r"^title:\s+'(.+?)'", content, re.MULTILINE)
                cat_m = re.search(r"^category:\s+'(.+?)'", content, re.MULTILINE)
                desc_m = re.search(r"^description:\s+'(.+?)'", content, re.MULTILINE)
                tags_m = re.search(r"^tags:\s+(\[.+?\])", content, re.MULTILINE)

                if name_m:
                    all_records.append({
                        "slug": slug,
                        "name": name_m.group(1),
                        "title": title_m.group(1) if title_m else name_m.group(1),
                        "category": cat_m.group(1) if cat_m else "general",
                        "tags": json.loads(tags_m.group(1)) if tags_m else [],
                        "description": (desc_m.group(1) if desc_m else "")[:150],
                        "collection": collection,
                    })
                    existing_records_count += 1

    print(f"  Existing records preserved: {existing_records_count}")

    # Phase 5: Build search index
    print("\n[Phase 5] Building search index...")
    built_path = build_search_index(all_records, search_index_path)
    print(f"  Search index: {built_path} ({len(all_records)} total records)")

    # Final summary
    print(f"\n{'=' * 70}")
    print(f"  INGESTION SUMMARY")
    print(f"{'=' * 70}")
    print(f"\n  Collection breakdown:")
    for coll in ["dmvs", "catalog-views", "stored-procedures", "functions"]:
        s = collection_stats[coll]
        print(f"    {coll:20s}  found: {s['found']:>4}  not found: {s['not_found']:>4}  errors: {s['errors']}")

    # Count total files per collection
    print(f"\n  Final content file counts:")
    for coll in sorted(SECTION_COLLECTION_MAP.values()):
        coll_dir = Path(content_output_dir) / coll
        count = len(list(coll_dir.glob("*.md"))) if coll_dir.exists() else 0
        print(f"    {coll}: {count}")

    print(f"\n  Search index: {len(all_records)} records")
    print(f"\n{'=' * 70}")
    print(f"  Pipeline complete. Run 'cd site && npm run build' next.")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
