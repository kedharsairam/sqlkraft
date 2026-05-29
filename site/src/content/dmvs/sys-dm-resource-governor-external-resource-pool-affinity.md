---
name: 'sys.dm_resource_governor_external_resource_pool_affinity'
title: 'sys.dm_resource_governor_external_resource_pool_affinity'
category: 'execution'
description: 'The number of external processes running at the moment of the'
pubDate: 2026-05-29
---

The number of external processes running at the moment of the

request. Not nullable.

Requires the

permission.

Requires the

permission on the server.

sys.dm_resource_governor_external_resource_pool_affinity (Transact-SQL)

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric


## Returns information about the current resource pool state, the current configuration of
resource pools, and resource pool statistics.

The ID of the resource pool. Not nullable.

The name of the resource pool. Not nullable.

The time when statistics was reset for this pool.

Not nullable.

The cumulative CPU usage in milliseconds since

the resource governor statistics were reset. Not

nullable.

The current total cache memory usage in

kilobytes. Not nullable.

The current total stolen memory usage in

kilobytes (KB). Most this usage would be for

compile and optimization, but it can also

include other memory users. Not nullable.

The current total used (stolen) memory for

memory grants. Not nullable.

The cumulative count of memory grants in this

resource pool. Not nullable.

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not supported

by serverless SQL pool in Azure Synapse Analytics.

ﾉ

The cumulative count of memory grant time-

outs in this resource pool. Not nullable.

The current count of memory grants. Not

nullable.

The sum, in kilobytes (KB), of current memory

grants. Not nullable.

The count of queries currently pending on

memory grants. Not nullable.

The maximum amount of memory, in kilobytes,

that the resource pool can use as query

workspace memory. Query workspace memory

is a subset of server target memory, and can be

further reduced under memory pressure. Not

nullable.

The amount of query workspace memory used,

in kilobytes, for the resource pool. Not nullable.

The target amount of query workspace

memory, in kilobytes, the resource pool is trying

to attain. Can be reduced under memory

pressure. Not nullable.

The number of failed memory allocations in the

pool since the resource governor statistics were

reset. Not nullable.

The current configuration for the guaranteed

average CPU bandwidth for all requests in the

resource pool when there's CPU contention.

Not nullable.

The current configuration for the maximum

average CPU bandwidth allowed for all requests

in the resource pool when there's CPU

contention. Not nullable.

The current configuration for the guaranteed

amount of memory for all requests in the

resource pool when there's memory contention.

This isn't shared with other resource pools. Not

nullable.

The current configuration for the percentage of

total server memory that can be used by

requests in this resource pool. Not nullable.

Hard cap on the CPU bandwidth that all

requests in the resource pool receive. Limits the

maximum CPU bandwidth level to the specified

level. The allowed range for value is from 1

through 100. Not nullable.

: SQL Server 2012 (11.x) and later

versions

The minimum I/O per second (IOPS) per disk

volume setting for this pool. Nullable.

if

the resource pool isn't governed for I/O. That is,

the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

The maximum I/O per second (IOPS) per disk

volume setting for this pool. Nullable.

if

the resource pool isn't governed for I/O. That is,

the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

The total read I/Os enqueued since the resource

governor statistics were reset. Nullable.

if

the resource pool isn't governed for I/O. That is,

the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

The total read I/Os issued since the resource

governor statistics were reset. Nullable.

if

the resource pool isn't governed for I/O. That is,

the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

The total read I/Os completed since the

resource governor statistics were reset. Not

nullable.

The total read I/Os throttled since the resource

governor statistics were reset. Nullable.

if

the resource pool isn't governed for I/O. That is,

the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

The total number of bytes read since the

resource governor statistics were reset. Not

nullable.

: SQL Server 2014 (12.x) and later

versions

Total time (in milliseconds) between read I/O

arrival and completion. Not nullable.

: SQL Server 2014 (12.x) and later

versions

Total time (in milliseconds) between read I/O

arrival and issue. Nullable.

if the resource

pool isn't governed for I/O. That is, the resource

pool

and

settings are 0.

To determine if the I/O setting for the pool is

causing latency, subtract

from

.

: SQL Server 2014 (12.x) and later

versions

The total write I/Os enqueued since the

resource governor statistics were reset.

Nullable.

if the resource pool isn't

governed for I/O. That is, the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

The total write I/Os issued since the resource

governor statistics were reset. Nullable.

if

the resource pool isn't governed for I/O. That is,

the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

The total write I/Os completed since the

resource governor statistics were reset. Not

nullable.

: SQL Server 2014 (12.x) and later

versions

The total write I/Os throttled since the resource

governor statistics were reset. Not nullable.

: SQL Server 2014 (12.x) and later

versions

The total number of bytes written since the

resource governor statistics were reset. Not

nullable.

: SQL Server 2014 (12.x) and later

versions

Total time (in milliseconds) between write I/O

arrival and completion. Not nullable.

: SQL Server 2014 (12.x) and later

versions

Total time (in milliseconds) between write I/O

arrival and issue. Nullable.

if the resource

pool isn't governed for I/O. That is, the resource

pool

and

settings are 0.

This is the delay introduced by I/O Resource

Governance.

: SQL Server 2014 (12.x) and later

versions

Total I/O issue violations. That is, the number of

times when the rate of I/O issue was lower than

the reserved rate. Nullable.

if the resource

pool isn't governed for I/O. That is, the resource

pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

Total time (in milliseconds) between the

scheduled issue and actual issue of I/O.

Nullable.

if the resource pool isn't

governed for I/O. That is, the resource pool

and

settings are 0.

: SQL Server 2014 (12.x) and later

versions

Internal use only.

SQL Server 2016 (13.x) and later

versions

Internal use only.

SQL Server 2016 (13.x) and later

versions

Total time (in milliseconds) between the

scheduled issue and actual issue of a non-

throttled I/O.

SQL Server 2016 (13.x) and later

versions

Total time (in milliseconds) between when a

runnable worker yields, and when the operating

system gives back control to another runnable

worker in the Database Engine. This could be

the Idle worker.

SQL Server 2016 (13.x) and later

versions

Total active CPU time (in milliseconds).

SQL Server 2016 (13.x) and later

versions

Total CPU violation delays (in milliseconds). That

is, total CPU time delay that was lower than the

minimum guaranteed delay between a runnable

worker yields, and the operating system gives

back control to another runnable worker in the

Database Engine.

SQL Server 2016 (13.x) and later

versions

Total CPU violations (in seconds). That is, total

time accrued when a CPU time violation was in-

flight.

SQL Server 2016 (13.x) and later

versions

Total CPU time used while in preemptive mode

scheduling for the workload group (in

milliseconds). Not nullable.

To execute code that is outside the Database

Engine (for example, extended stored

procedures and distributed queries), a thread

has to execute outside the control of the non-

preemptive scheduler. To do this, a worker

switches to preemptive mode.

SQL Server 2016 (13.x) and later

versions

The current configuration for the maximum

average CPU bandwidth allowed for all requests

in the resource pool when there's CPU

contention. Expressed in the unit of vCores and

might not reflect the total number of vCores or

logical CPUs available to a database, elastic

pool, or SQL managed instance.

: Azure SQL Database and Azure SQL

Managed Instance

```sql
active_processes_count
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
pool_id
```

```sql
name
```

```sql
statistics_start_time
```

```sql
total_cpu_usage_ms
```

```sql
cache_memory_kb
```

```sql
compile_memory_kb
```

```sql
used_memgrant_kb
```

```sql
total_memgrant_count
```

```sql
sys.dm_pdw_nodes_resource_governor_resource_pools
```

```sql
total_memgrant_timeout_count
```

```sql
active_memgrant_count
```

```sql
active_memgrant_kb
```

```sql
memgrant_waiter_count
```

```sql
max_memory_kb
```

```sql
used_memory_kb
```

```sql
target_memory_kb
```

```sql
out_of_memory_count
```

```sql
min_cpu_percent
```

```sql
max_cpu_percent
```

```sql
min_memory_percent
```

```sql
max_memory_percent
```

```sql
cap_cpu_percent
```

```sql
min_iops_per_volume
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
max_iops_per_volume
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
read_io_queued_total
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
read_io_issued_total
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
read_io_completed_total
```

```sql
read_io_throttled_total
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
read_bytes_total
```

```sql
read_io_stall_total_ms
```

```sql
read_io_stall_queued_ms
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
write_io_queued_total
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
write_io_issued_total
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
write_io_completed_total
```

```sql
write_io_throttled_total
```

```sql
write_bytes_total
```

```sql
write_io_stall_total_ms
```

```sql
write_io_stall_queued_ms
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
io_issue_violations_total
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
io_issue_delay_total_ms
```

```sql
NULL
```

```sql
MIN_IOPS_PER_VOLUME
```

```sql
MAX_IOPS_PER_VOLUME
```

```sql
io_issue_ahead_total_ms
```

```sql
reserved_io_limited_by_volume_total
```

```sql
io_issue_delay_non_throttled_total_ms
```

```sql
total_cpu_delayed_ms
```

```sql
total_cpu_active_ms
```

```sql
total_cpu_violation_delay_ms
```

```sql
total_cpu_violation_sec
```

```sql
total_cpu_usage_preemptive_ms
```

```sql
max_vcores
```
