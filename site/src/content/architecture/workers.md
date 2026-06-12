---
title: "Workers"
topic: "query-processing"
description: "represents the unit of work that needs to be completed to fulfill the request."
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

A

task

represents the unit of work that needs to be completed to fulfill the request. One or

more tasks can be assigned to a single request.

Parallel requests have several active tasks that are executed concurrently instead of

serially, with one

parent task

(or coordinating task) and multiple

child tasks. An execution

plan for a parallel request may have serial branches - areas of the plan with operators that

don't execute in parallel. The parent task is also responsible for executing those serial

operators.

Serial requests only have one active task at any given point in time during execution.

Tasks exist in various states throughout their lifetime. For more information about task

states, see

sys.dm_os_tasks. Tasks in SUSPENDED state are waiting on resources required

to execute the task to become available. For more information about waiting tasks, see

sys.dm_os_waiting_tasks.

A SQL Server

worker thread

, also known as worker or thread, is a logical representation of an

operating system thread. When executing

serial requests

, the SQL Server Database Engine

spawns a worker to execute the active task (1:1). When executing

parallel requests

in

row mode

,

the SQL Server Database Engine assigns a worker to coordinate the child workers responsible

for completing tasks assigned to them (also 1:1), called the

parent thread

(or coordinating

thread). The parent thread has a parent task associated with it. The parent thread is the point

of entry of the request and exists even before engine parses a query. The main responsibilities

of the parent thread are:

Coordinate a parallel scan.

Start parallel child workers.

Collect rows from parallel threads and send to the client.

Perform local and global aggregations.

The number of worker threads spawned for each task depends on:

Whether the request was eligible for parallelism as determined by the Query Optimizer.

７

Note

If a query plan has serial and parallel branches, one of the parallel tasks will be responsible

for executing the serial branch.

### max degree of parallelism (MAXDOP)

### Configure the max degree of parallelism Server Configuration Option
