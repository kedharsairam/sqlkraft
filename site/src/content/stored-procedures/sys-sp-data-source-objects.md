---
name: 'sys.sp_data_source_objects'
title: 'sys.sp_data_source_objects'
category: 'general'
description: 'SQL Server 2019 (15.x)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

If you

enable Query Store for secondary replicas

,

can only be

executed against the primary replica. The procedure's scope applies to the entire replica set.

Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later

versions, and in Azure SQL Database. For complete platform support, see

Query Store for

secondary replicas

.

The following example returns information about the queries in the Query Store.

SQL

After you identify the

plan_id

that you want to clear the statistics, use the following example to

delete the execution stats for a specific query plan. This example deletes the execution stats for

plan number 3.

SQL

sp_query_store_force_plan (Transact-SQL)

sp_query_store_remove_query (Transact-SQL)

sp_query_store_unforce_plan (Transact-SQL)

sp_query_store_remove_plan (Transact-SQL)

sp_query_store_flush_db (Transact-SQL)

Query Store catalog views (Transact-SQL)

Monitor performance by using the Query Store

Last updated on 11/18/2025

Related content

```sql
sp_query_store_reset_exec_stats
```

```sql
SELECT
txt.query_text_id,
txt.query_sql_text,
pl.plan_id,
qry.*
FROM
sys.query_store_plan
AS
pl
INNER
JOIN
sys.query_store_query
AS
qry
ON
pl.query_id = qry.query_id
INNER
JOIN
sys.query_store_query_text
AS
txt
ON
qry.query_text_id = txt.query_text_id;
EXECUTE
sp_query_store_reset_exec_stats 3;
```
