---
name: "DML support"
title: "DML support"
category: "statements"
description: "DacPac, BACPAC, or the Import/Export service, the import process creates schema objects"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

## Behavior notes

DacPac, BACPAC, or the Import/Export service, the import process creates schema objects

(including vector indexes) before loading data, which causes the import to fail.

: Drop vector indexes before exporting the database, and recreate the

indexes after import.

Vector indexes require a minimum number of rows with non-NULL vector values before the

index can be created.

: At least 100 rows with non-NULL vector values must exist in the

table.

: Attempting to create a vector index on a table with fewer than 100 rows

fails with error Msg 42266.

: Populate the table with at least 100 rows before creating the vector index. For

development and testing scenarios where fewer rows are needed,

works

without an index using a brute-force scan approach, though performance degrades with larger

datasets.

Once a DiskANN vector index is created using the latest version, the table is no longer read-

only. You can freely modify data using standard data manipulation language (DML) operations,

and changes are automatically reflected in vector search results.

This capability makes vector search suitable for live, transactional workloads where data

changes over time.

DML operations don't require dropping or rebuilding the vector index.

Changes are visible to vector search queries after the transaction commits.

### Example scenario:

## Monitoring vector index maintenance

`VECTOR_SEARCH`

```sql
Msg 42266, Level 16, State 1
Cannot create a vector index. The table contains only 8 rows with non-null vectors,
but at least 100 are required for vector index creation.
```
