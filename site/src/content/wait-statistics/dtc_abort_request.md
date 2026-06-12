---
name: "DTC_ABORT_REQUEST"
title: "DTC Abort Request Wait"
category: "blocking"
severity: "high"
description: "Occurs when waiting for a DTC abort operation. Indicates distributed transactions that are failing to abort cleanly, often leading to lingering transactions."
tags: ["dtc","abort","distributed"]
pubDate: "2026-05-29"
---

## Overview

Occurs when waiting for a DTC abort operation. Indicates distributed transactions that are failing to abort cleanly, often leading to lingering transactions.

## Key Metrics

| Metric | Description |
| --------- | ------------------- |
| Wait Type | `DTC_ABORT_REQUEST` |
| Category | Blocking |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `DTC_ABORT_REQUEST` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'DTC_ABORT_REQUEST'
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
