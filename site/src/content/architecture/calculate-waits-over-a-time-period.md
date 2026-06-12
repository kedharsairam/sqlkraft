---
title: "Calculate waits over a time period"
topic: "io-fundamentals"
description: "The following script calculates and returns latch waits over a time period."
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

The following script calculates and returns latch waits over a time period.

```sql
-- WAITING TASKS ordered by wait_duration_ms
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
BY wt.wait_duration_ms
DESC
;
```

```sql
/* Snapshot the current wait stats and store so that this can be compared over a time period
Return the statistics between this point in time and the last collection point in time.
**This data is maintained in tempdb so the connection must persist between each execution**
**alternatively this could be modified to use a persisted table in tempdb. if that is changed code should be included to clean up the table at some point.**
*/
USE tempdb;
GO
DECLARE
@current_snap_time
AS
DATETIME;
DECLARE
@previous_snap_time
AS
DATETIME;
SET
@current_snap_time =
GETDATE ();
IF NOT EXISTS (
SELECT name
FROM tempdb.sys.sysobjects
WHERE name
LIKE
'#_wait_stats%'
)
CREATE
TABLE
#_wait_stats (
wait_type
VARCHAR (128),
waiting_tasks_count
BIGINT
,
wait_time_ms
BIGINT
,
avg_wait_time_ms
INT
,
```

```sql
max_wait_time_ms
BIGINT
,
signal_wait_time_ms
BIGINT
,
avg_signal_wait_time
INT
,
snap_time DATETIME
);
INSERT
INTO
#_wait_stats (wait_type, waiting_tasks_count, wait_time_ms,
max_wait_time_ms, signal_wait_time_ms, snap_time)
SELECT wait_type,
waiting_tasks_count,
wait_time_ms,
max_wait_time_ms,
signal_wait_time_ms,
getdate ()
FROM sys.dm_os_wait_stats;
--get the previous collection point
SELECT
TOP 1 @previous_snap_time = snap_time
FROM
#_wait_stats
WHERE snap_time < (
SELECT
MAX (snap_time)
FROM
#_wait_stats)
ORDER
BY snap_time
DESC
;
--get delta in the wait stats
SELECT
TOP 10 s.wait_type,
(e.waiting_tasks_count - s.waiting_tasks_count)
AS
[waiting_tasks_count],
(e.wait_time_ms - s.wait_time_ms)
AS
[wait_time_ms],
(e.wait_time_ms - s.wait_time_ms) / ((e.waiting_tasks_count -
s.waiting_tasks_count))
AS
[avg_wait_time_ms],
(e.max_wait_time_ms)
AS
[max_wait_time_ms],
(e.signal_wait_time_ms - s.signal_wait_time_ms)
AS
[signal_wait_time_ms],
(e.signal_wait_time_ms - s.signal_wait_time_ms) /
((e.waiting_tasks_count - s.waiting_tasks_count))
AS
[avg_signal_time_ms],
s.snap_time
AS
[start_time],
e.snap_time
AS
[end_time],
DATEDIFF (ss, s.snap_time, e.snap_time)
AS
[seconds_in_sample]
FROM
#_wait_stats
AS e
INNER
JOIN (
SELECT
*
FROM
#_wait_stats
WHERE snap_time = @previous_snap_time)
AS s
ON (s.wait_type = e.wait_type)
WHERE e.snap_time = @current_snap_time
AND s.snap_time = @previous_snap_time
AND e.wait_time_ms > 0
AND (e.waiting_tasks_count - s.waiting_tasks_count) > 0
AND e.wait_type
NOT
IN (
'LAZYWRITER_SLEEP'
,
'SQLTRACE_BUFFER_FLUSH'
,
'SOS_SCHEDULER_YIELD'
,
'DBMIRRORING_CMD'
,
'BROKER_TASK_STOP'
,
'CLR_AUTO_EVENT'
,
'BROKER_RECEIVE_WAITFOR'
,
'WAITFOR'
,
'SLEEP_TASK'
,
'REQUEST_FOR_DEADLOCK_SEARCH'
,
'XE_TIMER_EVENT'
,
'FT_IFTS_SCHEDULER_IDLE_WAIT'
,
'BROKER_TO_FLUSH'
,
'XE_DISPATCHER_WAIT'
,
```
