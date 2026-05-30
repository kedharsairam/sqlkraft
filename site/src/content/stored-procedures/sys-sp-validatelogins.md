---
name: "sys.sp_validatelogins"
title: "sp_validatelogins"
category: "general"
description: "Reports information about Windows users and groups that are mapped to SQL Server principals but no longer exist in the Windows environment. Transact-SQL syntax conventions Windows security identifier (SID) of the Windows user or group. Name of the Windows user or group. If the orphaned server-level principal owns a database user, the database user must be removed before the orphaned server princip"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_validatelogins
  [ ; ]
---

## Description

Reports information about Windows users and groups that are mapped to SQL Server principals but no longer exist in the Windows environment. Transact-SQL syntax conventions Windows security identifier (SID) of the Windows user or group. Name of the Windows user or group. If the orphaned server-level principal owns a database user, the database user must be removed before the orphaned server principal can be removed. To remove a database user, use . If the server-level principal owns securables in the database, ownership of the securables must be transferred or they must be dropped. To transfer ownership of database securables, use ALTER AUTHORIZATION To remove mappings to Windows users and groups that no longer exist, use

## Syntax

```sql
sp_validatelogins
[ ; ]
```

## Remarks

Applies to:

Reports information about Windows users and groups that are mapped to SQL Server

principals but no longer exist in the Windows environment.

Transact-SQL syntax conventions

(success) or

Description

Windows security identifier (SID) of the Windows user or group.

Name of the Windows user or group.

If the orphaned server-level principal owns a database user, the database user must be

removed before the orphaned server principal can be removed. To remove a database user, use

. If the server-level principal owns securables in the database, ownership of the

securables must be transferred or they must be dropped. To transfer ownership of database

securables, use

ALTER AUTHORIZATION

To remove mappings to Windows users and groups that no longer exist, use

Expand table

## Examples

### Example 1

```sql
EXECUTE
sp_validatelogins;
GO
```
