---
name: LCK_M_SCH_M
title: "Schema Modification Lock Wait"
category: blocking
severity: high
description: "Occurs when waiting for a schema modification (Sch-M) lock. Blocks nearly everything. Typically from DDL operations (ALTER TABLE, CREATE INDEX) running concurrently with active queries."
tags: ["lock", "schema-modification", "ddl"]
pubDate: 2026-05-29
relatedScripts: ["monitor-ddl-blocking"]
---

## Overview

Occurs when waiting for a schema modification (Sch-M) lock. Blocks nearly everything. Typically from DDL operations (ALTER TABLE, CREATE INDEX) running concurrently with active queries.

## Key Metrics

| Metric    | Description   |
| --------- | ------------- |
| Wait Type | `LCK_M_SCH_M` |
| Category  | Blocking      |
| Severity  | HIGH          |

## Troubleshooting

### 1. Identify the source

Use the following query to identify the top queries contributing to `LCK_M_SCH_M` waits:

```sql
SELECT TOP 10
    [Wait Type] = wait_type,
    [Wait Seconds] = wait_time_ms / 1000,
    [Wait Count] = waiting_tasks_count,
    [Avg Wait Ms] = wait_time_ms / NULLIF(waiting_tasks_count, 0)
FROM sys.dm_os_wait_stats
WHERE wait_type = 'LCK_M_SCH_M'
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
