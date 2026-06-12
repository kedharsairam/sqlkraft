---
name: "sys.sp_xtp_flush_temporal_history"
title: "sp_xtp_flush_temporal_history"
category: "general"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Invokes the data flush task to move all committed rows from in-memory staging table to the The schema name for the current or temporal table."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_xtp_flush_temporal_history
  [ @schema_name = ]
  N
  'schema_name'
  , [ @object_name = ]
  N
  'object_name'
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Invokes the data flush task to move all committed rows from in-memory staging table to the The schema name for the current or temporal table.

## Syntax

```sql
sys.sp_xtp_flush_temporal_history
[ @schema_name = ]
N
'schema_name'
, [ @object_name = ]
N
'object_name'
```

## Permissions

SQL) x) and later versions Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Invokes the data flush task to move all committed rows from in-memory staging table to the disk-based history table. syntaxsql The schema name for the current or temporal table. The name of the current or temporal table. (success) or (failure). Requires permissions.
