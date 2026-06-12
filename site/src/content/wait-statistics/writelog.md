---
name: WRITELOG
title: "Write Log Wait"
category: io
severity: high
description: "Occurs when waiting for the transaction log to be flushed to disk. One of the most important I/O signals. High WRITELOG indicates log drive latency, excessive transactions, or insufficient log throughput."
tags: ["io", "log", "transaction", "flush"]
pubDate: 2026-05-29
relatedScripts: ["analyze-log-throughput"]
---

## Overview

Occurs when waiting for the transaction log to be flushed to disk. One of the most important I/O signals. High WRITELOG indicates log drive latency, excessive transactions, or insufficient log throughput.

## Key Metrics

| Metric | Description |
| --------- | ----------- |
| Wait Type | `WRITELOG` |
| Category | Io |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `WRITELOG` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'WRITELOG'
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
