---
name: 'sys.fn_stmt_sql_handle_from_sql_stmt'
title: 'sys.fn_stmt_sql_handle_from_sql_stmt'
category: 'system'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["function"]
pubDate: 2026-05-29
---

## Description
0

None

1

User

2

Simple

3

Forced

The following table lists the columns that


## returns.

## Description
The SQL handle.

The text of the Transact-SQL statement.

The query parameterization type.

(success) or

(failure).

Requires

permission on the database, and

permission on the Query Store

catalog views.

The following example executes a statement, and then uses

to return the SQL handle of that statement.

SQL

ﾉ

Expand table

Use the function to correlate Query Store data with other dynamic management views. The

following example:

SQL

sp_query_store_force_plan (Transact-SQL)

sp_query_store_remove_plan (Transact-SQL)

sp_query_store_unforce_plan (Transact-SQL)

sp_query_store_reset_exec_stats (Transact-SQL)

sp_query_store_flush_db (Transact-SQL)

sp_query_store_remove_query (Transact-SQL)

Query Store catalog views (Transact-SQL)

Monitor performance by using the Query Store

Last updated on 11/18/2025

Related content

```sql
sys.fn_stmt_sql_handle_from_sql_stmt
```

```sql
statement_sql_handle
```

```sql
query_sql_text
```

```sql
query_parameterization_type
```

```sql
0
```

```sql
1
```

```sql
EXECUTE
```

```sql
DELETE
```

```sql
sys.fn_stmt_sql_handle_from_sql_stmt
```

```sql
SELECT
*
FROM
sys.databases;
```

```sql
SELECT
*
FROM
sys.fn_stmt_sql_handle_from_sql_stmt(
'SELECT * FROM sys.databases'
,
NULL
);
SELECT
qt.query_text_id,
q.query_id,
qt.query_sql_text,
qt.statement_sql_handle,
q.context_settings_id,
qs.statement_context_id
FROM
sys.query_store_query_text
AS
qt
INNER
JOIN
sys.query_store_query
AS
q
ON
qt.query_text_id = q.query_text_id
CROSS
APPLY
sys.fn_stmt_sql_handle_from_sql_stmt(qt.query_sql_text,
NULL
)
AS
fn_handle_from_stmt
INNER
JOIN
sys.dm_exec_query_stats
AS
qs
ON
fn_handle_from_stmt.statement_sql_handle = qs.statement_sql_handle;
```
