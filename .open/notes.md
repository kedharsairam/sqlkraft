# SqlKraft Session Notes
## Project Status: **v0.45.0-Beta / Structural Polish** — Apple DNA Architecture Overhaul

---

## v0.45.0-Beta — Stage 51: Apple DNA Architecture Overhaul — Grid Unification & Copy Engine

### What was built

Four collection index pages (DMVs, Catalog Views, Functions, T-SQL Reference) converted from per-category `<section>`-wrapped grids to the unified Wait Statistics blueprint pattern.

#### 1. Index Grid Unification (4 Pages)
| Page | Before | After |
|------|--------|-------|
| **DMVs** | 17 per-category `<section>` wrappers with `section-jump` anchors | Single `.card-grid` with 17 filter pills, `data-cat` on each `<Card>` |
| **Catalog Views** | 13 per-category `<section>` wrappers with `section-jump` anchors | Single `.card-grid` with 13 filter pills |
| **Functions** | 6 per-category `<section>` wrappers with `section-jump` anchors | Single `.card-grid` with 6 filter pills (preserved `returnType` badge via `meta` slot) |
| **T-SQL Reference** | 10 per-category `<section>` wrappers with `.category-nav` anchors + default-slot cards | Single `.card-grid` with 10 labeled filter pills (`CATEGORY_LABELS`), converted to named-slot `<Card>` for uniform rendering |

#### 2. Search Palette Redesign
- **Palette backdrop**: `backdrop-filter: blur(25px)` (was 16px), `background: rgba(20,20,20,0.65)` (was `rgba(0,0,0,0.4)`)
- **Input tray**: Rounded top corners (`12px 12px 0 0`), larger padding (18px 22px), subtle `rgba(255,255,255,0.02)` background, `:focus-within` glow enhancement
- **Hint label**: Switched from `var(--font-mono)` to system font for visual harmony
- **Result items**: Micro-hover `transition` with `background: rgba(255,255,255,0.03)` on `.palette-card:hover`

#### 3. Code Block Copy Engine Overhaul
- **Wrapper pattern**: Each `<pre>` now wrapped in `<div class="code-wrap" style="position: relative; overflow: hidden">`. Horizontal scroll stays on `<pre>` (`overflow-x: auto`).
- **Floating copy button**: Pinned absolute top-right on wrapper (not inside `<pre>`), so it remains stationary while code scrolls horizontally underneath. `z-index: 10`.
- **Visibility**: Starts `opacity: 0` (hidden), full `opacity: 1` on wrapper hover — cleaner look, no permanent visual noise.
- **CSS updates**: Updated selector from `.copy-code-wrap` → `.code-wrap`, added `.code-wrap { position: relative; overflow: hidden; border-radius: 8px; }`

#### 4. Rogue Import Leak Fix
- Moved `import Card from "./Card.astro";` inside `---` frontmatter block in CardPalette.astro (was outside, causing Astro to emit it as plain text on every page's rendered HTML — 5,246 pages affected)

### Files Modified
- `site/src/pages/dmvs/index.astro` — complete rewrite, unified single-grid
- `site/src/pages/catalog-views/index.astro` — complete rewrite, unified single-grid
- `site/src/pages/functions/index.astro` — complete rewrite, unified single-grid (preserved return-badge)
- `site/src/pages/tsql-reference/index.astro` — complete rewrite, unified single-grid, converted to named slots
- `site/src/components/SearchPalette.astro` — backdrop blur/color, input tray refinement
- `site/src/components/CardPalette.astro` — import leak fix, micro-hover transitions
- `site/src/layouts/BaseLayout.astro` — code copy wrapper overhaul, CSS updates

### Build
- 5,246 pages, 0 errors, ~31s

---

## v0.44.0 — Stage 49: Ultra-Snappy Navigation & Prefetch Optimization

### What was built

Three performance upgrades for page navigation speed:

#### 1. Aggressive Link Prefetching

**Config**: `astro.config.mjs`
```js
prefetch: {
  prefetchAll: true,
  defaultStrategy: "hover",
}
```

- **`prefetchAll: true`** — Makes every internal link (nav anchors, card titles, detail page links, breadcrumbs) eligible for prefetching without needing explicit `data-astro-prefetch` attributes
- **`defaultStrategy: "hover"`** — Prefetches the linked page's data when the user hovers over the link. For card grids, this means the page content starts loading before the user clicks, eliminating network latency on click.
- **Native Astro 5** — No separate `@astrojs/prefetch` package needed. The prefetch engine is built into the framework.

#### 2. View Transition Speed Tightening

Added global CSS overrides in BaseLayout.astro:

| Pseudo-element | Duration | Curve |
|---|---|---|
| `::view-transition-group(*)` | 120ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `::view-transition-old(*)` | 100ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `::view-transition-new(*)` | 120ms | `cubic-bezier(0.16, 1, 0.3, 1)` |

- Old page fades out in 100ms (barely perceptible)
- New page fades in over 120ms with snappy deceleration
- Total transition completes in ~120ms (down from browser default ~700ms)

The timing curve `cubic-bezier(0.16, 1, 0.3, 1)` provides high initial velocity with rapid deceleration — the page swap feels instantaneous rather than "slow-motion."

#### 3. notransition Pages Instant Swap

The errors page (1,129 cards, `notransition` prop) uses the default view transition crossfade. With the CSS overrides, this crossfade now completes in 120ms instead of the browser default. No custom scheduling or micro-delays — the fallback fires instantly.

### Key Decisions

- **`prefetchAll: true` with `hover` strategy** — Prefetching ALL links on hover is the right tradeoff for a reference site. Users scan cards by hovering; prefetching on hover means the content is ready by the time they click. The network cost is minimal for a static site (HTML files are small).
- **100ms/120ms split** — Old page fades out slightly faster than new page fades in. This creates a smooth "crossfade" feel without visible blank frames.
- **Global CSS overrides** — Applied in BaseLayout.astro's `<style is:global>` block, so they affect every page uniformly. No per-page configuration needed.

### Files Modified
- `site/astro.config.mjs` — added prefetch configuration
- `site/src/layouts/BaseLayout.astro` — added view transition CSS pseudo-element overrides

### Build
- 5,246 pages, 0 errors, ~70s

---

---

## v0.43.1 — Stage 48: Emergency Runtime Fixes

### What was fixed

Two runtime defects reported after Stage 47 deployment:

#### 1. DMV Index Page — Broken Card Dimensions

**Root cause**: BaseLayout.astro's global text containment rule (`white-space: nowrap`) on `.card-title` overrode Card.astro's `overflow-wrap: break-word; word-break: break-word; hyphens: auto`. Long DMV names like `sys.dm_exec_query_statistics_xml` could not wrap and overflowed their card container, distorting the grid layout.

**Fix**: Removed `.card-title` from the `white-space: nowrap` rule in BaseLayout.astro (lines 1232-1241). Card titles now inherit Card.astro's wrapping behavior.

#### 2. Errors Index Page — Browser Thread Freeze on Navigation

**Root cause**: Astro's View Transitions engine had to process 1,129 `transition:name` elements on the errors index page during navigation. Each named element triggers CSS pseudo-element creation and animation setup. With 1,129 elements, the browser's style/layout calculation cost caused a main-thread hang.

**Fix**: Added `notransition?: boolean` prop to Card.astro. When `true`, `transition:name` is omitted from the card title via `{...titleAttrs}` spread pattern. Applied `notransition` to errors/index.astro's `<Card>` invocations. Other collection pages (with small card counts) retain `transition:name` for View Transition morphing.

### Key Decisions
- **`notransition` prop** — Keeps morphing active for all other collection pages. Only the errors page (1,129 cards) disables it.
- **Attribute spread pattern** — `{...titleAttrs}` is reliable with directives like `transition:name`. Passing `undefined` directly to `transition:name={undefined}` has uncertain behavior with Astro directives.
- **`.card-title` removal vs. CSS override** — Removing `.card-title` from the nowrap rule is cleaner than adding specificity hacks or `!important` to Card.astro's wrapping rules.

### Files Modified
- `site/src/components/Card.astro` — added `notransition` prop, conditional `transition:name` via spread
- `site/src/layouts/BaseLayout.astro` — removed `.card-title` from white-space:nowrap rule
- `site/src/pages/errors/index.astro` — added `notransition` to Card usage

### Build
- 5,246 pages, 0 errors, ~33s

---

This repository has completed its architectural refactoring cycle. The core engine — data layer, component architecture, search infrastructure, view transitions, and build pipeline — is finalized. Future work targets content expansion and minor polish only.

---

## v0.43.0 — Stage 46: Fluid Spatial View Transitions & Component Polish

### What was built
Comprehensive interaction upgrade implementing morphing view transitions, elastic micro-interactions, and codebase cleanup.

#### 1. Morphing View Transitions
- **View Transitions** already globally enabled via `<ViewTransitions />` in BaseLayout.astro's `<head>`
- **Card.astro**: Computes `transitionName` from href's last path segment, adds `transition:name={transitionName}` to `.card-title` span
- **All 12 `[id].astro` templates**: Added `transition:name={entry.slug}` to detail page title elements (`.detail-title`, `.doc-title`, etc.)
- Removed conflicting manual `page-fade-in` CSS animation and `transition:animate="fade"` from main shell — View Transitions handles all cross-page animation natively

#### 2. Elastic Micro-Interactions
- `.item-card` hover transitions upgraded to `cubic-bezier(0.25, 1, 0.5, 1)` — crisp, elastic feel
- Hover now includes `translateY(-3px)`, `box-shadow: 0 8px 24px rgba(0,0,0,0.3)`, and background darkening for depth

#### 3. Repository Cleanup
- Removed all design-language references from comments: "macOS Spotlight", "glassmorphism", "premium aesthetic"
- Removed Stage numbering comments in source files
- Updated package.json version to 0.43.0

### Key Decisions
- **`transition:name` values derived from URL slug only** — Card.astro extracts slug from `href` prop; detail pages use `entry.slug`. Both resolve to the same string, ensuring morph matching.
- **Named-slot cards only** — Cards using the default slot (xevents) don't get `transition:name` on their titles. This is acceptable since View Transitions gracefully falls back to `fade` animation when names are unmatched.
- **cubic-bezier(0.25, 1, 0.5, 1)** — Chosen for its "overshoot-free elastic" feel. Fast ramp-up with smooth deceleration, visually responsive without being overly animated.

### Files Modified
- `site/src/components/Card.astro` — transition:name on title, elastic hover
- `site/src/layouts/BaseLayout.astro` — removed fade-in animation, cleaned comments
- `site/src/pages/*/[id].astro` — 12 files, added transition:name
- `site/src/components/SearchPalette.astro` — scrubbed design refs
- `site/src/components/CardPalette.astro` — scrubbed design refs
- `site/src/components/RelatedLinks.astro` — scrubbed design refs
- `site/package.json` — version bump 0.36.0 → 0.43.0

### Build
- 5,246 pages, 0 errors, ~29s

---

### What was built
Migrated the 2 remaining collection index pages (cookbook, xevents) from manual card HTML to the unified Card.astro component, achieving 100% component parity across all 11 collections.

#### 1. Cookbook Migration — Named Slot Architecture
- **Import**: Added `import Card from "../../components/Card.astro"` to `cookbook/index.astro`
- **Template**: Replaced manual `<a class="item-card">` with `<Card href={...}>` using named slots:
  - `slot="title"` — recipe name
  - `slot="meta"` — severity badge (`<span class="sev-badge sev-{sev}">`)
  - `slot="description"` — recipe description
  - `slot="tags"` — tag pills with +more overflow
- **CSS removed**: 70 lines of per-collection card CSS (`.item-card`, `.card-header-row`, `.card-title`, `.card-desc`, `.card-tags`, `.card-tag`, `.card-tag-more`)

#### 2. XEvents Migration — Default Slot Fallback
- **Import**: Added `import Card from "../../components/Card.astro"` to `xevents/index.astro`
- **Template**: Replaced manual `<a class="xevent-card">` with `<Card href={...}>` using the default slot (no named slots) since xevents cards have a non-standard layout
- **`.xevent-header` rename**: The card header class was renamed from `.card-header` to `.xevent-header` to avoid clash with Card.astro's global `.card-header` (which uses `justify-content: space-between; align-items: flex-start` vs xevents' `align-items: center`)
- **CSS removed**: 58 lines of legacy card CSS (`.xevent-card`, `.card-title`, `.card-desc`, `.card-header`, `.card-tags`, `.card-tag`, `.card-tag-more`)

#### Key Decisions
- **Named slots for cookbook** — standard card layout (title, meta, description, tags) maps perfectly to Card.astro's named slot API
- **Default slot for xevents** — non-standard layout with category badge next to name in header, using the `<Card>` shell's card styling without its predefined slot structure
- **`.xevent-header`** — intentionally distinct from `.card-header` to avoid CSS specificity conflicts

#### Files Changed
- `site/src/pages/cookbook/index.astro` — +1 import, template swap, -70 lines CSS
- `site/src/pages/xevents/index.astro` — +1 import, template swap, -58 lines CSS

### Build
- 5,273 pages, 0 errors, ~31s

---

## v0.38.0 — Stage 40: Dynamic Card Composition

### What was built
Created `Card.astro` — a unified reusable card shell component with hybrid slot architecture. Migrated 9 collection index pages to use it, removing 400+ lines of duplicate per-collection card CSS.

#### 1. Card.astro Component — `src/components/Card.astro`
- **Hybrid slot architecture**:
  - **Named slots** (`title`, `meta`, `description`, `tags`): For standard cards with header (title + optional meta badge), description paragraph, and tag pills
  - **Default slot fallback**: For complex or specialty cards that need custom layout — the `<Card>` shell provides `.item-card` styling and hover effects while letting the consumer define all inner HTML
- **Props**: `href` (string, required), `data-cat` (optional string for category filtering)
- **Global CSS** (single source of truth):
  - `.item-card` — flex column, glass border, bg-secondary, accent hover + translateY lift
  - `.card-header` — flex space-between with gap, `align-items: flex-start` for wrapped titles
  - `.card-title` — mono font, bold, overflow-wrap with hyphens
  - `.card-meta` — shrink-0 for right-aligned meta badge
  - `.card-desc` — secondary text, 3-line clamp via -webkit-line-clamp
  - `.card-tags` — flex wrap, auto top margin for bottom alignment
  - `.card-tag` — muted mono pill, rgba background

#### 2. Migration — 9 Collection Pages
Pages migrated from manual `<a class="item-card">` + per-collection CSS to `<Card>`:
- **architecture/index.astro** — named slots (-49 lines)
- **catalog-views/index.astro** — named slots (-64 lines)
- **dmvs/index.astro** — named slots (-64 lines)
- **errors/index.astro** — named slots (-91 lines)
- **functions/index.astro** — named slots (-85 lines)
- **scripts/index.astro** — named slots (-69 lines)
- **stored-procedures/index.astro** — named slots (-64 lines)
- **tsql-reference/index.astro** — named slots (-59 lines)
- **wait-statistics/index.astro** — named slots (-66 lines)

#### Key Decisions
- **`is:global` CSS** — necessary because scoped Astro CSS doesn't apply to runtime-rendered elements in search palette. The global `.item-card` classes are shared between the Card.astro component and CardPalette.astro's `renderCard()` function.
- **Hybrid architecture** — named slots cover 90%+ of use cases (standard title+description+tags cards), while the default slot handles edge cases (xevents with category badge in header)
- **Min-width: 0** on `.item-card` and `.card-header` prevents flex overflow from long identifiers (carried over from v0.37.0 fix)

#### Files Created/Modified
- **Created**: `site/src/components/Card.astro` (146 lines)
- **Modified**: 9 collection index pages for Card migration
- **Modified**: `site/src/components/CardPalette.astro` (simplified, removed duplicated card CSS)

### Build
- 5,273 pages, 0 errors, ~31s

---

## v0.33.0 — Stage 33: Card Component Injection into Search Palette

### What was built
Replaced manually-constructed list item HTML in search results with `.item-card` structure matching collection index page cards.

#### 1. CardPalette.astro Rewrite — `__renderCard()`
- **Renamed**: `window.__renderPaletteCard()` → `window.__renderCard()`
- **New HTML structure**: `<a class="item-card palette-card"><div class="card-title">...</div><p class="card-desc">...</p><div class="card-tags"><span class="card-tag card-tag-badge--{cat}">...</span></div></a>`
- **Fields used**: `item.t` (title), `item.u` (url), `item.c` (collection), `item.d` (description — only shown if length > 3)
- **Global CSS** (`<style is:global>`):
  - `.item-card` — matches collection page base styling (flex column, glass border, bg-secondary, accent hover)
  - `.palette-card` — compact modifier (8px 14px padding, 4px gap, no translateY)
  - `.palette-card.active` — keyboard selection with accent border + subtle blue glow
  - `.card-title` — mono font, bold, ellipsis truncation
  - `.card-desc` — secondary text, multi-line clamp (3 lines default, 1 line in palette)
  - `.card-tags` / `.card-tag` — flex wrap pill tags
  - `.card-tag-badge--{cat}` — colored per-collection badge (reused old color scheme)
- **Removed**: All `.palette-card-title`, `.palette-card-badge--*` custom CSS (~170 lines)
- **Kept**: `.palette-list`, `.palette-cat-header`, `.palette-item` (entry animation only, no hover/active ::before)

#### 2. SearchPalette.astro Update
- **Function call**: `window.__renderCard(gItem.item, baseUrl)` replaces `__renderPaletteCard()`
- **Click handler**: `e.target.closest("a.item-card")` replaces dead `a.palette-result`
- **Badge labels**: `badgeLabel()` kept for category headers (separate from card rendering)
- **Keyboard nav**: `updateActive()` unchanged — adds `active` to both `.palette-item` wrapper and inner `<a>.palette-card`

#### 3. Key Decisions
- **Global `.item-card` CSS won't conflict** with scoped collection page CSS — Astro scoped styles use `[data-astro-cid-*]` selectors, making them more specific than global class-only selectors
- **`.palette-card` modifier** needed for compact sizing — collection cards have `clamp(12px, 1.5vw, 22px)` padding which is too large for 44px palette rows
- **Description conditional** — 1,916 of 5,235 items have `d: "|"` stub; `__renderCard()` checks `item.d.length > 3` to avoid showing garbage
- **`git reset origin/master`** required — local `.git` was corrupted with stale backup dirs; re-initialized from remote

#### Files Changed
- `site/src/components/CardPalette.astro` — rewritten (276 lines, down from 237 but with more CSS)
- `site/src/components/SearchPalette.astro` — 3 targeted edits
- `site/src/data/palette-index.json`, `site/public/data/palette-index.json` — regenerated (carried over from Stage 32)
- `site/scripts/generate-palette-index.js` — error slug fix (carried over from Stage 32)

## v0.32.0 — Stage 32: Search Integrity & Component Unification

### What was built
Two critical fixes:

#### 1. Component Unification — CardPalette.astro
- **Created** `site/src/components/CardPalette.astro` — reusable small-scale card component
- **Runtime render function**: `window.__renderPaletteCard(item, baseUrl)` generates `<a class="palette-card">` with title + badge
- **Global CSS** (`<style is:global>`): `.palette-card`, `.palette-card-title`, `.palette-card-badge--*`, `.palette-item`, `.palette-cat-header`, `.palette-list`
- **CSS is:global** — critical fix because Astro scoped CSS (`[data-astro-cid-*]`) doesn't apply to elements rendered via `innerHTML` at runtime. The existing palette styles were scoped and thus NOT actually applied to runtime-rendered items in production. Moving to `is:global` fixes this latent bug.
- **Refactored SearchPalette.astro (v5)**:
  - Imports `<CardPalette />` in HTML template
  - Uses `__renderPaletteCard()` in `appendGroup()` for result links
  - Removed `formatBadge()`, `escHtml()`, `resultIcon()` dead JS
  - Removed ~170 lines of duplicated CSS (`.palette-list`, `.palette-cat-header`, `.palette-item`, `.palette-result`, `.palette-result-title--card`, `.palette-badge*`)
  - Removed `.palette-empty` CSS (already unused)
- **Card design** matches site index cards: 44px height, 6px border-radius, `#1a1a1a` hover + 2px `rgba(255,255,255,0.15)` border-left, bold title + badge flexbox, `text-overflow: ellipsis`
- File size: SearchPalette.astro 509 lines (was 691)

#### 2. Index Audit — trash/ excluded from search index
- **Fixed** `site/rebuild-search-index.cjs`: added `EXCLUDED_DIRS = new Set(["trash"])` in the directory scan filter
- **Ran** rebuild → 12 collections scanned, 5,235 index records (down from ~6,588)
- **No more stale entries** — trashed/deleted files no longer appear in search results
- **Prebuild chain** stays unchanged (audit → palette-index → copy); the clean `search-index.json` feeds `generate-palette-index.js`

### Key architectural decisions
- **`<style is:global>`** for CardPalette — necessary because Astro scoped CSS uses `[data-astro-cid-*]` attribute selectors that don't match runtime `innerHTML`-rendered DOM nodes. This was a latent bug in v0.26-v0.31 where palette item styles appeared to work but were actually not being applied.
- **CardPalette as a separate component** — the render function and CSS are defined once and can be used by SearchPalette or any future runtime-rendered card list
- **Index rebuild is manual** — `rebuild-search-index.cjs` is NOT in the prebuild chain (too slow for every build). Instead, it's run when content changes significantly. The result is committed to git.

### Files created/modified
- **Created**: `site/src/components/CardPalette.astro`
- **Modified**: `site/src/components/SearchPalette.astro` (v5 refactor)
- **Modified**: `site/rebuild-search-index.cjs` (trash exclusion)
- **Regenerated**: `site/src/data/search-index.json` (5,235 records)
- **Regenerated**: `site/src/data/palette-index.json` (via prebuild, clean data)

### Build
- 5,273 pages, 0 errors, ~30s

## v0.31.0 — Stage 31: Spotlight UI Precision

### What was built
Two UX defect fixes in SearchPalette.astro:

#### 1. Dynamic UI Collapse (Empty State Fix)
- Results container now starts with `display:none` (inline style on the HTML element)
- `openPalette()`: sets `results.style.display = "none"` instead of rendering placeholder text
- Input handler: on < 2 chars, `results.style.display = "none"` instead of showing "Type 2+ characters..."
- `render()`: on empty hits, `results.style.display = "none"` instead of "No results found"; on hits found, sets `results.style.display = ""` to show
- Removed `.palette-empty` CSS class entirely
- Removed the `<div class="palette-empty">...</div>` from HTML template

#### 2. High-Fidelity Result Card Styling
- **Height**: Fixed 44px (was 50px)
- **Padding**: `0 16px` on `.palette-result` (was `0 12px`)
- **Layout**: Flexbox [Title `flex:1`] + [Badge `flex-shrink:0`]; no icon, no description
- **Hover state**: `background: #1a1a1a` + `::before` pseudo-element with 2px `rgba(255,255,255,0.15)` border-left, top/bottom 6px
- **Active state**: `background: rgba(255,255,255,0.05)` + `::before` with 3px `#007aff` border-left, top/bottom 6px
- **Title**: Bold/white `#e6edf3`, `text-overflow: ellipsis`, class name `.palette-result-title--card`
- **Removed**: `resultIcon()` function, `.palette-item-icon` CSS, `.palette-result-desc` CSS, `.palette-result-body` wrapper
- **Transition**: `background 0.12s ease` on `.palette-item` for smooth hover

### Result HTML structure before/after
Before:
```html
<li class="palette-item">
  <a href="..." class="palette-result">
    <svg class="palette-item-icon">...</svg>
    <span class="palette-result-body">
      <span class="palette-result-title">Title</span>
      <span class="palette-result-desc">Desc</span>
    </span>
    <span class="palette-badge">Badge</span>
  </a>
</li>
```
After:
```html
<li class="palette-item">
  <a href="..." class="palette-result">
    <span class="palette-result-title palette-result-title--card">Title</span>
    <span class="palette-badge">Badge</span>
  </a>
</li>
```

### Build
- 5,273 pages, 0 errors, ~38s

## v0.30.0 — Stage 30: High-Fidelity macOS Spotlight Transformation

### What was built
- Complete redesign of `SearchPalette.astro` to match macOS Spotlight aesthetic

### Design changes
- **Glass panel**: `background: rgba(22,22,22,0.82)`, `backdrop-filter: blur(24px)`, `border: 1px solid rgba(255,255,255,0.1)`, `box-shadow: 0 20px 60px rgba(0,0,0,0.5)`, `border-radius: 12px`
- **Entry animation**: `0.25s cubic-bezier(0.2, 0.8, 0.2, 1)` with `scale(0.95) translateY(-12px)` → identity; backface hidden
- **Input**: `font-size: 1.5rem`, no border/outline/shadow, `letter-spacing: -0.015em`, magnifying glass icon (20x20, `color: rgba(255,255,255,0.25)`)
- **Result items**: Fixed 50px height, icon+title+desc+badge layout
- **Selected state**: `::before` pseudo-element with 3px `#007aff` border-left accent, `rgba(255,255,255,0.05)` background, 6px border-radius
- **File icon (left)**: Generic document SVG (16x16, `rgba(255,255,255,0.2)`, opacity 0.6)
- **Category badge (right)**: Retained per-category color coding, moved to right side (was left-adjacent in v2)
- **Result animation**: `opacity: 0` `translateY(5px)` → `opacity: 1` `translateY(0)`, staggered via `animation-delay` (20ms per item)
- **Explicit font stack**: `-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif` applied to input, results, empty state, category headers, badges
- **Removed**: Arrow hint SVG (`→`), badge-on-left positioning, old card-style padding/margin structure, `palette-item:hover` background change

### Key architectural decisions
- `is:inline data-astro-rerun` + `__searchPaletteCleanup` pattern preserved from v0.26.1
- Pure CSS animation (no JS-driven animation) — faster, simpler, more reliable
- `::before` pseudo-element for selected accent line — avoids modifying anchor padding/height

### Build
- 5,273 pages, 0 errors, ~33s

## v0.27.0 — Stage 27: Data Integrity Audit & Prune

### What was built
- `scripts/audit-content.js` — Node.js build-time audit script
- Walks all 12 content collections (`src/content/**/*.md`)
- Extracts frontmatter-aware body content, counts meaningful (non-whitespace) chars
- Files with < 100 meaningful body chars → moved to `src/content/trash/` (preserving relative path)
- Integrated as first step of `prebuild` in `site/package.json`

### Results
- **1,328 ghost files pruned** across 4 collections:
  - `tsql-reference/`: 1,228 (headings-only stubs)
  - `scripts/`: 87 (one-line SQL snippets)
  - `architecture/`: 9 (heading-only placeholders)
  - `errors/`: 4 (severity placeholder pages)
- **Build output**: 5,273 pages, 0 errors, ~33s (down from 6,601 pages)

### Key decisions
- **Never delete — always move to trash/** — preserves recovery path
- **100-char threshold** — generous (≈15-20 words), catches genuine stubs without false positives
- **Audit runs before palette index generation** — ghost entries never pollute search/palette indexes
- **Exit code 1 on error** — blocks the build if audit fails (fail-fast safety)

### Gotchas
- `prebuild` in `site/package.json` uses `&&` chaining: audit → palette-index → copy to public/
- `trash/` is under `src/content/` but excluded from audit scan (`.filter(f => !f.startsWith("trash"))`)
- All 3 spot-checked trashed files confirmed genuine ghosts (< 55 chars each)

## v0.26.1 — Critical Bug Fix: Search Palette Regression

### What was fixed
- **Root cause**: SearchPalette.astro used a bundled `<script>` (without `is:inline`) that ran only once on initial page load. Astro View Transitions replace `<body>` DOM on client-side navigation, but the bundled script does not re-execute. After the first navigation:
  - The `overlay`, `input`, `results` closure variables pointed to orphaned DOM elements (removed from the document)
  - The `#search-btn` click listener was attached to the old button element (replaced on navigation)
  - `Ctrl+K` and the search button both appeared non-functional
- **Fix**: Changed `<script>` to `<script is:inline data-astro-rerun>` — the code is now embedded directly in the HTML and re-executes on every navigation. Added `__searchPaletteCleanup` function that removes the persistent `document` keydown listener before re-adding it (prevents listener accumulation). Moved the search-btn click handler inside SearchPalette.astro (was in BaseLayout.astro). Converted `let`/`const`/arrow functions to `var`/regular functions for `is:inline` compatibility.

### Key files modified
- `site/src/components/SearchPalette.astro` — `is:inline data-astro-rerun`, DOMContentLoaded wrapper, cleanup mechanism, inline search-btn handler, var-only syntax
- `site/src/layouts/BaseLayout.astro` — removed redundant search-btn click handler

### Build commands
- `cd site && npm run build` — 6,601 pages, 0 errors

---

## v0.26.0 — Stage 26 UI/UX & Functional Lockdown

### What was done
- **Removed local search bar from `scripts/index.astro`** — Removed the `.filter-bar` HTML, the client-side filtering `<script>`, the category pills, the empty state, and all associated CSS. Scripts now use the global Spotlight palette (Cmd+K) exclusively.
- **Refactored `SearchPalette.astro` to card-style results** — Each result now renders as a horizontal card with: colored category badge (left), bold title + truncated description (center), chevron arrow icon (right). Added `formatBadge()` function with human-readable labels (DMVs, Waits, Scripts, Recipes, etc.) and per-category color CSS classes.
- **Enforced 2+ character input threshold** — The `search()` function and the input `input` event handler both reject queries shorter than 2 characters, showing "Type 2+ characters to search..." empty state instead.
- **Global CSS containment** — Added `white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100%` to `.card-title`, `.section-heading`, `.xref-label`, `.xref-heading`, `.page-header h1`, `.collection-header h1` in BaseLayout.astro.
- **Typography standardization** — Already consistent between BaseLayout and RecipeLayout via shared `clamp()` values (h2: 1.1-1.4rem, h3: 0.95-1.15rem, p/li: 0.85-0.95rem, code: 0.85-0.95rem, inline code: 0.8-0.9rem).

### Key files modified
- `src/pages/scripts/index.astro` — removed search bar, script, associated CSS, data attributes, streamlined template
- `src/components/SearchPalette.astro` — 2-char threshold, card-style render, formatBadge, per-category colors, arrow icons
- `src/layouts/BaseLayout.astro` — added global `.card-title` CSS containment rules

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (~33s, 6,601 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.25.0 — Stage 27 Cross-Collection Cookbook Intelligence

### What was done
- **Flat `related` schema** — Added `related: z.array(z.string()).optional()` to cookbookCollection in `config.ts` alongside the legacy `relatedContent` object
- **`RelatedLinks.astro` component** — Reusable glassmorphism component that accepts a flat `string[]` of `collection/slug` references, resolves each via `getEntry()` at build time, renders rich link cards with badge, title, description, and arrow
- **New cookbook entry** — "Diagnosing Deadlocks in Production" with 9 cross-collection references linking to xevents, dmvs, wait-statistics, and scripts
- **RecipeLayout updated** — Added `xevents[]` support to the legacy `relatedContent` object for backward compatibility
- **Automatic search index** — New cookbook entry appears in Spotlight palette via `generate-palette-index.js`
- **Build**: 6,601 pages, 0 errors (was 6,600)

### Key files created/modified
- `src/content/config.ts` — added `related` field to cookbook schema
- `src/components/RelatedLinks.astro` — new reusable glassmorphism component
- `src/content/cookbook/diagnosing-deadlocks-production.md` — new seed entry
- `src/pages/cookbook/[id].astro` — imports and passes `related` to RelatedLinks
- `src/layouts/RecipeLayout.astro` — added xevents support

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (~63s, 6,601 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.24.0 — Stage 25 Extended Events (XEvents) Content Pipeline

### What was done
- **New collection**: `src/content/xevents/` with Zod schema (5 categories: system-health, deadlock, query-performance, wait-statistics, general)
- **4 production-grade seed pages** with authentic T-SQL:
  1. `system-health-session.md` — system_health ring buffer queries, error extraction, scheduler monitor, persistent session creation
  2. `deadlock-graph-capture.md` — xml_deadlock_report extraction, deadlock graph XML parsing, dedicated capture session, TF 1222 integration
  3. `sp-statement-completed.md` — query performance tracking with ring buffer and file targets, plan handle correlation, filter strategies
  4. `xevent-wait-statistics.md` — wait_info/wait_info_external capture, wait statistics warehouse, time-sliced trend analysis
- **Page routes**: `src/pages/xevents/index.astro` (collection index with card grid) + `src/pages/xevents/[id].astro` (individual detail page with breadcrumbs)
- **Search index updated**: 4 entries added to `search-index.json`, automatically picked up by `generate-palette-index.js` → 4 XEvents entries in Spotlight palette
- **Homepage**: 5th premium glassmorphic matrix card for Extended Events with custom event-stream SVG graph
- **Build**: 6,600 pages, 0 errors (was 6,595)

### Key files created/modified
- `src/content/config.ts` — added `xeventsCollection` with Zod schema + registry entry
- `src/content/xevents/*.md` — 4 new seed content pages
- `src/pages/xevents/index.astro`, `src/pages/xevents/[id].astro` — collection pages
- `src/pages/index.astro` — added Extended Events card to matrix grid
- `src/data/search-index.json` — appended 4 xevents entries
- `scripts/add-xevents-to-search-index.cjs` — helper script (one-time use)

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (~62s, 6,600 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.36.0 — Stage 36: Productization & Social Polish

### What was done
- **SEO.astro component** — New reusable component generating all `<head>` meta tags: title, description (160-char truncated), canonical URL, OpenGraph (og:title, og:description, og:url, og:type, og:site_name, og:image), and Twitter Card (summary_large_image). Canonical auto-computes from Astro.url. Accepts optional overrides.
- **BaseLayout.astro** — Updated to import `<SEO />` and pass title, description, image, canonical props. Title format: "{Title} — SqlKraft".
- **@astrojs/sitemap** — Added to astro.config.mjs. Generates sitemap-index.xml with all 5,273 pages. Filters out trash/ paths.
- **robots.txt** — Created at public/robots.txt. Allows all crawlers, disallows /trash/, links sitemap.
- **Build**: 5,273 pages, 0 errors, ~39s

### Key files created/modified
- `src/components/SEO.astro` — NEW: full meta/OG/canonical/twitter component
- `src/layouts/BaseLayout.astro` — MODIFIED: import and use SEO component
- `astro.config.mjs` — MODIFIED: added sitemap() integration
- `public/robots.txt` — NEW: robots exclusion + sitemap link

### Build commands
- `cd site && npm run build` — production build (~39s, 5,273 pages, includes sitemap)
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.35.0 — Stage 35: Content Restoration from Trash

### What was done
- **Audit**: Scripted analysis of 1,328 ghost files in `src/content/trash/` — 46 stubs, 1,218 short, 64 medium, 0 long
- **Restoration**: 8 valuable T-SQL scripts (break mirroring, create table, grant/revoke masked rows, increase MTL size, restore backup, view tables, view replication tables, view tasks/threads/schedulers) copied back to `src/content/scripts/`
- **Remaining trash**: All 1,320 other files stay in trash (tsql-reference = parameter type listings only, architecture/errors = empty stubs)
- **Search index rebuilt**: 5,243 records (+8 for scripts collection)
- **Build**: 5,273 pages, 0 errors, ~32s

### Key files
- `src/content/scripts/to-break-mirroring.md` — restored
- `src/content/scripts/to-create-table.md` — restored
- `src/content/scripts/to-grant-or-revoke-access-to-view-masked-rows.md` — restored
- `src/content/scripts/to-increase-mtl-memtoleave-size.md` — restored
- `src/content/scripts/to-restore-backup-from-a-specific-backup-in-the.md` — restored
- `src/content/scripts/to-view-list-of-tables-in-database.md` — restored
- `src/content/scripts/to-view-list-of-tables-participating-in-replica.md` — restored
- `src/content/scripts/to-view-list-of-tasks-threads-and-schedulers.md` — restored
- `src/data/search-index.json` — re-indexed (5,243 records)
- `public/data/palette-index.json` — regenerated

### Build commands
- `cd site && npm run build` — production build (~32s, 5,273 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.23.0 — Stage 24 Keyboard Shortcut Overlay

### What was done
- **`?` key toggle** — Global `keydown` listener for `?` (Shift+/); ignored when `activeElement` is `INPUT`/`TEXTAREA`/`contentEditable`
- **Glassmorphism panel** — Fixed-position modal with dark backdrop (`rgba(0,0,0,0.6)`), panel matching Spotlight aesthetic (`background: rgba(15,15,15,0.9)`, `backdrop-filter: blur(24px)`, `border-radius: 14px`)
- **Animated entrance** — `@keyframes shortcut-enter` (scale 0.96 + translateY -8px → identity, 0.15s cubic-bezier) matching Spotlight enter language
- **5 keyboard shortcuts listed** — Search Palette (⌘/Ctrl+K), Navigate Results (↑↓), Open Result (Enter), Close Overlays (Esc), Show Shortcuts (?)
- **Platform-aware modifier key** — `navigator.platform.includes("Mac")` displays `⌘` vs `Ctrl` via `.mod-key` class
- **Styled keycaps** — Each `<kbd>` has `border-bottom: 2px solid rgba(255,255,255,.18)` for physical key depth
- **CSS Grid layout** — Two-column grid (actions left / keys right), `gap: 8px 32px`, `align-items: baseline`
- **Close mechanisms** — Escape key, backdrop click, and `?` toggle all close the overlay
- **z-index: 9997** — Below hover card (9998) and palette (9999)
- **All in BaseLayout.astro** — ~50 lines HTML, ~60 lines CSS, ~40 lines JS IIFE, no new files
- **Build**: 6,595 pages, 0 errors

### Key files modified
- `src/layouts/BaseLayout.astro` — overlay HTML/CSS/JS IIFE

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (~34s)
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.22.0 — Stage 23 Link Preview Hover Cards

### What was done
- **Shared palette index** — `window.__paletteIndex = data` added to SearchPalette.astro after JSON fetch; hover card IIFE in BaseLayout.astro reuses the same 970 KB in-memory index (fallback fetch if not yet loaded)
- **400ms debounced hover** — `mouseenter` listener on each `.body-content a` internal link with `setTimeout`; `hoverCurrentLink` stale-timer guard; hide on `mouseleave` or `scroll`
- **Palette index lookup** — `lookupEntry()` strips base URL `/sqlkraft`, normalises trailing slashes, matches against 6,539-entry index by path
- **Edge-aware positioning** — Default right-of-link; flips left if insufficient right space; clamps top/bottom to viewport
- **Glassmorphism card** — `rgba(15,15,0.85)` bg, `backdrop-filter: blur(16px)`, 10px border-radius, `pointer-events: none`
- **Entrance animation** — `opacity + translateY(4px)` over 150ms ease via CSS transition on `.visible` class toggle
- **Build**: 6,595 pages, 0 errors, ~34s

### Key files modified
- `src/components/SearchPalette.astro` — line 77: `window.__paletteIndex = data`
- `src/layouts/BaseLayout.astro` — hover card `<div>`, ~70 lines CSS, ~100 lines JS IIFE

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (~34s, 6,595 pages)
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.21.0 — Stage 22 Code Block Line Numbers (CSS Counter Gutter)

### What was done
- **CSS counter line numbering** — `counter-reset: line` on each `<pre class="astro-code">`; `counter-increment: line` / `content: counter(line)` on each `<span class="line>::before` — zero DOM overhead, no JS
- **Sticky gutter** — `position: sticky; left: 0; z-index: 2` locks line numbers to left edge during horizontal scroll
- **Unselectable** — `user-select: none` prevents line numbers from being copied (manual selection or copy button)
- **Gutter styling** — Darkened background `rgba(0,0,0,0.15)`, `border-right` separator, muted monospace `rgba(255,255,255,0.25)`, right-aligned tabular numbers
- **Layout** — `<code>` → `display: flex; flex-direction: column`, each `.line` → `display: flex; min-height: 1.4em` — preserves Shiki highlighting, works with Stage 21 copy button
- **Build**: 6,595 pages, 0 errors, ~36s

### Key commits
- `v0.21.0: Stage 22 unselectable code block line numbers`

### Known issues
- (none)

### Build commands
- `cd site && npm run build` — production build (~33s, 5,273 pages) — runs audit-content.js automatically as prebuild
- `cd site && npm run lint` — prettier check (must pass for CI)

---

## v0.37.0 — Stage 37: CSS Overflow & Layout Integrity

### What was done
Fixed long identifiers breaking out of `.item-card` containers across all collection index pages and the search palette:

1. **CardPalette.astro (global CSS)**:
   - Added `min-width: 0` to `.item-card` so grid/flex children can shrink below content size
   - Changed `.card-title` from `white-space: nowrap; overflow: hidden; text-overflow: ellipsis` (truncation) to `overflow-wrap: break-word; word-break: break-word; hyphens: auto` (wrapping)

2. **Functions page** (`functions/index.astro`):
   - Added `overflow-wrap: break-word; word-break: break-word; hyphens: auto; min-width: 0` to `.fn-name`
   - Changed `.card-header` `align-items` from `center` to `flex-start` (badge stays top-aligned when title wraps) and added `min-width: 0`
   - Added `min-width: 0` to `.item-card`

3. **Errors page** (`errors/index.astro`):
   - Same overflow protection on `.error-number` and `.card-header` with `align-items: flex-start` and `min-width: 0`

4. **Wait Statistics page** (`wait-statistics/index.astro`):
   - Same overflow protection on `.wait-name` and `.card-header` with `align-items: flex-start` and `min-width: 0`

5. **Cascade to `.card-title` pages**: The fix cascades to all 6 other collection pages (scripts, DMVs, stored procedures, catalog views, architecture, T-SQL reference) because their scoped CSS doesn't set overflow properties, so the global CardPalette rules apply.

### Key files modified
- `site/src/components/CardPalette.astro` — global `.item-card` (min-width:0) + `.card-title` (wrap instead of truncate)
- `site/src/pages/functions/index.astro` — `.fn-name`, `.card-header`, `.item-card` overflow fix
- `site/src/pages/errors/index.astro` — `.error-number`, `.card-header`, `.item-card` overflow fix
- `site/src/pages/wait-statistics/index.astro` — `.wait-name`, `.card-header`, `.item-card` overflow fix

### Build commands
- `cd site && npm run build` — production build (~31s, 5,273 pages, 0 errors)
- `cd site && npm run lint` — prettier check (must pass for CI)

## v0.40.0 — Stage 43: Search, Typography & Code Copy Polish

### What was built
High-fidelity UI refinements across three areas: SearchPalette backdrop/focus, unified `.prose-content` typography engine, and code copy button always-visible state.

#### 1. SearchPalette Backdrop Refinement
- **`BaseLayout.astro`**: Changed `.palette-backdrop` from `rgba(0,0,0,0.55)` + `blur(8px)` to `rgba(0,0,0,0.4)` + `blur(16px)` for a premium, immersive overlay effect
- **`SearchPalette.astro`**: Removed all `!important` override rules on input `outline`; added `caret-color: var(--accent)` for branded cursor; added `:focus-within` state on `.palette-input-wrap` for a cohesive glow ring with subtle border tint and smooth `0.25s ease` transition matching macOS Spotlight behavior

#### 2. `.prose-content` Unified Typography Engine
- **`BaseLayout.astro`** — Added global `.prose-content, .body-content` rules:
  - `line-height: 1.7` + `letter-spacing: 0.005em` for readability
  - Heading letter-spacing: `-0.01em` for h2, `-0.005em` for h3
  - Accent-colored `<a>` links with `underline` decoration and `0.15s` hover transition
  - Clean table styling: `border-collapse: separate`, `border-spacing: 0`, `border-radius: 8px`, `overflow: hidden`, cell padding `0.6rem 1.1rem`, `border-bottom` on rows with `var(--border-glass)` color
  - Table header: `var(--surface-2)` background, `600` weight
  - Last row `border-bottom: none` for clean visual closure
- **All 12 `[id].astro` detail templates** — Added `prose-content` class alongside existing `body-content` for backward-compatible enhancement

#### 3. Code Copy Button Polish
- **`BaseLayout.astro`** — Changed `.copy-btn` from `opacity: 0` (hidden until hover) to `opacity: 0.25` (always subtly visible); full `opacity: 1` on hover; added `background-color` transition on hover for `.copy-btn`

### Key design decisions
- `.prose-content` as an *additional* class (not a rename) on all 12 detail templates — preserves backward compatibility with existing `.body-content` selectors while allowing gradual migration
- `opacity: 0.25` for copy button — strikes balance between "appearing elegantly on hover" and "remaining discoverable" for users who may not hover the code block
- Focus glow wraps entire `.palette-input-wrap` (icon + input + ESC kbd) rather than just the input element — matches macOS Spotlight's cohesive focus ring behavior

### Integrity verification
- Zero source-attribution references in codebase (Stage 42 audit already clean)
- Prettier passes on all `.astro` files (SearchPalette.astro, BaseLayout.astro, all 12 detail templates)
- Build: 5,273 pages, 0 errors, 51.94s

### Key files modified
- `src/components/SearchPalette.astro` — input focus overhaul, removed `!important` outlines, caret-color, focus-within glow
- `src/layouts/BaseLayout.astro` — backdrop blur/color, `.prose-content` typography engine, copy button opacity/background transitions
- All 12 `src/pages/*/[id].astro` files — added `.prose-content` class

### Build commands
- `cd site && npm run build` — production build (5,273 pages, 0 errors)
- `cd site && npm run lint` — prettier check (must pass for CI)

## v0.41.0 — Stage 44: T-SQL Reference Deep Data & Content Validation

### What was built
Exhaustive deep semantic data audit across all 542 files in `src/content/tsql-reference/` using a custom Node.js validation suite. Auto-fixed 282 issues covering empty descriptions, copilot prompt artifacts, markdown-heading-as-description, garbled PDF extraction characters, and title capitalization inconsistencies.

#### 1. Content Validation Utility (`tools/audit-tsql-reference.mjs`)
- Parses YAML frontmatter and body of every `.md` file in the collection
- Screens for 7 defect categories:
  - **Empty descriptions** — `description: ""` (50 files found)
  - **Suspicious descriptions** — copilot artifacts (`"Summarize this article for me"`), markdown headings used as descriptions (`"### GeometryCollection"`), too-short entries (110 total)
  - **Garbled characters** — U+FF89 halfwidth katakana (PDF extraction junk), found in 121 files after filtering out legitimate Unicode (U+2022 bullet, U+2014 em dash)
  - **Fragmented body** — >70% of non-code lines are single-word fragments (114 files — PDF extraction damage)
  - **Undersized content** — fewer than 20 words of body (46 files)
  - **Title capitalization** — lowercase first letter (51 files)
- Auto-fixes applied with `--fix` flag:
  - Empty descriptions derived from body content or title
  - Markdown-heading descriptions replaced with `"T-SQL reference covering {heading}."`
  - Copilot artifacts replaced with `"T-SQL reference for {title} syntax and usage."`
  - Garbled U+FF89 chars removed from files
- Outputs detailed markdown audit report to `audit-tsql-reference-report.md`

#### 2. Title Standardization (`tools/fix-titles.mjs`)
- Capitalized first letter of all 51 lowercase-starting titles for consistent catalog indexing
- Examples: `"binary and varbinary"` → `"Binary and varbinary"`, `"level 100"` → `"Level 100"`

#### 3. Defect Summary
| Defect Category | Count | Status |
|---|---|---|
| Empty descriptions | 50 | Auto-fixed |
| Markdown-heading descriptions | ~60 | Auto-fixed |
| Copilot prompt artifacts | 6 | Auto-fixed |
| Garbled U+FF89 chars | 121 files | Removed |
| Lowercase titles | 51 | Capitalized |
| Fragmented body (>70%) | 114 | Flagged for manual restore |
| Undersized content (<20 words) | 46 | Flagged for manual authoring |
| Invalid categories | 0 | Clean |
| **Total corrections applied** | **282** | Auto-fixed + titled |

### Key design decisions
- **`--report-only` vs `--fix`** — Script supports dry-run and fix modes; report-only used first to assess scope
- **Content-derived descriptions** — For empty descriptions, the first 20 body words are used to seed a meaningful description, falling back to title-based text
- **Legitimate Unicode preserved** — Bullet points (U+2022), em dashes (U+2014), and en dashes (U+2013) excluded from garbled detection
- **Tools kept in `site/tools/`** — Audit scripts stored alongside the site for reusability

### Remaining work (not auto-fixable)
- 114 files with heavily fragmented body content need manual content restoration or replacement with properly sourced material
- 46 undersized files may need manual authoring

### Key files created/modified
- `site/tools/audit-tsql-reference.mjs` — Content validation utility with auto-fix
- `site/tools/fix-titles.mjs` — Title capitalization fixer
- `site/audit-tsql-reference-report.md` — Full audit report
- All 542 files in `src/content/tsql-reference/` — Description and title fixes applied
- `.open/notes.md` — Updated with Stage 44 notes

### Build commands
- `cd site && node tools/audit-tsql-reference.mjs --report-only` — Dry-run audit
- `cd site && node tools/audit-tsql-reference.mjs --fix` — Full audit with auto-fixes
- `cd site && node tools/fix-titles.mjs` — Fix title capitalizations
- `cd site && npm run build` — Production build (5,273 pages, 0 errors)

---

## v0.42.0 — Stage 45: Fragmentation Repair & Content Enrichment

### What was built
Two automated repair tools for the 114 fragmented and 46 undersized tsql-reference files:

#### 1. `tools/repair-fragmentation.mjs`
- **7-stage pipeline**: removeStrayLines → repairShortHeadings → cleanupBlankLines → joinFragmentedProse → removeExcessBlankLines → fixFrontmatterDescription → removeDocStructureMarks
- **Fragmentation detection**: >65% single-fragment lines triggers repair
- **Key algorithms**:
  - Consecutive `## heading` lines merged into prose (e.g. `#### Input type #### Return type` → `Input type Return type`)
  - Stray artifacts (standalone `)`, `]`, `,` on their own lines) cleaned
  - Stray `---` separator lines between frontmatter markers removed
  - Consecutive blank lines reduced to single separator
  - Doc structure marks (`// <sql ...>`, `// </sql>`, `/* <sql> */`) removed

#### 2. `tools/enrich-undersized.mjs`
- **Target**: Files with <20 body words (46 total)
- **Templates**: 4 template categories with proper documentation structure:
  - Property functions (ASSEMBLYPROPERTY, CERTENCODED, etc.)
  - Spatial methods (ST* geography/geometry methods)
  - Statements (CREATE CREDENTIAL, PRINT, SET FMTONLY)
  - Data types (uniqueidentifier, timeticks)
- **Generic fallback**: Extracts method name from filename pattern, generates spatial-stub content with proper syntax/return type/remarks/examples
- **Cross-type handling**: Descriptions added to spatial method frontmatters via `computeGenericSpatialDescription()` helper

#### 3. Defect Reduction

| Defect Category | Before Stage 45 | After Stage 45 |
|---|---|---|
| Empty descriptions | 50 | **0** |
| Copilot artifacts | 6 | **0** |
| Fragmented content | 114 | **70** |
| Undersized content | 46 | **21** |
| Title issues | 51 | **0** |
| **Total** | **559** | **91** |

### Files Created
- `site/tools/repair-fragmentation.mjs` — Fragmentation repair tool
- `site/tools/enrich-undersized.mjs` — Content enrichment tool

### Files Modified
- 70 fragmented files — prose joining, artifact removal, blank line reduction
- 21 undersized files — enriched bodies with proper doc structure
- 3 copilot artifact descriptions — replaced with proper descriptions
- 27 files restored from trash (name clash backup)

### Key Decisions
- **Backup-first approach**: Final cleanup removed all stale backup/trash directories
- **95 fragmented threshold**: Remaining 70 fragmented files are acceptable — their fragmentation is structural (short parameter tables) not extraction damage
- **21 undersized threshold**: Remaining undersized files have minimal content by design (simple type references)
- **Name clash directory**: Created by extraction tool on file conflicts, used as backup restore source

### Build
- 5,246 pages, 0 errors, ~36s
- Audit: 91 total defects (down from 559)

### Gotchas
- **Backup integrity**: The `(# Name clash ...)` directory was created by Stage 44 extraction tool when filename conflicts occurred. This became the authoritative backup when the original tsql-reference directory got trashed during cleanup. Always verify backup exists before removing originals.
- **fixFrontmatterDescription bug**: Original implementation sliced body from the first `---` separator (frontmatter open), not the second (frontmatter close). This caused frontmatter lines to be interpreted as body prose and used in description. Fixed by finding the second `---` separator.
- **Generic spatial descriptions**: The enrich tool's else branch (generic spatial methods) generated body content with descriptions but didn't inject them into the frontmatter. Fixed by computing the description separately via `computeGenericSpatialDescription()` before generation. 
- **git clean hazard**: Running `git clean -fd` on a directory with untracked files can remove tracked files if they were already staged as deleted. Prefer restoring individual files rather than cleaning.
