---
name: 'sys.fn_backup_db_config'
title: 'managed_backup.fn_backup_db_config'
category: 'backup-restore'
description: 'SQL Server 2016 (13.x) and later versions Returns 0, 1 or more rows with SQL Server managed backup to Microsoft Azure configuration settings. Returns 1 row for the specified database, or returns the information for all the databases configured with SQL Server managed backup to Microsoft Azure on the instance. Use this stored procedure to review or determine the current SQL Server managed backup to'
tags: ["backup-restore", "function"]
pubDate: 2026-05-29
syntax: 'managed_backup.fn_backup_db_config (''database_name'' | '''' | NULL)'
---

## Description

SQL Server 2016 (13.x) and later versions Returns 0, 1 or more rows with SQL Server managed backup to Microsoft Azure configuration settings. Returns 1 row for the specified database, or returns the information for all the databases configured with SQL Server managed backup to Microsoft Azure on the instance. Use this stored procedure to review or determine the current SQL Server managed backup to Microsoft Azure configuration settings for a database or all the databases on an instance of

## Syntax

```sql
managed_backup.fn_backup_db_config ('database_name' | '' | NULL)
```

## Examples

### Example 1

```sql
Use msdb
GO
SELECT * FROM managed_backup.fn_backup_db_config('TestDB')
Use msdb
GO
SELECT * FROM managed_backup.fn_backup_db_config (NULL)
```
