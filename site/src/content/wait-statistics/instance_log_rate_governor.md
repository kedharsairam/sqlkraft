---
name: "INSTANCE_LOG_RATE_GOVERNOR"
title: "Instance Log Rate Governor Wait"
category: "triage"
severity: "high"
description: "Occurs when the instance-level log rate governor throttles log generation. Azure SQL DB only. Indicates the log generation rate exceeds the service tier's maximum log rate."
tags: ["log","governor","throttle","azure"]
pubDate: 2026-05-29
---

## Overview

Occurs when the instance-level log rate governor throttles log generation. Azure SQL DB only. Indicates the log generation rate exceeds the service tier's maximum log rate.

## Key Metrics

| Metric | Description |
| --------- | ---------------------------- |
| Wait Type | `INSTANCE_LOG_RATE_GOVERNOR` |
| Category | Triage |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `INSTANCE_LOG_RATE_GOVERNOR` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'INSTANCE_LOG_RATE_GOVERNOR'
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
