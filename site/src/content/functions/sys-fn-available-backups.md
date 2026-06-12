---
name: "sys.fn_available_backups"
title: "managed_backup.fn_available_backups"
category: "backup-restore"
description: "2016 (13.x) and later versions Returns a table of 0, one or more rows of the available backup files for the specified database. The backup files returned are backups created by SQL Server managed backup to Microsoft The name of the database. The @database_name is NVARCHAR(512). The table has a unique clustered constraint on (database_guid, backup_start_da"
tags: ["backup-restore","function"]
pubDate: 2026-05-29
syntax: "managed_backup.fn_available_backups ([@database_name = ] 'database name')"
---

## Description

2016 (13.x) and later versions Returns a table of 0, one or more rows of the available backup files for the specified database. The backup files returned are backups created by SQL Server managed backup to Microsoft The name of the database. The @database_name is NVARCHAR(512). The table has a unique clustered constraint on (database_guid, backup_start_date, and first_lsn,

## Syntax

```sql
managed_backup.fn_available_backups ([@database_name = ] 'database name')
```

## Examples

### Example 1

```sql
SELECT *
FROM msdb.managed_backup.fn_available_backups ('MyDB')
```
