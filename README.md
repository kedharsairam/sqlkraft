# SqlKraft

Enterprise SQL Server Reference Hub.

SqlKraft is a comprehensive reference engine built from the official SQL Server 2017 documentation (30,465 pages, 694 MB PDF). It provides structured, searchable access to:

- **Dynamic Management Views** (160+ DMVs)
- **Wait Statistics** (50+ wait types)
- **System Catalog Views** (150+ views)
- **System Functions** (all built-in functions)
- **System Stored Procedures**
- **T-SQL Language Reference**
- **Database Engine Errors**
- **Engine Architecture & Internals**

## Architecture

```
extractor/          Python pipeline — PDF extraction, classification, schema mapping
site/               Astro 5 static site — content collections, search, UI
```

## Getting Started

```bash
# Install site dependencies
cd site
npm install

# Development server
npm run dev

# Production build
npm run build
```

## Extraction Pipeline

```bash
cd extractor
pip install -r requirements.txt

# Dry run (5 sample pages)
python run_pipeline.py --section system-dmvs --dry-run

# Full DMV extraction (~766 pages)
python run_pipeline.py --section system-dmvs
```

## License

MIT
