# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.6.0] — 2026-05-29

### Added

- **`--color-muted` CSS variable** defined in BaseLayout (`#9ca3af`) — WCAG AAA-compliant against `--bg-secondary`, used for card body text.

### Changed

- **Hero section** — top padding increased from `64px` to `72px`, subtitle `margin-bottom` set to `3.5rem` for improved vertical rhythm.
- **Subtitle paragraph** — `max-width` changed from `640px` to `65ch`, `margin: 18px auto 3.5rem`, `line-height: 1.7`, horizontal padding added for narrow viewports.
- **Portal card grid** — migrated from `display: grid` to `display: flex` with `flex-wrap: wrap` and `justify-content: center`, so the 10th (asymmetrical trailing) card is naturally centered; card width fixed to `300px`.
- **Grid gap** — increased from `16px` to `1.75rem` (28px) for better breathing room.
- **Card padding** — increased from `24px` to `28px 24px 26px`; hover `translateY` deepened from `-2px` to `-3px`.
- **Card paragraph** — `color` changed from `var(--text-secondary)` to `var(--color-muted)` (#9ca3af, passes WCAG AAA); `line-height` bumped from `1.5` to `1.6`.
- **Card heading** — `margin-bottom` increased from `8px` to `10px`.
- **Footer** — top margin increased from `64px` to `72px`.
- **Responsive breakpoint** — added `@media (max-width: 680px)` with smaller hero fonts and full-width cards.

### Removed

- **Grid `grid-template-columns` layout** — replaced by flexbox for last-row centering.

## [0.5.0] — 2026-05-29

### Added

- **Phase 2: TSQL Diagnostic Scripts** — Populated the `scripts` collection with 270 curated diagnostic and administrative scripts from a local library. 270 articles across 13 categories — architecture (20), automation (29), backup-restore (25), database (76), general (6), high-availability (21), index-maintenance (11), installation (8), migration (3), performance (11), replication (5), security-audit (42), troubleshooting (13)
- **`scripts_ingester.py`** — Recursive Python ingestion engine that walks source directories, applies sanitization (IP/password/path scrubbing), maps folder names to Zod category enums, extracts descriptions from SQL comments, auto-derives tags, and generates proper YAML frontmatter with file-modification-based pubDate
- **Origin story blackout** — README.md scrubbed of all PDF-extraction references, homepage index.astro hero/subtitle/footer rephrased as curated DBA reference hub, scripts portal card added to homepage
- **Expanded scripts category enum** — 16 categories now supported in Zod schema: `high-availability`, `architecture`, `automation`, `backup-restore`, `configuration`, `database`, `general`, `index-maintenance`, `installation`, `migration`, `performance`, `replication`, `security-audit`, `monitoring`, `maintenance`, `troubleshooting`
- **Search index rebuilt** — 6,536 records across 10 collections (scripts: 270 unique entries)
- **Zero-error build** — 6,591 pages, zero errors, 148s build time

## [0.4.0] — 2026-05-29

### Added

- **Operations bulk ingestion (Stage 5)** — Populated the operations collection with 983 articles from Range 2 (p.14419-20029), transforming the placeholder scaffold into the largest collection by content count
- **PDF extraction (3,811 pages in 72s)** — Batch extraction of 11 untapped sections across Range 2: SSB Diagnose (401p), SSMS (187p), SqlPackage (165p), Profiler (346p), Linux (1,223p), Azure Synapse (503p), Azure Arc/docs (85p), Event Classes (193p), Configuration tools (258p), misc docs (378p). 43 batch JSON files, 28,299 headings, 10,520 code blocks
- **`batch_extract_operations.py`** — Automated extraction script for all 11 sections with one-shot execution, eliminating manual per-section calls
- **`operations_mapper.py`** — New extraction engine (290 lines) with `H2_OPS_TOPIC_MAP` for H2-to-topic resolution and keyword-based fallback heuristics. Handles 12 H2 chapters mapping to 9 of 14 operations topics
- **Operations content**: 983 articles across 9 topics — ssb-diagnose (88), ssms (36), sqlpackage (14), profiler (86), linux-operations (131), azure-synapse (56), event-classes (192), monitor (371), configuration (9)
- **Operations detail route** — New `operations/[id].astro` page with breadcrumb nav, topic badge, tag strip, code-block styling, and back navigation
- **Operations index page** — Card-grid layout with 14-topic sections, now dynamically renders all 983 articles with proper count and category grouping
- **Search index rebuilt** — 5,987 records across 10 collections (operations: 979 unique entries)
- **Zero-error build** — 6,034 pages, zero errors, zero schema validation failures

### Added (Phase 5 - Final Sweep)

- **5 missing operations topics populated** — `high-availability` (236 articles), `upgrade` (26), `migration` (30), `data-tools` (8), `azure-arc` (3). All 14 operations topics now have content
- **PDF extraction (1,636 pages)** — Three new sections: HA/Always On/FCI/Mirroring/Log Shipping (p.866-2043, 1,178p), Upgrade (p.6442-6655, 214p), Migration (p.7155-7398, 244p). 8,807 headings, 2,294 code blocks
- **`sweep_mapper.py`** — Post-processing mapper that handles page-range-based topic assignments for content outside Range 2, plus topic overrides for misclassified entries (SSDT→data-tools, Arc→azure-arc)
- **Classification fixes** — SSDT entries under SSB Diagnose H2 (p.14702-15077) correctly re-mapped from `ssb-diagnose` to `data-tools` (8 articles). Azure Arc entries under Azure Synapse H2 (p.17071-17573) re-mapped from `azure-synapse` to `azure-arc` (3 articles)
- **Search index rebuilt** — 6,266 records across 10 collections (operations: 1,258 unique entries, +279 from sweep)
- **Zero-error build** — 6,321 pages, zero errors, 64.46s build time

## [0.3.0] — 2026-05-29

### Added

- **Narrative gap analysis** — Comprehensive TOC blanket audit of 2,602 entries across Range 1 (p.1-5665, 23 H2 chapters) and Range 2 (p.14419-20029, 11 H2 chapters). Identified 21 untapped architecture topics (Tier 2–6 classification)
- **Architectural Classification Matrix** — 6-tier mapping system: Tier 1 (existing architecture 10 topics), Tier 2 (11 new architecture topics, ~75 articles), Tier 3 (new `operations` collection, 14 topics, ~173 articles), Tier 4 (error severity reference expansion), Tier 5 (XQuery in tsql-reference), Tier 6 (append-only low priority)
- **Schema extensions** — Added `xquery` to tsql-reference category enum; added 11 new topics to architecture enum (`collation`, `tables`, `change-data-capture`, `clr-integration`, `xml-data`, `json-data`, `spatial-data`, `sql-graph`, `filestream`, `service-broker`, `hierarchical-data`); registered new `operations` collection with 14-topic Zod schema
- **PDF extraction (3,623 pages in 47s)** — `database-design` section (p.2043-4178, 2,136 pages, 22 batch files) and `extra-arch` section (p.4179-5665, 1,487 pages, 15 batch files)
- **`narrative_mapper.py`** — New standalone extraction engine for narrative/conceptual content (460 lines). Handles three extraction types: error severities from `errors_p17659-17758.json` (15 files), XQuery from `xquery_*.json` (75 articles), expanded architecture from `database-design_*.json` + `extra-arch_*.json` (609 articles). Uses TOC-driven H2→H3 heading matching and `H2_TOPIC_MAP` dict for architecture topic routing
- **Content expansion**: 4,340 → 5,040 files (+700). Architecture grew 307 → 916 (+609), errors grew 1,114 → 1,129 (+15), tsql-reference grew 1,695 → 1,770 (+75), stored-procedures grew 46 → 699 (+653 from earlier tsql-reference migration)
- **Operations collection scaffolded** — 14-topic schema, placeholder `index.md`, page route created. Collection registered in config.ts and search index builder
- **UI routing updates** — tsql-reference index.astro: added `xquery: "XQuery"` to CATEGORY_LABELS. Architecture index.astro: added 11 new topic sections with card ranges. Home page: added operations portal card. New operations index.astro: topic-sections card grid layout
- **Search index rebuild** — 5,011 records across 10 collections (operations collection schema added)
- **Zero-error build** — 5,050 pages, zero errors, zero schema validation failures. 1 expected warning suppressed: empty scripts collection

### Fixed

- **Unicode encoding in Windows terminal** — Replaced `→` (U+2192), `—` (U+2014), `─` (U+2500) with ASCII equivalents in Python scripts to prevent `'charmap' codec can't encode character` errors during console output

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
