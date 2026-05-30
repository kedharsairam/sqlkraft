---
name: "sys.sp_delete_backuphistory"
title: "sp_delete_backuphistory"
category: "general"
description: "Reduces the size of the backup and restore history tables by deleting the entries for backup sets older than the specified date. More rows are added to the backup and restore history tables after each backup or restore operation is performed; therefore, we recommend that you Transact-SQL syntax conventions The oldest date retained in the backup and restore history tables. The backup and restore hi"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_delete_backuphistory"
---

## Description

Reduces the size of the backup and restore history tables by deleting the entries for backup sets older than the specified date. More rows are added to the backup and restore history tables after each backup or restore operation is performed; therefore, we recommend that you Transact-SQL syntax conventions The oldest date retained in the backup and restore history tables. The backup and restore history tables reside in the

## Syntax

```sql
sp_delete_backuphistory
```

## Examples

### Example 1

```sql
sp_delete_backuphistory
```

### Example 2

```sql
msdb
```

### Example 3

```sql
EXECUTE
```

### Example 4

```sql
USE
msdb;
GO
EXECUTE
sp_delete_backuphistory @oldest_date =
'2023-01-14'
;
GO
```

### Example 5

```sql
sp_delete_backuphistory
```

### Example 6

```sql
Test
```

### Example 7

```sql
USE
msdb;
GO
EXECUTE
managed_backup.sp_backup_config_schedule
@database_name =
'Test'
,
@scheduling_option =
'Custom'
,
@full_backup_freq_type =
'Daily'
,
@backup_begin_time =
'04:00'
,
@backup_duration =
'02:00'
,
@log_backup_freq =
'00:15'
;
GO
```

### Example 8

```sql
sp_delete_backuphistory
```

### Example 9

```sql
USE
msdb;
GO
EXECUTE
managed_backup.sp_backup_master_switch @new_state = 0;
GO
USE
msdb;
GO
EXECUTE
managed_backup.sp_backup_master_switch @new_state = 1;
GO
```
