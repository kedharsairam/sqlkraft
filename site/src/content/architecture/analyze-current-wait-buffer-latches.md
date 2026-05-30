---
title: "Analyze current wait buffer latches"
topic: "memory-management"
description: "A similar command can be run to clear the"
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

For a

only, clear the

DMV with the

following command:

SQL

A similar command can be run to clear the

DMV:

SQL

: This was illustrated in

Example of Latch Contention

.

: If the CPU utilization

on the system doesn't increase as concurrency driven by application throughput

increases, this is an indicator that SQL Server is waiting on something and symptomatic of

latch contention.

Analyze root cause. Even if each of the preceding conditions is true it's still possible that the

root cause of the performance issues lies elsewhere. In fact, in most cases suboptimal CPU

utilization is caused by other types of waits such as blocking on locks, I/O related waits or

network-related issues. As a rule of thumb it's always best to resolve the resource wait that

represents the greatest proportion of overall wait time before proceeding with more in-depth

analysis.

７

Note

Relative wait time for each wait type isn't included in the

DMV

because this DMW measures wait times since the last time that the instance of SQL

Server was started or the cumulative wait statistics were reset using

. To

calculate the relative wait time for each wait type take a snapshot of

before peak load, after peak load, and then calculate the

difference. The sample script

can be used for

this purpose.

Buffer latch contention manifests as an increase in wait times for latches with a

of

either

or

as displayed in the

DMV. To look at

the system in real-time run the following query on a system to join the

,

and

DMVs. The results can be used to determine

the current wait type for sessions executing on the server.

SQL

The statistics exposed by this query are described as follows:

## Description

ID of the session associated with the task.

The type of wait that SQL Server has recorded in the engine, which is

preventing a current request from being executed.

If this request has previously been blocked, this column returns the type of

the last wait. Isn't nullable.

The total wait time in milliseconds spent waiting on this wait type since SQL

Server instance was started or since cumulative wait statistics were reset.

ID of the session that is blocking the request.

ID of the execution context associated with the task.

The

column lists the exact page being waited for in

the format:

ﾉ

Expand table

The following query returns information for all non-buffer latches:

SQL

The statistics exposed by this query are described as follows:

## Description

The type of latch that SQL Server has recorded in the engine, which is

preventing a current request from being executed.

Number of waits on latches in this class since SQL Server restarted. This

counter is incremented at the start of a latch wait.

The total wait time in milliseconds spent waiting on this latch type.

Maximum time in milliseconds any request spent waiting on this latch type.

The values returned by this DMV are cumulative since last time the database engine was

restarted or the DMV was reset. Use the

column in

sys.dm_os_sys_info

to

find the last database engine startup time. On a system that has been running a long time this



ﾉ

Expand table

```sql
sys.dm_os_wait_stats
```

```sql
sys.dm_os_latch_stats
```

```sql
sys.dm_os_wait_stats
```

```sql
DBCC SQLPERF
```

```sql
sys.dm_os_wait_stats
```

```sql
DBCC SQLPERF ('sys.dm_os_wait_stats', 'CLEAR');
DBCC SQLPERF ('sys.dm_os_latch_stats', 'CLEAR');
```

```sql
wait_type
```

```sql
PAGELATCH_*
```

```sql
PAGEIOLATCH_*
```

```sql
sys.dm_os_wait_stats
```

```sql
sys.dm_os_wait_stats
```

```sql
sys.dm_exec_sessions
```

```sql
sys.dm_exec_requests
```

```sql
SELECT
wt.session_id,
wt.wait_type,
er.last_wait_type
AS
last_wait_type,
wt.wait_duration_ms,
wt.blocking_session_id,
wt.blocking_exec_context_id,
resource_description
FROM
sys.dm_os_waiting_tasks
AS
wt
INNER
JOIN
sys.dm_exec_sessions
AS
es
ON
wt.session_id = es.session_id
INNER
JOIN
sys.dm_exec_requests
AS
er
ON
wt.session_id = er.session_id
WHERE
es.is_user_process = 1
AND
wt.wait_type <>
'SLEEP_TASK'
ORDER
BY
wt.wait_duration_ms
DESC
;
```

```sql
session_id
```

```sql
wait_type
```

```sql
last_wait_type
```

```sql
wait_duration_ms
```

```sql
blocking_session_id
```

```sql
blocking_exec_context_id
```

```sql
resource_description
```

```sql
resource_description
```

```sql
<database_id>:<file_id>:<page_id>
```

```sql
latch_class
```

```sql
waiting_requests_count
```

```sql
wait_time_ms
```

```sql
max_wait_time_ms
```

```sql
sqlserver_start_time
```

```sql
SELECT
*
FROM
sys.dm_os_latch_stats
WHERE
latch_class <>
'BUFFER'
ORDER
BY
wait_time_ms
DESC
;
```
