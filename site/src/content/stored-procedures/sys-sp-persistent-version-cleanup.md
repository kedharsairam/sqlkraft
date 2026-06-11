---
name: "sys.sp_persistent_version_cleanup"
title: "sp_persistent_version_cleanup"
category: "general"
description: "SQL Server 2019 (15.x) and later versions SQL database in Microsoft Fabric Manually starts persistent version store (PVS) cleanup process, a key element of accelerated database recovery (ADR). The cleaner removes obsolete row versions from the in-row and off- , and also removes uncommitted changes in PVS from aborted transactions."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sys.sp_persistent_version_cleanup"
---

## Description

SQL Server 2019 (15.x) and later versions SQL database in Microsoft Fabric Manually starts persistent version store (PVS) cleanup process, a key element of accelerated database recovery (ADR). The cleaner removes obsolete row versions from the in-row and off- , and also removes uncommitted changes in PVS from aborted transactions. It isn't typically necessary to start the PVS cleanup process manually using

## Syntax

`sys.sp_persistent_version_cleanup`

## Examples

### Example 1

`sys.sp_persistent_version_cleanup`

### Example 2

`sys.sp_persistent_version_cleanup`

### Example 3

`sys.sp_persistent_version_cleanup`

### Example 4

```sql
SELECT
*
FROM sys.dm_exec_requests
WHERE command
LIKE
'%PERSISTED_VERSION_CLEANER%'
;
```

### Example 5

```sql
EXECUTE sys.sp_persistent_version_cleanup [database_name];
EXECUTE sys.sp_persistent_version_cleanup [WideWorldImporters];
```

### Example 6

```sql
USE
[WideWorldImporters];
GO
EXECUTE sys.sp_persistent_version_cleanup;
```
