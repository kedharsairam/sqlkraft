---
name: 'sys.memory_optimized_tables_internal_attri'
title: 'sys.memory_optimized_tables_internal_attri'
category: 'objects'
description: '## A. Returning all columns that are stored off-row'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## A. Returning all columns that are stored off-row


## Description
memory-optimized table first. There is a background task that

asynchronously moves rows from this internal table to the disk-based

history table.

minor_id

0 indicates a user or internal table

Non-0 indicates the ID of a column stored off-row. Joins with column_id in

sys.columns.

Each column stored off-row has a corresponding row in this system view.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following T-SQL script illustrates a table with multiple large non-LOB columns and a single

LOB column:

Transact-SQL

The following query shows all columns that are stored off-row, along with their sizes. A size of

-1 indicates a LOB column. All LOB columns are stored off-row.

Transact-SQL

## B. Returning memory consumption of all columns that are

## stored off-row

## C. Returning memory consumption of columnstore indexes on

## memory-optimized tables

To get more details about the memory consumption of off-row columns you can use the

following query, which shows the memory consumption of all internal tables and their indexes

that are used to store the off-row columns:

Transact-SQL

Use the following query to show the memory consumption of columnstore indexes on

memory-optimized tables:

Transact-SQL

Use the following query break down the memory consumption across internal structures used

for columnstore indexes on memory-optimized tables:

Transact-SQL

Last updated on 11/18/2025

```sql
CREATE TABLE dbo.LargeTableSample
(
Id   int IDENTITY PRIMARY KEY NONCLUSTERED,
C1   nvarchar(4000),
C2   nvarchar(4000),
C3   nvarchar(4000),
C4   nvarchar(4000),
Misc nvarchar(max)
) WITH (MEMORY_OPTIMIZED = ON);
GO
```

```sql
SELECT
QUOTENAME(SCHEMA_NAME(o.schema_id)) + N'.' + QUOTENAME(OBJECT_NAME(moa.object_id))
AS 'table',
c.name AS 'column',
c.max_length
FROM sys.memory_optimized_tables_internal_attributes moa
JOIN sys.columns c ON moa.object_id = c.object_id AND moa.minor_id=c.column_id
JOIN sys.objects o on moa.object_id=o.object_id
WHERE moa.type=5;
```

```sql
SELECT
QUOTENAME(SCHEMA_NAME(o.schema_id)) + N'.' + QUOTENAME(OBJECT_NAME(moa.object_id))
AS 'table',
c.name AS 'column',
c.max_length,
mc.memory_consumer_desc,
mc.index_id,
mc.allocated_bytes,
mc.used_bytes
FROM sys.memory_optimized_tables_internal_attributes moa
JOIN sys.columns c ON moa.object_id = c.object_id AND moa.minor_id=c.column_id
JOIN sys.dm_db_xtp_memory_consumers mc ON moa.xtp_object_id=mc.xtp_object_id
JOIN sys.objects o on moa.object_id=o.object_id
WHERE moa.type=5;
```

```sql
SELECT
QUOTENAME(SCHEMA_NAME(o.schema_id)) + N'.' + QUOTENAME(OBJECT_NAME(moa.object_id))
AS 'table',
i.name AS 'columnstore index',
SUM(mc.allocated_bytes) / 1024 as [allocated_kb],
```

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
