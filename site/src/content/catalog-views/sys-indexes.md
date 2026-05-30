---
name: "sys.indexes"
title: "sys.indexes"
category: "indexes"
description: "The percentage of space on each index page for storing data when the index is created or replaces the fill factor when the index was created, becoming the new default for the index and for any other nonclustered indexes rebuilt, because a clustered index is uses the fill factor value last specified for the index. This value is stored in the must be specified. If isn't specified, the default fill f"
tags: ["indexes", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SUM(mc.used_bytes) / 1024 as [used_kb]
  FROM sys.memory_optimized_tables_internal_attributes moa
  JOIN sys.indexes i ON moa.object_id = i.object_id AND i.type in (5,6)
  JOIN sys.dm_db_xtp_memory_consumers mc ON moa.xtp_object_id=mc.xtp_object_id
  JOIN sys.objects o on moa.object_id=o.object_id
  WHERE moa.type IN (0, 2, 3, 4)
  GROUP BY o.schema_id, moa.object_id, i.name;
  SELECT
  QUOTENAME(SCHEMA_NAME(o.schema_id)) + N'.' + QUOTENAME(OBJECT_NAME(moa.object_id))
  AS 'table',
  i.name AS 'columnstore index',
  moa.type_desc AS 'internal table',
  mc.index_id AS 'index',
  mc.memory_consumer_desc,
  mc.allocated_bytes / 1024 as [allocated_kb],
  mc.used_bytes / 1024 as [used_kb]
  FROM sys.memory_optimized_tables_internal_attributes moa
  JOIN sys.indexes i ON moa.object_id = i.object_id AND i.type in (5,6)
  JOIN sys.dm_db_xtp_memory_consumers mc ON moa.xtp_object_id=mc.xtp_object_id
  JOIN sys.objects o on moa.object_id=o.object_id
  WHERE moa.type IN (0, 2, 3, 4)
---

## Description

The percentage of space on each index page for storing data when the index is created or replaces the fill factor when the index was created, becoming the new default for the index and for any other nonclustered indexes rebuilt, because a clustered index is uses the fill factor value last specified for the index. This value is stored in the must be specified. If isn't specified, the default fill factor, 100, is used. For more information, see Specify Fill Factor for an Index Suppresses all informational messages that have severity levels from 0 through 10. rebuilds an index for a table or all indexes defined for a table. By allowing an index to be rebuilt dynamically, indexes enforcing either PRIMARY KEY or UNIQUE constraints can be rebuilt without having to drop and re-create those constraints. This means that an index

## Syntax

```sql
SUM(mc.used_bytes) / 1024 as [used_kb]
FROM sys.memory_optimized_tables_internal_attributes moa
JOIN sys.indexes i ON moa.object_id = i.object_id AND i.type in (5,6)
JOIN sys.dm_db_xtp_memory_consumers mc ON moa.xtp_object_id=mc.xtp_object_id
JOIN sys.objects o on moa.object_id=o.object_id
WHERE moa.type IN (0, 2, 3, 4)
GROUP BY o.schema_id, moa.object_id, i.name;
SELECT
QUOTENAME(SCHEMA_NAME(o.schema_id)) + N'.' + QUOTENAME(OBJECT_NAME(moa.object_id))
AS 'table',
i.name AS 'columnstore index',
moa.type_desc AS 'internal table',
mc.index_id AS 'index',
mc.memory_consumer_desc,
mc.allocated_bytes / 1024 as [allocated_kb],
mc.used_bytes / 1024 as [used_kb]
FROM sys.memory_optimized_tables_internal_attributes moa
JOIN sys.indexes i ON moa.object_id = i.object_id AND i.type in (5,6)
JOIN sys.dm_db_xtp_memory_consumers mc ON moa.xtp_object_id=mc.xtp_object_id
JOIN sys.objects o on moa.object_id=o.object_id
WHERE moa.type IN (0, 2, 3, 4)
```

## Remarks

The percentage of space on each index page for storing data when the index is created or

replaces the fill factor when the index was created, becoming the new default

for the index and for any other nonclustered indexes rebuilt, because a clustered index is

uses the fill factor value last specified for the index. This

value is stored in the

catalog view.

is specified,

must be specified. If

isn't specified,

the default fill factor, 100, is used. For more information, see

Specify Fill Factor for an Index

Suppresses all informational messages that have severity levels from 0 through 10.

rebuilds an index for a table or all indexes defined for a table. By allowing an

index to be rebuilt dynamically, indexes enforcing either PRIMARY KEY or UNIQUE constraints

can be rebuilt without having to drop and re-create those constraints. This means that an index

can be rebuilt without knowing the structure of a table or its constraints. This might occur after

a bulk copy of data into the table.

can rebuild all the indexes for a table in one statement. This is easier than

coding multiple

statements. Because the work is performed by

one statement,

is automatically atomic, whereas individual

statements must be included in a transaction to be atomic. Also,

offers more optimizations than individual

statements.

offline operation. If a nonclustered index is being rebuilt, a shared lock is held on the table in

question during the operation. This prevents modifications to the table. If the clustered index is

being rebuilt, an exclusive table lock is held. This prevents any table access, therefore

effectively making the table offline. To perform an index rebuild online, or to control the

degree of parallelism during the index rebuild operation, use the

statement with the

For more information about selecting a method to rebuild or reorganize an index, see

Reorganize and Rebuild Indexes

## Examples

### Example 1

```sql
0
```

### Example 2

```sql
EXECUTE sp_describe_first_result_set @tsql = N
'SELECT object_id, name, type_desc FROM sys.indexes'
;
EXECUTE sp_describe_first_result_set @tsql = N
'
SELECT object_id, name, type_desc
FROM sys.indexes
WHERE object_id = @id1'
, @params = N
'@id1 int'
;
```

### Example 3

```sql
CREATE
TABLE dbo.t (
a
INT
PRIMARY
KEY
,
b1
INT
);
GO
CREATE
VIEW dbo.v
AS
SELECT b1
AS b2
FROM dbo.t;
GO
EXECUTE sp_describe_first_result_set N
'SELECT b2 AS b3 FROM dbo.v'
,
NULL
, 0;
```
