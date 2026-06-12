---
name: PAGEIOLATCH_UP
title: "Page I/O Latch (Update) Wait"
category: io
severity: medium
description: "Occurs when a task waits for a data page I/O operation with an update latch. Less common than SH/EX variants; indicates pages being read for update operations."
tags: ["io", "buffer-pool", "update", "page"]
pubDate: 2026-05-29
relatedScripts: ["analyze-io-latency"]
---

## Overview

Occurs when a task waits for a data page I/O operation with an update latch. Less common than SH/EX variants; indicates pages being read for update operations.

## Key Metrics

| Metric | Description |
| --------- | ---------------- |
| Wait Type | `PAGEIOLATCH_UP` |
| Category | Io |
| Severity | MEDIUM |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `PAGEIOLATCH_UP` waits:

```sql
SELECT TOP 10
 [Wait Type] = wait_type,
 [Wait Seconds] = wait_time_ms / 1000,
 [Wait Count] = waiting_tasks_count,
 [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'PAGEIOLATCH_UP'
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
