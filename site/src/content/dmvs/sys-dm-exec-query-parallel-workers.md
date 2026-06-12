---
name: "sys.dm_exec_query_parallel_workers"
title: "sys.dm_exec_query_parallel_workers"
category: "execution"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Returns worker availability information per node. Number of schedulers on this node. Maximum number of workers for parallel queries. Number of workers reserved by parallel queries, plus number of main Number of workers available for tasks."
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Returns worker availability information per node. Number of schedulers on this node. Maximum number of workers for parallel queries. Number of workers reserved by parallel queries, plus number of main Number of workers available for tasks. every incoming request consumes at least 1 worker, which is subtracted from the free worker count.

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

2016 (13.x) and later versions Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns worker availability information per node. NUMA node ID. Number of schedulers on this node. Maximum number of workers for parallel queries. Number of workers reserved by parallel queries, plus number of main workers used by all requests. Number of workers available for tasks. every incoming request consumes at least 1 worker, which is subtracted from the free worker count. It is possible that the free worker count can be a negative number on a heavily loaded server. Number of workers used by parallel queries. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. Requires VIEW SERVER PERFORMANCE STATE permission on the server. ﾉ
