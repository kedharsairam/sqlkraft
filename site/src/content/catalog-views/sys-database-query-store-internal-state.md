---
name: "sys.database_query_store_internal_state"
title: "sys.database_query_store_internal_state"
category: "query-store"
description: "2025 (17.x) Azure SQL Database Contains information about queue length and memory usage for the Query Store when the Query Store for secondary replicas is enabled. Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database."
tags: ["query-store","catalog-view"]
pubDate: 2026-05-29
syntax: "pending_message_count"
---

## Description

2025 (17.x) Azure SQL Database Contains information about queue length and memory usage for the Query Store when the Query Store for secondary replicas is enabled. Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform support, see Query Store for secondary replicas The number of messages waiting in the queue on the primary for the replica where the system view is being viewed from. Not The amount of memory in total taken up by the messages in the queue. Not nullable. For information on configured replicas for Query Store, see sys.query_store_replicas (Transact- Learn more about Query Store and related concepts in the following articles: Monitor performance by using the Query Store Query Store for secondary replicas sys.database_query_store_internal_state (Transact-SQL) sys.query_store_replicas (Transact-SQL)

## Syntax

`pending_message_count`

## Remarks

2025 (17.x)

Contains information about queue length and memory usage for the Query Store when the

Query Store for secondary replicas is enabled.

Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later

versions, and in Azure SQL Database. For complete platform support, see

Query Store for

secondary replicas

Description

The number of messages waiting in the queue on the primary for

the replica where the system view is being viewed from. Not

The amount of memory in total taken up by the messages in the

queue. Not nullable.

Requires the

permission.

For information on configured replicas for Query Store, see

sys.query_store_replicas (Transact-

Learn more about Query Store and related concepts in the following articles:

Monitor performance by using the Query Store

Query Store for secondary replicas

sp_query_store_clear_message_queues (Transact-SQL)

sys.query_store_wait_stats (Transact-SQL)

sys.query_store_runtime_stats (Transact-SQL)

Expand table

sys.database_query_store_internal_state (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

Monitor performance by using the Query Store

Best practices for monitoring workloads with Query Store

sys.query_store_replicas (Transact-SQL)

sys.sp_query_store_force_plan (Transact-SQL)

sys.database_query_store_internal_state (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

Monitoring Performance By Using the Query Store

Best Practice with the Query Store
