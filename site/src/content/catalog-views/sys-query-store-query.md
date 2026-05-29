---
name: 'sys.query_store_query'
title: 'sys.query_store_query'
category: 'query-store'
description: 'Azure Synapse Analytics always returns'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

Azure Synapse Analytics always returns

.

Azure Synapse Analytics always returns

.

The

column is populated only when the statement is compiled from a Transact‑SQL

module. A module is any schema‑scoped object that has a row in

sys.sql_modules

.

Because the query optimizer expands non-indexed views before it produces a plan, only the

underlying tables remain, though indexed views do appear as tables.

Requires the

permission.

sys.database_query_store_options (Transact-SQL)

sys.query_context_settings (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query_text (Transact-SQL)

sys.query_store_wait_stats (Transact-SQL)

sys.query_store_runtime_stats (Transact-SQL)

sys.query_store_runtime_stats_interval (Transact-SQL)

sys.fn_stmt_sql_handle_from_sql_stmt (Transact-SQL)

Query Store hints

Monitor performance by using the Query Store

System catalog views (Transact-SQL)

Query Store stored procedures (Transact-SQL)

Last updated on 11/18/2025

3

4

Related content

```sql
NULL
```

```sql
None
```

```sql
object_id
```

```sql
VIEW DATABASE STATE
```
