---
name: "sys.allocation_units"
title: "sys.allocation_units"
category: "compatibility"
description: "SQL database in Microsoft Fabric Contains a row for each allocation unit in the database."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  p.partition_number,
  p.rows,
  p.data_compression_desc
  FROM
  sys.partitions
  AS
  p
  INNER
  JOIN
  sys.allocation_units
  AS
  au
  ON
  p.partition_id = au.container_id
  ORDER
  BY
  SpaceUsed_MB
  DESC
  ;
---

## Description

SQL database in Microsoft Fabric Contains a row for each allocation unit in the database. ID of the allocation unit. Is unique within a database. 1 = In-row data (all data types, except LOB data types) Description of the allocation unit type: ID of the storage container associated with the allocation unit. If type = 1 or 3 in a rowstore index container_id = If type = 1 or 3 in a columnstore index, container_id =

## Syntax

```sql
p.partition_number,
p.rows,
p.data_compression_desc
FROM sys.partitions
AS p
INNER
JOIN sys.allocation_units
AS au
ON p.partition_id = au.container_id
ORDER
BY
SpaceUsed_MB
DESC
;
```
