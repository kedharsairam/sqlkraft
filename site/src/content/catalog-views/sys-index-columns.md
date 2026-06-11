---
name: "sys.index_columns"
title: "sys.index_columns"
category: "objects"
description: "Analytics Platform System (PDW) Contains one row per column that is part of an index or unordered table (heap)."
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: "data_clustering_ordinal"
---

## Description

Analytics Platform System (PDW) Contains one row per column that is part of an index or unordered table (heap). ID of the object the index is defined on. ID of the index in which the column is defined. = Row Identifier (RID) in a nonclustered index. Ordinal (1-based) within set of key-columns. 0 = Not a key column, or is an XML index, columnstore index, Note: An XML or spatial or JSON index can't be a key because

## Syntax

`data_clustering_ordinal`

## Arguments

Applies to:

Azure SQL Managed Instance

Returns information about the index key. Returns NULL for XML indexes.

Transact-SQL syntax conventions

Is the object identification number of the table or indexed view.

Is the index identification number.

Is the index key column position.

Is the name of the property for which information will be returned.

is a character

string and can be one of the following values.

Description

Column ID at the

position of the index.

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Instead, use

Expand table

sys.indexes (Transact-SQL)

sys.index_columns (Transact-SQL)

sys.stats (Transact-SQL)

sys.stats_columns (Transact-SQL)

Last updated on 11/18/2025

DROP INDEX (Transact-SQL)

EVENTDATA (Transact-SQL)

sys.index_columns (Transact-SQL)

sys.indexes (Transact-SQL)

sys.spatial_index_tessellations (Transact-SQL)

sys.spatial_indexes (Transact-SQL)

Spatial Indexes Overview

## Examples

### Example 1

```sql
0
```

### Example 2

`sys.index_columns`

### Example 3

```sql
0
```

### Example 4

`data_clustering_ordinal`

### Example 5

`Production.BillOfMaterials`

### Example 6

```sql
USE
AdventureWorks2022;
GO
SELECT i.name
AS index_name
,COL_NAME(ic.object_id,ic.column_id)
AS column_name
,ic.index_column_id
,ic.key_ordinal
,ic.is_included_column
FROM sys.indexes
AS i
INNER
JOIN sys.index_columns
AS ic
ON i.object_id = ic.object_id
AND i.index_id = ic.index_id
WHERE i.object_id = OBJECT_ID(
'Production.BillOfMaterials'
);
```
