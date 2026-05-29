"""
operations_mapper.py — v0.5.0 Operations Content Ingestion Engine

Extracts operational/admin content from Range 2 batch JSON files (p.14419-20029)
and maps them into src/content/operations/ with correct topic assignments.

H2 section -> topic mapping for 11 operational chapters:
  - SSB Diagnose                    -> ssb-diagnose
  - SSMS                             -> ssms
  - SqlPackage                      -> sqlpackage
  - SQL Server Profiler              -> profiler
  - SQL Server on Linux              -> linux-operations
  - Azure Synapse Analytics          -> azure-synapse
  - Azure Arc-enabled data services  -> azure-arc
  - Event classes                    -> event-classes
  - Database Engine tutorial         -> configuration
  - Writing T-SQL Statements         -> configuration
  - Offline SQL Server documentation -> monitor (or configuration)

Usage:
  python operations_mapper.py
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
OPS_DIR = CONTENT_DIR / "operations"

# -- Range 2 page boundaries --
R2_START = 14419
R2_END = 20029

# -- H2 section -> topic mapping for operations --
# Keyed by lowercase H2 title prefix (matched via .startswith)
H2_OPS_TOPIC_MAP = {
    "ssb diagnose": "ssb-diagnose",
    "sql server management studio": "ssms",
    "sqlpackage": "sqlpackage",
    "sql server profiler": "profiler",
    "what is sql server on linux": "linux-operations",
    "azure synapse analytics": "azure-synapse",
    "azure arc-enabled data services": "azure-arc",
    "event classes": "event-classes",
    "database engine": "configuration",
    "writing t-sql statements": "configuration",
    "offline sql server documentation": "monitor",
}

# Pages that should be skipped (navigation, appends, etc.)
SKIP_PAGE_TITLES = {
    "in this article", "see also", "next steps", "prerequisites",
    "additional resources", "related content", "related tasks",
    "related sections", "feedback", "submit and view feedback for",
    "contents", "overview", "introduction",
}

# Batch file prefixes for Range 2 operations content
OPS_BATCH_PREFIXES = [
    "operations-tools",
    "operations-ssb",
    "operations-ssms",
    "operations-sqlpackage",
    "operations-profiler",
    "operations-dbe-tutorial",
    "operations-linux",
    "operations-synapse",
    "operations-arc-docs",
    "operations-eventclasses",
    "operations-misc",
]

# -- Helpers --

def slugify(text: str) -> str:
    """Convert heading text to a URL-friendly slug."""
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def find_batch_files(prefixes: list[str]) -> list[Path]:
    """Find all batch JSON files matching any of the given prefixes, sorted."""
    files = []
    for prefix in prefixes:
        files.extend(sorted(BATCH_DIR.glob(f"{prefix}_p*.json")))
    return sorted(set(files))


def load_batch_pages(prefixes: list[str]) -> list[dict]:
    """Load all pages from batch files with given prefixes."""
    pages = []
    for bf in find_batch_files(prefixes):
        try:
            with open(bf, "r", encoding="utf-8") as f:
                pages.extend(json.load(f))
        except Exception as e:
            print(f"  WARN: Could not load {bf.name}: {e}")
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


def tidy_code_block(code: str) -> str:
    """Clean up a code block - dedent, strip leading/trailing whitespace."""
    lines = code.split("\n")
    # Remove common leading whitespace
    if lines:
        min_indent = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
        if min_indent > 0:
            lines = [l[min_indent:] if l.strip() else l for l in lines]
    return "\n".join(lines).strip()


# -- Topic resolution --


def resolve_topic(parent_h2_title: str, entry_title: str, entry_page: int) -> str:
    """Resolve the operations topic for a TOC entry based on its parent H2."""
    key = parent_h2_title.lower().strip()
    # Direct H2 match
    for h2_prefix, topic in H2_OPS_TOPIC_MAP.items():
        if key.startswith(h2_prefix):
            return topic
    # Fallback: heuristic from title keywords
    title_lower = entry_title.lower()
    if any(kw in title_lower for kw in ["ssb", "service broker", "dialog", "conversation"]):
        return "ssb-diagnose"
    if any(kw in title_lower for kw in ["ssms", "management studio", "object explorer"]):
        return "ssms"
    if "sqlpackage" in title_lower or "dacpac" in title_lower or "bacpac" in title_lower:
        return "sqlpackage"
    if "profiler" in title_lower or "trace" in title_lower:
        return "profiler"
    if "linux" in title_lower:
        return "linux-operations"
    if "synapse" in title_lower:
        return "azure-synapse"
    if "azure arc" in title_lower:
        return "azure-arc"
    if "event class" in title_lower or "event subclass" in title_lower:
        return "event-classes"
    if any(kw in title_lower for kw in ["tutorial", "writing", "statements"]):
        return "configuration"
    # Misc / offline docs -> best guess
    if any(kw in title_lower for kw in ["monitor", "monitoring", "alert", "performance"]):
        return "monitor"
    if any(kw in title_lower for kw in ["upgrade", "migration", "migrate"]):
        return "upgrade"
    if any(kw in title_lower for kw in ["backup", "restore", "availability", "always on", "ha"]):
        return "high-availability"
    if any(kw in title_lower for kw in ["tool", "utility", "command", "config"]):
        return "configuration"
    if any(kw in title_lower for kw in ["data tool", "ssdt", "visual studio"]):
        return "data-tools"
    # Default
    return "configuration"


# ============================================================
# MAIN EXTRACTION
# ============================================================

def extract_operations():
    """Extract operations articles from Range 2 batch files."""
    print("\n" + "=" * 60)
    print("PHASE: OPERATIONS EXTRACTION (p.14419-20029)")
    print("=" * 60)

    # Load TOC
    with open(TOC_PATH, "r", encoding="utf-8") as f:
        toc = json.load(f)

    # Find all Range 2 TOC entries
    r2_toc = [e for e in toc if e.get("page") and R2_START <= e["page"] <= R2_END]
    print(f"  Range 2 TOC entries: {len(r2_toc)}")

    # Load all operations batch pages
    all_pages = load_batch_pages(OPS_BATCH_PREFIXES)
    pages_by_num = {p["page_number"]: p for p in all_pages}

    # Also load existing errors pages for the overlap region (p.17659-19458)
    # This covers "Offline SQL Server documentation" H2 which overlaps with our errors section
    try:
        error_files = sorted(BATCH_DIR.glob("errors_p*.json"))
        for ef in error_files:
            with open(ef, "r", encoding="utf-8") as f:
                for pg in json.load(f):
                    pn = pg["page_number"]
                    if pn not in pages_by_num:
                        pages_by_num[pn] = pg
        print(f"  Merged {len(error_files)} error batch files for overlap coverage")
    except Exception as e:
        print(f"  WARN: Could not load error batch files: {e}")

    # Group TOC entries by H2 section
    # We maintain a stack to track the current H2 for each page range
    h2_sections = []
    current_h2 = None
    current_h2_page = None
    current_entries = []

    for e in r2_toc:
        if e["depth"] == 2:
            if current_h2:
                h2_sections.append((current_h2, current_h2_page, current_entries))
            current_h2 = e["title"]
            current_h2_page = e.get("page")
            current_entries = []
        elif e["depth"] >= 3 and current_h2:
            current_entries.append(e)

    # Flush last H2
    if current_h2:
        h2_sections.append((current_h2, current_h2_page, current_entries))

    # Also handle depth-3+ entries before the first H2 (p.14419-14676 tools/config)
    pre_h2_entries = [e for e in r2_toc if e["depth"] >= 3 and e.get("page", 0) < 14677]
    if pre_h2_entries and (not h2_sections or h2_sections[0][1] != 14677):
        h2_sections.insert(0, ("Command-line Tools & Configuration", 14419, pre_h2_entries))

    print(f"  H2 sections found: {len(h2_sections)}")

    count = 0
    topic_counts = defaultdict(int)
    slug_counts = defaultdict(int)

    for h2_title, h2_page, entries in h2_sections:
        print(f"\n  H2: {h2_title} (p.{h2_page}) -> {len(entries)} entries")

        for entry in entries:
            title = entry["title"].strip()
            page_num = entry.get("page")
            depth = entry["depth"]

            if not page_num or title.lower() in SKIP_PAGE_TITLES:
                continue

            # Skip very short or navigation-only entries
            if len(title) < 3:
                continue

            # Resolve topic
            topic = resolve_topic(h2_title, title, page_num)

            # Generate slug
            slug = slugify(title)

            # Ensure uniqueness
            if slug in slug_counts:
                slug_counts[slug] += 1
                slug = f"{slug}-{slug_counts[slug]}"
            else:
                slug_counts[slug] = 1

            # Get page content
            page = pages_by_num.get(page_num)
            if not page:
                # Try nearby pages
                for delta in range(1, 6):
                    page = pages_by_num.get(page_num + delta)
                    if page:
                        break
                if not page:
                    for delta in range(1, 6):
                        page = pages_by_num.get(page_num - delta)
                        if page:
                            break
            if not page:
                continue

            body_text = extract_body_text(page)
            code_blocks = extract_code_blocks(page)

            # Build article body
            body_parts = []
            if body_text:
                body_parts.append(body_text)
            if code_blocks:
                tidied_blocks = []
                for cb in code_blocks[:5]:  # max 5 code blocks per article
                    tc = tidy_code_block(cb)
                    if tc:
                        tidied_blocks.append(tc)
                if tidied_blocks:
                    body_parts.append("\n".join(["```cmd"] + tidied_blocks + ["```"]))

            body = "\n\n".join(body_parts) if body_parts else f"Operational guide: {title}."

            # Build frontmatter
            desc = body_text[:200] if body_text else f"SQL Server operations guide: {title}"
            frontmatter = {
                "title": title,
                "topic": topic,
                "description": desc[:250],
                "tags": [topic, slug],
                "pubDate": datetime(2025, 12, 1),
            }

            fpath = OPS_DIR / f"{slug}.md"
            # Don't overwrite index.md
            if slug == "index":
                fpath = OPS_DIR / f"op-{slug}.md"
            if not fpath.exists():
                write_content_file(fpath, frontmatter, body)
                count += 1
                topic_counts[topic] += 1

    print(f"\n  Created {count} operations articles")
    print("\n  By topic:")
    for topic in sorted(topic_counts.keys()):
        print(f"    {topic}: {topic_counts[topic]}")

    return count, topic_counts


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("OPERATIONS MAPPER --- v0.5.0")
    print("=" * 60)

    print("\n  Cleaning existing operations content (except index.md)...")
    if OPS_DIR.exists():
        existing = list(OPS_DIR.glob("*.md"))
        for f in existing:
            if f.name != "index.md":
                f.unlink()
        print(f"  Removed {len(existing) - 1} existing files")

    total, topic_counts = extract_operations()

    print("\n" + "=" * 60)
    print("EXTRACTION SUMMARY")
    print("=" * 60)
    print(f"  Total new files:  {total}")
    for topic in sorted(topic_counts.keys()):
        print(f"    {topic}: {topic_counts[topic]}")
    print("=" * 60)


if __name__ == "__main__":
    main()
