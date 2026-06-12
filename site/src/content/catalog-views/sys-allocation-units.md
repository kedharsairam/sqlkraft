---
name: "sys.allocation_units"
title: "sys.allocation_units"
category: "compatibility"
description: "Contains a row for each allocation unit in the database."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
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

Contains a row for each allocation unit in the database.

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
