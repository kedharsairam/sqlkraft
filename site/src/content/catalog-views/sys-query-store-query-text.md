---
name: "sys.query_store_query_text"
title: "sys.query_store_query_text"
category: "query-store"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Contains the Transact-SQL text and the SQL handle of the query. SQL text of the query, as provided by the user. Includes whitespaces, hints, and comments. Comments and spaces before and after the query text are ignored. Comments and spaces inside text aren't ignored. SQL handle of the individual query. Query text is a part "
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: "is_part_of_encrypted_module"
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Contains the Transact-SQL text and the SQL handle of the query. SQL text of the query, as provided by the user. Includes whitespaces, hints, and comments. Comments and spaces before and after the query text are ignored. Comments and spaces inside text aren't ignored. SQL handle of the individual query. Query text is a part of an encrypted module.

## Syntax

```sql
is_part_of_encrypted_module
```

## Permissions

Applies to: SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics SQL database in Microsoft Fabric Contains the Transact-SQL text and the SQL handle of the query. Description Primary key. SQL text of the query, as provided by the user. Includes whitespaces, hints, and comments. Comments and spaces before and after the query text are ignored. Comments and spaces inside text aren't ignored. SQL handle of the individual query. Query text is a part of an encrypted module. Query text contains a password or other unmentionable words. Azure Synapse Analytics always returns zero ( ). SQL Server 2019 (15.x) and previous versions require permission on the server. SQL Server 2022 (16.x) and later versions require permission on the server. sys.database_query_store_options (Transact-SQL) sys.query_context_settings (Transact-SQL) sys.query_store_plan (Transact-SQL) sys.query_store_query (Transact-SQL) sys.query_store_runtime_stats (Transact-SQL) sys.query_store_wait_stats (Transact-SQL) ﾉ Expand table 1 1 1 Related content After you identify the query_id and plan_id that you want to force, use the following example to force the query to use a plan. SQL Use sys.query_store_plan_forcing_locations , joined with sys.query_store_replicas , to retrieve Query Store for readable secondaries . SQL sys.query_store_plan_forcing_locations (Transact-SQL) sys.query_store_replicas (Transact-SQL) sp_query_store_remove_plan (Transact-SQL) sp_query_store_remove_query (Transact-SQL) sp_query_store_unforce_plan (Transact-SQL) Query Store catalog views (Transact-SQL) Monitor performance by using the Query Store sp_query_store_reset_exec_stats (Transact-SQL) sp_query_store_flush_db (Transact-SQL) Best Practice with the Query Store Last updated on 04/23/2026 Related content
