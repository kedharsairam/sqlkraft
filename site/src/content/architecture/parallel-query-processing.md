---
title: "Parallel query processing"
topic: "query-processing"
description: "In this case, SQL Server doesn't use the value 100 to optimize the query. It uses a general"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

In this case, SQL Server doesn't use the value 100 to optimize the query. It uses a general

estimate.

provides parallel queries to optimize query execution and index operations for

computers that have more than one microprocessor (CPU). Because SQL Server can perform a

query or index operation in parallel by using several operating system worker threads, the

operation can be completed quickly and efficiently.

During query optimization, SQL Server looks for queries or index operations that might benefit

from parallel execution. For these queries, SQL Server inserts exchange operators into the

query execution plan to prepare the query for parallel execution. An exchange operator is an

operator in a query execution plan that provides process management, data redistribution, and

flow control. The exchange operator includes the

,

,

and

logical operators as subtypes, one or more of which can appear in the

Showplan output of a query plan for a parallel query.

Constructs that inhibit parallelism include:

For more information on scalar user-defined functions, see

Create User-defined

Functions. Starting with SQL Server 2019 (15.x), the SQL Server Database Engine has the

ability to inline these functions, and unlock use of parallelism during query processing.

For more information on scalar UDF inlining, see

Intelligent query processing in SQL

databases.

For more information on Remote Query, see

Showplan Logical and Physical Operators

Reference.

）

Important

Certain constructs inhibit SQL Server's ability to use parallelism on the entire execution

plan, or parts or the execution plan.

### Dynamic cursors

### Recursive queries

### Multi-statement table-valued functions (MSTVFs)

### TOP keyword

### NonParallelPlanReason

### QueryPlan

For more information on cursors, see

DECLARE CURSOR.

For more information on recursion, see

Guidelines for Defining and Using Recursive

Common Table Expressions

and

Recursion in T-SQL.

For more information on MSTVFs, see

Create User-defined Functions (Database Engine).

For more information, see

TOP (Transact-SQL).

A query execution plan can contain the

attribute in the

element, which describes why parallelism wasn't used. Values for this attribute include:

## Description

MaxDOPSetToOne

to 1.

EstimatedDOPIsOne

Estimated degree of parallelism is 1.

NoParallelWithRemoteQuery

Parallelism isn't supported for remote

queries.

NoParallelDynamicCursor

dynamic cursors.

NoParallelFastForwardCursor

forward cursors.

NoParallelCursorFetchByBookmark

cursors that fetch by bookmark.

NoParallelCreateIndexInNonEnterpriseEdition

Parallel index creation not supported

for non-Enterprise edition.

NoParallelPlansInDesktopOrExpressEdition

Desktop and Express edition.

NonParallelizableIntrinsicFunction

Query is referencing a non-

parallelizable intrinsic function.

CLRUserDefinedFunctionRequiresDataAccess

Parallelism not supported for a CLR

UDF that requires data access.

ﾉ

## Description

TSQLUserDefinedFunctionsNotParallelizable

Query is referencing a T-SQL User

Defined Function that wasn't

parallelizable.

TableVariableTransactionsDoNotSupportParallelNestedTransaction

Table variable transactions don't

support parallel nested transactions.

DMLQueryReturnsOutputToClient

DML query returns output to client

and isn't parallelizable.

MixedSerialAndParallelOnlineIndexBuildNotSupported

parallel plans for a single online

index build.

CouldNotGenerateValidParallelPlan

Verifying parallel plan failed, failing

back to serial.

NoParallelForMemoryOptimizedTables

referenced In-Memory OLTP tables.

NoParallelForDmlOnMemoryOptimizedTable

an In-Memory OLTP table.

NoParallelForNativelyCompiledModule

referenced natively compiled

modules.

NoRangesResumableCreate

Range generation failed for a

resumable create operation.

After exchange operators are inserted, the result is a parallel-query execution plan. A parallel-

query execution plan can use more than one worker thread. A serial execution plan, used by a

non-parallel (serial) query, uses only one worker thread for its execution.

is determined by the complexity of the plan and the degree of parallelism.

doesn't mean the number of worker threads that are being used.

task.

request

or per query limit. This means that during a parallel query execution, a

single request can spawn multiple tasks that are assigned to a

scheduler.

specified by the MAXDOP might be used concurrently at any given point of query execution,

when different tasks are executed concurrently.

Thread and Task

Architecture Guide.

the following conditions is true:

### running on a computer that has more than one microprocessor

### or CPU

### sufficient worker threads are available

### type of query or index operation executed

```sql
Distribute Streams
```

```sql
Repartition Streams
```

```sql
Gather Streams
```

```sql
DECLARE
@ProductId
INT
= 100;
SELECT
*
FROM
Products
WHERE
ProductId = @ProductId;
```
