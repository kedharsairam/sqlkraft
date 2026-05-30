---
name: "Upgrade vector indexes to the latest version"
title: "Upgrade vector indexes to the latest version"
category: "statements"
description: "Newly created vector indexes automatically use the latest data structure, which provides:"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

### Deprecation notice

## Migrating from earlier vector index versions

## Step 1: Identify existing vector indexes

Newly created vector indexes automatically use the latest data structure, which provides:

: Removes the previous limitation that made vector-indexed tables

read-only after index creation. You can now perform INSERT, UPDATE, DELETE, and

MERGE operations while maintaining vector index functionality with automatic, real-time

index maintenance

: Predicates in the WHERE clause are applied during the vector search

process, not after retrieval

: The query optimizer automatically determines whether to use the

DiskANN index or kNN search based on query characteristics

: Vector quantization techniques have been integrated to provide

better storage efficiency and faster query performance, with these optimizations being

transparent to users

For details on

earlier vector index version limitations

, see the Limitations and considerations

section.

Vector indexes created using an earlier version must be dropped and recreated to enable the

latest capabilities. This section explains how to identify, migrate, and verify vector index

versions.

Use the following query to identify vector indexes that require migration:

）

Important

: Vector indexes created using an earlier data structure are supported

in the current release but will be retired in a future version. To ensure future compatibility

and access to the latest vector search capabilities, migrate existing vector indexes using

the steps below.

### Uses latest version

### Created using an earlier version

## Step 2: Drop and recreate the vector index

### Service impact

Already supports iterative filtering, full DML support, optimizer-driven execution and

improved quantization

No migration required

Uses legacy post-filter behavior

Doesn't support the latest vector search capabilities

Migration is strongly recommended to ensure future compatibility

Vector indexes created using an earlier format can't be upgraded in place. To enable the latest

DiskANN capabilities, drop and recreate the index.

How to interpret the results

２

Warning

: Dropping a vector index immediately disables approximate vector search

on the affected table until the index is recreated. Plan migrations during maintenance

windows for production systems.

Drop the existing index

## Step 3: Verify the index version

After recreation, verify the index is using the latest version:

The

column should display

for the latest version.

If you attempt to use the

parameter in

with a latest version vector index,

SQL Server returns the following error:

Recreate the index

７

Note

Vector indexes created using the current

statement automatically

use the latest DiskANN format. No additional options or flags are required.

#### Output

### Post-filtering only

### Read-only tables

### Manual TOP_N tuning

```sql
SELECT i.name
AS index_name,
t.name
AS table_name,
JSON_VALUE(v.build_parameters,
'$.Version'
)
AS index_version,
```

```sql
CASE
WHEN
JSON_VALUE(v.build_parameters,
'$.Version'
) >=
'3'
THEN
'Uses latest version (no migration required)'
WHEN
JSON_VALUE(v.build_parameters,
'$.Version'
) <
'3'
THEN
'Created using an earlier version (migration recommended)'
ELSE
'Unknown format'
END
AS migration_status
FROM sys.vector_indexes
AS v
INNER
JOIN sys.indexes
AS i
ON v.object_id = i.object_id
AND v.index_id = i.index_id
INNER
JOIN sys.tables
AS t
ON v.object_id = t.object_id
ORDER
BY t.name, i.name;
```

`index_version`

```sql
3
```

`TOP_N`

`VECTOR_SEARCH`

```sql
DROP
INDEX vec_idx
ON dbo.wikipedia_articles;
```

```sql
CREATE
VECTOR
INDEX vec_idx
ON dbo.wikipedia_articles (title_vector)
WITH (
TYPE
=
'DISKANN'
,
METRIC =
'COSINE'
);
```

```sql
CREATE VECTOR INDEX
```

```sql
SELECT i.name
AS index_name,
t.name
AS table_name,
JSON_VALUE(v.build_parameters,
'$.Version'
)
AS index_version
FROM sys.vector_indexes
AS v
INNER
JOIN sys.indexes
AS i
ON v.object_id = i.object_id
AND v.index_id = i.index_id
INNER
JOIN sys.tables
AS t
ON v.object_id = t.object_id
WHERE i.name =
'vec_idx'
;
```
