---
name: ASYNC_NETWORK_IO
title: "Async Network I/O Wait"
category: latency
severity: medium
description: "Occurs when the task is waiting for the network to send data to the client. High values often indicate the client application is not consuming results fast enough — the classic 'slow client' signal."
tags: ["network", "client", "result-set"]
pubDate: 2026-05-29
relatedScripts: ["diagnose-slow-client"]
---

## Overview

Occurs when the task is waiting for the network to send data to the client. High values often indicate the client application is not consuming results fast enough — the classic 'slow client' signal.

## Key Metrics

| Metric    | Description        |
| --------- | ------------------ |
| Wait Type | `ASYNC_NETWORK_IO` |
| Category  | Latency            |
| Severity  | MEDIUM             |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `ASYNC_NETWORK_IO` waits:

```sql
SELECT TOP 10
    [Wait Type] = wait_type,
    [Wait Seconds] = wait_time_ms / 1000,
    [Wait Count] = waiting_tasks_count,
    [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'ASYNC_NETWORK_IO'
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
