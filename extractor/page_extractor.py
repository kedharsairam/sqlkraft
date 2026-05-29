"""
page_extractor.py — Incremental Page Stream Extractor

Reads the PDF page-by-page within TOC-defined page ranges.
For each page, extracts:
  - Heading hierarchy (via font size analysis)
  - Body paragraphs
  - Code blocks (monospaced regions)
  - Tables (structured row/column data)
  - Internal hyperlinks

Outputs structured JSON per section, NOT per page (to avoid bloat).

Design: Streaming — never holds more than N pages in memory at once.
"""

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Optional

import fitz


# Font size thresholds for heading detection (SQL Server doc uses specific sizes)
HEADING_FONT_SIZES = {
    1: (18, 999),    # H1: 18pt+
    2: (14, 17.9),   # H2: 14-17pt
    3: (12, 13.9),   # H3: 12-13pt
    4: (10, 11.9),   # H4: 10-11pt
}

# Monospace font names (SQL Server docs use Consolas/Courier for code)
MONO_FONTS = {"consolas", "courier", "couriernew", "couriern", "cour"}

# Heading texts to ignore (table headers, UI elements, structural noise)
HEADING_BLOCKLIST = {
    "expand table", "applies to:", "important", "note", "caution",
    "warning", "tip", "see also", "related content", "required permissions",
    "dynamic management view", "description", "permissions for sql server",
    "sql", "feedback", "submit and view feedback for",
    "in this article", "prerequisites", "recommended content",
    "additional resources", "next steps", "quickstart",
}


def detect_heading_level(font_name: str, font_size: float, text: str = "") -> Optional[int]:
    """Detect heading level from font properties.

    Filters out table headers and UI text by checking the text content
    against a blocklist.
    """
    font_lower = font_name.lower()
    # Bold + large font = heading
    is_bold = "bold" in font_lower or "bd" in font_lower
    if not is_bold:
        return None

    # Filter out blocklisted text (table headers, etc.)
    text_lower = text.strip().lower()
    if text_lower in HEADING_BLOCKLIST or any(
        text_lower.startswith(b) for b in HEADING_BLOCKLIST
    ):
        return None

    for level, (lo, hi) in HEADING_FONT_SIZES.items():
        if lo <= font_size <= hi:
            return level
    return None


def is_code_font(font_name: str) -> bool:
    """Check if font is monospaced (code block indicator)."""
    font_lower = font_name.lower()
    return any(m in font_lower for m in MONO_FONTS)


def extract_page_structure(page: fitz.Page) -> dict[str, Any]:
    """Extract structured content from a single PDF page."""
    blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_LIGATURES | fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]

    headings = []
    paragraphs = []
    code_blocks = []
    tables = []

    current_code: list[str] = []
    in_code = False

    for block in blocks:
        if block["type"] == 0:  # Text block
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue

                    font_name = span["font"]
                    font_size = span["size"]

                    # Heading detection
                    heading_level = detect_heading_level(font_name, font_size, text)
                    if heading_level:
                        if in_code and current_code:
                            code_blocks.append("\n".join(current_code))
                            current_code = []
                            in_code = False
                        headings.append({
                            "level": heading_level,
                            "text": text,
                            "font": font_name,
                            "size": round(font_size, 1),
                        })
                        continue

                    # Code block detection
                    if is_code_font(font_name):
                        in_code = True
                        current_code.append(text)
                    else:
                        if in_code and current_code:
                            code_blocks.append("\n".join(current_code))
                            current_code = []
                            in_code = False
                        paragraphs.append({
                            "text": text,
                            "font": font_name,
                            "size": round(font_size, 1),
                        })

        elif block["type"] == 1:  # Image block
            pass  # Skip images for now; can extract alt text later

    # Flush remaining code block
    if in_code and current_code:
        code_blocks.append("\n".join(current_code))

    # Table detection (PDF tables rendered as positioned text)
    tables_data = detect_tables(blocks)

    return {
        "headings": headings,
        "paragraphs": paragraphs,
        "code_blocks": code_blocks,
        "tables": tables_data,
    }


def detect_tables(blocks: list[dict]) -> list[dict[str, Any]]:
    """Heuristic table detection: look for aligned text columns."""
    # Placeholder — full table extraction requires positional analysis
    # Will be enhanced in subsequent passes
    return []


def extract_section(
    pdf_path: str,
    section_name: str,
    start_page: int,
    end_page: int,
    output_dir: str,
    batch_size: int = 100,
) -> dict[str, Any]:
    """
    Extract a page range as a streaming batch operation.

    Args:
        pdf_path: Path to PDF file
        section_name: Logical section name (e.g., "system-dmvs")
        start_page: First page (1-indexed)
        end_page: Last page (inclusive)
        output_dir: Output directory for section JSON
        batch_size: Pages to hold in memory before flush

    Returns:
        Summary dict with extraction stats
    """
    doc = fitz.open(pdf_path)
    total_pages = min(end_page, doc.page_count)
    actual_start = max(1, start_page)

    pages_data = []
    stats = {
        "section": section_name,
        "page_range": f"{actual_start}-{total_pages}",
        "total_pages_processed": 0,
        "headings_found": 0,
        "code_blocks_found": 0,
        "output_files": [],
    }

    for page_num in range(actual_start - 1, total_pages):
        page = doc[page_num]
        structure = extract_page_structure(page)
        structure["page_number"] = page_num + 1

        headings = structure["headings"]
        code_blocks = structure["code_blocks"]

        stats["headings_found"] += len(headings)
        stats["code_blocks_found"] += len(code_blocks)

        pages_data.append(structure)

        # Flush every batch_size pages
        if len(pages_data) >= batch_size:
            batch_start = page_num + 2 - batch_size
            batch_end = page_num + 1
            filename = f"{section_name}_p{batch_start}-{batch_end}.json"
            out_path = Path(output_dir) / filename
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(pages_data, f, indent=2, ensure_ascii=False)
            stats["output_files"].append(str(out_path))
            pages_data = []
            stats["total_pages_processed"] += batch_size

    # Flush remaining
    if pages_data:
        remaining_start = actual_start + stats["total_pages_processed"]
        filename = f"{section_name}_p{remaining_start}-{total_pages}.json"
        out_path = Path(output_dir) / filename
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(pages_data, f, indent=2, ensure_ascii=False)
        stats["output_files"].append(str(out_path))
        stats["total_pages_processed"] += len(pages_data)

    doc.close()
    return stats


def extract_pages_dry_run(
    pdf_path: str,
    start_page: int,
    end_page: int,
    sample_size: int = 5,
) -> list[dict[str, Any]]:
    """
    Quick sample extraction for testing — extracts first N pages from range.
    Does NOT write to disk.
    """
    doc = fitz.open(pdf_path)
    actual_end = min(start_page + sample_size - 1, end_page, doc.page_count)
    samples = []

    for page_num in range(start_page - 1, actual_end):
        page = doc[page_num]
        structure = extract_page_structure(page)
        structure["page_number"] = page_num + 1
        samples.append(structure)

    doc.close()
    return samples


if __name__ == "__main__":
    import sys
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\kedhar\Desktop\sql-sql-server-ver17.pdf"
    output = sys.argv[2] if len(sys.argv) > 2 else "output"

    # DMV section: p.20800-21566 (~766 pages)
    print(f"[page_extractor] DMV section extraction starting...")
    result = extract_section(pdf_path, "system-dmvs", 20800, 21566, output)
    print(json.dumps(result, indent=2))
    print(f"[page_extractor] Done.")
