# SqlKraft — Session Notes (v0.3.0)

## Decisions
- **Clean-slate restart**: All legacy projects moved to `_legacy_backup/`. No code reused from previous SqlKraft v1.0.0, Lumina, or MSSQL Scripts projects.
- **Astro 5 static site**: No Tailwind, no kedhar-ui. Pure CSS with CSS custom properties. Black background (#000000), secondary bg (#0d1117), accent (#2f80ed).
- **Extraction pipeline**: Python PyMuPDF streaming parser in `extractor/` directory. Never loads the 694 MB PDF into memory.
- **Metadata-only search**: Fuse.js index restricted to `name`, `title`, `slug`, `category`, `tags`, and max 150-char description. Enforced in `generate-search-index.cjs`.
- **Single collection for wait-stats**: All 50 types in one directory, differentiated by `category` (8 enum values) and `severity` (5 levels).
- **`schema_mapper_v2.py` over modifying v1**: New mapper handles all content types with stricter name prefix filters. Single-quoted YAML avoids escape-interpretation bugs (`\u003c`).
- **Architecture TOC sidebar client-side**: Astro static generation with JS that reads `#docBody` headings on `DOMContentLoaded` — avoids re-render complexity.
- **Narrative mapper separate from schema_mapper_v2**: Narrative content (conceptual articles, not reference objects) uses dedicated `narrative_mapper.py` with TOC-driven heading-to-page matching
- **Expanded architecture as sub-articles of existing collection**: 609 new articles added to `architecture/` collection under 11 new `topic` values — avoids splintering into collections
- **XQuery integrated into tsql-reference**: reused existing `tsql-reference` collection with new `xquery` category value — no dedicated XQuery collection needed
- **Operations collection scaffolded but empty**: 14-topic schema registered, placeholder file created, page route built — Range 2 content (p.14419-20029) deferred to v0.4.0
- **Background PDF extraction for 3,623 pages**: extracted at ~77 pages/second using `page_extractor.py` streaming engine
- **Unicode chars fixed in Python**: replaced extended Unicode with ASCII equivalents to avoid `'charmap' codec can't encode character` errors on Windows terminal

## Gotchas
- **YAML null vs undefined**: When YAML frontmatter has `description:` with no value, it parses as `null`, not `undefined`. Zod `.default()` doesn't handle null. Fixed with `z.preprocess((v) => (v ?? ""), z.string())` on all description and tags fields.
- **YAML double-quote escape bug**: Double-quoted YAML processes escape sequences (`\u003c`, `\n`). Single-quoted YAML treats them as literal text. All frontmatter string values must use single-quoted YAML output.
- **Prettier + Astro**: Prettier 3.8+ cannot infer parser for `.astro` files without `.prettierrc` containing `{ "plugins": ["prettier-plugin-astro"], "overrides": [{ "files": "*.astro", "options": { "parser": "astro" } }] }`.
- **Function/SP content density**: 2,953 pages of system-functions section covers both `sys.fn_` (29 files) and `sys.sp_` (46 files). Low count due to dense multi-column reference page layout — heading detection misses many entries.
- **Catalog views high dedup ratio**: 743 records → 248 files. Many entries span 2-3 batch files, producing duplicates that overwrite. Acceptable for v0.3.0.
- **Unicode encoding on Windows**: Python's `print()` with non-ASCII characters fails in Windows PowerShell console. All narrative_mapper.py output strings must use ASCII-compatible characters only.
- **TOC heading matching accuracy**: H3-level heading extraction from TOC requires exact `#heading` anchor matching. Pages with variant heading formats (e.g., parenthetical suffixes) may generate duplicate or untargeted entries. Acceptable for v0.3.0.
- **YAML frontmatter block scalars**: Multi-line descriptions (e.g., error severity descriptions) need `|` literal block scalars in YAML to preserve newlines. Enforced in `build_frontmatter()` via `yaml.dump(..., default_style='|')` for description fields.
- **`H2_TOPIC_MAP` completeness**: Not all H2 titles in the TOC map to architecture topics — some map to tsql-reference (XQuery) or errors (severities). Each extraction type needs explicit mapping config.

## Next Steps
1. **Populate operations collection** — Range 2 (p.14419-20029) has 1,124 TOC entries ready — SSMS, Profiler, SQLPackage, Linux ops, Event Classes, migration, monitoring, HA, configuration — ~173 articles
2. **Populate scripts collection** — 0 files currently — extract diagnostic/library scripts from batch data or TOC entries
3. **TOC gap analysis for remaining untapped ranges** — p.1-2042 (intro/business-continuity, ~2,042 pages) and p.20030-30180 (tsql-reference non-object pages, ~10,150 pages)
4. **Extraction quality v3** — improve syntax-block boundary detection for stored-procedures with non-standard heading hierarchies, enhance return-column table extraction

## Key Metrics
- **Total content files**: 5,040 (architecture 916, catalog-views 275, dmvs 151, errors 1,129, functions 49, scripts 0, stored-procedures 699, tsql-reference 1,770, wait-statistics 50, operations 1)
- **Build page count**: 5,050. Build time: ~75s, zero errors
- **Search index**: 5,011 records across 10 collections (operations added)
- **Content growth this session**: 4,340 → 5,040 files (+700). Architecture +609, errors +15, tsql-reference +75
- **PDF coverage**: 16,304 pages indexed in batch JSON files (up from 12,681). Still untapped: ~12,192 pages

## Relevant Files
- `extractor/narrative_mapper.py` — v0.3.0 narrative extraction engine (460 lines). Handles error severities, XQuery, expanded architecture with TOC-driven heading matching
- `extractor/schema_mapper_v2.py` — Multi-type mapper for reference objects (stored-procedures, catalog-views, etc.)
- `site/src/content/config.ts` — Updated Zod enums (xquery, 11 new architecture topics, operations collection)
- `site/src/pages/operations/index.astro` — New operations collection index page with 14-topic card grid
- `site/src/pages/architecture/index.astro` — Updated with 11 new topic sections
- `site/src/pages/tsql-reference/index.astro` — Added xquery category label
- `site/src/pages/index.astro` — Added operations portal card
- `site/src/data/search-index.json` — 5,011 metadata-only records
