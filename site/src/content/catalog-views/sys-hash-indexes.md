---
name: "sys.hash_indexes"
title: "sys.hash_indexes"
category: "indexes"
description: "SQL Server 2014 (12.x) and later Shows the current hash indexes and the hash index properties. Hash indexes are supported In-Memory OLTP (In-Memory Optimization) The sys.hash_indexes view contains the same columns as the sys.indexes view and an additional . For more information about the other columns in the Count of hash buckets for hash indexes. For more information about the bucket_count value,"
tags: ["indexes", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT object_name([object_id]) AS 'table_name', [object_id],
  [name] AS 'index_name', [type_desc], [bucket_count]
  FROM sys.hash_indexes
  WHERE OBJECT_NAME([object_id]) = 'T1';
---

## Description

SQL Server 2014 (12.x) and later Shows the current hash indexes and the hash index properties. Hash indexes are supported In-Memory OLTP (In-Memory Optimization) The sys.hash_indexes view contains the same columns as the sys.indexes view and an additional . For more information about the other columns in the Count of hash buckets for hash indexes. For more information about the bucket_count value, including guidelines

## Syntax

```sql
SELECT object_name([object_id]) AS 'table_name', [object_id],
[name] AS 'index_name', [type_desc], [bucket_count]
FROM sys.hash_indexes
WHERE OBJECT_NAME([object_id]) = 'T1';
```

## Examples

### Example 1

```sql
SELECT object_name([object_id]) AS 'table_name', [object_id],
[name] AS 'index_name', [type_desc], [bucket_count]
FROM sys.hash_indexes
WHERE OBJECT_NAME([object_id]) = 'T1';
```

### Example 2

```sql
NONCLUSTERED HASH
```

### Example 3

`sys.hash_indexes`

### Example 4

`Production.Product`

### Example 5

```sql
SELECT i.name
AS index_name,
i.type_desc,
is_unique,
ds.type_desc
AS filegroup_or_partition_scheme,
ds.name
AS filegroup_or_partition_scheme_name,
ignore_dup_key,
is_primary_key,
is_unique_constraint,
fill_factor,
is_padded,
is_disabled,
allow_row_locks,
allow_page_locks
FROM sys.indexes
AS i
INNER
JOIN sys.data_spaces
AS ds
ON i.data_space_id = ds.data_space_id
WHERE is_hypothetical = 0
AND i.index_id <> 0
AND i.object_id = OBJECT_ID(
'Production.Product'
);
GO
```
