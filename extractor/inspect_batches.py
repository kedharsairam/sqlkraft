"""Quick batch inspector — print first 3 pages of each section."""
import json
from pathlib import Path

output_dir = Path("output")
samples = {
    "errors": "errors_p17659-17758.json",
    "catalog-views": "system-catalog-views_p20031-20130.json",
    "functions": "system-functions_p21567-21666.json",
    "architecture": "architecture_p5666-5765.json",
}

for section, fname in samples.items():
    fp = output_dir / fname
    if not fp.exists():
        print(f"\n=== {section}: file not found ===")
        continue
    with open(fp) as f:
        data = json.load(f)
    
    print(f"\n=== {section} ({len(data)} pages, {fname}) ===")
    for page in data[:3]:
        pn = page["page_number"]
        headings = page.get("headings", [])
        paragraphs = page.get("paragraphs", [])
        code_blocks = page.get("code_blocks", [])
        
        print(f"  Page {pn}: {len(headings)} headings, {len(paragraphs)} paras, {len(code_blocks)} code")
        for h in headings[:5]:
            print(f"    H{h['level']}: {h['text'][:100]}")
        for p in paragraphs[:3]:
            txt = p['text'][:120]
            print(f"    P: {txt}")
        for cb in code_blocks[:1]:
            print(f"    CODE: {cb[:80]}...")
        print()
