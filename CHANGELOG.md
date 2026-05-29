# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.11.0] — 2026-05-29

### Added

- **Category-tailored section architecture** — Five flat-list index pages (dmvs, catalog-views, stored-procedures, functions, errors) now group content into semantic categorical sections with jump-nav pill bars: dmvs (12 categories), catalog-views (4), stored-procedures (10), functions (7), errors (5 severities). Each section has scroll-linked heading with border-bottom divider and `scroll-margin-top: 72px`
- **Multi-column compact card grid** — All 10 index page card grids changed from `clamp(300px, 30vw, 480px)` to `clamp(240px, 18vw, 320px)` enabling 3–4 columns on 1080p displays; grid gap reduced from `clamp(10px, 1.5vw, 18px)` to `clamp(8px, 1vw, 14px)`
- **Severity-colored error badges** — Error index cards display inline severity badge with color-coded border/background per critical/high/medium/low/info classification using `SEVERITY_COLORS` map

### Changed

- **Global link color unified** — All `a { color: var(--accent) }` links changed to `var(--text-primary)` in BaseLayout; breadcrumb/detail-footer links use `var(--text-secondary)`; cat-badge background `rgba(47, 128, 237, 0.12)` → `rgba(255, 255, 255, 0.06)`, color `var(--accent)` → `var(--text-secondary)`; `:not(pre) > code` color from `var(--accent)` → `#e6edf3`; detail-title accent → `var(--text-primary)`
- **Section-jump pill links** — Category jump nav uses `var(--text-secondary)` with border-glass border, hover transitions to `var(--text-primary)` and white border — clean neutral interaction model replacing blue accent pills
- **Category badges removed from section-grouped pages** — Since category is now the section heading, per-card `.cat-badge` is redundant and removed from dmvs, catalog-views, stored-procedures, functions, errors index cards

### Fixed

- **Orphaned template code in section-grouped pages** — Removed dangling HTML/JSX remnants from old template in `errors/index.astro`, `functions/index.astro`, `dmvs/index.astro`, and `stored-procedures/index.astro` that were causing build-time compilation errors (`category is not defined`)
- **Errors index breadcrumb link color** — Changed from `var(--accent)` to `var(--text-secondary)` for neutral link consistency

## [0.10.0] — 2026-05-29

### Removed

- **All user-facing item counts purged from UI** — bracketed `({sorted.length})` counters removed from all 10 collection index page titles and subheadings; `(entries.length)` removed from T-SQL Reference category navigation; `({cat.label})` and `All (N)` pill counters removed from Wait Statistics filter strip; dynamic Script count span `#script-count` and its JS update logic eliminated — counts are now tracked only in `README.md` Repository Scale Matrix
- **Card description JS truncation eliminated** — `.slice(0, 150)` and `.slice(0, 120)` removed from all 10 collection index page card templates; full description text preserved in DOM with CSS `-webkit-line-clamp: 3` handling visual truncation at word boundaries via clean ellipsis

### Changed

- **Subpage design refactored to premium neutral palette** — bright blue `.card-title` accent colors changed to `var(--text-primary)` across DMVs, Catalog Views, Functions, Stored Procedures, T-SQL Reference, and Scripts pages; category and severity filter pills on Scripts and Wait Statistics pages redesigned with subtle neutral backgrounds and `var(--text-secondary)` border colors, removing all bright blue accent tones
- **T-SQL Reference category navigation** — `.cat-nav-count` badges removed; hover border color changed from accent to neutral secondary; category heading row counts removed
- **Card description truncation standardized** — T-SQL Reference card description clamp increased from 2 to 3 lines, matching all other collections; syntax preview slice increased from 100 to 200 characters

### Added

- **Repository Scale Matrix** — added to `README.md` documenting all 10 collections with record counts and descriptions for developer reference only

## [0.9.1] — 2026-05-29

### Fixed

- **Prettier formatting** — `BaseLayout.astro` aligned CSS comment blocks and `index.astro` comment indentation auto-formatted to pass CI lint gate; build: 6,591 pages in 24s, zero errors

## [0.9.0] — 2026-05-29

### Added

- **Unified spacing rhythm** — 6 new math-based CSS spacing variables in `BaseLayout.astro`: `--space-xs` (0.5rem), `--space-sm` (0.75rem), `--space-md` (1.5rem), `--space-lg` (2.5rem), `--space-xl` (4rem) — single-source-of-truth for all vertical gaps and margins across every page
- **Component tokens** — `--card-padding: 1.75rem` and `--code-padding: 1.75rem` variables enforce consistent inner spacing on cards and code blocks

### Changed

- **Hero vertical void eliminated** — `.app-shell` padding-top tightened from `calc(var(--nav-height) + clamp(24px, 3vw, 48px))` to `calc(var(--nav-height) + var(--space-lg))` (= 2.5rem fixed); `.hero` padding-top removed entirely (was `clamp(48px, 6vw, 80px)`) — the "massive gap" between nav bottom and "SqlKraft." title is exactly 2.5rem at all viewports
- **Homepage hero flow** — `.tagline` margin-top uses `--space-xs` (0.5rem), `.subtitle` uses `--space-sm` (0.75rem) top and `--space-lg` (2.5rem) bottom — clean mathematical progression: nav → 2.5rem → title → 0.5rem → tagline → 0.75rem → subtitle → 2.5rem → portal cards
- **Card padding hardened to 1.75rem** — all 10 collection index item cards max padding increased from `22px` to `28px`; homepage portal cards standardized to uniform `clamp(18px, 2vw, 28px)`
- **Code block padding** — `.body-content pre` max padding increased from `24px` to `28px` to match `--code-padding`
- **Table spacing** — `.body-content table` bottom margin unified to `var(--space-md)` (was hardcoded `16px`)
- **Footer spacing** — homepage footer margin-top uses `clamp(var(--space-xl), 6vw, 5rem)` for tighter floor gap

### Fixed

- **No functional changes** — all 6,591 pages rebuild clean, zero lint/build errors

## [0.8.0] — 2026-05-29

### Changed

- **Global container limit** — `--max-width` expanded from `1040px` to `1500px`; `--content-max-width` viewport ratio from `92vw` to `95vw`; horizontal fluid padding increased from `32px` max to `40px` max — site now dynamically commands 1500px of horizontal estate on 1920x1080 monitors, reducing dead margin space by ~460px total
- **Homepage portal cards** — flex-basis expanded from `clamp(250px, 30vw, 360px)` to `clamp(300px, 25vw, 440px)` — cards now fill 3 wide columns on 1080p viewports instead of 2 narrow ones
- **All 10 collection index card grids** — min column width expanded from `clamp(250px, 35vw, 380px)` to `clamp(300px, 30vw, 480px)` — cards stretch proportionally with the wider canvas, reducing unnecessary vertical stacking
- **Nav bar** — automatically rebalances edge-to-edge with the wider `--content-max-width` variable
- **Build**: 6,591 pages in 57s, zero errors

## [0.7.1] — 2026-05-29

### Fixed

- **Prettier formatting** — 4 fluid-stage source files (`BaseLayout.astro`, `dmvs/index.astro`, `scripts/index.astro`, `wait-statistics/index.astro`) auto-formatted to pass CI lint gate

## [0.7.0] — 2026-05-29

### Added

- **Fluid CSS variable system** — 6 new CSS custom properties in BaseLayout: `--content-max-width`, `--fluid-gap-sm`, `--fluid-gap-md`, `--fluid-gap-lg`, `--fluid-padding-h`, `--fluid-padding-v` — all using `clamp()` for viewport-adaptive sizing across all page types.
- **Global fluid override layer** — `is:global` rules in BaseLayout with `!important` on 15+ body-content selectors (`h2`, `h3`, `p`, `li`, `pre`, `code`, `table`, `th`, `td`) enforce fluid font-size, padding, and responsive table overflow across all 6,591 pages without editing individual page components.

### Changed

- **Homepage hero** — `h1` font-size: `clamp(2.25rem, 5vw, 4.5rem)` with `letter-spacing: -0.02em`; tagline `clamp(1rem, 2.5vw, 1.5rem)`; subtitle `clamp(0.875rem, 1.5vw, 1rem)` with `max-width: min(65ch, 90vw)`; portal cards `flex: 0 0 clamp(250px, 30vw, 360px)`, gap `clamp(1rem, 2vw, 1.75rem)`; footer `margin-top: clamp(48px, 6vw, 80px)`
- **Nav bar** — inner container uses `--content-max-width` and `--fluid-padding-h`; link font-size `clamp(11px, 1.3vw, 14px)`
- **App shell** — fluid padding and margins throughout
- **Global responsive tables** — `overflow-x: auto` with `-webkit-overflow-scrolling: touch` on all `.body-content table` elements
- **Global code blocks** — fluid padding `clamp(12px, 2vw, 24px)`, fluid font-size `clamp(0.85rem, 1.2vw, 0.95rem)`
- **All collection index pages** — breadcrumbs, page headers, card grids, item cards converted to `clamp()` values for padding, font-size, gap, border-radius across all 10 content collections
- **All collection detail pages** — breadcrumbs, detail titles, badges, tag strips, footers converted to `clamp()` values; redundant scoped `.body-content` CSS blocks removed (replaced by BaseLayout global `!important` fluid layer)
- **Responsive card grids** — `grid-template-columns: minmax(clamp(250px, 35vw, 380px), 1fr)` for adaptive column sizing on all viewport widths
- **Build time** — improved to ~62s (from ~71s) for all 6,591 pages

### Removed

- **Redundant scoped `.body-content` CSS** — stripped from all 10 collection detail pages (`[id].astro`) since BaseLayout global `!important` fluid rules now handle all body typography

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
