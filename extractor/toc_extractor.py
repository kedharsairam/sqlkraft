"""
toc_extractor.py — TOC Structural Indexer

Extracts the full Table of Contents from the SQL Server 2017 PDF.
Produces a structured index of all 7,783+ TOC entries with depth, title,
and page numbers, categorized by DBA relevance tier.

Phase A output (already verified in pre-session analysis).
"""

import json
from pathlib import Path
from typing import Any

import fitz


def extract_toc(pdf_path: str) -> list[dict[str, Any]]:
    """Extract full TOC from PDF with depth, title, and page number."""
    doc = fitz.open(pdf_path)
    raw_toc = doc.get_toc(simple=False)
    doc.close()

    structured = []
    for entry in raw_toc:
        depth, title, page = entry[0], entry[1], entry[2]
        structured.append({
            "depth": depth,
            "title": title.strip(),
            "page": page if page > 0 else None,
        })
    return structured


def build_section_map(toc: list[dict[str, Any]]) -> dict[str, Any]:
    """Build a hierarchical section map from flat TOC entries."""
    sections = {}
    current_l1 = None
    current_l2 = None

    for entry in toc:
        d = entry["depth"]
        if d == 1:
            current_l1 = entry["title"]
            sections[current_l1] = {
                "title": entry["title"],
                "page": entry["page"],
                "subsections": {},
            }
            current_l2 = None
        elif d == 2 and current_l1:
            current_l2 = entry["title"]
            sections[current_l1]["subsections"][current_l2] = {
                "title": entry["title"],
                "page": entry["page"],
                "entries": [],
            }
        elif d >= 3 and current_l1 and current_l2:
            sections[current_l1]["subsections"][current_l2]["entries"].append({
                "title": entry["title"],
                "page": entry["page"],
                "depth": d,
            })

    return sections


def save_toc_index(toc: list[dict[str, Any]], output_dir: str) -> str:
    """Save TOC index to JSON file."""
    out_path = Path(output_dir) / "toc_index.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(toc, f, indent=2, ensure_ascii=False)
    return str(out_path)


if __name__ == "__main__":
    import sys
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\kedhar\Desktop\sql-sql-server-ver17.pdf"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"

    print(f"[toc_extractor] Extracting TOC from {pdf_path}...")
    toc = extract_toc(pdf_path)
    print(f"[toc_extractor] {len(toc)} TOC entries extracted.")

    save_toc_index(toc, output_dir)
    section_map = build_section_map(toc)

    l1_count = len(section_map)
    l2_count = sum(len(s["subsections"]) for s in section_map.values())
    print(f"[toc_extractor] {l1_count} top-level sections, {l2_count} chapter-level sections.")
    print(f"[toc_extractor] TOC index saved to {output_dir}/toc_index.json")
