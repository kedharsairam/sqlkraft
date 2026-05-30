"""
batch_extract_operations.py — Stage 5: Operations Range Extraction

Extracts all untapped pages from Range 2 (p.14419-20029) as section-specific
batch JSON files for the operations collection.

Sections to extract:
  1. p.14419-14676  — Configuration & Tools (command-line, services)
  2. p.14677-15077  — SSB Diagnose
  3. p.15078-15264  — SQL Server Management Studio (SSMS)
  4. p.15265-15429  — SqlPackage
  5. p.15430-15775  — SQL Server Profiler
  6. p.15776-15847  — Database Engine Tutorial / Writing T-SQL
  7. p.15848-17070  — SQL Server on Linux
  8. p.17071-17573  — Azure Synapse Analytics
  9. p.17574-17658  — Azure Arc + Offline docs (pre-errors header)
  10. p.19459-19651  — Event Classes
  11. p.19652-20029  — Misc docs gap (to catalog-views at 20031)

Output: operations_*.json files in extractor/output/
"""

import sys
import time
from pathlib import Path

# Add parent to path so we can import page_extractor
sys.path.insert(0, str(Path(__file__).parent))
from page_extractor import extract_section

PDF_PATH = r"C:\Users\kedhar\Desktop\sql-sql-server-ver17.pdf"
OUTPUT_DIR = str(Path(__file__).parent / "output")


def extract_range(section_name, start, end):
    """Extract a page range and print stats."""
    print(f"\n{'='*60}")
    print(f"Extracting: {section_name} (p.{start}-{end})")
    print(f"{'='*60}")
    t0 = time.time()
    stats = extract_section(PDF_PATH, section_name, start, end, OUTPUT_DIR, batch_size=100)
    elapsed = time.time() - t0
    print(f"  Pages: {stats['total_pages_processed']}")
    print(f"  Headings: {stats['headings_found']}")
    print(f"  Code blocks: {stats['code_blocks_found']}")
    print(f"  Files: {len(stats['output_files'])}")
    print(f"  Time: {elapsed:.1f}s")
    return stats


def main():
    print("=" * 60)
    print("STAGE 5: OPERATIONS BATCH EXTRACTION")
    print("Range 2: p.14419-20029 (3,811 untapped pages)")
    print("=" * 60)

    t_start = time.time()
    total_pages = 0
    total_files = 0

    sections = [
        # Section 1: Configuration & Tools
        ("operations-tools", 14419, 14676),

        # Section 2: SSB Diagnose
        ("operations-ssb", 14677, 15077),

        # Section 3: SSMS
        ("operations-ssms", 15078, 15264),

        # Section 4: SqlPackage
        ("operations-sqlpackage", 15265, 15429),

        # Section 5: Profiler
        ("operations-profiler", 15430, 15775),

        # Section 6: Database Engine Tutorial / Writing T-SQL
        ("operations-dbe-tutorial", 15776, 15847),

        # Section 7: SQL Server on Linux
        ("operations-linux", 15848, 17070),

        # Section 8: Azure Synapse
        ("operations-synapse", 17071, 17573),

        # Section 9: Azure Arc + Offline docs (pre-errors)
        ("operations-arc-docs", 17574, 17658),

        # Section 10: Event Classes
        ("operations-eventclasses", 19459, 19651),

        # Section 11: Misc docs gap
        ("operations-misc", 19652, 20029),
    ]

    for name, start, end in sections:
        stats = extract_range(name, start, end)
        total_pages += stats["total_pages_processed"]
        total_files += len(stats["output_files"])

    elapsed = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"EXTRACTION COMPLETE")
    print(f"{'='*60}")
    print(f"  Total pages:  {total_pages}")
    print(f"  Total files:  {total_files}")
    print(f"  Total time:   {elapsed:.1f}s ({total_pages/elapsed:.0f} pgs/s)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
