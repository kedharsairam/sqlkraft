---
name: "Reorganize indexes"
title: "Reorganize indexes"
category: "statements"
description: "On multiprocessor computers, just like other queries do,"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

On multiprocessor computers, just like other queries do,

automatically

uses more processors to perform the scan and sort operations that are associated with

modifying the index. Conversely,

is a single threaded operation. For

more information, see

Configure parallel index operations

.

In SQL database in Microsoft Fabric,

is not supported, but

is.

Rebuilding an index drops and re-creates the index. This removes fragmentation, reclaims disk

space by compacting the pages based on the specified or existing fill factor setting, and

reorders the index rows in contiguous pages. When

is specified, all indexes on the table

are dropped and rebuilt in a single transaction. Foreign key constraints don't have to be

dropped in advance. When indexes with 128 extents or more are rebuilt, the Database Engine

defers the actual page deallocations, and their associated locks, until after the transaction

commits. For more information, see

Deferred deallocation

.

For more information, see

Optimize index maintenance to improve query performance and

reduce resource consumption

.

Reorganizing an index uses minimal system resources. It defragments the leaf level of clustered

and nonclustered indexes on tables and views by physically reordering the leaf-level pages to

match the logical, left to right, order of the leaf nodes. Reorganizing also compacts the index

pages. Compaction is based on the existing fill factor value.

When

is specified, relational indexes, both clustered and nonclustered, and XML indexes

on the table are reorganized. Some

restrictions

apply when specifying

.

For more information, see

Optimize index maintenance to improve query performance and

reduce resource consumption

.

７

Note

For a table with an ordered columnstore index,

doesn't re-sort

the data. To resort the data use

.

```sql
ALTER INDEX REBUILD
```

```sql
ALTER INDEX REORGANIZE
```

```sql
ALTER INDEX ALL
```

```sql
ALTER INDEX <index
name>
```

```sql
ALL
```

```sql
ALL
```

```sql
ALL
```

```sql
ALTER INDEX REORGANIZE
```

```sql
CREATE [CLUSTERED] COLUMNSTORE INDEX ... ORDER (...)
... WITH (DROP_EXISTING = ON)
```
