---
name: 'sys.dm_db_log_space_usage'
title: 'sys.dm_db_log_space_usage'
category: 'execution'
description: 'The following query returns the databases with more than 100 VLFs in the log files. Large'
pubDate: 2026-05-29
---

The following query returns the databases with more than 100 VLFs in the log files. Large

numbers of VLFs can affect the database startup, restore, and recovery time.

SQL

The following query determines the last log backup start times for the databases in the

instance.

SQL

System dynamic management views

Database related dynamic management views (Transact-SQL)

sys.dm_db_log_space_usage

sys.dm_db_log_info

Last updated on 01/29/2026

## smallint

## int

## int

```sql
SELECT
name
AS
'Database Name'
,
total_vlf_count
AS
'VLF count'
FROM
sys.databases
AS
s
CROSS
APPLY
sys.dm_db_log_stats(s.database_id)
WHERE
total_vlf_count > 100;
```

```sql
SELECT
name
AS
'Database Name'
,
log_backup_time
AS
'last log backup start time'
FROM
sys.databases
AS
s
CROSS
APPLY
sys.dm_db_log_stats(s.database_id);
```
