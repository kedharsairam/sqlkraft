---
name: 'sys.query_store_runtime_stats_interval'
title: 'sys.query_store_runtime_stats_interval'
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

Contains information about the start and end time of each interval over which runtime

execution statistics information for a query has been collected.


## Description
Primary key.

Start time of the interval.

End time of the interval.

Always NULL.

Requires the

permission.

sys.database_query_store_options (Transact-SQL)

sys.query_context_settings (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

sys.query_store_query_text (Transact-SQL)

sys.query_store_runtime_stats (Transact-SQL)

sys.query_store_wait_stats (Transact-SQL)

Monitoring Performance By Using the Query Store

Catalog Views (Transact-SQL)

Query Store Stored Procedures (Transact-SQL)

Last updated on 11/18/2025

ﾉ

Expand table

See Also
