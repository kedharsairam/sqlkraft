---
name: CXPACKET
title: "Class CXPACKET Wait"
category: top-consumer
severity: high
description: "Occurs when waiting for parallel query execution to complete. Caused by skewed parallelism, exchange buffers filling up, or uneven row distribution across threads. The most commonly observed high-signal wait type."
tags: ["parallelism", "cpu", "skew"]
pubDate: 2026-05-29
relatedScripts: ["diagnose-parallelism-skew"]
---

## Overview

Occurs when waiting for parallel query execution to complete. Caused by skewed parallelism, exchange buffers filling up, or uneven row distribution across threads. The most commonly observed high-signal wait type.

## Key Metrics

| Metric    | Description  |
| --------- | ------------ |
| Wait Type | `CXPACKET`   |
| Category  | Top Consumer |
| Severity  | HIGH         |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `CXPACKET` waits:

```sql
SELECT TOP 10
    [Wait Type] = wait_type,
    [Wait Seconds] = wait_time_ms / 1000,
    [Wait Count] = waiting_tasks_count,
    [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'CXPACKET'
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
