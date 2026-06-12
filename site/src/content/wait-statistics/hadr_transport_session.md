---
name: HADR_TRANSPORT_SESSION
title: "HADR Transport Session Wait"
category: latency
severity: medium
description: "Occurs when waiting for the AG transport session to become available. Indicates network connectivity issues or AG communication bottlenecks between replicas."
tags: ["ag", "transport", "network"]
pubDate: 2026-05-29
relatedScripts: ["diagnose-ag-network"]
---

## Overview

Occurs when waiting for the AG transport session to become available. Indicates network connectivity issues or AG communication bottlenecks between replicas.

## Key Metrics

| Metric | Description |
| --------- | ------------------------ |
| Wait Type | `HADR_TRANSPORT_SESSION` |
| Category | Latency |
| Severity | MEDIUM |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `HADR_TRANSPORT_SESSION` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'HADR_TRANSPORT_SESSION'
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
