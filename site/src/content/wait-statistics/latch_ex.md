---
name: "LATCH_EX"
title: "Exclusive Latch Wait"
category: "memory"
severity: "high"
description: "Occurs when waiting for an exclusive latch on an in-memory structure. Unlike PAGEIOLATCH, this is pure memory contention — no disk I/O involved. Typically indicates NUMA node contention or THREADPOOL-like pressure."
tags: ["latch","memory","contention"]
pubDate: 2026-05-29
relatedScripts: ["diagnose-latch-contention"]
---

## Overview

Occurs when waiting for an exclusive latch on an in-memory structure. Unlike PAGEIOLATCH, this is pure memory contention — no disk I/O involved. Typically indicates NUMA node contention or THREADPOOL-like pressure.

## Key Metrics

| Metric | Description |
| --------- | ----------- |
| Wait Type | `LATCH_EX` |
| Category | Memory |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `LATCH_EX` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'LATCH_EX'
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
