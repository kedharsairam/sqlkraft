#! /usr/bin/env python3
"""
run_pipeline.py — SqlKraft Extraction Pipeline Orchestrator

Phase B: Incremental stream-parsing of the full 30,465-page PDF.

Execution flow:
  1. toc_extractor.py  — Extract TOC index (fast, <30s)
  2. page_extractor.py — Extract page content per section (streaming)
  3. content_classifier.py — Classify content per DBA tier & structure
  4. schema_mapper.py — Generate Astro Content Collection .md files

Usage:
  python run_pipeline.py [--pdf PATH] [--section SECTION_NAME]
                         [--pages START-END] [--dry-run] [--output DIR]

Examples:
  # Full extraction of DMV section (~766 pages)
  python run_pipeline.py --section system-dmvs --pages 20800-21566

  # Dry-run test (5 sample pages)
  python run_pipeline.py --section system-dmvs --pages 20800-21566 --dry-run

  # Full pipeline (TOC + DMV extraction)
  python run_pipeline.py --section system-dmvs --pages 20800-21566
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

# Ensure extractor modules are importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# Section page ranges (from Phase A TOC analysis)
SECTION_PAGE_RANGES = {
    "errors-events":         (17659, 19458),
    "event-classes":         (19459, 20030),
    "system-catalog-views":  (20031, 20722),
    "system-compat-views":   (20723, 20799),
    "system-dmvs":           (20800, 21566),
    "system-functions":      (21567, 24519),
    "system-tables":         (24520, 24861),
    "tsql-reference":        (24862, 30180),
    "xquery":                (30181, 30465),
    "errors":                (17659, 19458),
    "architecture":          (5666, 6112),
    "manage-monitor-tune":   (10967, 12669),
    "security":              (13239, 14177),
    "business-continuity":   (244, 2042),
    "database-design":       (2043, 4178),
}

# DBA tier labels for reporting
TIER_LABELS = {1: "Daily Toolkit", 2: "Performance", 3: "BCDR", 4: "Admin/Security", 5: "Reference"}


def parse_page_range(page_spec: str) -> tuple[int, int]:
    """Parse 'START-END' page range string."""
    parts = page_spec.split("-")
    return int(parts[0]), int(parts[1])


def run_toc_extraction(pdf_path: str, output_dir: str) -> dict:
    """Run TOC extraction."""
    from toc_extractor import extract_toc, save_toc_index, build_section_map

    print("\n[Pipeline] === PHASE A: TOC Extraction ===")
    start = time.time()

    toc = extract_toc(pdf_path)
    save_toc_index(toc, output_dir)
    section_map = build_section_map(toc)

    elapsed = time.time() - start
    l1 = len(section_map)
    l2 = sum(len(s["subsections"]) for s in section_map.values())

    print(f"  TOC entries: {len(toc)}")
    print(f"  L1 sections: {l1}, L2 chapters: {l2}")
    print(f"  Time: {elapsed:.2f}s")

    return {"toc_count": len(toc), "l1": l1, "l2": l2, "elapsed_s": round(elapsed, 2)}


def run_page_extraction(
    pdf_path: str,
    section: str,
    page_range: tuple[int, int],
    output_dir: str,
    dry_run: bool = False,
) -> dict:
    """Run page-level extraction for a section."""
    start_page, end_page = page_range
    section_name = section

    print(f"\n[Pipeline] === PHASE B: Page Extraction [{section_name}] ===")
    print(f"  Page range: {start_page}-{end_page} ({end_page - start_page + 1} pages)")
    start = time.time()

    if dry_run:
        from page_extractor import extract_pages_dry_run
        samples = extract_pages_dry_run(pdf_path, start_page, end_page, sample_size=5)
        elapsed = time.time() - start

        print(f"  DRY RUN — extracted {len(samples)} sample pages:")
        for s in samples:
            h_texts = [h["text"][:80] for h in s["headings"]]
            print(f"    p.{s['page_number']}: {', '.join(h_texts) if h_texts else '(no headings)'}")
        print(f"  Time: {elapsed:.2f}s")

        return {"mode": "dry_run", "samples": len(samples), "elapsed_s": round(elapsed, 2)}

    else:
        from page_extractor import extract_section
        result = extract_section(pdf_path, section_name, start_page, end_page, output_dir)
        elapsed = time.time() - start

        print(f"  Pages processed: {result['total_pages_processed']}")
        print(f"  Headings found: {result['headings_found']}")
        print(f"  Code blocks found: {result['code_blocks_found']}")
        print(f"  Output files: {len(result['output_files'])}")
        print(f"  Time: {elapsed:.2f}s")

        return {
            "mode": "full",
            "section": section_name,
            "pages": result["total_pages_processed"],
            "headings": result["headings_found"],
            "code_blocks": result["code_blocks_found"],
            "files": len(result["output_files"]),
            "elapsed_s": round(elapsed, 2),
        }


def run_classification(output_dir: str) -> dict:
    """Run content classification on extracted batches."""
    from content_classifier import classify_section, generate_description

    print(f"\n[Pipeline] === PHASE C: Content Classification ===")

    # Load batch files and classify
    batch_files = sorted(Path(output_dir).glob("*.json"))
    classification_results = {}

    for bf in batch_files:
        if bf.name == "toc_index.json":
            continue
        # Classify by batch filename
        section_key = bf.stem.split("_p")[0]
        cls = classify_section(section_key.replace("-", " "))
        tier = cls["tier"]
        tier_label = TIER_LABELS.get(tier, "Unknown")
        classification_results[bf.name] = {
            "tier": tier,
            "tier_label": tier_label,
            "content_type": cls["content_type"],
            "label": cls["label"],
        }

    # Summary
    tier_counts = {}
    for cr in classification_results.values():
        t = cr["tier"]
        tier_counts[t] = tier_counts.get(t, 0) + 1

    print(f"  Files classified: {len(classification_results)}")
    for t, count in sorted(tier_counts.items()):
        print(f"    Tier {t} ({TIER_LABELS.get(t, '?')}): {count} files")

    return {"classified": len(classification_results), "tiers": tier_counts}


def run_schema_mapping(output_dir: str, content_dir: str) -> dict:
    """Run schema mapping to generate content collection .md files."""
    from schema_mapper import process_dmv_batch, build_search_index

    print(f"\n[Pipeline] === PHASE D: Schema Mapping ===")
    start = time.time()

    batch_files = sorted(Path(output_dir).glob("system-dmvs_*.json"))
    all_records = []

    for bf in batch_files:
        records = process_dmv_batch(str(bf), content_dir)
        all_records.extend(records)

    # Build search index
    search_path = os.path.join(content_dir, "..", "data", "search-index.json")
    build_search_index(all_records, search_path)

    elapsed = time.time() - start

    # Category summary
    categories = {}
    for r in all_records:
        cat = r.get("category", "unknown")
        categories[cat] = categories.get(cat, 0) + 1

    print(f"  Content files generated: {len(all_records)}")
    print(f"  Search index: {search_path}")
    print(f"  Category breakdown: {json.dumps(categories)}")
    print(f"  Time: {elapsed:.2f}s")

    return {"records": len(all_records), "categories": categories, "elapsed_s": round(elapsed, 2)}


def main():
    parser = argparse.ArgumentParser(description="SqlKraft PDF Extraction Pipeline")
    parser.add_argument("--pdf", default=r"C:\Users\kedhar\Desktop\sql-sql-server-ver17.pdf",
                        help="Path to SQL Server 2017 PDF")
    parser.add_argument("--section", default="system-dmvs",
                        help="Section key from SECTION_PAGE_RANGES")
    parser.add_argument("--pages", default=None,
                        help="Page range in format START-END (overrides section defaults)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Extract only 5 sample pages for testing")
    parser.add_argument("--output", default="output",
                        help="Output directory for extracted data")
    parser.add_argument("--content", default="../site/src/content",
                        help="Astro content collections target directory")
    parser.add_argument("--skip-toc", action="store_true",
                        help="Skip TOC extraction (use existing)")
    parser.add_argument("--skip-classify", action="store_true",
                        help="Skip classification phase")
    parser.add_argument("--skip-mapping", action="store_true",
                        help="Skip schema mapping phase")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    content_dir = Path(args.content)
    content_dir.mkdir(parents=True, exist_ok=True)

    # Resolve page range
    if args.pages:
        page_range = parse_page_range(args.pages)
    elif args.section in SECTION_PAGE_RANGES:
        page_range = SECTION_PAGE_RANGES[args.section]
    else:
        print(f"Unknown section '{args.section}'. Available sections:")
        for k, (s, e) in sorted(SECTION_PAGE_RANGES.items()):
            print(f"  {k:30s} p.{s}-{e} ({e-s+1:>5} pages)")
        sys.exit(1)

    pipeline_results = {}

    # === Phase A: TOC ===
    if not args.skip_toc:
        pipeline_results["toc"] = run_toc_extraction(args.pdf, str(output_dir))
    else:
        print("\n[Pipeline] Skipping TOC extraction (--skip-toc)")

    # === Phase B: Page Extraction ===
    page_result = run_page_extraction(
        args.pdf, args.section, page_range, str(output_dir), args.dry_run
    )
    pipeline_results["extraction"] = page_result

    if args.dry_run:
        print("\n[Pipeline] Dry run complete. No files written.")
        print(json.dumps(pipeline_results, indent=2))
        return

    # === Phase C: Classification ===
    if not args.skip_classify:
        pipeline_results["classification"] = run_classification(str(output_dir))
    else:
        print("\n[Pipeline] Skipping classification (--skip-classify)")

    # === Phase D: Schema Mapping ===
    if not args.skip_mapping:
        mapping_result = run_schema_mapping(str(output_dir), str(content_dir))
        pipeline_results["mapping"] = mapping_result
    else:
        print("\n[Pipeline] Skipping schema mapping (--skip-mapping)")

    # === Final Report ===
    print("\n" + "=" * 70)
    print("PIPELINE EXECUTION COMPLETE")
    print("=" * 70)
    print(json.dumps(pipeline_results, indent=2))
    print("\nNext: cd site && npm install && npm run build")


if __name__ == "__main__":
    main()
