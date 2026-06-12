---
name: "CMEMTHREAD"
title: "Class CMEMTHREAD Wait"
category: "memory"
severity: "high"
description: "Occurs when waiting on a thread-safe memory allocation object. High values indicate memory object contention, often from frequent ad-hoc query compilations or parameterization inefficiencies."
tags: ["memory","thread","allocation","compile"]
pubDate: "2026-05-29"
relatedScripts: ["diagnose-memory-pressure"]
---

## Overview

Occurs when waiting on a thread-safe memory allocation object. High values indicate memory object contention, often from frequent ad-hoc query compilations or parameterization inefficiencies.

## Key Metrics

| Metric | Description |
| --------- | ------------ |
| Wait Type | `CMEMTHREAD` |
| Category | Memory |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `CMEMTHREAD` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'CMEMTHREAD'
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
