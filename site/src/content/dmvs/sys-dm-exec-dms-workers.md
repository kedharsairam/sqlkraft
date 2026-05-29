---
name: "sys.dm_exec_dms_workers"
title: "sys.dm_exec_dms_workers"
category: "execution"
description: "SQL Server 2016 (13.x) and later versions Holds information about all workers completing DMS steps. This view shows the data for the last 1000 requests and active requests; active requests always have the data present in this view. sys.dm_exec_distributed_request_steps sys.dm_exec_dms_workers (Transact-SQL) sys.dm_exec_compute_nodes (Transact- 'DIRECT_CONVERTER', 'DIRECT_READER', 'FILE_READER', 'H"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
---

## Description

SQL Server 2016 (13.x) and later versions Holds information about all workers completing DMS steps. This view shows the data for the last 1000 requests and active requests; active requests always have the data present in this view. sys.dm_exec_distributed_request_steps sys.dm_exec_dms_workers (Transact-SQL) sys.dm_exec_compute_nodes (Transact- 'DIRECT_CONVERTER', 'DIRECT_READER', 'FILE_READER', 'HASH_CONVERTER',

## Code Blocks

```sql
nvarchar(32)
```

```sql
int
```
