---
name: EXECSYNC
title: "Class EXECSYNC Wait"
category: baseline
severity: low
description: "Occurs during parallel query synchronization phases such as exchange iterator completion and batching. Normal part of parallel execution and rarely actionable by itself."
tags: ["parallelism", "synchronization"]
pubDate: 2026-05-29
---

## Overview

Occurs during parallel query synchronization phases such as exchange iterator completion and batching. Normal part of parallel execution and rarely actionable by itself.

## Key Metrics

| Metric    | Description |
| --------- | ----------- |
| Wait Type | `EXECSYNC`  |
| Category  | Baseline    |
| Severity  | LOW         |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `EXECSYNC` waits:

```sql
SELECT TOP 10
    [Wait Type] = wait_type,
    [Wait Seconds] = wait_time_ms / 1000,
    [Wait Count] = waiting_tasks_count,
    [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'EXECSYNC'
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
