---
name: "RESOURCE_SEMAPHORE_QUERY_COMPILE"
title: "Query Compile Resource Semaphore Wait"
category: "triage"
severity: "high"
description: "Occurs when waiting for memory to compile queries. High values indicate the compile memory lock is contended, often from a high rate of ad-hoc query compilations or plan cache churn."
tags: ["memory","compile","plan-cache"]
pubDate: "2026-05-29"
relatedScripts: ["diagnose-plan-cache-churn"]
---

## Overview

Occurs when waiting for memory to compile queries. High values indicate the compile memory lock is contended, often from a high rate of ad-hoc query compilations or plan cache churn.

## Key Metrics

| Metric | Description |
| --------- | ---------------------------------- |
| Wait Type | `RESOURCE_SEMAPHORE_QUERY_COMPILE` |
| Category | Triage |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `RESOURCE_SEMAPHORE_QUERY_COMPILE` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'RESOURCE_SEMAPHORE_QUERY_COMPILE'
ORDER BY wait_time_ms DESC;
```

### 2. Related diagnostics

- Review overall wait statistics using `sys.dm_os_wait_stats`
- Check session-level waits via `sys.dm_exec_session_wait_stats`
- Correlate with `sys.dm_exec_requests` for blocking analysis

## See Also

- [sys.dm_os_wait_stats (Transact-SQL)](/sqlkraft/dmvs/sys-dm-os-wait-stats/)
- [sys.dm_exec_session_wait_stats (Transact-SQL)](/sqlkraft/dmvs/sys-dm-exec-session-wait-stats/)
- [sys.dm_os_waiting_tasks (Transact-SQL)](/sqlkraft/dmvs/sys-dm-os-waiting-tasks/)
