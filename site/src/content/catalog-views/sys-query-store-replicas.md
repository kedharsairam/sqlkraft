---
name: "sys.query_store_replicas"
title: "sys.query_store_replicas"
category: "query-store"
description: "Contains information about Query Store replicas, when Query Store for readable secondaries enabled. You can use this information to determine what Query Store to force or unforce a plan on a secondary replica with sys.sp_query_store_set_query_hints Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform"
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  ON
  qsr.replica_group_id = qsp.replica_group_id
  WHERE
  qsr.replica_name =
  'yourSecondaryReplicaName'
  ;
---

## Description

Contains information about Query Store replicas, when Query Store for readable secondaries enabled. You can use this information to determine what Query Store to force or unforce a plan on a secondary replica with sys.sp_query_store_set_query_hints Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform support, see

## Syntax

```sql
ON qsr.replica_group_id = qsp.replica_group_id
WHERE qsr.replica_name =
'yourSecondaryReplicaName'
;
```

## Permissions

Applies to: SQL Server 2025 (17.x) Azure SQL Database Contains information about Query Store replicas, when Query Store for readable secondaries is enabled. You can use this information to determine what to use when using Query Store to force or unforce a plan on a secondary replica with sys.sp_query_store_set_query_hints . Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform support, see Query Store for secondary replicas . Description Identifies the replica set number for this replica. 1=Primary 2=Secondary 3=Geo-Primary 4=Geo-Secondary 5 or greater=Named replica Instance name of the replica. for replicas in Azure SQL Managed Instance. This catalog view returns the same row data on all replicas. The catalog view contains a row per replica for every where it was observed. For example, a two-replica availability group initially contains two rows. After a failover, it contains four rows: one row for each replica in both the primary and secondary roles. Requires the permission. Query Store for readable secondaries ﾉ Expand table Related content sys.query_store_replicas (Transact-SQL) sys.sp_query_store_force_plan (Transact-SQL) sys.database_query_store_internal_state (Transact-SQL) sys.query_store_plan (Transact-SQL) sys.query_store_query (Transact-SQL) Monitoring Performance By Using the Query Store Best Practice with the Query Store Last updated on 11/18/2025 Related content sys.query_store_replicas (Transact-SQL) sys.query_store_plan_forcing_locations (Transact-SQL) Last updated on 11/18/2025 sys.query_store_replicas (Transact-SQL) sys.query_store_plan_forcing_locations (Transact-SQL) sp_query_store_force_plan (Transact-SQL) sp_query_store_remove_plan (Transact-SQL) sp_query_store_remove_query (Transact-SQL) sp_query_store_reset_exec_stats (Transact-SQL) sp_query_store_flush_db (Transact-SQL) Query Store catalog views (Transact-SQL) Monitor performance by using the Query Store Best Practice with the Query Store Last updated on 11/18/2025 Related content
