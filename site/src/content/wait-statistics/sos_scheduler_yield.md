---
name: "SOS_SCHEDULER_YIELD"
title: "Class SOS_SCHEDULER_YIELD Wait"
category: "scheduling"
severity: "medium"
description: "Occurs when a task voluntarily yields the scheduler for other tasks to execute. High counts indicate CPU pressure or inefficient query plans that refuse to yield. Normal under healthy CPU load."
tags: ["scheduler","cpu","yield"]
pubDate: 2026-05-29
relatedScripts: ["monitor-cpu-pressure"]
---

## Overview

Occurs when a task voluntarily yields the scheduler for other tasks to execute. High counts indicate CPU pressure or inefficient query plans that refuse to yield. Normal under healthy CPU load.

## Key Metrics

| Metric | Description |
| --------- | --------------------- |
| Wait Type | `SOS_SCHEDULER_YIELD` |
| Category | Scheduling |
| Severity | MEDIUM |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `SOS_SCHEDULER_YIELD` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'SOS_SCHEDULER_YIELD'
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
