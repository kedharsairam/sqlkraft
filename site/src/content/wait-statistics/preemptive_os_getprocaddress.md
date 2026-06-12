---
name: "PREEMPTIVE_OS_GETPROCADDRESS"
title: "Preemptive OS GetProcAddress Wait"
category: "baseline"
severity: "info"
description: "Occurs during preemptive OS operations where SQL Server calls Windows API GetProcAddress to resolve DLL function addresses. Typically a startup or configuration operation."
tags: ["os","preemptive","api"]
pubDate: "2026-05-29"
---

## Overview

Occurs during preemptive OS operations where SQL Server calls Windows API GetProcAddress to resolve DLL function addresses. Typically a startup or configuration operation.

## Key Metrics

| Metric | Description |
| --------- | ------------------------------ |
| Wait Type | `PREEMPTIVE_OS_GETPROCADDRESS` |
| Category | Baseline |
| Severity | INFO |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `PREEMPTIVE_OS_GETPROCADDRESS` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'PREEMPTIVE_OS_GETPROCADDRESS'
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
