---
title: "Analyze current wait buffer latches"
topic: "memory-management"
description: ""
tags: ["memory-management","architecture"]
pubDate: 2026-05-29
---

For a

only, clear the

DMV with the

following command:

A similar command can be run to clear the

DMV:

: This was illustrated in

Example of Latch Contention.

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

Server was started or the cumulative wait statistics were reset using. To

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

The statistics exposed by this query are described as follows:

## Description

preventing a current request from being executed.

the last wait. Isn't nullable.

The total wait time in milliseconds spent waiting on this wait type since SQL

Server instance was started or since cumulative wait statistics were reset.

The following query returns information for all non-buffer latches:

The statistics exposed by this query are described as follows:

## Description

preventing a current request from being executed.

Number of waits on latches in this class since SQL Server restarted. This

counter is incremented at the start of a latch wait.

The total wait time in milliseconds spent waiting on this latch type.

Maximum time in milliseconds any request spent waiting on this latch type.

restarted or the DMV was reset.

sys.dm_os_sys_info

to

find the last database engine startup time.



ﾉ

`sys.dm_os_wait_stats`

`sys.dm_os_latch_stats`

`sys.dm_os_wait_stats`

```sql
DBCC SQLPERF
```

`sys.dm_os_wait_stats`

```sql
DBCC SQLPERF ('sys.dm_os_wait_stats', 'CLEAR');
DBCC SQLPERF ('sys.dm_os_latch_stats', 'CLEAR');
```

`wait_type`

```sql
PAGELATCH_*
```

```sql
PAGEIOLATCH_*
```

`sys.dm_os_wait_stats`

`sys.dm_os_wait_stats`

`sys.dm_exec_sessions`

`sys.dm_exec_requests`

```sql
SELECT wt.session_id,
wt.wait_type,
er.last_wait_type
AS last_wait_type,
wt.wait_duration_ms,
wt.blocking_session_id,
wt.blocking_exec_context_id,
resource_description
FROM sys.dm_os_waiting_tasks

INNER
JOIN sys.dm_exec_sessions

ON wt.session_id = es.session_id
INNER
JOIN sys.dm_exec_requests

ON wt.session_id = er.session_id
WHERE es.is_user_process = 1
AND wt.wait_type <>
'SLEEP_TASK'
ORDER
BY wt.wait_duration_ms
DESC
;
```

`session_id`

`wait_type`

`last_wait_type`

`wait_duration_ms`

`blocking_session_id`

`blocking_exec_context_id`

`resource_description`

`resource_description`

```sql
<database_id>:<file_id>:<page_id>
```

`latch_class`

`waiting_requests_count`

`wait_time_ms`

`max_wait_time_ms`

`sqlserver_start_time`

```sql
SELECT
*
FROM sys.dm_os_latch_stats
WHERE latch_class <>
'BUFFER'
ORDER
BY wait_time_ms
DESC
;
```
