# SqlKraft — Session Notes

## v0.50.0-Beta — Global CSS Override for Spotlight Search UI Components

### What was done

1. **Fixed Astro scoped CSS blind spot** (SearchPalette.astro)
   - Changed `<style>` to `<style is:global>` — Astro's scoped CSS uses data-attribute selectors
     that only apply to compile-time elements. Search palette results are injected at runtime
     via `innerHTML`, so scoped CSS never matched them. Now emits unscoped global styles.

2. **!important enforcement on category headers** (CardPalette.astro)
   - Every `.palette-cat-header` property now has `!important` to dominate over
     inherited/user-agent styles: font-size, font-weight, letter-spacing, text-transform,
     color, padding, margin, border, position, z-index, background, backdrop-filter, font-family

### Root cause
- `.palette-list`, `.palette-cat-header`, `.palette-result`, `.palette-item` elements are
  created by `render()` / `__renderCard()` via `innerHTML` — they never existed in the
  Astro component template at compile time, so scoped data-attribute CSS never matched them.
- CardPalette.astro already used `<style is:global>` (v0.48.0), but SearchPalette.astro
  still used `<style>` (scoped), which caused the `.palette-list` and text-decoration rules
  to silently fail.

### Build results
- 5,241 pages, 0 errors, ~48s
