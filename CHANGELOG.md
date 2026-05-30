# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.48.0] — 2026-05-31 — **Emergency Search Layout Clean-Up and Card Overflow Fix**

### Fixed

- **Search palette card block regression (critical)** — Search results were rendering as full `.item-card` blocks inheriting `min-height: 160px`, glass borders, and massive padding from Card.astro's global CSS. Each result appeared as a floating card block instead of a compact list row.
  - Rewrote `__renderCard()` in CardPalette.astro to output `<a class="palette-result">` instead of `<a class="item-card palette-card">`
  - Removed `import Card from "./Card.astro"` — palette no longer inherits card CSS globals
  - Results are now tight 44px horizontal rows: title left + badge right, no description block
  - Hover: subtle `rgba(255, 255, 255, 0.05)` background — no border glow, no transform, no shadow
  - Active (keyboard): `rgba(47, 128, 237, 0.08)` accent tint
  - Removed `.card-tag`, `.card-tag-badge`, `.palette-card`, `.palette-card-desc` CSS classes
  - Added `.palette-result`, `.palette-badge`, `.palette-badge--*` self-contained classes
  - Updated click handler in SearchPalette.astro from `a.item-card` to `a.palette-result`

- **Card description container overflow** — Added `text-overflow: ellipsis` and `word-break: break-word` to `.card-desc` in Card.astro. Long unbroken string fragments (raw SQL arrays, concatenated tokens) no longer extend past the card's physical padding boundaries.

### Changed

- `site/package.json` — version updated to `0.48.0-beta`
- `site/src/components/CardPalette.astro` — Major rewrite (v7): compact 44px row layout, self-contained CSS, no Card.astro dependency
- `site/src/components/Card.astro` — Added `text-overflow: ellipsis; word-break: break-word;` to `.card-desc`
- `site/src/components/SearchPalette.astro` — Updated click delegation selector to `a.palette-result`

### Build

- 5,241 pages, 0 errors

---

## [0.47.0] — 2026-05-31 — **Wait Stats Card Blueprint Lock, Spotlight macOS-native Redesign, Automated Sanitization Engine**

### Added

- **Wait Statistics Card Blueprint locked globally** — Card.astro now enforces `min-height: 160px` on every `.item-card` across all 11 collection index pages. `.card-desc` uses `flex: 1` to fill available space, pushing tags to the bottom of every card. All cards now render at identical height regardless of description length, matching the Wait Statistics dashboard gold standard.

- **Automated Markdown Sanitization Engine** — Created `scripts/sanitize-content.js`, a build-time pipeline script that scans all 5,233 markdown content files for structural defects and auto-corrects them:
  - **Dangling headings** — Orphaned `##` / `###` lines immediately before `---` with no body text are merged into the preceding heading
  - **Stray code block artifacts** — Isolated bare `sql` / `tsql` / `text` lines that aren't part of proper fenced code blocks are removed
  - **Fragmented sentences** — Single-word lines (3 chars or fewer) that break natural prose are consolidated into the preceding paragraph
  - **Blank line normalization** — Excessive blank lines (3+ consecutive) collapsed to 2 max
  - Integrated as the first step of the `prebuild` and `predev` hooks in `package.json`
  - **Live run results**: 1,598 files modified, 5 empty stub files deleted, 471 dangling headings fixed, 5,454 stray code blocks removed, 5,181 fragmented sentences consolidated, 719 excessive blank line runs normalized

- **Native macOS Spotlight search palette (v6)** — Complete redesign of SearchPalette.astro and CardPalette.astro to match native macOS Spotlight behavior:
  - **Zero text-underlines** across all palette links via `text-decoration: none !important`
  - **12px unified vertical padding** on every palette result item for consistent breathing room
  - **Crisp monochromatic typography** — System font stack, tighter tracking, muted color palette
  - **Hidden scrollbar container** — `scrollbar-width: thin` for Firefox, native macOS-style auto-hiding scrollbar in Chrome
  - **Visual separation between result sets** — Category groups separated by `border-top`, individual items separated by `rgba(255,255,255,0.03)` bottom borders, last item border removed

### Changed

- `site/package.json` — version updated to `0.47.0-beta`; added `"sanitize": "node scripts/sanitize-content.js"` script; `prebuild` and `predev` now run sanitizer first
- `site/src/components/Card.astro` — Added `min-height: 160px` to `.item-card`; added `flex: 1` to `.card-desc` for uniform card height enforcement
- `site/src/components/SearchPalette.astro` — Added zero text-decoration rules, hidden scrollbar CSS, visual separation between result sets
- `site/src/components/CardPalette.astro` — Changed `.palette-item` padding from `0` to `12px 0` for unified vertical rhythm; added `.palette-item` border-bottom separation; added `text-decoration: none !important` to `.palette-card`

### Removed

- **5 empty content stubs deleted**: `alter-table.md`, `datetimeoffset.md`, `reconfigure.md`, `type.md`, and one additional zero-body file detected and purged by the sanitization engine
- **Stage 53 half-measures wiped** — Previous search palette row redesign and 2-line card description clamp replaced by the full macOS-native redesign

### Build

- 5,246 pages, 0 errors

---

## [0.46.0] — 2026-05-30 — **macOS Spotlight Search Rows, Compact Cards, Content Cleanup**

### Added

- **Native macOS Spotlight search results** — Redesigned search palette result rows with clear typographic contrast: title in 14px medium weight on the left, uppercase category badge (ARCH, DMV, T-SQL, etc.) on the right in a single flex row. All link underlines removed. 12px padding, `rounded-lg` (10px) hover states. Layout matches macOS Spotlight behavior exactly.

- **Compact card descriptions** — Changed `.card-desc` line clamp from 3 lines to 2 lines across all index pages. Ensures uniform card height and compact dashboard tokens matching the Wait Statistics gold standard.

### Fixed

- **`@@SERVERNAME` metadata corruption** — Replaced dangling `#### syntaxsql` / `### nvarchar` ingestion artifacts with proper structured markdown: syntax block, return type, remarks, and example.

- **`access-objects-in-the-same-order` broken text** — Consolidated fragmented paragraphs with excessive line breaks, removed dangling single-word `sql` code blocks. Converted raw text to proper subheadings and bullet lists.

### Changed

- `site/src/components/CardPalette.astro` — `__renderCard()` HTML structure changed to `.palette-result-row` (flex row: title + badge). CSS: `.palette-card` padding 12px, border-radius 10px, added `.palette-result-row` / `.palette-result-title` styles. Removed `.palette-card .card-title`.
- `site/src/components/Card.astro` — `.card-desc` `-webkit-line-clamp` changed from 3 to 2.
- `site/src/content/tsql-reference/servername.md` — Full rewrite with syntax/doc/example.
- `site/src/content/architecture/access-objects-in-the-same-order.md` — Consolidated paragraphs, fixed bullet list structure.
- `site/package.json` — version updated to `0.46.0-beta`.

### Build

- 5,246 pages, 0 errors, ~33s

---

## [0.45.1] — 2026-05-30 — **Absolute Grid Completion**

### Changed

- **7/7 sectioned pages unified** — Converted remaining 3 index pages (stored-procedures, cookbook, errors) to the Wait Statistics blueprint: single `.card-grid` + `.category-strip` filter pills with JS `filterCards()`. All 11 collection index pages now use the identical grid layout.
- Error page (1,129 cards) retains `notransition` prop — no View Transition naming to prevent browser freeze.

### Build

- 5,246 pages, 0 errors

---

## [0.44.0] — 2026-05-30 — **Ultra-Snappy Navigation & Prefetch Optimization**

### Added

- **Aggressive link prefetching** — Configured Astro 5's built-in prefetch engine in `astro.config.mjs`: `prefetchAll: true` with `defaultStrategy: 'hover'`. Every internal link (nav links, index cards, detail page links) prefetches its destination on hover, eliminating network fetch latency on click. No separate integration package needed — native to Astro 5.

- **Tightened View Transition timing** — Added global CSS overrides for all `::view-transition-group(*)`, `::view-transition-old(*)`, and `::view-transition-new(*)` pseudo-elements in BaseLayout.astro:
  - Old page (fade out): 100ms
  - New page (fade in): 120ms
  - Entire group lifecycle: 120ms
  - Timing curve: `cubic-bezier(0.16, 1, 0.3, 1)` — high-velocity deceleration for snappy feel

- **notransition pages instant swap** — The CSS overrides apply globally, including to the errors page (with `notransition` cards). The default crossfade fallback now completes in 120ms instead of the browser's default ~700ms, ensuring instant document swap on high-card-count pages.

### Changed

- `site/astro.config.mjs` — added `prefetch: { prefetchAll: true, defaultStrategy: "hover" }`
- `site/src/layouts/BaseLayout.astro` — added view transition CSS pseudo-element overrides

### Build

- 5,246 pages, 0 errors, ~70s

## [0.43.1] — 2026-05-30 — **Emergency Runtime Fix**

### Fixed

- **DMV card dimensions (broken layout)** — Removed `white-space: nowrap` from `.card-title` rule in BaseLayout.astro's global text containment block. `.card-title` no longer forced to single-line overflow; Card.astro's own `overflow-wrap: break-word; word-break: break-word; hyphens: auto` rules now apply correctly, allowing long DMV names to wrap naturally.

- **Errors page browser-thread freeze** — Added `notransition` prop to Card.astro. When set, `transition:name` attribute is omitted from card titles, preventing Astro's View Transitions engine from processing 1,129 named elements (the root cause of the main-thread hang on navigation). Applied `notransition` to all Card usages in `errors/index.astro`. All other collection pages retain View Transition morphing.

### Changed

- `site/src/components/Card.astro` — added `notransition?: boolean` prop; conditionally sets `transition:name` via `{...titleAttrs}` spread (only when `!notransition`)
- `site/src/layouts/BaseLayout.astro` — removed `.card-title` from `white-space: nowrap` overflow rule
- `site/src/pages/errors/index.astro` — added `notransition` to `<Card>` invocation

### Build

- 5,246 pages, 0 errors, ~33s

## [0.43.0] — 2026-05-30 — **Stable / Production Ready**

The architectural refactoring cycle is complete. All core systems — data layer, component architecture, search infrastructure, view transitions, build pipeline — are finalized.

### Added

- **Stage 46: Fluid Spatial View Transitions & Component Polish** — Comprehensive interaction upgrade for seamless page navigation:

  1. **Morphing View Transitions** — Astro View Transitions engine globally active. Added `transition:name` attributes to Card.astro's `.card-title` (derived from href slug) and matching attributes on all 12 detail page templates (`transition:name={entry.slug}`). Card titles now visually scale and morph into detail page headers on navigation, eliminating jarring page jumps.

  2. **Elastic Micro-Interactions** — `.item-card` hover states upgraded with `cubic-bezier(0.25, 1, 0.5, 1)` timing curve for border-color, transform, background, and box-shadow transitions. Hover now shifts `translateY(-3px)` with subtle shadow depth and background darkening for a crisp, instantaneous feel.

  3. **Repository Cleanup** — Removed manual page-fade-in CSS animation (conflicted with View Transitions). Removed `transition:animate="fade"` from main shell. Scrubbed all design-language references ("macOS Spotlight", "glassmorphism", Stage numbering) from comments across BaseLayout.astro, SearchPalette.astro, CardPalette.astro, and RelatedLinks.astro.

- **Version bump**: 0.36.0 → 0.43.0 (package.json)

### Changed

- `src/components/Card.astro` — added `transition:name` prop on title, elastic cubic-bezier hover transitions
- `src/layouts/BaseLayout.astro` — removed manual page-fade animation, removed `transition:animate="fade"`, cleaned design language comments
- All 12 `src/pages/*/[id].astro` — added `transition:name={entry.slug}` on detail page titles
- `src/components/SearchPalette.astro` — scrubbed design language references
- `src/components/CardPalette.astro` — scrubbed design language references
- `src/components/RelatedLinks.astro` — scrubbed design language references

### Build

- 5,246 pages, 0 errors, ~29s
- Prettier lint passes

## [0.41.0] — 2026-05-30

### Added

- **Stage 44: T-SQL Reference Deep Content Validation** — Exhaustive semantic audit across all 542 files in `src/content/tsql-reference/`:

  1. **Content Validation Utility** — Created `tools/audit-tsql-reference.mjs`, a Node.js script that scans every file for: empty/suspicious descriptions, garbled PDF extraction artifacts (U+FF89 halfwidth katakana), fragmented body content (>70% single-word lines), undersized content (<20 words), and title capitalization inconsistencies. Outputs detailed markdown audit report.

  2. **Auto-Fix & Repair** — Applied 282 automated corrections:
     - **50 empty descriptions** filled from body content or title
     - **60 markdown-heading-as-description** entries replaced with meaningful prose
     - **6 copilot-prompt artifacts** (`"Summarize this article for me"`) replaced
     - **121 files had garbled Unicode artifacts removed** (U+FF89 PDF extraction junk)
     - **51 titles capitalized** (lowercase first-letter fix for catalog indexing)

  3. **Title Standardization** — Created `tools/fix-titles.mjs` to capitalize all 51 lowercase-starting titles for consistent catalog rendering.

  4. **Audit Report** — Full report written to `audit-tsql-reference-report.md` documenting all defects, fixes applied, and recommendations for remaining manual work (114 fragmented files flagged for future restoration).

### Infrastructure

- Build: 5,273 pages, 0 errors, ~31s
- Package: version bumped to 0.41.0

## [0.40.0] — 2026-05-30

### Added

- **Stage 43: Search, Typography & Code Copy Polish** — High-fidelity UI refinements across three areas:

  1. **SearchPalette Backdrop & Focus** — Backdrop changed from `rgba(0,0,0,0.55)` + `blur(8px)` to `rgba(0,0,0,0.4)` + `blur(16px)` for premium immersive overlay. Removed all `!important` outline overrides; added `caret-color: var(--accent)`; added `:focus-within` glow ring on `.palette-input-wrap` with subtle border tint and smooth `0.25s ease` transition (macOS Spotlight behavior).

  2. **Unified `.prose-content` Typography Engine** — Created global prose styling with `line-height: 1.7`, `letter-spacing: 0.005em`, optimized heading letter-spacing, accent-colored prose links with hover transition, and clean table styling (border-glass borders, `0.6rem 1.1rem` cell padding, rounded corners). Applied as additional class to all 12 detail templates for backward compatibility.

  3. **Code Copy Button Polish** — Changed from `opacity: 0` (hidden until hover) to `opacity: 0.25` (always subtly visible), full opacity on hover; added background darkening transition.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~52s
- Package: version bumped to 0.40.0

## [0.39.0] — 2026-05-30

### Changed

- **Stage 41: Cookbook & XEvents Card Migration** — Migrated 2 remaining collection index pages (cookbook, xevents) to the unified Card.astro component, achieving 100% component parity across all 11 collections:

  1. **Cookbook** — Replaced manual `<a class="item-card">` with `<Card>` using named slots (`title`, `meta` for severity badge, `description`, `tags`). Removed 70 lines of per-collection CSS.

  2. **XEvents** — Replaced manual `<a class="xevent-card">` with `<Card>` using the default slot fallback (non-standard card layout). Renamed `.card-header` to `.xevent-header` to avoid clash with Card.astro's global `.card-header` CSS.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~31s
- Package: version bumped to 0.39.0

## [0.38.0] — 2026-05-30

### Added

- **Stage 40: Dynamic Card Composition** — Created `Card.astro` (`src/components/Card.astro`), a unified reusable card shell component with hybrid slot architecture:

  1. **Named slots** (`title`, `meta`, `description`, `tags`): For standard cards with header, description, and tag pills.

  2. **Default slot fallback**: For complex/specialty cards — the `<Card>` shell provides `.item-card` styling and hover effects while letting the consumer define all inner HTML.

  3. **Global CSS** — All card-level CSS centralized in `<style is:global>`: `.item-card` (glass border, accent hover, translateY lift), `.card-header` (flex space-between, align-items: flex-start), `.card-title` (mono font, overflow-wrap), `.card-desc` (3-line clamp), `.card-tags`, `.card-tag`.

### Changed

- **Migrated 9 collection index pages** from manual card HTML + per-collection CSS to `<Card>` component: architecture, catalog-views, dmvs, errors, functions, scripts, stored-procedures, tsql-reference, wait-statistics.
- **CardPalette.astro** — simplified, removed duplicated card CSS.
- **400+ lines of duplicate card CSS removed** across all collection pages.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~31s
- Package: version bumped to 0.38.0

## [0.37.0] — 2026-05-30

### Fixed

- **CSS Overflow & Layout Integrity** — Long identifiers (function names, wait types, error numbers) breaking out of `.item-card` containers across all collection index pages and the search palette:

  1. **CardPalette.astro (global CSS)** — Added `min-width: 0` to `.item-card` so grid/flex children can shrink below content size. Changed `.card-title` from `white-space: nowrap; overflow: hidden; text-overflow: ellipsis` (truncation) to `overflow-wrap: break-word; word-break: break-word; hyphens: auto` (wrapping) so all identifiers remain fully visible and readable.

  2. **Functions Page** — Added `overflow-wrap: break-word; word-break: break-word; hyphens: auto; min-width: 0` to `.fn-name`. Changed `.card-header` `align-items` from `center` to `flex-start` (badge stays top-aligned when title wraps) and added `min-width: 0`.

  3. **Errors Page** — Added same overflow protection to `.error-number` and `.card-header`, with `align-items: flex-start` and `min-width: 0`.

  4. **Wait Statistics Page** — Added same overflow protection to `.wait-name` and `.card-header`, with `align-items: flex-start` and `min-width: 0`.

  Fix cascades to all 6 other collection pages using `.card-title` (scripts, DMVs, stored procedures, catalog views, architecture, T-SQL reference) — their scoped CSS doesn't set overflow properties, so the global CardPalette rules apply.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~31s
- Package: version bumped to 0.37.0

## [0.36.0] — 2026-05-30

### Added

- **Stage 36: Productization & Social Polish** — SEO standardization, OpenGraph meta, sitemap generation, and robots.txt for search engine readiness:

  1. **SEO.astro Component** — New reusable component generating all `<head>` meta tags: `<title>`, `<meta name="description">` (160-char truncated), `<link rel="canonical">` (self-referencing full URL), OpenGraph (`og:title`, `og:description`, `og:url`, `og:type`, `og:site_name`, `og:image`), and Twitter Card (`summary_large_image`). Canonical URL auto-computes from `Astro.url`. Accepts optional `canonicalUrl`, `ogImage`, and `ogType` overrides per page.

  2. **BaseLayout Integration** — Updated to import `<SEO />` and pass all props (title, description, image, canonical) through. Title format: `"{Title} — SqlKraft"` (site suffix). OG image defaults to favicon.svg.

  3. **@astrojs/sitemap Integration** — Added to `astro.config.mjs`. Generates `sitemap-index.xml` at build time with all 5,273 pages. Filters out `trash/` paths. Weekly changefreq, 0.7 priority.

  4. **robots.txt** — Created at `public/robots.txt`. Allows all crawlers (`Allow: /`), explicitly disallows `Disallow: /trash/`, points to `Sitemap: https://kedharsairam.github.io/sqlkraft/sitemap-index.xml`.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~39s (includes sitemap generation)
- Package: `@astrojs/sitemap` added; package.json version bumped to 0.36.0

## [0.35.0] — 2026-05-30

### Added

- **Content Restoration from Trash** — Audited 1,328 ghost files in `src/content/trash/` and restored 8 valuable T-SQL scripts back to the live scripts collection:

  1. **Trash Audit** — Scripted audit of all 1,328 ghost files across 4 collections (tsql-reference: 1,228, scripts: 87, architecture: 9, errors: 4). Body length distribution: 46 stubs, 1,218 short, 64 medium, 0 long.

  2. **Script Restoration** — 8 script files with real SQL code (break mirroring, create table, grant/revoke masked rows, increase MTL size, restore backup, view tables, view replication tables, view tasks/threads/schedulers) restored to `src/content/scripts/`. All other 1,320 files remain in trash (tsql-reference files were parameter type listings without prose; architecture/errors were empty stubs).

  3. **Search Index Updated** — Rebuilt `search-index.json` (5,243 records, up from 5,235) and `palette-index.json` to include the restored scripts.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~32s (scripts collection grew from 183 to 191 entries)

## [0.34.0] — 2026-05-30

### Added

- **Stage 34: Spotlight Category Grouping** — Category headers now sticky with macOS-style behavior:

  1. **Sticky Headers** — `.palette-cat-header` uses `position: sticky; top: 0; z-index: 1;` with a semi-transparent background (`rgba(22,22,22,0.92)`) and `backdrop-filter: blur(12px)` so headers stay visible at the top of the results list while scrolling through a group, matching macOS Spotlight behavior.

  2. **Refined Styling** — Headers updated with `letter-spacing: 0.1em`, muted `rgba(255,255,255,0.25)` color, and subtle bottom border (`rgba(255,255,255,0.04)`) for clear visual separation between groups.

  3. **Keyboard Nav Preserved** — `resultItems` selector already targets only `.palette-item` elements, skipping `.palette-cat-header`. Category grouping and custom sort order (`catOrder`) were already implemented in Stage 32.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~15s

## [0.33.0] — 2026-05-30

### Added

- **Stage 33: Card Component Injection into Search Palette** — Replaced manually-constructed list item HTML in search results with `.item-card` structure matching collection index page cards:

  1. **Component Injection** — Rewrote `CardPalette.astro` to expose `window.__renderCard()` which generates HTML matching the `.item-card` / `.card-title` / `.card-desc` / `.card-tags` / `.card-tag` structure used by DMVs, Functions, Errors, and all other collection index pages. Search results now render as beautiful, clickable, high-fidelity tiles identical to the site's design language.

  2. **Global Card CSS** — Defined shared global styles in `CardPalette.astro` for `.item-card`, `.card-title`, `.card-desc`, `.card-tags`, `.card-tag` that match collection page visual language (mono font titles, secondary text descriptions, pill-style tags, glass border, `var(--bg-secondary)` background). Added `.palette-card` modifier for compact palette sizing with active keyboard selection state. Removed all manual `.palette-card-*` custom CSS classes.

  3. **SearchPalette Refactor** — Updated `SearchPalette.astro` to call `__renderCard()` instead of the old `__renderPaletteCard()`. Fixed click event delegation selector from dead `a.palette-result` to `a.item-card`. Removed stale category badge CSS. No more custom padding, font-weight, or border styling on list items — all styling handled by the Card.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~25s

## [0.32.0] — 2026-05-30

### Added

- **Stage 32: Search Integrity & Component Unification** — Two critical fixes:

  1. **Component Unification (UI)** — Created `CardPalette.astro` as a reusable small-scale card component for search palette results, matching the visual style of site index cards (44px height, 6px border-radius, `#1a1a1a` hover with 2px border-left accent, bold title + category badge typography, `text-overflow: ellipsis` truncation). Refactored `SearchPalette.astro` (v5) to use `CardPalette` via `window.__renderPaletteCard()` runtime render function. CSS split: palette item/card/badge styles moved to `CardPalette.astro` with `<style is:global>` for proper runtime rendering (Astro scoped CSS did not apply to `innerHTML`-rendered elements). Removed ~170 lines of duplicated CSS and dead JS (`formatBadge`, `escHtml`, `resultIcon`) from SearchPalette.

  2. **Index Audit (404 Prevention)** — Fixed `rebuild-search-index.cjs` to exclude the `trash/` directory via `EXCLUDED_DIRS` filter. Regenerated `search-index.json` from actual content files only: 12 collections scanned (trash skipped), 5,235 index records (down from ~6,588). All URLs now match production build paths — no entries for trashed/deleted files that would produce 404s.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~30s
- Search index: 5,235 records across 12 collections (clean, no trash entries)

## [0.31.0] — 2026-05-30

### Fixed

- **Stage 31: Spotlight UI Precision** — Two UX defects resolved in SearchPalette component:

  1. **Dynamic UI Collapse** — The results container now uses `display: none` when input length < 2 characters, making the palette appear as a minimal search bar when idle. The "Type 2+ characters to search..." permanent text has been removed entirely — the input placeholder serves this role instead.

  2. **High-Fidelity Result Card Styling** — Each result row redesigned as a compact card: fixed 44px height, generous `16px` side padding, flexbox layout with [Title (bold/white)] + [Category badge (right-aligned)], distinct hover state with `#1a1a1a` background tint and subtle 2px `rgba(255,255,255,0.15)` border-left accent. `text-overflow: ellipsis` enforced on all titles. File icon and description line removed for cleaner single-line cards.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~38s

## [0.30.0] — 2026-05-30

### Changed

- **Stage 30: High-Fidelity macOS Spotlight Transformation** — Complete redesign of `SearchPalette.astro` to match the macOS Spotlight aesthetic. Card-style result rows replaced with fixed 50px icon+title+desc+badge layout. Selected state now uses `#007aff` 3px border-left accent via `::before` pseudo-element. Input font-size set to `1.5rem` with no outline/shadow/border. Glass panel upgraded: `backdrop-filter: blur(24px)`, `border: 1px solid rgba(255,255,255,0.1)`, `box-shadow: 0 20px 60px rgba(0,0,0,0.5)`, `border-radius: 12px`. Entry animation: `0.25s cubic-bezier(0.2, 0.8, 0.2, 1)` with scale(0.95) translateY(-12px). Result items fade-in with `translateY(5px)` staggered by `animation-delay` (20ms per item). Generic file icon (document SVG) replaces arrow-hint and left side badge. Right-side category badges retained. All result/animation CSS now uses explicit `-apple-system` font stack.

### Infrastructure

- Build: 5,273 pages, 0 errors, ~33s

## [0.27.0] — 2026-05-30

### Added

- **Stage 27: Data Integrity Audit & Prune** — Created `scripts/audit-content.js`, a build-time audit script that scans all `src/content/**/*.md` files, extracts body content (excluding YAML frontmatter), and moves files with < 100 meaningful non-whitespace body characters to `src/content/trash/`. Integrated as the first step of the `prebuild` hook in `site/package.json`.

### Infrastructure

- **1,328 ghost files pruned** — Empty/placeholder content stubs detected and moved to `trash/` across 4 collections: `tsql-reference` (1,228), `scripts` (87), `architecture` (9), `errors` (4). All trashed files preserve their relative path structure for easy recovery.
- **Build output reduced** — From ~6,601 to 5,273 pages (1,328 fewer empty pages). Build time: ~33s, 0 errors.
- **Prebuild pipeline** — Audit runs before palette index generation, ensuring ghost files never pollute the search index or appear in production builds.

## [0.26.1] — 2026-05-30

### Fixed

- **Critical: Search palette unresponsive on View Transitions (v0.26.0 regression)** — The bundled `<script>` in SearchPalette.astro only ran once on initial page load. Astro View Transitions replace `<body>` DOM on navigation, orphaning the overlay/input/results closure references and the search-btn click listener. Fixed by changing to `<script is:inline data-astro-rerun>` so the code is embedded directly in HTML and re-executes on every navigation. Added `__searchPaletteCleanup` to prevent duplicate document-level keydown listeners. Moved search-btn click handler into SearchPalette for reliable re-attachment.

## [0.26.0] — 2026-05-30

### Changed

- **Stage 26: UI/UX & Functional Lockdown** — Removed local search bar from `scripts/index.astro` (all search now via global Spotlight `Cmd+K`); refactored `SearchPalette.astro` to card-style result rows with category badge | title+description | arrow icon; enforced 2+ character input threshold before search activates; added global CSS containment (`text-overflow: ellipsis`) on `.card-title` and all component headings; standardized typography across BaseLayout and RecipeLayout

### Infrastructure

- 6,601 pages, 0 build errors, 0 lint warnings
- Git history consolidated from legacy backup; force-pushed to GitHub

## [0.22.0] — 2026-05-30

### Added

- **Stage 23: Premium Inline Link Previews (Hover Cards)** — Zero-latency glassmorphic hover card link previews across all 6,595 content pages:
  - **Shared palette index** — `window.__paletteIndex` set by SearchPalette.astro after the palette index JSON fetch resolves; hover card code reuses the same 970 KB in-memory index with a fallback fetch if not yet loaded
  - **400ms debounced hover** — `mouseenter` on each internal `.body-content` `<a>` tag starts a debounce timer; hover card only appears after 400ms of sustained hover (prevents flash on accidental cursor passes)
  - **Palette index lookup** — `lookupEntry()` normalizes the link `href` (strips base URL `/sqlkraft`, normalises trailing slashes) and matches against the 6,539-entry palette index by path; card shows title, description, and category
  - **Glassmorphism card** — `background: rgba(15,15,15,0.85)`, `backdrop-filter: blur(16px)`, `border: 1px solid rgba(255,255,255,0.08)`, `border-radius: 10px`, `box-shadow: 0 8px 32px rgba(0,0,0,0.5)`
  - **Entrance animation** — `opacity: 0 → 1` + `translateY(4px) → 0` over 150ms ease for a premium fade-in; exit reverses the same transition
  - **Edge-aware positioning** — Card placed to the right of the hovered link by default; flips to the left if insufficient right viewport space; clamped to prevent bottom/top overflow
  - **`pointer-events: none`** on the card element ensures it never blocks clicks on the link underneath
  - **Hide on scroll** — A passive `scroll` event listener hides the card when the user scrolls
  - **Stale-timer guard** — `hoverCurrentLink` variable prevents race conditions where an old timeout fires after the cursor has moved to a different link
  - **Build**: 6,595 pages, 0 errors, ~34s

### Changed

- **SearchPalette.astro** — Added `window.__paletteIndex = data` on line 77 so the palette index is globally accessible to the hover card system
- **BaseLayout.astro** — Added empty `<div id="link-preview-card">` container (line 98), ~70 lines of hover card CSS (glassmorphism, transitions, title/description/meta typography), and ~100 lines of Vanilla JS IIFE (index init, debounced hover logic, entry lookup, edge-aware positioning, scroll hide)

## [0.19.0] — 2026-05-30

### Added

- **Stage 20: Spotlight Command Palette** (`src/components/SearchPalette.astro`) — Apple-grade Ctrl+K/⌘K search overlay replacing the Fuse.js-based SearchOverlay:
  - **Pure Vanilla JS fuzzy search** — Custom character-by-character scorer with positional/word-boundary/consecutive bonuses; no third-party libraries (Fuse.js removed)
  - **Lightweight palette index** — `palette-index.json` (970 KB, down from 2 MB) generated at build time from the full `search-index.json` via `scripts/generate-palette-index.js`
  - **Glassmorphism overlay** — `background: rgba(15, 15, 15, 0.75)`, `backdrop-filter: blur(24px)`, `border: 1px solid rgba(255,255,255,0.08)`, premium shadow depth, centered at `top: 15vh`
  - **Smooth enter animation** — `palette-enter` keyframe (scale 0.96 + translateY, 0.15s cubic-bezier)
  - **Category-grouped results** — Hits organized under section headers (DMVs, Wait Statistics, Scripts, etc.) with predefined category sort order
  - **Keyboard-first navigation** — ArrowDown/ArrowUp cycle results with visual active state (left border highlight + background tint), Enter navigates to URL
  - **Global shortcut** — Cmd+K/Ctrl+K toggle; Escape/backdrop-click to close; auto-focus on open
  - **Debounced input** — 120ms timeout prevents excessive re-renders during fast typing
  - **Result limit** — Top 28 matches with score descending

### Changed

- **BaseLayout.astro** — Replaced `SearchOverlay` import + usage with `SearchPalette`; updated inline script to use `window.__openPalette()` for both desktop search button and mobile drawer trigger
- **package.json** — `predev` and `prebuild` now run `node scripts/generate-palette-index.js` before the copy step; `fuse.js` dependency removed

### Removed

- **SearchOverlay.astro** — Deleted (replaced by SearchPalette)
- **fuse.js** — Uninstalled (no longer needed)

## [0.19.1] — 2026-05-30

### Fixed

- **Stage 20.1: SearchPalette 404 routing & UI polish** — Post-launch fixes for the Spotlight command palette:
  - **BASE_URL injection** — `data-base-url` attribute on the palette div reads from `import.meta.env.BASE_URL` in Astro frontmatter; all result `href` values now correctly prepend `/sqlkraft/` for GitHub Pages routing, fixing 404 errors on every palette navigation
  - **Structured list markup** — Results rendered as `<ul class="palette-list">` / `<li class="palette-item">` with `border-radius: 8px`, `rgba(255,255,255,0.08)` hover state, and single-line truncated description (`text-overflow: ellipsis`); category headers are distinct `<li>` elements with `role="separator"`, muted uppercase text, and `border-top` divider
  - **Navbar search pill width** — `.nav-search-btn` widened to `min-width: 200px` with `justify-content: space-between` for proper desktop appearance

## [0.21.0] — 2026-05-30

### Added

- **Stage 22: Code Block Line Numbers (CSS Counter Gutter)** — Professional line numbering on all Shiki-highlighted code blocks across all 6,595 pages:
  - **CSS counter line numbering** — `counter-reset: line` on each `<pre class="astro-code">`; `counter-increment: line` / `content: counter(line)` on each `<span class="line>::before` — zero DOM overhead, no JS, works on every Shiki-rendered code block
  - **Sticky gutter** — `position: sticky; left: 0; z-index: 2` on `::before` locks the line number gutter to the left edge during horizontal scroll of long code lines
  - **Unselectable numbers** — `user-select: none` (plus vendor prefixes) on the `::before` pseudo-element prevents line numbers from being included in manual text selection or the universal copy-to-clipboard button (which uses `pre.textContent` — CSS-generated content is excluded from `.textContent` per DOM spec)
  - **Apple-grade visual styling** — Darkened gutter (`background: rgba(0,0,0,0.15)`) with `border-right: 1px solid rgba(255,255,255,0.05)` separator; muted monospace color `rgba(255,255,255,0.25)`; right-aligned tabular numbers at `3.4ch` minimum width; `0.75em` margin after separator for clean code spacing
  - **Zero-interference layout** — `<code>` becomes `display: flex; flex-direction: column`; each `.line` is `display: flex` with `min-height: 1.4em` — preserves full Shiki syntax highlighting, works with the existing copy button positioning, adds zero new DOM elements

## [0.20.0] — 2026-05-30

### Added

- **Stage 21: Premium Content Reader Experience** — Three client-side enhancements that elevate the reading experience across all 6,595 content pages:
  - **Sticky right-rail Table of Contents** (`#toc-sidebar`) — Dynamically generated from `.body-content` h2/h3 headings on pages with ≥2 headings; active section tracking via `IntersectionObserver` with `rootMargin: "-80px 0px -70% 0px"`; smooth-scroll click navigation; hidden at ≤1200px via `display: none !important`; only activates when `.body-content` exists
  - **Universal copy-to-clipboard** — Every `<pre>` block inside `.body-content` gets an injected `.code-copy-btn` button (absolute-positioned, top-right); invisible by default (`opacity: 0`, `pointer-events: none`), appears on `.copy-code-wrap:hover`; swaps to checkmark for 2 seconds on success; shows "Failed" for 2 seconds on error via `navigator.clipboard.writeText(pre.textContent)`
  - **View Transitions API** — `import { ViewTransitions } from "astro:transitions"` with `<ViewTransitions />` in `<head>`; `transition:animate="fade"` on `<main class="app-shell">` for cross-page fade transitions; CSS `@keyframes page-fade-in` fallback for browsers without View Transitions support

### Changed

- **BaseLayout.astro** — +222 lines of global inline JS for TOC generation (heading ID assignment, fragment-link building, IntersectionObserver tracking) and copy button injection (`pre.style.position = "relative"`, button creation, click handler); CSS for `.toc-sidebar` (fixed position, sticky right rail), `.code-copy-btn` (absolute, hidden until hover), `.copy-code-wrap:hover` (reveals button), and `.toc-link.active` (muted highlight); `<ViewTransitions />` component imported and rendered in `<head>`

### Removed

- **scripts/[id].astro** — Stale per-page copy button HTML, JavaScript click handler, and CSS class removed (subsumed by the universal BaseLayout utility)

## [0.18.1] — 2026-05-30

### Changed

- **Stage 19.8: The Minimalist Pivot & Layout Purge** — Complete removal of the SQL Server Execution Engine Pipeline diagram from the homepage to achieve a true typography-first, Apple-grade hero section:
  - **Pipeline canvas purged** — Removed the entire `pipeline-section` including Protocol Layer block, Relational Engine container (Parser → Algebrizer → Optimizer → Executor), Storage Engine container (Access Methods ↔ Transaction Manager ↔ Buffer Pool), and all down-arrow connectors
  - **Hero re-balanced** — Added generous `margin-bottom: clamp(3.5rem, 6vw, 6rem)` to the hero section so the page breathes without the diagram
  - **Matrix grid flush** — Set `margin-top: 0` on the directory grid (spacing now handled entirely by hero margin)
  - **All pipeline CSS removed** — Deleted `.pipeline-section`, `.pipeline-panel`, `.pipeline-label`, `.protocol-block`, `.engine-block-*`, `.engine-container-*`, `.pipe-node`, `.pipe-arrow`, `.pipe-icon`, `.bi-arrow`, `.pipeline-down-arrow`, and every related class
  - **Search elevated** — The existing Ctrl+K/⌘K global search overlay (anchored in the top navigation bar) remains as the primary command-entry point, perfectly balanced in the top nav
  - **Card counts confirmed absent** — The four directory cards remain clean without the `160+`/`50+`/`270+`/`3` badges as instructed in Stage 19.7
  - **Responsive simplified** — Pipeline-specific breakpoint rules removed; only matrix-grid and secondary-links responsiveness remains

## [0.18.0] — 2026-05-30

### Changed

- **Stage 19.7: Authentic Engine Architecture & Noise Reduction** — Homepage (`src/pages/index.astro`) refactored to accurately represent SQL Server's query execution stack and remove consumer-oriented UI elements:
  - **Stripped card counts** — Removed numeric count badges (`160+`, `50+`, `270+`, `3`) from all four directory matrix cards for a cleaner, more enterprise-utility aesthetic
  - **Vertical block architecture** — Replaced the two-row horizontal stepper with a top-down nested schematic matching SQL Server's true architectural stack:
    - **Protocol Layer (SNI / TDS)** — Wide entry block at the top with globe SVG icon and thin border
    - **Relational Engine / Query Processor** — Bordered container with sequential flow: [Parser] → [Algebrizer] → [Optimizer] → [Executor] (Algebrizer added with tree-struct SVG icon; replaces the previous Optimizer-first ordering)
    - **Storage Engine** — Bordered container with interconnected blocks: [Access Methods] ↔ [Transaction Manager] ↔ [Buffer Pool] (Transaction Manager replaces Transaction Log; uses bidirectional arrows to reflect peer relationships)
    - **Vertical down-arrows** — Subtle SVG arrows connecting Protocol Layer → Relational Engine → Storage Engine
  - **CSS restructure** — `.pipeline-engine-row`, `.pipeline-engine-label`, `.engine-label-text`, `.engine-label-divider`, `.pipeline-engine-steps`, `.pipe-group*`, and `.matrix-count` removed; replaced with `.engine-block*`, `.protocol-block`, `.pipeline-down-arrow`, `.engine-block-container`, `.engine-container-steps`, `.engine-container-interconnected`, and `.bi-arrow` classes

## [0.17.2] — 2026-05-30

### Fixed

- **Stage 19.6: Engine Architecture Correction** — Corrected the SQL Server Execution Engine Pipeline layout on the homepage (`src/pages/index.astro`) to accurately reflect SQL Server internals:
  - **Two-row stacked layout** — Replaced single horizontal track with architecturally distinct rows: Relational Engine (top) and Storage Engine (bottom), separated by a subtle border for visual breathing room
  - **Relational Engine corrected** — Sequence is now [Parser] → [Optimizer] → [Executor] (Executor was missing; play-triangle SVG icon added)
  - **Storage Engine corrected** — Sequence is now [Access Methods] → [Buffer Pool] → [Transaction Log] (Access Methods moved to first position with magnifier SVG icon; determines page requests before Buffer Pool retrieval)
  - **Labels as category headers** — Engine labels now act as category headers separated from the step nodes by a subtle vertical divider, not inline badges with arrows
  - **Responsive** — Rows collapse to stacked label-above-steps layout at 900px; steps stack vertically at 540px

## [0.17.1] — 2026-05-30

### Changed

- **Apple-grade proportional tuning** — Visual refinements to the homepage (`src/pages/index.astro`):
  - **Hero left-aligned** — Title, tagline, and subtitle now align to the left-edge grid axis instead of centered; reduced vertical gap to pipeline panel
  - **Flattened pipeline** — Converted vertical stack into a cohesive horizontal architectural track; engine labels (`Relational Engine`, `Storage Engine`) now sit inline as start-nodes in the flow with a compact arrow divider between groups; drastically reduced container height
  - **Sub-surface background depth** — Fixed `bg-canvas` with radial gradient aura (ellipse at 50%/30%) plus 48px geometric grid lines at `rgba(255,255,255,0.006)` creating visible glassmorphism material depth for the `backdrop-filter: blur(20px)` panel
  - **Card padding & metric integration** — Matrix card padding increased to `clamp(1.5rem, 2vw, 2rem)`; metric counts (`160+`, `50+`, etc.) moved into `matrix-title-row` alongside category headers for proportional integration
  - **Secondary links** — Changed from centered to left-aligned for consistency with hero
- **Pipeline responsive** — Groups stack vertically at 900px breakpoint; divider hidden; arrow rotation on mobile

## [0.17.0] — 2026-05-30

### Changed

- **Apple-grade homepage rewrite** — Complete redesign of `src/pages/index.astro` with premium UX:
  - **Execution Engine Pipeline** — Full-width glass panel (`backdrop-filter: blur(20px)`, `rgba(15,15,15,0.6)`) showing SQL Server processing flow: Relational Engine (Parser → Optimizer) → Storage Engine (Buffer Pool → Access Methods → Transaction Log) with inline SVG icons and flow arrows
  - **Unified Directory Matrix** — Four symmetrical cards (DMV Directory, Wait Statistics, T-SQL Scripts, Troubleshooting Cookbook) in a responsive 4-column grid, each with unique mini SVG data visualization
  - **Secondary link pills** — 7 additional collection links in pill-shaped buttons below the matrix
  - **Apple-grade transition curve** — All interactive elements use `cubic-bezier(0.16, 1, 0.3, 1)` with 0.4s duration; hover micro-lift with border opacity increase
  - **Responsive grid** — 4 → 2 → 1 column at 900px and 540px breakpoints; pipeline nodes stack vertically on mobile

## [0.16.0] — 2026-05-30

### Added

- **Adaptive mobile navigation drawer** — Full-screen overlay menu with hamburger toggle for viewports ≤ 768px:
  - Hamburger button with CSS-only animated X transition (3-line → rotate cross via `.is-active`)
  - Dark semi-transparent overlay (`rgba(0,0,0,0.97)`) with `backdrop-filter: blur(16px)` matching the premium aesthetic
  - Smooth `opacity` + `translateY` entrance/exit transitions (`0.2s ease-out`)
  - Search trigger with `Ctrl+K` hint badge at the top of the drawer — tapping opens the search overlay
  - All 11 nav links rendered with 17px type, `var(--space-sm)` vertical padding, and `border-radius: 6px` touch targets
  - Body scroll locked (`overflow: hidden`) while drawer is open
  - Drawer closes automatically when any nav link or search trigger is tapped
  - Desktop nav links and search button hidden via `display: none` at the breakpoint; hamburger shown

## [0.15.0] — 2026-05-30

### Added

- **Cross-Collection Troubleshooting Cookbook** — New `cookbook` content collection with 3 initial scenario-based diagnostic guides:
  - *High CPU Diagnostic Path* — Cross-references `sys.dm_os_schedulers`, `sys.dm_exec_query_stats`, `SOS_SCHEDULER_YIELD` waits, and CPU diagnostic scripts
  - *Memory Pressure Triage* — Cross-references `sys.dm_os_process_memory`, `RESOURCE_SEMAPHORE` waits, `PAGEIOLATCH_SH` waits, and buffer pool analysis scripts
  - *Locking & Blocking Outages* — Cross-references `sys.dm_tran_locks`, `LCK_M_*` wait types, blocking identification scripts, and deadlock graph capture
- **`src/pages/cookbook/index.astro`** — Category-grouped index page with severity badges, jump-nav pill bar, and the same `minmax(clamp(240px, 18vw, 320px), 1fr)` card grid used across all collections
- **`src/pages/cookbook/[id].astro`** — Dynamic detail route rendering recipe content with breadcrumbs, tags, and severity badge
- **`src/layouts/RecipeLayout.astro`** — Cross-reference card grid with type-labeled icons (V=DMV, W=Wait, S=Script, E=Error) linking back to existing detail pages
- **`relatedContent` schema field** — New structured frontmatter field (`{ dmvs?: [], waits?: [], scripts?: [], errors?: [] }`) enabling per-recipe cross-collection linking
- **"Recipes" nav link** — Added to the global navigation bar between Scripts and Search
- **Search index integration** — `cookbook` collection added to `rebuild-search-index.cjs`; search index now includes 3 recipe records (6,539 total)

## [0.14.0] — 2026-05-30

### Added

- **Mac-aware keyboard shortcut detection** — Badge and `aria-label` dynamically switch to `⌘K` on macOS (`navigator.platform.includes("Mac")`); SearchOverlay placeholder updates to `(⌘K)` as well

### Changed

- **Search shortcut badge polished** — `.search-shortcut` now styled as a proper badge with `background: rgba(255,255,255,0.1)`, `border: 1px solid var(--border-glass)`, `border-radius: 4px`, and `padding: 2px 6px` for a crisp, minimalist look
- **Nav search button hover neutralized** — `.nav-search-btn:hover` border color changed from `var(--accent)` (blue) to `var(--text-primary)` (white) completing the site-wide accent→neutral sweep

## [0.13.0] — 2026-05-29

### Added

- **Arrow-key navigation with active selection** — Search results now track `activeIndex` state; ArrowUp/ArrowDown cycle through results with smooth `scrollIntoView`; Enter navigates to the selected result. Active item gets `background: rgba(255,255,255,0.05)` and `border-left: 2px solid var(--text-secondary)` highlight
- **Ctrl+K placeholder hint** — Search input placeholder updated to `"Search references... (Ctrl+K)"` for discoverability
- **Programmatic result navigation** — `navigateToResult()` helper updates the recently viewed list in `sessionStorage` before navigating, so both click and Enter-key selection are tracked

### Changed

- **Result name color neutralized** — `.result-name` color changed from `var(--accent)` to `var(--text-primary)` matching the site-wide accent→neutral conversion; `.result-cat` background changed from `rgba(47,128,237,0.12)` accent tint to neutral `rgba(255,255,255,0.06)`
- **Hover state refined** — `.result-item:hover` uses `rgba(255,255,255,0.05)` (was accent blue `rgba(47,128,237,0.08)`) for consistent neutral palette

## [0.12.0] — 2026-05-29

### Added

- **Wait Statistics diagnostic section panels** — Individual wait statistic detail pages now render `## Overview` with cool left-border accent (`#58a6ff`), `## Troubleshooting`/`## Diagnostic Mechanics` with warm left-border accent (`#d29922`), and `## See Also` with muted border — each section gets panel background and 3px left-border rail for visual scanning
- **Compact border-muted property tables** — All `.body-content` tables across DMV, Catalog View, Script, and Wait Statistics detail pages refactored with `border: 1px solid var(--border-glass)`, `padding: 0.5rem 1rem` cell padding, `rgba(255,255,255,0.02)` header background, rounded corners via `overflow: hidden`, and last-row border removal

### Changed

- **Script Copy widget redesigned** — Copy button repositioned to `top: clamp(20px, 3vw, 36px)` to align with code block margin; converted to terminal-adjacent `rgba(13,17,23,0.85)` background with `backdrop-filter: blur(4px)`; hover state now includes `transform: translateY(-1px)` lift and `box-shadow: 0 2px 8px rgba(0,0,0,0.3)`; border uses `rgba(255,255,255,0.1)` for premium neutral shell integration
- **Detail title accent → primary** — `.detail-title` color changed from `var(--accent)` to `var(--text-primary)` on DMV, Catalog View, and Script detail pages (Wait Statistics was already `var(--text-primary)`)
- **Cat-badge accent → secondary** — `.cat-badge` color changed from `var(--accent)` to `var(--text-secondary)` on DMV, Catalog View, and Script detail pages for neutral palette consistency
- **Wait Statistics related-scripts callout neutralized** — Border changed from `1px solid var(--accent)` to `1px solid var(--border-glass)`, background from blue tint `rgba(47,128,237,0.06)` to neutral `rgba(255,255,255,0.03)`; script link pills also neutralized with `var(--text-secondary)` color and `var(--border-glass)` border

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
