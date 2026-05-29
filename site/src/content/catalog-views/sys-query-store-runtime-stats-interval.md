---
name: 'sys.query_store_runtime_stats_interval'
title: 'sys.query_store_runtime_stats_interval'
category: 'query-store'
description: 'SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the start and end time of each interval over which runtime execution statistics information for a query has been collected. sys.database_query_store_options (Transact-SQL) sys.query_context_settings (Transact-SQL) sys.query_store_plan (Transact-SQL) sys.query_store_query (Transact-SQL) sys.query_s'
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  LEFT
  JOIN
  sys.query_store_runtime_stats qsrs
  ON
  qspl.plan_id = qsrs.plan_id
  LEFT
  JOIN
  sys.query_store_runtime_stats_interval qsrsi
  ON
  qsrs.runtime_stats_interval_id = qsrsi.runtime_stats_interval_id
  WHERE
  qspl.plan_type = 1
  or
  qspl.plan_type = 2
  ORDER
  BY
  qspl.query_id, qsrs.last_execution_time;
  GO
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the start and end time of each interval over which runtime execution statistics information for a query has been collected. sys.database_query_store_options (Transact-SQL) sys.query_context_settings (Transact-SQL) sys.query_store_plan (Transact-SQL) sys.query_store_query (Transact-SQL) sys.query_store_query_text (Transact-SQL)

## Syntax

```sql
LEFT
JOIN
sys.query_store_runtime_stats qsrs
ON
qspl.plan_id = qsrs.plan_id
LEFT
JOIN
sys.query_store_runtime_stats_interval qsrsi
ON
qsrs.runtime_stats_interval_id = qsrsi.runtime_stats_interval_id
WHERE
qspl.plan_type = 1
or
qspl.plan_type = 2
ORDER
BY
qspl.query_id, qsrs.last_execution_time;
GO
```

## Permissions

Applies to: SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics SQL database in Microsoft Fabric Contains information about the start and end time of each interval over which runtime execution statistics information for a query has been collected. Description Primary key. Start time of the interval. End time of the interval. Always NULL. Requires the permission. sys.database_query_store_options (Transact-SQL) sys.query_context_settings (Transact-SQL) sys.query_store_plan (Transact-SQL) sys.query_store_query (Transact-SQL) sys.query_store_query_text (Transact-SQL) sys.query_store_runtime_stats (Transact-SQL) sys.query_store_wait_stats (Transact-SQL) Monitoring Performance By Using the Query Store Catalog Views (Transact-SQL) Query Store Stored Procedures (Transact-SQL) Last updated on 11/18/2025 ﾉ Expand table See Also sys.query_store_plan (Transact-SQL) sys.query_store_query (Transact-SQL) sys.query_store_runtime_stats (Transact-SQL) sys.query_store_wait_stats (Transact-SQL) sys.query_store_runtime_stats_interval (Transact-SQL) Monitoring Performance By Using the Query Store Catalog Views (Transact-SQL) Query Store Stored Procedures (Transact-SQL) Last updated on 11/18/2025 See Also sys.query_store_runtime_stats_interval (Transact-SQL) Monitor performance by using the Query Store System catalog views (Transact-SQL) Query Store stored procedures (Transact-SQL) sys.fn_stmt_sql_handle_from_sql_stmt (Transact-SQL) Last updated on 11/18/2025
