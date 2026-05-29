---
name: 'sys.memory_optimized_tables_internal_attributes'
title: 'sys.memory_optimized_tables_internal_attributes'
category: 'objects'
description: 'To get more details about the memory consumption of off-row columns you can use the following query, which shows the memory consumption of all internal tables and their indexes that are used to store the off-row columns: Use the following query to show the memory consumption of columnstore indexes on'
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
  QUOTENAME(SCHEMA_NAME(o.schema_id)) + N'.' + QUOTENAME(OBJECT_NAME(moa.object_id))
  AS 'table',
  c.name AS 'column',
  c.max_length
  FROM sys.memory_optimized_tables_internal_attributes moa
  JOIN sys.columns c ON moa.object_id = c.object_id AND moa.minor_id=c.column_id
  JOIN sys.objects o on moa.object_id=o.object_id
  WHERE moa.type=5;
---

## Description

To get more details about the memory consumption of off-row columns you can use the following query, which shows the memory consumption of all internal tables and their indexes that are used to store the off-row columns: Use the following query to show the memory consumption of columnstore indexes on

## Syntax

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
