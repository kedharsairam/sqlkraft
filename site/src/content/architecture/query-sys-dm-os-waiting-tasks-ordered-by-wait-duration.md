---
title: "Query sys.dm_os_waiting_tasks ordered by wait duration"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

This section contains scripts that can be used to help diagnose and troubleshoot latch

contention issues.

The following sample script queries

, and returns latch waits ordered

by session ID:

The following sample script queries

, and returns latch waits ordered

by wait duration:

Employing this strategy can cause a large number of waits on the

latch type because this strategy can lead to a large

number of page splits occurring in the non-leaf levels of the B-tree. If this occurs, SQL

Server must acquire shared (

) latches at all levels followed by exclusive (

) latches on

pages in the B-tree where a page split is possible. Check the

DMV

for a high number of waits on the

latch type after

padding rows.

`sys.dm_os_waiting_tasks`

`sys.dm_os_waiting_tasks`

`ACCESS_METHODS_HOBT_VIRTUAL_ROOT`

`SH`

`EX`

`sys.dm_os_latch_stats`

`ACCESS_METHODS_HOBT_VIRTUAL_ROOT`

```sql
-- WAITING TASKS ordered by session_id
SELECT wt.session_id,
wt.wait_type,
er.last_wait_type
AS last_wait_type,
wt.wait_duration_ms,
wt.blocking_session_id,
wt.blocking_exec_context_id,
resource_description
FROM sys.dm_os_waiting_tasks
AS wt
INNER
JOIN sys.dm_exec_sessions
AS es
ON wt.session_id = es.session_id
INNER
JOIN sys.dm_exec_requests
AS er
ON wt.session_id = er.session_id
WHERE es.is_user_process = 1
AND wt.wait_type <>
'SLEEP_TASK'
ORDER
BY session_id;
```
