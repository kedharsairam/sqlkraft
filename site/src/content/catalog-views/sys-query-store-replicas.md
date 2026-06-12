---
name: "sys.query_store_replicas"
title: "sys.query_store_replicas"
category: "query-store"
description: "Contains information about Query Store replicas, when Query Store for readable secondaries enabled. You can use this information to determine what Query Store to force or unforce a plan on a secondary replica with sys.sp_query_store_set_query_hints Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform"
tags: ["query-store","catalog-view"]
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

Contains information about Query Store replicas, when Query Store for readable secondaries enabled. You can use this information to determine what Query Store to force or unforce a plan on a secondary replica with sys.sp_query_store_set_query_hints Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database.

## Syntax

```sql
ON qsr.replica_group_id = qsp.replica_group_id
WHERE qsr.replica_name =
'yourSecondaryReplicaName'
;
```

## Permissions
