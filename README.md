# SqlKraft

A SQL Server reference that runs entirely in the browser. 5,149 entries across 12 collections — T-SQL, system stored procedures, catalog views, DMVs, wait statistics, engine errors, and the diagnostic scripts that go with them.

No server. No database. No account. No tracking. The whole thing is static HTML, so it loads the same on Wi-Fi, on 3G, or on a plane with nothing turned on.

<p align="center">
  <a href="https://kedharsairam.github.io/sqlkraft/"><img src="https://img.shields.io/badge/Open-sqlkraft-blue?style=for-the-badge" alt="Open SqlKraft"></a>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</p>

---

## Collections

These are the counts the build actually emits. They used to be a wish and a half — the table claimed 1,740 T-SQL entries when there were 508.

| Collection | Entries | Coverage |
|---|---:|---|
| Operations & Administration | 1,271 | HA, migration, monitoring, SSMS, Profiler, Linux |
| Database Engine Errors | 1,062 | Error codes with severity classification and troubleshooting |
| Architecture & Internals | 906 | Query processing, memory, locking, I/O, storage engine |
| System Stored Procedures | 696 | Administrative and maintenance procedures |
| T-SQL Reference | 508 | Statements, queries, data types, operators, hints, predicates |
| Catalog Views | 270 | Database metadata, objects, indexes, security |
| T-SQL Diagnostic Scripts | 181 | Curated performance, indexing, security, HA scripts |
| Dynamic Management Views | 148 | Execution, I/O, memory, indexing, OS internals |
| Wait Statistics | 50 | Wait types across baseline, triage, blocking, I/O |
| System Functions | 49 | Aggregate, analytic, conversion, string, date/time |
| Cookbook | 4 | Worked examples |
| Extended Events | 4 | System health, deadlock, query performance, wait analysis |
| **Total** | **5,149** | **12 collections, 5,184 published pages** |

---

## What it does

**Searches everything at once** — <kbd>Ctrl</kbd>+<kbd>K</kbd> opens a command palette over all 5,149 entries. There is no search backend and no query to a server, so there is nothing to rate-limit and nothing to log.

**Resolves cross-references at build time** — DMVs, wait types, scripts and errors link to each other through a shared 832 KB palette index. Hover a name, get the page. The cost is paid once, during the build, and never again on the reader's side.

**Keeps your place in a long page** — a right-rail contents list tracks the section you are reading, and the type scale is fluid, so the same page holds together on a phone and on a wide monitor.

**Copies without ceremony** — every code block has a copy button, highlighted at build time, with unselectable line numbers and a sticky gutter so a long snippet stays readable.

---

## Architecture

A static site. No server, no database, no runtime framework. Content is Markdown with YAML frontmatter, validated against Zod schemas at build time and compiled to flat HTML. A content audit runs before each build, which is what caught the bad counts above.

```
site/src/
├── content/       # 12 Markdown collections, Zod-validated
├── components/    # Card, SearchPalette, SEO
├── layouts/       # BaseLayout, RecipeLayout
├── pages/         # index + [id] detail pages
└── data/          # search-index.json, palette-index.json (generated)
```

<details>
<summary><strong>Build from source</strong></summary>

```bash
git clone https://github.com/kedharsairam/sqlkraft.git
cd sqlkraft/site

npm install
npm run dev       # development server
npm run build     # 5,184 pages of flat HTML
npm run preview   # serve the build locally
npm run lint      # lint
npm run format    # format
```

A full build takes about 30 seconds and emits roughly 180 MB of HTML. That sounds like a lot until you notice it is a reference you download once and then keep — no cold start, no origin to be down when you need to check an error code at 2am.

</details>

## Support

If you enjoy SqlKraft, buy me a coffee:

<p align="center">
  <a href="https://buymeacoffee.com/kedhartech"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="182"></a>
</p>

## License

MIT — see [LICENSE](LICENSE) for details.
