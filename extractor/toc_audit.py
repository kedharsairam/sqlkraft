"""
toc_audit.py - Exhaustive TOC Dictionary Audit & Gap Matrix

Reads toc_index.json (7,783 entries) and extracts EVERY database object
reference. Compiles a definitive target checklist per collection type
and prints the true gap matrix vs. current extraction.

Usage:
    python toc_audit.py [--toc output/toc_index.json] [--content ../site/src/content]
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

# -
# Regex patterns for object name extraction
# -

DMV_PATTERN = re.compile(r"(?:sys\.)?dm_[a-z_0-9]+", re.IGNORECASE)
CATALOG_VIEW_PATTERN = re.compile(r"sys\.([a-z_][a-z_0-9]+)", re.IGNORECASE)
SP_PATTERN = re.compile(r"(?:sys\.)?sp_[a-z_0-9]+", re.IGNORECASE)
FN_PATTERN = re.compile(r"(?:sys\.)?fn_[a-z_0-9]+", re.IGNORECASE)

# Bare object name patterns (without sys. prefix but clearly DB objects)
BARE_DMV = re.compile(r"^dm_[a-z_0-9]+$", re.IGNORECASE)
BARE_SP = re.compile(r"^sp_[a-z_0-9]+$", re.IGNORECASE)
BARE_FN = re.compile(r"^fn_[a-z_0-9]+$", re.IGNORECASE)

# T-SQL statement/keyword patterns
TSQL_STATEMENT_PATTERN = re.compile(
    r"^(SELECT|INSERT|UPDATE|DELETE|MERGE|CREATE|ALTER|DROP|GRANT|DENY|"
    r"REVOKE|BACKUP|RESTORE|DBCC|SET|DECLARE|BEGIN|COMMIT|ROLLBACK|"
    r"SAVE|TRUNCATE|EXECUTE|EXEC|OPEN|CLOSE|FETCH|CURSOR|IF|ELSE|WHILE|"
    r"BREAK|CONTINUE|WAITFOR|PRINT|RAISERROR|THROW|TRY|CATCH|RETURN|"
    r"WITH|USE|GO|SHUTDOWN|KILL|RECONFIGURE|CHECKPOINT|BULK\s+INSERT|"
    r"READTEXT|WRITETEXT|UPDATETEXT|FREETEXT|CONTAINSTABLE|FREETEXTTABLE|"
    r"OPENQUERY|OPENROWSET|OPENDATASOURCE|OPENXML|SP\$)"
    r"(?:\s|$)", re.IGNORECASE
)

# Wait type patterns
WAIT_TYPE_PATTERN = re.compile(r"^[a-z_]+(?:_[a-z_]+)*_wait", re.IGNORECASE)
WAIT_TYPE_BARE = re.compile(r"^[a-z_]+(?:_[a-z_]+)*$", re.IGNORECASE)

# -
# Section boundary detection (from TOC depth/title)
# -

SECTION_MARKERS = {
    "dynamic management": "dmvs",
    "catalog view": "catalog-views",
    "system functions": "functions",
    "system stored procedures": "stored-procedures",
    "system tables": "catalog-views",
    "compatibility view": "catalog-views",
    "errors": "errors",
    "wait": "wait-statistics",
    "transact-sql": "tsql-reference",
    "t-sql": "tsql-reference",
    "xquery": "tsql-reference",
    "architecture": "architecture",
}

# -
# TOC parsing
# -

def load_toc(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def identify_section_context(toc: list[dict]) -> list[dict]:
    """
    Walk the TOC tree and tag each entry with the active section context.
    Entries inherit context from parent depth-1/depth-2 entries.
    """
    enriched = []
    current_section = None
    current_subsection = None

    for entry in toc:
        d = entry["depth"]
        title = entry["title"]
        page = entry.get("page")

        if d == 1:
            current_section = title
            current_subsection = None
        elif d == 2:
            current_subsection = title

        # Determine collection type from section/subsection
        section_context = None
        combined = (current_section or "") + " " + (current_subsection or "")
        combined_lower = combined.lower()

        for marker, collection in SECTION_MARKERS.items():
            if marker in combined_lower:
                section_context = collection
                break

        enriched.append({
            "depth": d,
            "title": title,
            "page": page,
            "section": current_section,
            "subsection": current_subsection,
            "context": section_context,
        })

    return enriched


# -
# Object extraction from TOC entries
# -

def extract_objects(enriched_toc: list[dict]) -> dict:
    """
    Extract all database object references from enriched TOC entries.
    Returns dict of collection -> list of object dicts.
    """
    objects = {
        "dmvs": [],
        "catalog-views": [],
        "stored-procedures": [],
        "functions": [],
        "tsql-reference": [],
        "errors": [],
        "wait-statistics": [],
        "architecture": [],
    }

    seen_names = defaultdict(set)  # collection -> set of names (for dedup)

    for entry in enriched_toc:
        title = entry["title"]
        context = entry["context"]
        page = entry["page"]

        # - DMVs -
        dmv_match = DMV_PATTERN.search(title)
        bare_dmv = BARE_DMV.match(title)
        if dmv_match:
            name = dmv_match.group(0).lower()
            if not name.startswith("sys."):
                name = "sys." + name
            if name not in seen_names["dmvs"]:
                seen_names["dmvs"].add(name)
                objects["dmvs"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })
        elif bare_dmv and context == "dmvs":
            name = "sys." + bare_dmv.group(0).lower()
            if name not in seen_names["dmvs"]:
                seen_names["dmvs"].add(name)
                objects["dmvs"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })

        # - Catalog Views -
        cv_match = CATALOG_VIEW_PATTERN.search(title)
        if cv_match and "dm_" not in title.lower() and "sp_" not in title.lower() and "fn_" not in title.lower():
            name = "sys." + cv_match.group(1).lower()
            if name not in seen_names["catalog-views"] and name not in seen_names["dmvs"]:
                seen_names["catalog-views"].add(name)
                objects["catalog-views"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })

        # - Stored Procedures -
        sp_match = SP_PATTERN.search(title)
        bare_sp = BARE_SP.match(title)
        if sp_match:
            name = sp_match.group(0).lower()
            if not name.startswith("sys."):
                name = "sys." + name
            if name not in seen_names["stored-procedures"]:
                seen_names["stored-procedures"].add(name)
                objects["stored-procedures"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })
        elif bare_sp and context in ("stored-procedures", "functions"):
            name = "sys." + bare_sp.group(0).lower()
            if name not in seen_names["stored-procedures"]:
                seen_names["stored-procedures"].add(name)
                objects["stored-procedures"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })

        # - Functions -
        fn_match = FN_PATTERN.search(title)
        bare_fn = BARE_FN.match(title)
        if fn_match and "sp_" not in title.lower():
            name = fn_match.group(0).lower()
            if not name.startswith("sys."):
                name = "sys." + name
            if name not in seen_names["functions"]:
                seen_names["functions"].add(name)
                objects["functions"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })
        elif bare_fn and context == "functions":
            name = "sys." + bare_fn.group(0).lower()
            if name not in seen_names["functions"]:
                seen_names["functions"].add(name)
                objects["functions"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })

        # - T-SQL Reference -
        tsql_match = TSQL_STATEMENT_PATTERN.match(title)
        if tsql_match and context == "tsql-reference":
            name = tsql_match.group(0).strip().lower()
            if name not in seen_names["tsql-reference"]:
                seen_names["tsql-reference"].add(name)
                objects["tsql-reference"].append({
                    "name": name,
                    "title": title,
                    "page": page,
                    "context": context,
                })

        # - Errors -
        if context == "errors" and page:
            err_match = re.search(r"(\d{4,5})", title)
            if err_match:
                err_num = err_match.group(1)
                if err_num not in seen_names["errors"]:
                    seen_names["errors"].add(err_num)
                    objects["errors"].append({
                        "name": err_num,
                        "title": title,
                        "page": page,
                        "context": context,
                    })

        # - Architecture -
        if context == "architecture" and entry["depth"] >= 2 and page:
            if title not in seen_names["architecture"]:
                seen_names["architecture"].add(title)
                objects["architecture"].append({
                    "name": title,
                    "title": title,
                    "page": page,
                    "context": context,
                })

    return objects


# -
# Current extraction audit
# -

def count_extracted(content_dir: str) -> dict:
    """Count currently extracted markdown files per collection."""
    counts = {}
    content_path = Path(content_dir)
    if not content_path.exists():
        return counts
    for coll_dir in content_path.iterdir():
        if coll_dir.is_dir():
            count = len(list(coll_dir.glob("*.md")))
            counts[coll_dir.name] = count
    return counts


def extract_names_from_md(content_dir: str, collection: str) -> set:
    """Extract 'name' field from frontmatter of all files in a collection."""
    names = set()
    coll_path = Path(content_dir) / collection
    if not coll_path.exists():
        return names
    for md_file in coll_path.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        name_match = re.search(r"^name:\s+'(.+?)'", content, re.MULTILINE)
        if name_match:
            names.add(name_match.group(1).lower())
        else:
            # Fallback: use filename without extension
            names.add(md_file.stem.lower())
    return names


# -
# Gap matrix printer
# -

def print_gap_matrix(toc_objects: dict, extracted_counts: dict, content_dir: str):
    """Print the definitive gap matrix."""
    print("=" * 80)
    print("  SQLKRAFT - EXHAUSTIVE TOC DICTIONARY AUDIT")
    print("=" * 80)

    total_in_pdf = 0
    total_extracted = 0
    total_gap = 0

    collections = [
        ("dmvs", "Dynamic Management Views (sys.dm_*)"),
        ("catalog-views", "Catalog Views (sys.*)"),
        ("stored-procedures", "System Stored Procedures (sys.sp_*)"),
        ("functions", "System Functions (sys.fn_*)"),
        ("tsql-reference", "T-SQL Statements & Keywords"),
        ("errors", "Error Codes"),
        ("wait-statistics", "Wait Statistics"),
        ("architecture", "Architecture / Narrative"),
    ]

    for key, label in collections:
        in_pdf = len(toc_objects.get(key, []))
        extracted = extracted_counts.get(key, 0)
        gap = max(0, in_pdf - extracted)

        # For extracted, also check actual name matches
        extracted_names = extract_names_from_md(content_dir, key)
        pdf_names = set(o["name"].lower() for o in toc_objects.get(key, []))
        overlap = len(extracted_names & pdf_names)

        total_in_pdf += in_pdf
        total_extracted += extracted
        total_gap += gap

        print(f"\n  {'-' * 70}")
        print(f"  [{key}] {label}")
        print(f"  {'-' * 70}")
        print(f"    In PDF (TOC):        {in_pdf:>5}")
        print(f"    Currently extracted:  {extracted:>5}  ({overlap} name-matched)")
        print(f"    GAP:                  {gap:>5}  ({gap/in_pdf*100:.1f}% of PDF)" if in_pdf > 0 else f"    GAP:                  {gap:>5}")

        if gap > 0 and in_pdf > 0:
            missing = pdf_names - extracted_names
            print(f"    Missing items ({min(len(missing), 20)} shown):")
            for i, m in enumerate(sorted(missing)[:20]):
                # Find page number
                page_info = ""
                for obj in toc_objects[key]:
                    if obj["name"].lower() == m:
                        page_info = f" (p.{obj['page']})" if obj.get("page") else ""
                        break
                print(f"      {i+1:>3}. {m}{page_info}")
            if len(missing) > 20:
                print(f"      ... and {len(missing) - 20} more")

    print(f"\n  {'=' * 70}")
    print(f"  TOTALS:")
    print(f"    In PDF (TOC entries):    {total_in_pdf:>6}")
    print(f"    Currently extracted:     {total_extracted:>6}")
    print(f"    TOTAL GAP:               {total_gap:>6}")
    if total_in_pdf > 0:
        print(f"    Coverage:                {(total_extracted/total_in_pdf*100):.1f}%")
    print(f"  {'=' * 70}")

    return total_in_pdf, total_extracted, total_gap


# -
# Untapped page range report
# -

def print_untapped_ranges(toc: list[dict]):
    """Report page ranges that have TOC entries but were never batch-extracted."""
    pdf_path = r"C:\Users\kedhar\Desktop\sql-sql-server-ver17.pdf"

    # Already extracted page ranges
    extracted_ranges = [
        (5666, 6112),     # architecture
        (17659, 19458),   # errors
        (20031, 20722),   # catalog-views
        (20800, 21566),   # dmvs
        (21567, 24519),   # functions
        (24862, 30180),   # tsql-reference
    ]

    def is_extracted(page):
        if page is None:
            return True
        for s, e in extracted_ranges:
            if s <= page <= e:
                return True
        return False

    # Aggregate page ranges of TOC entries that are NOT extracted
    untapped = []
    for entry in toc:
        page = entry.get("page")
        if page and not is_extracted(page):
            untapped.append(entry)

    if not untapped:
        print("\n  No untapped TOC entries found.")
        return []

    # Group into continuous page ranges
    untapped.sort(key=lambda x: x["page"] or 0)
    ranges = []
    current_start = None
    current_end = None

    for entry in untapped:
        p = entry["page"]
        if current_start is None:
            current_start = p
            current_end = p
        elif p <= current_end + 3:  # Allow small gaps (3 page threshold)
            current_end = max(current_end, p)
        else:
            ranges.append((current_start, current_end))
            current_start = p
            current_end = p

    if current_start is not None:
        ranges.append((current_start, current_end))

    print(f"\n  {'-' * 70}")
    print(f"  UNTAPPED PAGE RANGES ({len(ranges)} ranges, {len(untapped)} TOC entries)")
    print(f"  {'-' * 70}")

    total_untapped_pages = 0
    for s, e in ranges:
        count = e - s + 1
        # Sample titles in this range
        sample_titles = [x["title"] for x in untapped if s <= (x["page"] or 0) <= e][:5]
        total_untapped_pages += count
        print(f"\n    p.{s}-{e} ({count} pages)")
        for t in sample_titles:
            print(f"      - {t[:90]}")
        if count > 5:
            print(f"      ... and {count - 5} more pages")

    print(f"\n  Total untapped pages: {total_untapped_pages}")
    return ranges


# -
# Object page range extraction (for nested re-extraction)
# -

def print_page_range_breakdown(toc_objects: dict):
    """For each collection, show the page ranges where objects live."""
    print(f"\n  {'-' * 70}")
    print(f"  OBJECT PAGE RANGES (for targeted extraction)")
    print(f"  {'-' * 70}")

    for collection, objects in toc_objects.items():
        if not objects:
            continue
        pages = sorted([o["page"] for o in objects if o.get("page")])
        if not pages:
            continue
        print(f"\n    [{collection}] {len(objects)} objects across p.{pages[0]}-{pages[-1]}")
        # Show gaps
        if len(pages) > 1:
            gaps = []
            for i in range(1, len(pages)):
                gap = pages[i] - pages[i - 1]
                if gap > 50:
                    gaps.append(f"  p.{pages[i-1]}-{pages[i]} ({gap}pg gap)")
            if gaps:
                for g in gaps[:5]:
                    print(f"      Gap: {g}")


# -
# Main
# -

def main():
    toc_path = sys.argv[1] if len(sys.argv) > 1 else "output/toc_index.json"
    content_dir = sys.argv[2] if len(sys.argv) > 2 else "../site/src/content"

    print(f"[toc_audit] Loading TOC from {toc_path}...")
    toc = load_toc(toc_path)
    print(f"[toc_audit] {len(toc)} entries loaded.")

    print(f"[toc_audit] Enriching with section context...")
    enriched = identify_section_context(toc)

    print(f"[toc_audit] Extracting database objects from TOC...")
    toc_objects = extract_objects(enriched)

    # Count per collection
    for coll, objs in toc_objects.items():
        print(f"  {coll}: {len(objs)}")

    print(f"[toc_audit] Counting current extraction from {content_dir}...")
    extracted_counts = count_extracted(content_dir)
    for coll, count in sorted(extracted_counts.items()):
        print(f"  {coll}: {count} files")

    print(f"\n")
    total_in_pdf, total_extracted, total_gap = print_gap_matrix(toc_objects, extracted_counts, content_dir)

    print(f"\n{'=' * 80}")
    print(f"  UNTAPPED PAGE RANGES")
    print(f"{'=' * 80}")
    untapped_ranges = print_untapped_ranges(toc)

    print(f"\n{'=' * 80}")
    print(f"  OBJECT PAGE RANGE BREAKDOWN")
    print(f"{'=' * 80}")
    print_page_range_breakdown(toc_objects)

    print(f"\n{'=' * 80}")
    print(f"  RECOMMENDED ACTIONS")
    print(f"{'=' * 80}")

    # Compile recommendations
    for collection in ["dmvs", "catalog-views", "stored-procedures", "functions"]:
        in_pdf = len(toc_objects.get(collection, []))
        extracted = extracted_counts.get(collection, 0)
        gap = max(0, in_pdf - extracted)
        if gap > 0:
            print(f"\n  [{collection}] Re-extract with improved parser:")
            print(f"    Gap: {in_pdf} in PDF vs {extracted} extracted ({gap} missing)")
            print(f"    Action: Run schema_mapper_v2.py with parser improvements")

    for s, e in untapped_ranges:
        print(f"\n  [p.{s}-{e}] Extract this untapped page range:")
        print(f"    Action: python page_extractor.py --pages {s}-{e} --section new-section")

    print(f"\n{'=' * 80}\n")


if __name__ == "__main__":
    main()
