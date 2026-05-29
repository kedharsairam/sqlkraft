"""Inspect deeper content pages beyond section indices."""
import json
from pathlib import Path

output_dir = Path("output")

# Check deeper pages: error entries, actual catalog views, architecture narrative
inspections = {
    "errors_mid": "errors_p18459-18558.json",       # Middle of error section
    "catalog_view_mid": "system-catalog-views_p20331-20430.json",
    "functions_mid": "system-functions_p21967-22066.json",
    "architecture_mid": "architecture_p5866-5965.json",
}

for label, fname in inspections.items():
    fp = output_dir / fname
    if not fp.exists():
        print(f"\n=== {label}: {fname} not found ===")
        continue
    with open(fp) as f:
        data = json.load(f)
    
    print(f"\n=== {label} ({fname}) — Page range: {data[0]['page_number']}-{data[-1]['page_number']} ===")
    
    # Show first 5 pages that have headings (non-empty pages)
    shown = 0
    for page in data:
        if shown >= 5:
            break
        headings = page.get("headings", [])
        if not headings:
            continue
        pn = page["page_number"]
        paragraphs = page.get("paragraphs", [])
        code_blocks = page.get("code_blocks", [])
        
        print(f"  Page {pn} — {len(headings)} headings, {len(code_blocks)} code blocks")
        for h in headings[:4]:
            print(f"    H{h['level']}: {h['text'][:100]}")
        for cb in code_blocks[:2]:
            print(f"    CODE: {cb[:100]}")
        # First useful paragraph
        for p in paragraphs:
            t = p['text'].strip()
            if len(t) > 40:
                print(f"    TEXT: {t[:140]}")
                break
        print()
        shown += 1
