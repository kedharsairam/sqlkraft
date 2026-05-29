---
name: 'sys.dm_resource_governor_workload_groups'
title: 'sys.dm_resource_governor_workload_groups'
category: 'execution'
description: 'Identified for informational purposes only. Not'
pubDate: 2026-05-29
---

Identified for informational purposes only. Not

supported. Future compatibility is not

guaranteed.

`

The identifier for the node that this distribution

is on.

: Azure Synapse Analytics, Analytics

Platform System (PDW)

Resource governor workload groups and resource pools have a many-to-one mapping. As a

result, many of the resource pool statistics are derived from the workload group statistics.

Statistics are tracked since the last start of the Database Engine and can be reset by executing

.

This dynamic management view shows the in-memory configuration. To see the stored

configuration metadata, use the

catalog view.

Requires

permission.

Requires

permission on the server.

Dynamic Management Views and Functions (Transact-SQL)

sys.dm_resource_governor_workload_groups (Transact-SQL)

sys.resource_governor_resource_pools (Transact-SQL)

ALTER resource governor (Transact-SQL)

Last updated on 11/18/2025

## sys.dm_pdw_nodes_resource_governor_workload_groups

Article

•

05/19/2025

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)


## Returns workload group statistics and the current in-memory configuration of the workload
group. This view can be joined with

sys.dm_resource_governor_resource_pools

to get the

resource pool name.

ID of the workload group. Not nullable.

Name of the workload group. Not nullable.

ID of the resource pool. Not nullable.

: Starting with SQL Server 2016 (13.x).

ID of the external resource pool. Not nullable.

The time when statistics collection for the

workload group started. Not nullable.

Cumulative count of completed requests in the

workload group. Not nullable.

Cumulative count of requests queued after the

limit was reached. Not

nullable.

Current request count. Not nullable.

Current queued request count. Not nullable.

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not

supported by serverless SQL pool in Azure Synapse Analytics.

ﾉ

Cumulative count of requests exceeding the

CPU limit. Not nullable.

Cumulative CPU usage, in milliseconds, by this

workload group. Not nullable.

Maximum CPU usage, in milliseconds, for a

single request. Not nullable.

This is a measured value, unlike

, which is a

configurable setting. For more information, see

REQUEST_MAX_CPU_TIME_SEC

.

Current count of blocked tasks. Not nullable.

Cumulative count of lock waits that occurred.

Not nullable.

Cumulative sum of elapsed time, in

milliseconds, that a lock is held. Not nullable.

Cumulative count of query optimizations in this

workload group. Not nullable.

Cumulative count of suboptimal plan

generations that occurred in this workload

group due to memory pressure. Not nullable.

Cumulative count of memory grants that

reached the maximum limit on the per-request

memory grant size. Not nullable.

Maximum memory grant size, in kilobytes, of a

single request since the statistics were reset.

Not nullable.

Current count of parallel thread usage. Not

nullable.

Current configuration value for the relative

importance of a request in this workload group.

Importance is one of the following, with

being the default:

,

, or

.

Not nullable.

Current setting for the maximum memory grant,

as a percentage, for a single request. Not

nullable.

Current setting for maximum CPU use limit, in

seconds, for a single request. Not nullable.

Current setting for memory grant time-out, in

seconds, for a single request. Not nullable.

Current setting for the maximum number of

concurrent requests in the workload group. Not

nullable.

Configured maximum degree of parallelism for

the workload group. The default value, 0, uses

global settings. Not nullable.

: Starting with SQL Server 2012 (11.x).

Effective maximum degree of parallelism for the

workload group. Not nullable.

: Starting with SQL Server 2016 (13.x).

Total CPU time used while in preemptive mode

scheduling for the workload group, measured in

milliseconds. Not nullable.

To execute code that is outside the Database

Engine (for example, extended stored

procedures and distributed queries), a thread

has to execute outside the control of the non-

preemptive scheduler. To do this, a worker

switches to preemptive mode.

: Azure SQL Managed Instance and

starting with SQL Server 2019 (15.x).

Current setting for the maximum memory grant,

as a percentage, for a single request. The value

is similar to

.

However, unlike

which


## returns an
value,


## returns a
value. Starting with SQL Server

2019 (15.x), the parameter

accepts

values with a possible range of 0-100 and stores

them as the

data type. Prior to SQL

Server 2019 (15.x),

is an

with possible range of 1-100. For more

information, see

CREATE WORKLOAD GROUP

.

Not nullable.

: Starting with SQL Server 2025 (17.x)

Preview

The current data space consumed in the

data files by all sessions in the workload group,

in kilobytes. Nullable.

: Starting with SQL Server 2025 (17.x)

Preview

The peak data space consumed in the

data files by all sessions in the workload group

since the server startup, or since resource

governor statistics were reset, in kilobytes.

Nullable.

: Starting with SQL Server 2025 (17.x)

Preview

The number of times a request was aborted

with error 1138 because it would exceed the

limit on tempdb data space consumption for

the workload group. Nullable.

: Azure Synapse Analytics, Analytics

Platform System (PDW)

The identifier for the node that this distribution

is on.

This dynamic management view shows the in-memory configuration. To see the stored

configuration metadata, use the

sys.resource_governor_workload_groups

catalog view.

```sql
total_cpu_usage_actual_ms
```

```sql
pdw_node_id
```

```sql
ALTER RESOURCE GOVERNOR RESET STATISTICS
```

```sql
sys.resource_governor_resource_pools
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
group_id
```

```sql
name
```

```sql
pool_id
```

```sql
external_pool_id
```

```sql
statistics_start_time
```

```sql
total_request_count
```

```sql
total_queued_request_count
```

```sql
GROUP_MAX_REQUESTS
```

```sql
active_request_count
```

```sql
queued_request_count
```

```sql
total_cpu_limit_violation_count
```

```sql
total_cpu_usage_ms
```

```sql
max_request_cpu_time_ms
```

```sql
request_max_cpu_time_sec
```

```sql
blocked_task_count
```

```sql
total_lock_wait_count
```

```sql
total_lock_wait_time_ms
```

```sql
total_query_optimization_count
```

```sql
total_suboptimal_plan_generation_count
```

```sql
total_reduced_memgrant_count
```

```sql
max_request_grant_memory_kb
```

```sql
active_parallel_thread_count
```

```sql
importance
```

```sql
Medium
```

```sql
Low
```

```sql
Medium
```

```sql
High
```

```sql
request_max_memory_grant_percent
```

```sql
request_max_cpu_time_sec
```

```sql
request_memory_grant_timeout_sec
```

```sql
group_max_requests
```

```sql
max_dop
```

```sql
effective_max_dop
```

```sql
total_cpu_usage_preemptive_ms
```

```sql
request_max_memory_grant_percent_numeric
```

```sql
request_max_memory_grant_percent
```

```sql
request_max_memory_grant_percent
```

```sql
integer
```

```sql
request_max_memory_grant_percent_numeric
```

```sql
float
```

```sql
REQUEST_MAX_MEMORY_GRANT_PERCENT
```

```sql
float
```

```sql
REQUEST_MAX_MEMORY_GRANT_PERCENT
```

```sql
integer
```

```sql
tempdb_data_space_kb
```

```sql
tempdb
```

```sql
peak_tempdb_data_space_kb
```

```sql
tempdb
```

```sql
total_tempdb_data_limit_violation_count
```

```sql
pdw_node_id
```
