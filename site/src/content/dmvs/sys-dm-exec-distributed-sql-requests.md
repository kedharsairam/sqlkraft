---
name: 'sys.dm_exec_distributed_sql_requests'
title: 'sys.dm_exec_distributed_sql_requests'
category: 'execution'
description: 'SQL Server 2016 (13.x) and later Holds information about all SQL query distributions as part of a SQL step in the query. This view shows the data for the last 1000 requests; active requests always have the data present in sys.dm_exec_requests (Transact- sys.dm_exec_distributed_request_steps sys.dm_exec_compute_nodes (Transact-SQL) Set to -1 for requests that run at the node scope not the distribut'
tags: ["execution", "dmv"]
pubDate: 2026-05-29
---

## Description

SQL Server 2016 (13.x) and later Holds information about all SQL query distributions as part of a SQL step in the query. This view shows the data for the last 1000 requests; active requests always have the data present in sys.dm_exec_requests (Transact- sys.dm_exec_distributed_request_steps sys.dm_exec_compute_nodes (Transact-SQL) Set to -1 for requests that run at the node scope not the distribution scope.
