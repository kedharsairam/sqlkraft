---
name: 'sys.sp_flush_commit_table_on_demand'
title: 'sys.sp_flush_commit_table_on_demand'
category: 'general'
description: 'Transact-SQL syntax conventions'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

(success) or

(failure).

SQL

Here's the result set.

Output

This procedure must be run in a database that has change tracking enabled.

Only a member of the

server role or

database role can execute this

procedure.

About Change Tracking (SQL Server)

Troubleshoot change tracking auto cleanup issues

Change Tracking Functions (Transact-SQL)

Change Tracking tables (Transact-SQL)

Change Tracking stored procedures (Transact-SQL)

Related content

```sql
0
```

```sql
1
```

```sql
DECLARE
@deleted_rows
AS
BIGINT
;
DECLARE
@date_cleanedup
AS
DATETIME;
DECLARE
@cleanup_ts
AS
BIGINT
;
EXECUTE
sys.sp_flush_commit_table_on_demand 3000,
@deleted_rows = @deleted_rows
OUTPUT
,
@date_cleanedup = @date_cleanedup
OUTPUT
,
@cleanup_ts = @cleanup_ts
OUTPUT
;
PRINT CONCAT('Number of rows deleted: ', @deleted_rows);
PRINT CONCAT('Cleanup date: ', @date_cleanedup);
PRINT CONCAT('
Change
tracking
version
:
', @cleanup_ts);
GO
Started executing query at Line 1
The value returned by change_tracking_hardened_cleanup_version() is 17.
The value returned by safe_cleanup_version() is 17.
(0 rows affected)
Number of rows deleted: 100
Cleanup date: Aug 29 2022  8:59PM
Change tracking Version: 17
Total execution time: 00:00:02.008
```
