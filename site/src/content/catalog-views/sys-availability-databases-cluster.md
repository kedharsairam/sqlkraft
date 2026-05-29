---
name: 'sys.availability_databases_cluster'
title: 'sys.availability_databases_cluster'
category: 'databases-files'
description: 'Returns one row for each availability database on the instance of SQL Server that hosts an availability replica for any Always On availability group in the Windows Server Failover Clustering (WSFC) cluster, regardless of whether the local copy database has been joined to the Unique identifier of the availability group in which the database NULL = database isn''t part of an availability replica in a'
tags: ["databases-files", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns one row for each availability database on the instance of SQL Server that hosts an availability replica for any Always On availability group in the Windows Server Failover Clustering (WSFC) cluster, regardless of whether the local copy database has been joined to the Unique identifier of the availability group in which the database NULL = database isn't part of an availability replica in an

## Permissions

SQL) ﾃ Summarize this article for me Applies to: SQL Server Returns one row for each availability database on the instance of SQL Server that hosts an availability replica for any Always On availability group in the Windows Server Failover Clustering (WSFC) cluster, regardless of whether the local copy database has been joined to the availability group yet. Description Unique identifier of the availability group in which the database is participating. NULL = database isn't part of an availability replica in an availability group. Unique identifier of the database within the availability group, if any, in which the database is participating. is the same for this database on the primary replica and on every secondary replica on which the database has been joined to the availability group. NULL = database isn't part of an availability replica in any availability group. Name of the database that was added to the availability group. If the caller of isn't the owner of the database, the minimum permissions required to see the corresponding row are ALTER ANY DATABASE or VIEW ANY ７ Note When a database is added to an availability group, the primary database is automatically joined to the group. Secondary databases must be prepared on each secondary replica before they can be joined to the availability group. ﾉ Expand table

## Code Blocks


```sql
group_id
```


```sql
group_database_id
```


```sql
database_name
```
