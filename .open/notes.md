# SqlKraft Session Notes

## v0.7.0 — Stage 8 Fluid Responsive Design System

### What was done
- **Fluid CSS variable system** — 6 new CSS custom properties in BaseLayout (`--content-max-width`, `--fluid-gap-sm/md/lg`, `--fluid-padding-h/v`) using `clamp()` for viewport-adaptive sizing
- **Global fluid override layer** — `is:global` rules with `!important` on 15+ body-content selectors enforce fluid font-sizes, padding, and responsive table overflow across all 6,591 pages
- **Homepage hero** — all values converted to `clamp()` for true fluid scaling
- **Nav bar** — fluid inner container and link font sizes
- **Global responsive tables** — `overflow-x: auto` with `-webkit-overflow-scrolling: touch`
- **All 10 collection index pages** — breadcrumbs, page headers, card grids, item cards converted to `clamp()` values
- **All 10 collection detail pages** — layout CSS converted to `clamp()`; redundant `.body-content` scoped CSS blocks removed (handled by BaseLayout global `!important` layer)
- **Build**: 6,591 pages built in 62s, zero errors

### Key commits
- (pending push — Stage 8 fluid CSS edits across BaseLayout, index.astro, scripts/index.astro, scripts/[id].astro, dmvs/index.astro, dmvs/[id].astro, wait-statistics/index.astro, wait-statistics/[id].astro, operations/index.astro, architecture/index.astro, tsql-reference/index.astro, stored-procedures/index.astro, functions/index.astro, errors/index.astro, catalog-views/index.astro + all 7 remaining [id].astro detail pages)

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (62s, 6,591 pages)
- `cd site && node rebuild-search-index.cjs` — search index regeneration

## v0.8.0 — Stage 9 Horizon Stretching

### What was done
- **Global container** `--max-width` expanded from 1040px to 1500px; `--content-max-width` from 92vw to 95vw; `--fluid-padding-h` max from 32px to 40px
- **Homepage portal cards** flex-basis: `clamp(250px, 30vw, 360px)` → `clamp(300px, 25vw, 440px)`
- **All 10 collection card grids** min column width: `clamp(250px, 35vw, 380px)` → `clamp(300px, 30vw, 480px)`
- Build: 6,591 pages, 0 errors, ~57s
- CI green, deployed

## v0.9.0 / v0.9.1 — Stage 10 Spacing Uniformity Audit

### What was done
- **Unified spacing CSS variables** in BaseLayout: `--space-xs` (0.5rem), `--space-sm` (0.75rem), `--space-md` (1.5rem), `--space-lg` (2.5rem), `--space-xl` (4rem), `--card-padding` (1.75rem), `--code-padding` (1.75rem)
- **Hero vertical void eliminated**: `.app-shell` padding-top uses `var(--space-lg)`, hero padding-top removed — exact 2.5rem gap from nav bottom to "SqlKraft." title
- **Card padding hardened to 1.75rem**: all 10 collection index cards max 28px, portal cards uniform `clamp(18px, 2vw, 28px)`
- **Code blocks** max padding 24px → 28px; **tables** margin-bottom unified to `var(--space-md)`
- Build: 6,591 pages, 0 errors, 24s
- CI green (v0.9.1), deployed

### Key commits
- `a1145d70` — v0.9.1 prettier formatting fix
- `3fb29082` — v0.9.1 changelog entry
- `3b62f5f6` — v0.9.0 spacing uniformity audit

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (24s, 6,591 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)
- `cd site && node rebuild-search-index.cjs` — search index regeneration

## v0.10.0 — Stage 12 UX Cleanliness Sweep

### What was done
- **Metrics purge**: Removed `({sorted.length})` from all 10 collection index h1 titles; removed `(entries.length)` from tsql-reference category headings; removed pill counts from wait-statistics; removed `#script-count` JS counter from scripts page
- **Subpage design refactoring**: Changed bright blue `.card-title` to neutral `var(--text-primary)` across dmvs, catalog-views, functions, stored-procedures, tsql-reference, scripts; filter pills on scripts and wait-statistics pages redesigned with subtle neutral palette (no bright blue accents); tsql-reference `.cat-nav-count` badges removed
- **Card truncation fix**: Removed `.slice(0, 150)` from all 10 index page card descriptions, replaced with `||` fallback; standardized `-webkit-line-clamp: 3` across all collections (tsql-reference was 2 -> 3); syntax preview slice increased to 200 chars
- **README.md**: Added Repository Scale Matrix table

### Key commits
- `e1f1bb94` — v0.10.0 changelog entry
- `fad333b2` — design: purge user-facing metrics, fix card truncations, unify subpage design

### Known issues
- (none)

## v0.12.0 — Stage 14 Detail View Architectures & Polish

### What was done
- **Compact border-muted property tables**: All `.body-content` tables across DMV, Catalog View, Script, and Wait Statistics detail pages refactored with `border: 1px solid var(--border-glass)`, `padding: 0.5rem 1rem`, header bg `rgba(255,255,255,0.02)`, rounded corners, last-row border removal
- **Wait Statistics diagnostic section panels**: `## Overview` with cool blue left-border, `## Troubleshooting`/`## Diagnostic Mechanics` with warm amber left-border, `## See Also` muted — each h2 gets 3px border-left rail panel treatment
- **Script Copy widget polished**: Terminal-adjacent dark semi-transparent bg (`rgba(13,17,23,0.85)`), `backdrop-filter: blur(4px)`, hover `translateY(-1px)` lift + box-shadow, aligned with pre margin-top via `top: clamp(20px, 3vw, 36px)`
- **Detail title & badge accent → neutral**: `.detail-title` → `var(--text-primary)`, `.cat-badge` → `var(--text-secondary)` on DMV/Catalog/Scripts detail pages (v0.11.0 scope extension)
- **Wait Statistics callout neutralized**: Replaced blue accent border with `var(--border-glass)`, script links use neutral palette

### Key commits
- (pending — `v0.12.0: finalize custom detail-view architectures and script copy utility`)

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (27.85s, 6,591 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)

## v0.13.0 — Stage 15 Spotlight-Grade Search UX & Keyboard Navigation

### What was done
- **Arrow-key navigation**: Track `activeIndex` state, ArrowUp/Down cycle through results, Enter navigates, `scrollIntoView({ block: 'nearest' })` for smooth scrolling
- **Active selection styling**: `.result-item.active` gets `background: rgba(255,255,255,0.05)` + `border-left: 2px solid var(--text-secondary)` — clean neutral highlight
- **Ctrl+K placeholder hint**: Input placeholder now shows `"Search references... (Ctrl+K)"`
- **Programmatic navigation**: `navigateToResult()` helper syncs recently viewed list before navigating
- **Accent→neutral sweep**: Result name color `var(--accent)` → `var(--text-primary)`, cat-badge from blue tint → neutral `rgba(255,255,255,0.06)`, hover from accent blue → neutral `rgba(255,255,255,0.05)`

### Key commits
- (pending — `feat: implement global keyboard shortcuts, arrow-key navigation, and contextual search snippets`)

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (26.95s, 6,591 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)

### Next Steps
Stage 16 (TBD — cookbook browsing mode, mobile nav hamburger, or new collection ingestion)
