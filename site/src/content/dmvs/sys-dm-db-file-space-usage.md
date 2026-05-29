---
name: 'sys.dm_db_file_space_usage'
title: 'sys.dm_db_file_space_usage'
category: 'execution'
description: 'permission on the database, or membership in the'
pubDate: 2026-05-29
---

either the

permission on the database, or membership in the

server role is required.

The following query returns the total free log space in megabytes (MB) available in

.

SQL

System dynamic management views

Database related dynamic management views (Transact-SQL)

sys.dm_db_file_space_usage

sys.dm_db_task_space_usage (Transact-SQL)

sys.dm_db_session_space_usage (Transact-SQL)

sys.dm_db_log_info (Transact-SQL)

sys.dm_db_log_stats (Transact-SQL)

Last updated on 11/18/2025

## int

```sql
VIEW DATABASE STATE
```

```sql
##MS_ServerStateReader##
```

```sql
tempdb
```

```sql
USE
tempdb;
GO
SELECT
(total_log_size_in_bytes - used_log_space_in_bytes) * 1.0 / 1024 / 1024
AS
[free
log
space
in
MB]
FROM
sys.dm_db_log_space_usage;
```
