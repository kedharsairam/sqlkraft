# SqlKraft

**Lightning-fast, comprehensive personal reference engine for the SQL Server community.**

A statically compiled documentation shell rendering over 5,200 meticulously structured reference entries across 11 core collections. Built with Astro 5 for sub-30ms static delivery with zero runtime dependencies.

## Collections

| Collection | Entries | Coverage |
|---|---|---|
| T-SQL Reference | 1,740 | Statements, queries, data types, operators, hints, predicates |
| Operations & Administration | 1,258 | HA, migration, monitoring, SSMS, Profiler, Linux |
| Database Engine Errors | 1,129 | Error codes with severity classification and troubleshooting |
| Architecture & Internals | 916 | Query processing, memory, locking, I/O, storage engine |
| System Stored Procedures | 699 | Administrative and maintenance procedures |
| Catalog Views | 275 | Database metadata, objects, indexes, security |
| T-SQL Diagnostic Scripts | 270 | Curated performance, indexing, security, HA scripts |
| Dynamic Management Views | 151 | Execution, I/O, memory, indexing, OS internals |
| Wait Statistics | 49 | Wait types across baseline, triage, blocking, I/O |
| System Functions | 49 | Aggregate, analytic, conversion, string, date/time |
| Extended Events | 4 | System health, deadlock, query performance, wait analysis |
| **Total** | **~6,500** | **11 collections across 5,246 published pages** |

## Features

- **Global command palette** — Instant keyboard-driven navigation (Ctrl+K / ⌘K) with fuzzy search across all 5,200+ entries, zero external search dependencies
- **Fluid view transitions** — Morphing page-to-page navigation with shared element transitions between card grids and detail views
- **Syntax-optimized code blocks** — Language-aware syntax highlighting via Shiki, unselectable line numbers with sticky gutter, one-click clipboard copy with visual feedback
- **Responsive spatial layout** — Fluid typography system using `clamp()` throughout; glass-panel overlay architecture; sticky right-rail table of contents with intersection-based scroll tracking
- **Cross-reference intelligence** — Inline hover preview cards resolving at build time from a shared 970 KB palette index; related-content bridges between DMVs, waits, scripts, XEvents, and errors
- **Production-grade static delivery** — Astro 5 static site generation; sub-30 second full build; 5,246 pages compiled to optimized flat HTML; automated sitemap generation

## Quick Start

```bash
# Clone the repository
git clone https://github.com/kedharsairam/sqlkraft.git
cd sqlkraft/site

# Install dependencies
npm install

# Start the development server
npm run dev

# Build for production
npm run build

# Preview the production build
npm run preview
```

## Architecture

SqlKraft is a purely static site — no server, no database, no runtime framework. Content is authored in Markdown with YAML frontmatter, validated against Zod schemas at build time, and compiled into flat HTML. The build pipeline runs a content audit before each build to maintain data integrity.

```
src/
├── content/          # 11 Markdown content collections with Zod validation
│   ├── tsql-reference/
│   ├── operations/
│   ├── errors/
│   ├── architecture/
│   ├── stored-procedures/
│   ├── catalog-views/
│   ├── scripts/
│   ├── dmvs/
│   ├── wait-statistics/
│   ├── functions/
│   └── xevents/
├── components/       # Reusable Astro components (Card, SearchPalette, SEO, etc.)
├── layouts/          # BaseLayout + RecipeLayout with global CSS tokens
├── pages/            # Index + [id] detail pages for all collections
└── data/             # Search and palette indexes (build-time generated)
```

## Development

```bash
# Lint all source files
npm run lint

# Auto-format source files
npm run format
```

## Build Output

- **5,246 pages** — Flat HTML directory structure, no client-side rendering
- **~29s build time** — Incremental builds are faster; sitemap generated automatically
- **0 runtime dependencies** — Pure HTML + CSS + vanilla JS (copy button, search palette, hover cards, keyboard shortcuts)

## License

MIT — see [LICENSE](LICENSE) for details.
