---
name: "sys.index_resumable_operations"
title: "sys.index_resumable_operations"
category: "indexes"
description: "SQL Server 2017 (14.x) and later versions SQL database in Microsoft Fabric is a system view that monitors and checks the current execution status for resumable Index rebuild or creation. : SQL Server (2017 and newer), and Azure SQL Database ID of the object to which this index belongs (not nullable)."
tags: ["indexes", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
  *
  FROM
  sys.index_resumable_operations
  WHERE
  STATE = 1;
---

## Description

SQL Server 2017 (14.x) and later versions SQL database in Microsoft Fabric is a system view that monitors and checks the current execution status for resumable Index rebuild or creation. : SQL Server (2017 and newer), and Azure SQL Database ID of the object to which this index belongs (not nullable). ID of the index (not nullable). is unique only within the object. Last MAX_DOP used (default = 0) Partition number within the owning index or heap. For non-

## Syntax

```sql
SELECT
*
FROM sys.index_resumable_operations
WHERE
STATE = 1;
```

## Examples

### Example 1

```sql
SELECT
*
FROM sys.index_resumable_operations
WHERE
STATE = 1;
```
