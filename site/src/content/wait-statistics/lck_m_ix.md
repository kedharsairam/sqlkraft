---
name: "LCK_M_IX"
title: "Intent Exclusive Lock Wait"
category: "blocking"
severity: "high"
description: "Occurs when waiting for an intent exclusive (IX) lock. Frequently observed during DML operations (INSERT/UPDATE/DELETE) on pages blocked by other transactions holding incompatible locks."
tags: ["lock","intent-exclusive","dml"]
pubDate: "2026-05-29"
relatedScripts: ["diagnose-blocking-chains"]
---

## Overview

Occurs when waiting for an intent exclusive (IX) lock. Frequently observed during DML operations (INSERT/UPDATE/DELETE) on pages blocked by other transactions holding incompatible locks.

## Key Metrics

| Metric | Description |
| --------- | ----------- |
| Wait Type | `LCK_M_IX` |
| Category | Blocking |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `LCK_M_IX` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'LCK_M_IX'
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
