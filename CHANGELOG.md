# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

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
