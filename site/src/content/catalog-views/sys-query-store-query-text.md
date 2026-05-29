---
name: 'sys.query_store_query_text'
title: 'sys.query_store_query_text'
category: 'query-store'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

SQL database in Microsoft Fabric

Contains the Transact-SQL text and the SQL handle of the query.


## Description
Primary key.

SQL text of the query, as provided by the user. Includes

whitespaces, hints, and comments. Comments and

spaces before and after the query text are ignored.

Comments and spaces inside text aren't ignored.

SQL handle of the individual query.

Query text is a part of an encrypted module.

Query text contains a password or other unmentionable

words.

Azure Synapse Analytics always returns zero (

).

SQL Server 2019 (15.x) and previous versions require

permission on the

server.

SQL Server 2022 (16.x) and later versions require

permission on

the server.

sys.database_query_store_options (Transact-SQL)

sys.query_context_settings (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

sys.query_store_runtime_stats (Transact-SQL)

sys.query_store_wait_stats (Transact-SQL)

ﾉ

Expand table

1

1

1

Related content

sys.query_store_runtime_stats_interval (Transact-SQL)

Monitor performance by using the Query Store

System catalog views (Transact-SQL)

Query Store stored procedures (Transact-SQL)

sys.fn_stmt_sql_handle_from_sql_stmt (Transact-SQL)

Last updated on 11/18/2025

```sql
query_text_id
```

```sql
query_sql_text
```

```sql
statement_sql_handle
```

```sql
is_part_of_encrypted_module
```

```sql
has_restricted_text
```

```sql
0
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```
