---
name: THREADPOOL
title: "Class THREADPOOL Wait"
category: triage
severity: critical
description: "Occurs when a task is waiting for an available worker thread. Indicates all worker threads are busy — typically from blocker chains, excessive parallel queries, or connection storms. A server-wide crisis signal."
tags: ["threads", "worker", "pool-exhaustion"]
pubDate: 2026-05-29
relatedScripts: ["diagnose-blocking-chains"]
---

## Overview

Occurs when a task is waiting for an available worker thread. Indicates all worker threads are busy — typically from blocker chains, excessive parallel queries, or connection storms. A server-wide crisis signal.

## Key Metrics

| Metric    | Description  |
| --------- | ------------ |
| Wait Type | `THREADPOOL` |
| Category  | Triage       |
| Severity  | CRITICAL     |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `THREADPOOL` waits:

```sql
SELECT TOP 10
    [Wait Type] = wait_type,
    [Wait Seconds] = wait_time_ms / 1000,
    [Wait Count] = waiting_tasks_count,
    [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'THREADPOOL'
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
