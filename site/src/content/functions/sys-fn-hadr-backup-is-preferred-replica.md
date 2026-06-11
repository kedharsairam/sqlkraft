---
name: "sys.fn_hadr_backup_is_preferred_replica"
title: "sys.fn_hadr_backup_is_preferred_replica"
category: "backup-restore"
description: "Used to determine if the current replica is the preferred backup replica. Transact-SQL syntax conventions The name of the database to be backed up. is type sysname. Returns data type if the database on the current instance is on the preferred replica, For databases that aren't part of an availability group, this function always returns If the specified database doesn't exist, the function returns"
tags: ["backup-restore", "function"]
pubDate: 2026-05-29
syntax: |
  sys.fn_hadr_backup_is_preferred_replica (
  'dbname'
  )
---

## Description

Used to determine if the current replica is the preferred backup replica. Transact-SQL syntax conventions The name of the database to be backed up. is type sysname. Returns data type if the database on the current instance is on the preferred replica, For databases that aren't part of an availability group, this function always returns If the specified database doesn't exist, the function returns a different value based on the version of SQL Server: Starting with SQL Server 2019 , and SQL Server 2022 , the function returns In earlier versions, the function returns Use this function in a backup script to determine if the current database is on the replica that is preferred for backups. You can run a script on every availability replica. Each of these jobs looks

## Syntax

```sql
sys.fn_hadr_backup_is_preferred_replica (
'dbname'
)
```

## Remarks

Applies to:

Used to determine if the current replica is the preferred backup replica.

Transact-SQL syntax conventions

The name of the database to be backed up.

is type sysname.

Returns data type

if the database on the current instance is on the preferred replica,

For databases that aren't part of an availability group, this function always returns

If the specified database doesn't exist, the function returns a different value based on the

version of SQL Server:

Starting with SQL Server 2019

, and SQL Server 2022

, the function returns

In earlier versions, the function returns

Use this function in a backup script to determine if the current database is on the replica that is

preferred for backups. You can run a script on every availability replica. Each of these jobs looks
