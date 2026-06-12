---
title: "Parallel index operations"
topic: "index-architecture"
description: ""
tags: ["index-architecture","architecture"]
pubDate: 2026-05-29
---

this plan has two exchange segments, with degree of parallelism equal to 4, it uses eight

worker threads.

For more information on the operators used in this example, see the

Showplan Logical and

Physical Operators Reference.

The query plans built for the index operations that create or rebuild an index, or drop a

clustered index, allow for parallel, multi-worker threaded operations on computers that have

multiple microprocessors.

uses the same algorithms to determine the degree of parallelism (the total number

of separate worker threads to run) for index operations as it does for other queries. The

maximum degree of parallelism for an index operation is subject to the

max degree of

parallelism

server configuration option. You can override the max degree of parallelism value

for individual index operations by setting the MAXDOP index option in the CREATE INDEX,

ALTER INDEX, DROP INDEX, and ALTER TABLE statements.

When the SQL Server Database Engine builds an index execution plan, the number of parallel

operations is set to the lowest value from among the following:

The number of microprocessors, or CPUs in the computer.

The number specified in the max degree of parallelism server configuration option.

The number of CPUs not already over a threshold of work performed for SQL Server

worker threads.

For example, on a computer that has eight CPUs, but where max degree of parallelism is set to

6, no more than six parallel worker threads are generated for an index operation. If five of the

CPUs in the computer exceed the threshold of SQL Server work when an index execution plan

is built, the execution plan specifies only three parallel worker threads.

The main phases of a parallel index operation include the following:

A coordinating worker thread quickly and randomly scans the table to estimate the

distribution of the index keys. The coordinating worker thread establishes the key

boundaries that will create a number of key ranges equal to the degree of parallel

７

Note

Parallel index operations are only available in Enterprise Edition, starting with SQL Server

2008 (10.0.x).
