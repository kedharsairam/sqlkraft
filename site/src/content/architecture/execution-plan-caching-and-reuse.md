---
title: "Execution plan caching and reuse"
topic: "query-processing"
description: "### Extended Stored Procedures"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

## Bound Trees

## Extended Stored Procedures

greater reuse of the stored procedure and trigger execution plans.

has a pool of memory that is used to store both execution plans and data buffers.

The percentage of the pool allocated to either execution plans or data buffers fluctuates

dynamically, depending on the state of the system. The part of the memory pool that is used to

store execution plans is referred to as the plan cache.

The plan cache has two stores for all compiled plans:

The

cache store (OBJCP) used for plans related to persisted objects (stored

procedures, functions, and triggers).

The

SQL Plans

cache store (SQLCP) used for plans related to autoparameterized, dynamic,

or prepared queries.

The query below provides information about memory usage for these two cache stores:

execution plans have the following main components:

(or Query Plan)

The query plan produced by the compilation process is mostly a re-entrant, read-only

data structure used by any number of users. It stores information about:

Physical operators that implement the operation described by logical operators.

７

Note

The plan cache has two additional stores that aren't used for storing plans:

The

cache store (PHDR) used for data structures used during plan

compilation for views, constraints, and defaults. These structures are known as

Bound Trees or Algebrizer Trees.

The

cache store (XPROC) used for predefined system

procedures, like

or

, that are defined using a DLL, not

using Transact-SQL statements. The cached structure contains only the function

name and the DLL name in which the procedure is implemented.

## Execution Context

## Cardinality Estimation

The order of these operators, which determines the order in which data is accessed,

filtered, and aggregated.

The number of estimated rows flowing through the operators.

What support objects must be created, such as

worktables

or workfiles in. No

user context or runtime information is stored in the query plan. There are never more

than one or two copies of the query plan in memory: one copy for all serial executions

and another for all parallel executions. The parallel copy covers all parallel executions,

regardless of their degree of parallelism.

Each user that is currently executing the query has a data structure that holds the data

specific to their execution, such as parameter values. This data structure is referred to as

the execution context. The execution context data structures are reused, but their content

isn't. If another user executes the same query, the data structures are reinitialized with the

context for the new user.

When any Transact-SQL statement is executed in SQL Server, the Database Engine first looks

through the plan cache to verify that an existing execution plan for the same Transact-SQL

statement exists. The Transact-SQL statement qualifies as existing if it literally matches a

previously executed Transact-SQL statement with a cached plan, character per character. SQL

Server reuses any existing plan it finds, saving the overhead of recompiling the Transact-SQL

statement. If no execution plan exists, SQL Server generates a new execution plan for the

query.

７

Note

In newer versions of the Database Engine, information about the statistics objects

that were used for

is also stored.

７

Note

has an efficient algorithm to find any existing execution plans for any specific

Transact-SQL statement. In most systems, the minimal resources that are used by this scan are

less than the resources that are saved by being able to reuse existing plans instead of

compiling every Transact-SQL statement.

The algorithms to match new Transact-SQL statements to existing, unused execution plans in

the plan cache require that all object references be fully qualified. For example, assume that

is the default schema for the user executing the below

statements. While in this

example it isn't required that the

table is fully qualified to execute, it means that the

second statement isn't matched with an existing plan, but the third is matched:

Changing any of the following SET options for a given execution will affect the ability to reuse

plans, because the Database Engine performs

constant folding

and these options affect the

results of such expressions:

ANSI_NULL_DFLT_OFF

FORCEPLAN

ARITHABORT

DATEFIRST

ANSI_PADDING

NUMERIC_ROUNDABORT

ANSI_NULL_DFLT_ON

LANGUAGE

The execution plans for some Transact-SQL statements aren't persisted in the plan cache,

such as bulk operation statements running on rowstore or statements containing string

literals larger than 8 KB in size. These plans only exist while the query is being executed.

## query plan hash

## query hash

## Plan Handle

```sql
SELECT
*
FROM sys.dm_os_memory_clerks
WHERE name
LIKE
'%plans%'
;
```

`sp_executeSql`

`xp_cmdshell`

`tempdb`

`Person`

`SELECT`

`Person`

```sql
USE
AdventureWorks2022;
GO
SELECT
*
FROM
Person;
GO
SELECT
*
FROM
Person.Person;
GO
SELECT
*
FROM
Person.Person;
GO
```
