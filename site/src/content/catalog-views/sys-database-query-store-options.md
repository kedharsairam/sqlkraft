---
name: 'sys.database_query_store_options'
title: 'sys.database_query_store_options'
category: 'query-store'
description: ': SQL Server 2017 (14.x) and'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

## Description
(default)

: SQL Server 2017 (14.x) and

later versions.

Currently unused.

Requires the

permission, or a greater permission such as

.

In SQL Server 2016 (13.x) through SQL Server 2019 (15.x), requires the

permission. In SQL Server 2022 (16.x) and later versions, requires the

permission on the database, or a greater permission such as

.

An

value of

is the expected state when Query Store

for secondary replicas is enabled. For more information, see

Query Store for secondary replicas

.

sys.query_context_settings (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

sys.query_store_query_text (Transact-SQL)

sys.query_store_runtime_stats (Transact-SQL)

sys.query_store_wait_stats (Transact-SQL)

sys.query_store_runtime_stats_interval (Transact-SQL)

Monitoring Performance By Using the Query Store

System catalog views (Transact-SQL)

sys.fn_stmt_sql_handle_from_sql_stmt (Transact-SQL)

Query Store stored procedures (Transact-SQL)

Last updated on 02/25/2026

Related content

```sql
ON
```

```sql
actual_state_additional_info
```

```sql
VIEW DATABASE PERFORMANCE STATE
```

```sql
VIEW DATABASE STATE
```

```sql
VIEW DATABASE STATE
```

```sql
VIEW DATABASE
PERFORMANCE STATE
```

```sql
VIEW DATABASE
STATE
```

```sql
actual_state_desc
```

```sql
READ_CAPTURE_SECONDARY
```
