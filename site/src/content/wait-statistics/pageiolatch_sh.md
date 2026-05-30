---
name: PAGEIOLATCH_SH
title: "Page I/O Latch (Shared) Wait"
category: io
severity: high
description: "Occurs when a task waits for a data page to be read from disk into the buffer pool (shared latch). High durations indicate disk I/O subsystem latency — slow reads, insufficient IOPS, or missing indexes causing excessive page access."
tags: ["io", "buffer-pool", "disk-read", "page"]
pubDate: 2026-05-29
relatedScripts: ["analyze-io-latency"]
---

## Overview

Occurs when a task waits for a data page to be read from disk into the buffer pool (shared latch). High durations indicate disk I/O subsystem latency — slow reads, insufficient IOPS, or missing indexes causing excessive page access.

## Key Metrics

| Metric    | Description      |
| --------- | ---------------- |
| Wait Type | `PAGEIOLATCH_SH` |
| Category  | Io               |
| Severity  | HIGH             |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `PAGEIOLATCH_SH` waits:

```sql
SELECT TOP 10
    [Wait Type] = wait_type,
    [Wait Seconds] = wait_time_ms / 1000,
    [Wait Count] = waiting_tasks_count,
    [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'PAGEIOLATCH_SH'
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
