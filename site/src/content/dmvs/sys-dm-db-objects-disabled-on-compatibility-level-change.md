---
name: "sys.dm_db_objects_disabled_on_compatibility_level_change"
title: "sys.dm_db_objects_disabled_on_compatibility_level_change"
category: "execution"
description: "SQL database in Microsoft Fabric Lists the indexes and constraints that will be disabled as a result of changing compatibility level in SQL Server. Indexes and constraints that contain persisted computed columns whose expressions use spatial UDTs will be disabled after upgrading or changing compatibility level. Use this dynamic management function to determine the impact of a change in compatibili"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_objects_disabled_on_compatibility_level_change ( compatibility_level )"
---

## Description

SQL database in Microsoft Fabric Lists the indexes and constraints that will be disabled as a result of changing compatibility level in SQL Server. Indexes and constraints that contain persisted computed columns whose expressions use spatial UDTs will be disabled after upgrading or changing compatibility level. Use this dynamic management function to determine the impact of a change in compatibility

## Syntax

```sql
sys.dm_db_objects_disabled_on_compatibility_level_change ( compatibility_level )
```

## Examples

### Example 1

```sql
// ErrorNumber: 8674
// ErrorSeverity: EX_USER
// ErrorFormat: The query processor is unable to produce a plan because the table or view '%.*ls' is disabled.
// ErrorCause: The table has a disabled heap.
// ErrorCorrectiveAction: Rebuild the disabled heap to enable it.
// ErrorInserts: table or view name
// ErrorOwner: mtintor
// ErrorFirstProduct: SQL11
```

### Example 2

```sql
SELECT
*
FROM sys.dm_db_objects_disabled_on_compatibility_level_change(120);
GO
```
