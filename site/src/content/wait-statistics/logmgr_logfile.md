---
name: "LOGMGR_LOGFILE"
title: "Log Manager Log File Wait"
category: "io"
severity: "medium"
description: "Occurs when waiting for log file space — either waiting for log growth to complete or waiting for VLFs to be truncated. High values indicate oversized VLFs or slow log backups."
tags: ["io","log","vlf","backup"]
pubDate: 2026-05-29
relatedScripts: ["monitor-log-file-space"]
---

## Overview

Occurs when waiting for log file space — either waiting for log growth to complete or waiting for VLFs to be truncated. High values indicate oversized VLFs or slow log backups.

## Key Metrics

| Metric | Description |
| --------- | ---------------- |
| Wait Type | `LOGMGR_LOGFILE` |
| Category | Io |
| Severity | MEDIUM |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `LOGMGR_LOGFILE` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'LOGMGR_LOGFILE'
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
