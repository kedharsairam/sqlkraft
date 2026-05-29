# SqlKraft

Enterprise SQL Server Reference Hub — a curated, high-performance static encyclopedia and operational playbook for the DBA community.

SqlKraft provides structured, searchable access to:

- **Dynamic Management Views** (160+ DMVs)
- **Wait Statistics** (50+ wait types)
- **System Catalog Views** (150+ views)
- **System Functions** (all built-in functions)
- **System Stored Procedures**
- **T-SQL Language Reference**
- **Database Engine Errors**
- **Engine Architecture & Internals**
- **Operations & Administration Guides**
- **TSQL Diagnostic Scripts** (270+ scripts)

## Getting Started

```bash
# Install site dependencies
cd site
npm install

# Development server
npm run dev

# Production build
npm run build
```

## Repository Scale Matrix

| Collection | Records | Description |
|---|---|---|
| T-SQL Reference | 1,740 | Language statements, queries, data types, operators, hints, predicates |
| Operations | 1,258 | Administration, monitoring, migration, HA, SSMS, Profiler, Linux |
| Database Engine Errors | 1,129 | Error codes with severity classification and troubleshooting |
| Architecture | 916 | Query processing, memory, locking, I/O, internals |
| System Stored Procedures | 699 | Administrative and maintenance procedures |
| System Catalog Views | 275 | Database metadata, objects, indexes, security |
| TSQL Diagnostic Scripts | 270 | Curated performance, indexing, security, HA scripts |
| Dynamic Management Views | 151 | Execution, I/O, memory, indexing, OS internals DMVs |
| Wait Statistics | 49 | Wait types across baseline, triage, blocking, I/O categories |
| System Functions | 49 | Aggregate, analytic, conversion, string, date/time functions |
| **Total** | **6,536** | **10 collections — searchable, static, zero-dependency** |

## License

MIT
