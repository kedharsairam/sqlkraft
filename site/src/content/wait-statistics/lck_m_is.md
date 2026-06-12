---
name: "LCK_M_IS"
title: "Intent Shared Lock Wait"
category: "blocking"
severity: "medium"
description: "Occurs when waiting for an intent shared (IS) lock. Typical in hierarchy locking scenarios where a table-level IS lock is blocked by an existing X or U lock on a child object."
tags: ["lock","intent-shared"]
pubDate: "2026-05-29"
relatedScripts: ["diagnose-lock-contention"]
---

## Overview

Occurs when waiting for an intent shared (IS) lock. Typical in hierarchy locking scenarios where a table-level IS lock is blocked by an existing X or U lock on a child object.

## Key Metrics

| Metric | Description |
| --------- | ----------- |
| Wait Type | `LCK_M_IS` |
| Category | Blocking |
| Severity | MEDIUM |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `LCK_M_IS` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'LCK_M_IS'
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
