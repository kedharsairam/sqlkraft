---
name: 'sys.dm_exec_cached_plans'
title: 'sys.dm_exec_cached_plans'
category: 'execution'
description: 'Azure SQL Managed Instance'
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric


## Returns a row for each Transact-SQL execution plan, common language runtime (CLR)
execution plan, and cursor associated with a plan.


## syntaxsql
Is a token that uniquely identifies a query execution plan for a batch that has executed and its

plan resides in the plan cache.

is

.

The

can be obtained from the following dynamic management objects:

sys.dm_exec_cached_plans (Transact-SQL)

sys.dm_exec_query_stats (Transact-SQL)

sys.dm_exec_requests (Transact-SQL)

sys.dm_exec_procedure_stats (Transact-SQL)

sys.dm_exec_trigger_stats (Transact-SQL)

ﾉ

Expand table


## Description
Number of times the execution context or cursor has been

used.

Column is not nullable.

Memory address of the execution context or cursor.

Column is not nullable.

The Plan cache object type. Column is not nullable. Possible

values are:

Executable plan

CLR compiled function

CLR compiled procedure

Cursor

Requires

permission on the server.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.


## Permissions for SQL Server 2022 and later
ﾉ

Expand table

One-to-one

Execution Related Dynamic Management Views and Functions (Transact-SQL)

Dynamic Management Views and Functions (Transact-SQL)

sys.syscacheobjects (Transact-SQL)

Last updated on 11/18/2025

Next steps

## memory_object_address

## pool_id

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric


## Returns a row for each query plan that is cached by SQL Server for faster query execution. You
can use this dynamic management view to find cached query plans, cached query text, the

amount of memory taken by cached plans, and the reuse count of the cached plans.

In Azure SQL Database, dynamic management views can't expose information that would

impact database containment or expose information about other databases the user has access

to. To avoid exposing this information, every row that contains data that doesn't belong to the

connected tenant is filtered out. In addition, the values in the columns

and

are filtered; the column value is set to

.


## Description
ID of the hash bucket in which the entry is cached. The value

indicates a range from 0 through the hash table size for the

type of cache.

For the SQL Plans and Object Plans caches, the hash table size

can be up to 10,007 on 32-bit systems and up to 40,009 on 64-

bit systems. For the Bound Trees cache, the hash table size can

be up to 1,009 on 32-bit systems and up to 4,001 on 64-bit

systems. For the Extended Stored Procedures cache the hash

table size can be up to 127 on 32-bit and 64-bit systems.

Number of cache objects that are referencing this cache object.

must be at least 1 for an entry to be in the cache.

Number of times the cache object has been looked up. Not

incremented when parameterized queries find a plan in the

cache. Can be incremented multiple times when using

showplan.

７

Note

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not supported by serverless SQL

pool in Azure Synapse Analytics.

ﾉ

Expand table


## Description
Number of bytes consumed by the cache object.

Memory address of the cached entry. This value can be used

with

sys.dm_os_memory_objects

to get the memory breakdown

of the cached plan and with

sys.dm_os_memory_cache_entries

_entries to obtain the cost of

caching the entry.

Type of object in the cache. The value can be one of:

Compiled Plan

Compiled Plan Stub

Parse Tree

Extended Proc

CLR Compiled Func

CLR Compiled Proc

Type of object. Below are the possible values and their

corresponding descriptions.

Proc: Stored procedure

Prepared: Prepared statement

Ad hoc: Ad hoc query. Refers to Transact-SQL submitted as

language events by using

or

sqlcmd

instead of as remote

procedure calls.

ReplProc: Replication-filter-procedure

Trigger: Trigger

View: View

Default: Default

UsrTab: User table

SysTab: System table

Check: CHECK constraint

Rule: Rule

Identifier for the in-memory plan. This identifier is transient and

remains constant only while the plan remains in the cache. This

value might be used with the following dynamic management

functions:

sys.dm_exec_sql_text

sys.dm_exec_query_plan

sys.dm_exec_plan_attributes

The ID of the resource pool against which this plan memory

usage is accounted for.

The identifier for the node that this distribution is on.

## Basic

## S0

## S1

## elastic pools

```sql
plan_handle
```

```sql
plan_handle
```

```sql
sys.dm_exec_cached_plan_dependent_objects(plan_handle)
```

```sql
VIEW SERVER STATE
```

```sql
dm_exec_cached_plan_dependent_objects
dm_os_memory_objects
memory_object_address
```

```sql
NULL
```

```sql
bucketid
```

```sql
refcounts
```

```sql
refcounts
```

```sql
usecounts
```

```sql
sys.dm_pdw_nodes_exec_cached_plans
```

```sql
size_in_bytes
```

```sql
memory_object_address
```

```sql
cacheobjtype
```

```sql
objtype
```

```sql
plan_handle
```

```sql
pool_id
```

```sql
pdw_node_id
```
