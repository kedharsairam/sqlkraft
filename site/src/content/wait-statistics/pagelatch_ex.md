---
name: "PAGELATCH_EX"
title: "Page Latch (Exclusive) Wait"
category: "memory"
severity: "high"
description: "Occurs when waiting for an exclusive latch on a buffer pool page already in memory — no I/O is involved. Classic symptom of page-level contention, often on the last page of indexes (PAGELATCH_UP + allocation contention)."
tags: ["latch","page","contention","allocation"]
pubDate: 2026-05-29
relatedScripts: ["diagnose-page-latch-contention"]
---

## Overview

Occurs when waiting for an exclusive latch on a buffer pool page already in memory — no I/O is involved. Classic symptom of page-level contention, often on the last page of indexes (PAGELATCH_UP + allocation contention).

## Key Metrics

| Metric | Description |
| --------- | -------------- |
| Wait Type | `PAGELATCH_EX` |
| Category | Memory |
| Severity | HIGH |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `PAGELATCH_EX` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'PAGELATCH_EX'
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
