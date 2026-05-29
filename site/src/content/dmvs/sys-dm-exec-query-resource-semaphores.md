---
name: 'sys.dm_exec_query_resource_semaphores'
title: 'sys.dm_exec_query_resource_semaphores'
category: 'execution'
description: 'Analytics Platform System (PDW) Returns the information about the current query-resource semaphore status in SQL Server. provides general query-execution memory status and allows you to determine whether the system can access enough memory. This view complements memory information obtained from complete picture of server memory status. one row for the regular resource semaphore and another row for'
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: 'sys.dm_pdw_nodes_exec_query_resource_semaphores'
---

## Description

Analytics Platform System (PDW) Returns the information about the current query-resource semaphore status in SQL Server. provides general query-execution memory status and allows you to determine whether the system can access enough memory. This view complements memory information obtained from complete picture of server memory status. one row for the regular resource semaphore and another row for the small-query resource

## Syntax

```sql
sys.dm_pdw_nodes_exec_query_resource_semaphores
```

## Examples

### Example 1

```sql
ORDER BY
```

### Example 2

```sql
sys.dm_exec_query_resource_semaphores
```

### Example 3

```sql
sys.dm_os_memory_clerks
```

### Example 4

```sql
type
= 'MEMORYCLERK_SQLQERESERVATIONS'
```

### Example 5

```sql
sys.dm_exec_query_memory_grants
```

### Example 6

```sql
--Find all queries waiting in the memory queue
SELECT
*
FROM
sys.dm_exec_query_memory_grants
WHERE
grant_time
IS
NULL
;
```

### Example 7

```sql
-- retrieve every query plan from the plan cache
USE
master
;
GO
SELECT
*
FROM
sys.dm_exec_cached_plans cp
CROSS
APPLY
sys.dm_exec_query_plan(cp.plan_handle);
GO
```
