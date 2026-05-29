---
name: 'sys.dm_fts_memory_buffers'
title: 'sys.dm_fts_memory_buffers'
category: 'full-text'
description: 'SQL database in Microsoft Fabric Returns information about memory buffers belonging to a specific memory pool that are used as part of a full-text crawl or a full-text crawl range. ID of the allocated memory pool. Address of the allocated memory buffer. Name of the shared memory buffer for which this allocation was Current state of memory buffer. Number of rows that this buffer is currently handli'
tags: ["full-text", "dmv"]
pubDate: 2026-05-29
syntax: |
  dm_fts_memory_buffers.pool_id
  dm_fts_memory_pools.pool_id
---

## Description

SQL database in Microsoft Fabric Returns information about memory buffers belonging to a specific memory pool that are used as part of a full-text crawl or a full-text crawl range. ID of the allocated memory pool. Address of the allocated memory buffer. Name of the shared memory buffer for which this allocation was Current state of memory buffer. Number of rows that this buffer is currently handling.

## Syntax

```sql
dm_fts_memory_buffers.pool_id
dm_fts_memory_pools.pool_id
```

## Permissions

SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns information about memory buffers belonging to a specific memory pool that are used as part of a full-text crawl or a full-text crawl range. ID of the allocated memory pool. 0 = Small buffers 1 = Large buffers Address of the allocated memory buffer. Name of the shared memory buffer for which this allocation was made. Current state of memory buffer. 0 = Free 1 = Busy Number of rows that this buffer is currently handling. Amount, in bytes, of memory in use in this buffer. Percentage of allocated memory used. On SQL Server and SQL Managed Instance, requires permission. ７ The following column will be removed in a future release of Microsoft SQL Server: . Avoid using this column in new development work, and plan to modify applications that currently use it. ﾉ
