---
name: 'sys.dm_exec_query_plan'
title: 'sys.dm_exec_query_plan'
category: 'execution'
description: 'dynamic management view. The plan handles are'
pubDate: 2026-05-29
---

querying the

dynamic management view. The plan handles are

stored in the

column of

. Then use the CROSS APPLY

operator to pass the plan handles to

as follows. The Showplan

output for each plan is in the

column of the table that is returned.

SQL

The following example returns the query plans and average CPU time for the top five queries.

The

function specifies the default values 0 and -1 to return all

statements in the batch in the query plan.

SQL

sys.dm_exec_query_plan (Transact-SQL)

Last updated on 11/18/2025

## sys.dm_exec_query_stats

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric


## Returns aggregate performance statistics for cached triggers. The view contains one row per
trigger, and the lifetime of the row is as long as the trigger remains cached. When a trigger is

removed from the cache, the corresponding row is eliminated from this view. At that time, a

Performance Statistics SQL trace event is raised similar to

.

Database ID in which the trigger resides.

In Azure SQL Database, the values are unique within a single

database or an elastic pool, but not within a logical server.

Object identification number of the trigger.

Type of the object:

TA = Assembly (CLR) trigger

TR = SQL trigger


## Description of the object type:
CLR_TRIGGER

SQL_TRIGGER

This can be used to correlate with queries in

that were executed from within this

trigger.

Identifier for the in-memory plan. This identifier is transient

and remains constant only while the plan remains in the

cache. This value may be used with the

dynamic management view.

Time at which the trigger was added to the cache.

Last time at which the trigger was executed.

The number of times that the trigger has been executed since

it was last compiled.

ﾉ

The total amount of CPU time, in microseconds, that was

consumed by executions of this trigger since it was compiled.

CPU time, in microseconds, that was consumed the last time

the trigger was executed.

The maximum CPU time, in microseconds, that this trigger has

ever consumed during a single execution.

The maximum CPU time, in microseconds, that this trigger has

ever consumed during a single execution.

The total number of physical reads performed by executions

of this trigger since it was compiled.

The number of physical reads performed the last time the

trigger was executed.

The minimum number of physical reads that this trigger has

ever performed during a single execution.

The maximum number of physical reads that this trigger has

ever performed during a single execution.

The total number of logical writes performed by executions of

this trigger since it was compiled.

The number of logical writes performed the last time the

trigger was executed.

The minimum number of logical writes that this trigger has

ever performed during a single execution.

The maximum number of logical writes that this trigger has

ever performed during a single execution.

The total number of logical reads performed by executions of

this trigger since it was compiled.

The number of logical reads performed the last time the

trigger was executed.

The minimum number of logical reads that this trigger has

ever performed during a single execution.

The maximum number of logical reads that this trigger has

ever performed during a single execution.

The total elapsed time, in microseconds, for completed

executions of this trigger.

Elapsed time, in microseconds, for the most recently

completed execution of this trigger.

The minimum elapsed time, in microseconds, for any

completed execution of this trigger.

The maximum elapsed time, in microseconds, for any

completed execution of this trigger.

The total number of pages spilled by execution of this trigger

since it was compiled.

: Starting with SQL Server 2017 (14.x) CU3

The number of pages spilled the last time the trigger was

executed.

: Starting with SQL Server 2017 (14.x) CU3

The minimum number of pages that this trigger has ever

spilled during a single execution.

: Starting with SQL Server 2017 (14.x) CU3

The maximum number of pages that this trigger has ever

spilled during a single execution.

: Starting with SQL Server 2017 (14.x) CU3

The total number of page server reads performed by

executions of this trigger since it was compiled.

: Azure SQL Database Hyperscale

The number of page server reads performed the last time the

trigger was executed.

: Azure SQL Database Hyperscale

The minimum number of page server reads that this trigger

has ever performed during a single execution.

: Azure SQL Database Hyperscale

The maximum number of page server reads that this trigger

has ever performed during a single execution.

: Azure SQL Database Hyperscale

## Basic

## S0

## S1

## elastic pools

```sql
sys.dm_exec_query_stats
```

```sql
plan_handle
```

```sql
sys.dm_exec_query_stats
```

```sql
sys.dm_exec_text_query_plan
```

```sql
query_plan
```

```sql
USE
master
;
GO
SELECT
*
FROM
sys.dm_exec_query_stats
AS
qs
CROSS
APPLY
sys.dm_exec_text_query_plan(qs.plan_handle, qs.statement_start_offset,
qs.statement_end_offset);
GO
```

```sql
SELECT
TOP 5 total_worker_time/execution_count
AS
[
Avg
CPU
Time
],
Plan_handle, query_plan
FROM
sys.dm_exec_query_stats
AS
qs
CROSS
APPLY
sys.dm_exec_text_query_plan(qs.plan_handle, 0, -1)
ORDER
BY
total_worker_time/execution_count
DESC
;
GO
```
