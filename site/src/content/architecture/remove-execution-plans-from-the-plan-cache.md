---
title: "Remove execution plans from the plan cache"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Notice there are now two entries in the

DMV output:

The

column shows the value

in the first record, which is the plan executed

once with.

The

column shows the value

in the second record, which is the plan

executed with

, because it was executed twice.

The different

refers to a different execution plan entry in the plan

cache. However, the

value is the same for both entries because they refer to

the same batch.

The execution with

set to OFF has a new

, and it's available

for reuse for calls that have the same set of SET options. The new plan handle is

necessary because the execution context was reinitialized due to changed SET options.

But that doesn't trigger a recompile: both entries refer to the same plan and query, as

evidenced by the same

and

values.

What this effectively means is that we have two plan entries in the cache corresponding to the

same batch, and it underscores the importance of making sure that the plan cache affecting

SET options are the same, when the same queries are executed repeatedly, to optimize for plan

reuse and keep plan cache size to its required minimum.

Execution plans remain in the plan cache as long as there is enough memory to store them.

When memory pressure exists, the SQL Server Database Engine uses a cost-based approach to

determine which execution plans to remove from the plan cache. To make a cost-based

decision, the SQL Server Database Engine increases and decreases a current cost variable for

each execution plan according to the following factors.



Tip

A common pitfall is that different clients can have different default values for the SET

options. For example, a connection made through SQL Server Management Studio

automatically sets

to ON, while SQLCMD sets

to

OFF. Executing the same queries from these two clients will result in multiple plans (as

described in the example above).

When a user process inserts an execution plan into the cache, the user process sets the current

cost equal to the original query compile cost; for ad hoc execution plans, the user process sets

the current cost to zero. Thereafter, each time a user process references an execution plan, it

resets the current cost to the original compile cost; for ad hoc execution plans the user process

increases the current cost. For all plans, the maximum value for the current cost is the original

compile cost.

When memory pressure exists, the SQL Server Database Engine responds by removing

execution plans from the plan cache. To determine which plans to remove, the SQL Server

Database Engine repeatedly examines the state of each execution plan and removes plans

when their current cost is zero. An execution plan with zero current cost isn't removed

automatically when memory pressure exists; it is removed only when the SQL Server Database

Engine examines the plan and the current cost is zero. When examining an execution plan, the

Database Engine pushes the current cost toward zero by decreasing the current

cost if a query isn't currently using the plan.

The SQL Server Database Engine repeatedly examines the execution plans until enough have

been removed to satisfy memory requirements. While memory pressure exists, an execution

plan might have its cost increased and decreased more than once. When memory pressure no

longer exists, the SQL Server Database Engine stops decreasing the current cost of unused

execution plans and all execution plans remain in the plan cache, even if their cost is zero.

The SQL Server Database Engine uses the resource monitor and user worker threads to free

memory from the plan cache in response to memory pressure. The resource monitor and user

worker threads can examine plans run concurrently to decrease the current cost for each

unused execution plan. The resource monitor removes execution plans from the plan cache

when global memory pressure exists. It frees memory to enforce policies for system memory,

process memory, resource pool memory, and maximum size for all caches.

The maximum size for all caches is a function of the buffer pool size and can't exceed the

maximum server memory. For more information on configuring the maximum server memory,

see the

setting in.

The user worker threads remove execution plans from the plan cache when single cache

memory pressure exists. They enforce policies for maximum single cache size and maximum

single cache entries.

The following examples illustrate which execution plans get removed from the plan cache:

An execution plan is frequently referenced so that its cost never goes to zero. The plan

remains in the plan cache and isn't removed unless there is memory pressure and the

current cost is zero.

`sys.dm_exec_cached_plans`

`usecounts`

```sql
1
```

```sql
SET ANSI_DEFAULTS OFF
```

`usecounts`

```sql
2
```

```sql
SET ANSI_DEFAULTS ON
```

`memory_object_address`

`sql_handle`

`ANSI_DEFAULTS`

`plan_handle`

`query_plan_hash`

`query_hash`

```sql
000000
0x0300130095555D02C864C10061AB000001000000000000000000000000000000000000000000000000
000000
```

`QUOTED_IDENTIFIER`

`QUOTED_IDENTIFIER`

```sql
max server memory
```

`sp_configure`
