---
name: "sys.masked_columns"
title: "sys.masked_columns"
category: "objects"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric view to query for table-columns that have a dynamic data masking function applied to them. This view inherits from the indicating if the column is masked, and if so, what masking function is defined. This view only shows the columns on which there is a masking function applied."
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT tbl.name as table_name, c.name AS column_name, c.is_masked,
  c.masking_function
  FROM sys.masked_columns AS c
  JOIN sys.tables AS tbl
  ON c.object_id = tbl.object_id
  WHERE is_masked = 1;
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric view to query for table-columns that have a dynamic data masking function applied to them. This view inherits from the indicating if the column is masked, and if so, what masking function is defined. This view only shows the columns on which there is a masking function applied.

## Syntax

```sql
SELECT tbl.name as table_name, c.name AS column_name, c.is_masked,
c.masking_function
FROM sys.masked_columns AS c
JOIN sys.tables AS tbl
ON c.object_id = tbl.object_id
WHERE is_masked = 1;
```

## Examples

### Example 1

```sql
SELECT tbl.name as table_name, c.name AS column_name, c.is_masked,
c.masking_function
FROM sys.masked_columns AS c
JOIN sys.tables AS tbl
ON c.object_id = tbl.object_id
WHERE is_masked = 1;
```
