# SqlKraft — Session Notes (v0.2.0)

## Decisions
- **Clean-slate restart**: All legacy projects moved to `_legacy_backup/`. No code reused from previous SqlKraft v1.0.0, Lumina, or MSSQL Scripts projects.
- **Astro 5 static site**: No Tailwind, no kedhar-ui. Pure CSS with CSS custom properties. Black background (#000000), secondary bg (#0d1117), accent (#2f80ed).
- **Extraction pipeline**: Python PyMuPDF streaming parser in `extractor/` directory. Never loads the 694 MB PDF into memory.
- **Metadata-only search**: Fuse.js index restricted to `name`, `title`, `slug`, `category`, `tags`, and max 150-char description. Enforced in `generate-search-index.cjs`.
- **Single collection for wait-stats**: All 50 types in one directory, differentiated by `category` (8 enum values) and `severity` (5 levels).
- **`schema_mapper_v2.py` over modifying v1**: New mapper handles all content types with stricter name prefix filters. Single-quoted YAML avoids escape-interpretation bugs (`\u003c`).
- **Architecture TOC sidebar client-side**: Astro static generation with JS that reads `#docBody` headings on `DOMContentLoaded` — avoids re-render complexity.

## Gotchas
- **YAML null vs undefined**: When YAML frontmatter has `description:` with no value, it parses as `null`, not `undefined`. Zod `.default()` doesn't handle null. Fixed with `z.preprocess((v) => (v ?? ""), z.string())` on all description and tags fields.
- **YAML double-quote escape bug**: Double-quoted YAML processes escape sequences (`\u003c`, `\n`). Single-quoted YAML treats them as literal text. All frontmatter string values must use single-quoted YAML output.
- **Prettier + Astro**: Prettier 3.8+ cannot infer parser for `.astro` files without `.prettierrc` containing `{ "plugins": ["prettier-plugin-astro"], "overrides": [{ "files": "*.astro", "options": { "parser": "astro" } }] }`.
- **Function/SP content density**: 2,953 pages of system-functions section covers both `sys.fn_` (29 files) and `sys.sp_` (46 files). Low count due to dense multi-column reference page layout — heading detection misses many entries.
- **Catalog views high dedup ratio**: 743 records → 248 files. Many entries span 2-3 batch files, producing duplicates that overwrite. Acceptable for v0.2.0.

## Next Steps
1. **T-SQL Reference extraction** — remaining 5,319 pages (p.24862-30180) from the PDF
2. **T-SQL Reference UI** — index/detail pages with syntax-highlighted code blocks  
3. **Search integration** — wire up Fuse.js client-side search across all 3,431 metadata entries
4. **Tune extraction quality** — improve body-text stitching, dedup page noise, syntax-block emphasis detection
5. **Scripts content** — populate the scripts collection with T-SQL diagnostic/library scripts

## Relevant Files
- `extractor/schema_mapper_v2.py` — Multi-type mapper (873 lines). `BATCH_PROCESSORS` dict maps section prefixes to parser functions. `VALID_NAME_PATTERNS` dict enforces prefix validation per collection.
- `site/src/pages/errors/index.astro` — High-density error code card grid with severity color badges
- `site/src/pages/architecture/[id].astro` — Document reading layout with sticky TOC sidebar
- `site/src/pages/functions/[id].astro` — Function detail page with return-type badge
- `site/src/data/search-index.json` — 3,431 metadata-only records
