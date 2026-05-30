"""
sweep_mapper.py — Phase 5 Final Sweep Operations Mapper

Processes three new page ranges (HA, Upgrade, Migration) plus fixes
misclassified entries (SSDT -> data-tools, Azure Arc -> azure-arc).

Runs after operations_mapper.py — adds/overwrites, never clears.

Usage:
  python sweep_mapper.py
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

# Less aggressive skip set — keeps "overview" and "introduction" entries
SKIP_PAGE_TITLES = {
    "in this article", "see also", "next steps", "prerequisites",
    "additional resources", "related content", "related tasks",
    "related sections", "feedback", "submit and view feedback for",
    "contents",
}

# -- Phase 5 target ranges --
# (start_page, end_page, topic, batch_prefix)
NEW_RANGES = [
    (866, 2043, "high-availability", "ops-ha"),
    (6442, 6655, "upgrade", "ops-upgrade"),
    (7155, 7398, "migration", "ops-migration"),
]

# -- Page-range overrides for existing Range 2 misclassified entries --
# (start_page, end_page, override_topic, keyword_list)
OVERRIDES = [
    # SSDT entries under SSB Diagnose H2 -> reclassify to data-tools
    (14702, 15077, "data-tools", ["data tool", "ssdt", "visual studio"]),
    # Azure Arc entries under Azure Synapse H2 -> reclassify to azure-arc
    (17071, 17573, "azure-arc", ["azure arc"]),
]

# Range 2 batch prefixes (for loading existing content for overrides)
R2_BATCH_PREFIXES = [
    "operations-tools", "operations-ssb", "operations-ssms",
    "operations-sqlpackage", "operations-profiler", "operations-dbe-tutorial",
    "operations-linux", "operations-synapse", "operations-arc-docs",
    "operations-eventclasses", "operations-misc",
]


# -- Helpers (mirror operations_mapper.py) --

def load_batch_pages(prefixes):
    """Load all pages from batch files matching any prefix."""
    pages = []
    for prefix in prefixes:
        for bf in sorted(BATCH_DIR.glob(f"{prefix}_p*.json")):
            try:
                with open(bf, "r", encoding="utf-8") as f:
                    pages.extend(json.load(f))
            except Exception as e:
                print(f"  WARN: Could not load {bf.name}: {e}")
    return sorted(pages, key=lambda p: p["page_number"])


def extract_body_text(page):
    lines = []
    for p in page.get("paragraphs", []):
        text = p.get("text", "").strip()
        if text and text.lower() not in SKIP_PAGE_TITLES:
            lines.append(text)
    return "\n\n".join(lines)


def extract_code_blocks(page):
    return page.get("code_blocks", [])


def tidy_code_block(code):
    lines = code.split("\n")
    if lines:
        min_indent = min(
            (len(l) - len(l.lstrip())) for l in lines if l.strip()
        ) if any(l.strip() for l in lines) else 0
        if min_indent > 0:
            lines = [l[min_indent:] if l.strip() else l for l in lines]
    return "\n".join(lines).strip()


def build_frontmatter(fields):
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


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def write_content_file(filepath, frontmatter, body):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    content = build_frontmatter(frontmatter) + "\n\n" + body.strip()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("SWEEP MAPPER — Phase 5 Final Sweep")
    print("=" * 60)

    # Load TOC
    with open(TOC_PATH, "r", encoding="utf-8") as f:
        toc = json.load(f)
    print(f"  TOC entries loaded: {len(toc)}")

    # Load ALL batch pages (new ranges + existing Range 2 + errors)
    all_pages = {}

    # New ranges
    new_prefixes = [r[3] for r in NEW_RANGES]
    for p in load_batch_pages(new_prefixes):
        all_pages[p["page_number"]] = p
    print(f"  New range pages loaded: {len([r for r in NEW_RANGES])} prefixes")

    # Range 2 existing files (for overrides)
    for p in load_batch_pages(R2_BATCH_PREFIXES):
        if p["page_number"] not in all_pages:
            all_pages[p["page_number"]] = p

    # Error batch files (overlap coverage)
    for ef in sorted(BATCH_DIR.glob("errors_p*.json")):
        try:
            with open(ef, "r", encoding="utf-8") as f:
                for pg in json.load(f):
                    pn = pg["page_number"]
                    if pn not in all_pages:
                        all_pages[pn] = pg
        except Exception as e:
            print(f"  WARN: Could not load {ef.name}: {e}")

    print(f"  Total unique pages available: {len(all_pages)}")

    slug_counts = defaultdict(int)
    total_created = 0
    topic_counts = defaultdict(int)

    # ---- Step 1: Process new ranges (HA, Upgrade, Migration) ----
    for start_page, end_page, topic, prefix in NEW_RANGES:
        range_entries = [
            e for e in toc
            if e.get("page")
            and start_page <= e["page"] <= end_page
            and e["depth"] >= 3
        ]
        print(f"\n  Range {start_page}-{end_page} ({topic}): {len(range_entries)} entries")

        for entry in range_entries:
            title = entry["title"].strip()
            page_num = entry.get("page")

            if not page_num or len(title) < 3:
                continue
            if title.lower() in SKIP_PAGE_TITLES:
                continue

            slug = slugify(title)
            if slug in slug_counts:
                slug_counts[slug] += 1
                slug = f"{slug}-{slug_counts[slug]}"
            else:
                slug_counts[slug] = 1

            # Find page content
            page = all_pages.get(page_num)
            if not page:
                # Look nearby
                for delta in range(1, 6):
                    page = all_pages.get(page_num + delta)
                    if page:
                        break
            if not page:
                for delta in range(1, 6):
                    page = all_pages.get(page_num - delta)
                    if page:
                        break
            if not page:
                continue

            body_text = extract_body_text(page)
            code_blocks = extract_code_blocks(page)

            body_parts = []
            if body_text:
                body_parts.append(body_text)
            if code_blocks:
                tidied = []
                for cb in code_blocks[:5]:
                    tc = tidy_code_block(cb)
                    if tc:
                        tidied.append(tc)
                if tidied:
                    body_parts.append("\n".join(["```cmd"] + tidied + ["```"]))

            body = "\n\n".join(body_parts) if body_parts else f"SQL Server {topic} guide: {title}."
            desc = body_text[:200] if body_text else f"SQL Server {topic}: {title}"

            frontmatter = {
                "title": title,
                "topic": topic,
                "description": desc[:250],
                "tags": [topic, slug],
                "pubDate": datetime(2025, 12, 1),
            }

            fpath = OPS_DIR / f"{slug}.md"
            if slug == "index":
                fpath = OPS_DIR / f"op-{slug}.md"

            write_content_file(fpath, frontmatter, body)
            total_created += 1
            topic_counts[topic] += 1

    # ---- Step 2: Process topic overrides (SSDT->data-tools, Arc->azure-arc) ----
    for ov_start, ov_end, override_topic, keywords in OVERRIDES:
        override_entries = [
            e for e in toc
            if e.get("page")
            and ov_start <= e["page"] <= ov_end
            and e["depth"] >= 3
            and any(kw in e["title"].lower() for kw in keywords)
        ]
        print(f"\n  Override {ov_start}-{ov_end} to '{override_topic}': {len(override_entries)} entries")

        for entry in override_entries:
            title = entry["title"].strip()
            page_num = entry.get("page")

            if not page_num or len(title) < 3:
                continue

            slug = slugify(title)
            if slug in slug_counts:
                slug_counts[slug] += 1
                slug = f"{slug}-{slug_counts[slug]}"
            else:
                slug_counts[slug] = 1

            page = all_pages.get(page_num)
            if not page:
                continue

            body_text = extract_body_text(page)
            code_blocks = extract_code_blocks(page)

            body_parts = []
            if body_text:
                body_parts.append(body_text)
            if code_blocks:
                tidied = []
                for cb in code_blocks[:5]:
                    tc = tidy_code_block(cb)
                    if tc:
                        tidied.append(tc)
                if tidied:
                    body_parts.append("\n".join(["```cmd"] + tidied + ["```"]))

            body = "\n\n".join(body_parts) if body_parts else f"SQL Server {override_topic} guide: {title}."
            desc = body_text[:200] if body_text else f"SQL Server {override_topic}: {title}"

            frontmatter = {
                "title": title,
                "topic": override_topic,
                "description": desc[:250],
                "tags": [override_topic, slug],
                "pubDate": datetime(2025, 12, 1),
            }

            fpath = OPS_DIR / f"{slug}.md"
            if slug == "index":
                fpath = OPS_DIR / f"op-{slug}.md"

            write_content_file(fpath, frontmatter, body)
            total_created += 1
            topic_counts[override_topic] += 1

    # ---- Summary ----
    print(f"\n{'=' * 60}")
    print(f"SWEEP COMPLETE")
    print(f"{'=' * 60}")
    print(f"  Total files created/updated: {total_created}")
    print(f"\n  By topic:")
    for topic in sorted(topic_counts.keys()):
        print(f"    {topic}: {topic_counts[topic]}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
