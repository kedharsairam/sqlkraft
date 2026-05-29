# SqlKraft Session Notes

## v0.4.0 Capstone — Phase 5 Final Sweep Complete

### What was done
- **3 new PDF extractions** (1,636 pages): HA (p.866-2043), Upgrade (p.6442-6655), Migration (p.7155-7398)
- **303 operations articles added**: high-availability (236), upgrade (26), migration (30), data-tools (8), azure-arc (3)
- **Classification fixes**: SSDT entries re-mapped from ssb-diagnose→data-tools (8 articles), Azure Arc re-mapped from azure-synapse→azure-arc (3 articles)
- **Search index**: 6,266 records (+279 from sweep)
- **Build**: 6,321 pages, zero errors, 64.46s
- **Committed**: `0abe4e1` v0.4.0 capstone pushed, CI green

### All 14 operations topics now populated
- azure-arc: 3, azure-synapse: 53, configuration: 10, data-tools: 8, event-classes: 192, high-availability: 236, linux-operations: 129, migration: 30, monitor: 370, profiler: 85, sqlpackage: 14, ssb-diagnose: 80, ssms: 35, upgrade: 26

### Total content: 6,310 files, 10 collections, 6,266 search index records

### Key scripts
- `extractor/sweep_mapper.py` — New! Post-processing mapper for page-range-based topic assignments and classification overrides
- `extractor/operations_mapper.py` — v0.5.0 main operations ingestion engine (Range 2)
- `extractor/narrative_mapper.py` — v0.4.0 narrative content engine

### Known issues
- Scripts collection remains empty (intentional — no scripts have been extracted yet)
- p.1-865 first pages (intro/backup/restore) still untapped but not needed for current scope
- p.9568-14418 (replication, tools, Analysis Services, SSRS, MDS, full-text search) still untapped

### Build commands
- `cd site && npm run build` — production build
- `cd site && node rebuild-search-index.cjs` — search index regeneration
- `cd extractor && python operations_mapper.py` — Range 2 operations extraction
- `cd extractor && python sweep_mapper.py` — Phase 5 sweep (runs after operations_mapper.py)
