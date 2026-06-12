---
name: "ASYNC_IO_COMPLETION"
title: "Async I/O Completion Wait"
category: "io"
severity: "medium"
description: "Occurs when a task waits for asynchronous I/O operations to complete. Covers a broad range of I/O operations including checkpoint writes, lazy writer, and backup reads."
tags: ["io","async","checkpoint"]
pubDate: "2026-05-29"
---

## Overview

Occurs when a task waits for asynchronous I/O operations to complete. Covers a broad range of I/O operations including checkpoint writes, lazy writer, and backup reads.

## Key Metrics

| Metric | Description |
| --------- | --------------------- |
| Wait Type | `ASYNC_IO_COMPLETION` |
| Category | Io |
| Severity | MEDIUM |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `ASYNC_IO_COMPLETION` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'ASYNC_IO_COMPLETION'
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
