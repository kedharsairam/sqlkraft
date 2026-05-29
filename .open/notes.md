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

### Next Steps
1. Verify deploy completes on GitHub
2. Stage 11 (TBD — search enhancements, cookbook browsing, dark mode refinements, or new feature)
