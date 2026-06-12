---
title: "Degree of parallelism (DOP)"
topic: "query-processing"
description: "The serial execution plan is trivial, or does not exceed the cost threshold for parallelism"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

The serial execution plan is trivial, or does not exceed the cost threshold for parallelism

setting.

The serial execution plan has a lower total estimated subtree cost than any parallel

execution plan explored by the optimizer.

The query contains scalar or relational operators that can't be run in parallel. Certain

operators can cause a section of the query plan to run in serial mode, or the whole plan

to run in serial mode.

automatically detects the best degree of parallelism for each instance of a parallel

query execution or index data definition language (DDL) operation. It does this based on the

following criteria:

1. Whether SQL Server is

, such as a symmetric multiprocessing computer (SMP). Only computers that have

more than one CPU can use parallel queries.

2. Whether. Each query or index operation requires a

certain number of worker threads to execute. Executing a parallel plan requires more

worker threads than a serial plan, and the number of required worker threads increases

with the degree of parallelism. When the worker thread requirement of the parallel plan

for a specific degree of parallelism can't be satisfied, the SQL Server Database Engine

decreases the degree of parallelism automatically or completely abandons the parallel

plan in the specified workload context. It then executes the serial plan (one worker

thread).

3. The. Index operations that create or rebuild

an index, or drop a clustered index and queries that use CPU cycles heavily are the best

candidates for a parallel plan. For example, joins of large tables, large aggregations, and

sorting of large result sets are good candidates. Simple queries, frequently found in

transaction processing applications, find the additional coordination required to execute a

query in parallel outweigh the potential performance boost. To distinguish between

queries that benefit from parallelism and those that don't benefit, the SQL Server

Database Engine compares the estimated cost of executing the query or index operation

７

Note

The total estimated subtree cost of a parallel plan can be lower than the cost threshold for

parallelism setting. This indicates that the total estimated subtree cost of the serial plan

exceeded it, and the query plan with the lower total estimated subtree cost was chosen.

### sufficient number of rows to process

### current distribution statistics are available

with the

cost threshold for parallelism

value. Users can change the default value of 5

using

sp_configure

if proper testing found that a different value is better suited for the

running workload.

4. Whether there are a. If the Query Optimizer

determines that the number of rows is too low, it doesn't introduce exchange operators

to distribute the rows. Thus, the operators are executed serially. Executing the operators

in a serial plan avoids scenarios when the startup, distribution, and coordination costs

exceed the gains achieved by parallel operator execution.

5. Whether. If the highest degree of parallelism

isn't possible, lower degrees are considered before the parallel plan is abandoned. For

example, when you create a clustered index on a view, distribution statistics can't be

evaluated, because the clustered index doesn't yet exist. In this case, the SQL Server

Database Engine can't provide the highest degree of parallelism for the index operation.

However, some operators, such as sorting and scanning, can still benefit from parallel

execution.

At execution time, the SQL Server Database Engine determines whether the current system

workload and configuration information previously described allow for parallel execution. If

parallel execution is warranted, the SQL Server Database Engine determines the optimal

number of worker threads and spreads the execution of the parallel plan across those worker

threads. When a query or index operation starts executing on multiple worker threads for

parallel execution, the same number of worker threads is used until the operation is completed.

The SQL Server Database Engine re-examines the optimal number of worker thread decisions

every time an execution plan is retrieved from the plan cache. For example, one execution of a

query can result in the use of a serial plan, a later execution of the same query can result in a

parallel plan using three worker threads, and a third execution can result in a parallel plan

using four worker threads.

The update and delete operators in a parallel query execution plan are executed serially, but

the

clause of an

or a

statement might be executed in parallel. The actual

data changes are then serially applied to the database.

Up to SQL Server 2012 (11.x), the insert operator is also executed serially. However, the SELECT

part of an INSERT statement might be executed in parallel. The actual data changes are then

serially applied to the database.

７

Note

Parallel index operations are only available in SQL Server Enterprise, Developer, and

Evaluation editions.

### max degree of parallelism (MAXDOP)

### MAX_DOP

### MAXDOP

### MAXDOP

### MAXDOP

`WHERE`

`UPDATE`

`DELETE`
