---
name: "sys.sp_delete_backup_file_snapshot"
title: "sp_delete_backup_file_snapshot"
category: "general"
description: "SQL Server 2016 (13.x) and later versions Deletes a specified backup snapshot from the specified database. Use this system stored procedure in conjunction with the identify and delete orphaned backup snapshots. For more information, see Backups for Database Files in Azure Transact-SQL syntax conventions The name of the database containing the snapshot to be deleted, provided as a Unicode string. T"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sys.fn_db_backup_file_snapshots"
---

## Description

SQL Server 2016 (13.x) and later versions Deletes a specified backup snapshot from the specified database. Use this system stored procedure in conjunction with the identify and delete orphaned backup snapshots. For more information, see Backups for Database Files in Azure Transact-SQL syntax conventions The name of the database containing the snapshot to be deleted, provided as a Unicode string. The URL of the snapshot to be deleted, provided as a Unicode string.

## Syntax

```sql
sys.fn_db_backup_file_snapshots
```
