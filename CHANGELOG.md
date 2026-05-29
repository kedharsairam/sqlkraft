# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.2.0] — 2026-05-29

### Added

- **Mass extraction (Phase B)** — Full PDF extraction for 4 remaining sections: Errors (1,800p), Catalog Views (692p), System Functions (2,953p), Architecture (447p). Total 5,892 pages in 89s
- **`schema_mapper_v2.py`** — Multi-type extraction mapper with strict name prefix filtering (`sys.dm_`, `sys.fn_`, `sys.sp_`, `sys.`) and single-quoted YAML to prevent escape-interpretation bugs
- **3,431 content items** across 6 collections, deduplicated to ~1,830 unique files: architecture (307), catalog-views (248), dmvs (36), errors (1,114), functions (29), stored-procedures (46)
- **Error Codes UI** — Color-coded card grid with severity badges (critical/red, high/orange, medium/yellow, low/blue, info/gray). Detail pages with error number badge, category pill, tag strip, and body content
- **Catalog Views UI** — Monospace `sys.*` name cards with category badges and detail pages
- **Functions UI** — Card grid with green return-type badges; detail pages showing return type, category, tags, body content
- **Stored Procedures UI** — Matching functions pattern with index + detail pages
- **Architecture UI** — Topic-grouped index (10 architecture topics) with separate card grids per section; document reading detail layout with sticky TOC sidebar (client-side generated from `<h2>`/`<h3>` headings)
- **Nav bar expansion** — Links to DMVs, Waits, Errors, Catalog, Functions, SPs, Arch, Scripts
- **Search index regeneration** — 3,431 metadata-only records across all 9 collections

### Fixed

- **YAML escape string vulnerability** — Doubled-quoted strings in frontmatter allowed escape sequence interpretation (`\u003c` → `<`). Switched to single-quoted YAML with `'` → `''` escaping for all string fields
- **Missing detail page routes** — `functions/[id].astro` and `stored-procedures/[id].astro` were never created (only index pages existed), causing zero child page generation
- **Content directory population** — 6 of 9 content directories now have files (was 3 of 9)

## [0.1.0] — 2026-05-29

### Added

- **Project foundation** — fresh Astro 5 scaffold with `extractor/` (Python pipeline) and `site/` (Astro frontend) sub-systems
- **PDF extraction pipeline** — `run_pipeline.py` streaming orchestrator with TOC indexing, page-level extraction, content classification, and schema mapping
- **Content collection schemas** — Zod-validated schemas for DMVs, wait statistics, catalog views, functions, stored procedures, T-SQL reference, error codes, and architecture
- **Metadata-only search guardrails** — `generate-search-index.cjs` restricts index payload to `name`, `title`, `slug`, `category`, `tags`, and max 150-char description — never ingests full body text
- **Homepage hub** — Launchpad with 8 portal cards linking to content domains
- **Base layout** — Navigation bar, dark theme, CSS custom properties
- **CI/CD foundation** — GitHub workflows for lint + build and GitHub Pages deploy
- **Wait Statistics pages** — Card-grid index with 8 sub-category filter tabs + detail pages with severity badges, tag strips, and related scripts callouts. 50 wait types across 8 categories
- **DMV reference pages** — Index catalog + detail pages for 37 extracted DMVs with category badges and tag navigation
- **Scripts catalog** — Index and detail pages for T-SQL diagnostic scripts library
- **Null-safe content schemas** — All 9 collections use `z.preprocess` to handle null/empty frontmatter fields gracefully
- **Favicon** — SqlKraft branded SVG favicon
- **Prettier formatting** — `.prettierrc` with Astro plugin, automated formatting for all source files
