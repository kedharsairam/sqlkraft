---
title: 'Schedule of parallel tasks'
topic: 'thread-task'
description: '### AdventureWorks2016_EXT sample'
tags: ["thread-task", "architecture"]
pubDate: 2026-05-29
---

### AdventureWorks2016_EXT sample

### database

In this scenario and up to SQL Server 2014 (12.x), Worker 1 is allowed to basically monopolize

the scheduler by having more overall quantum time.

Starting with SQL Server 2016 (13.x), cooperative scheduling includes Large Deficit First (LDF)

scheduling. With LDF scheduling, quantum usage patterns are monitored and one worker

thread doesn't monopolize a scheduler. In the same scenario, Worker 2 is allowed to consume

repeated quantum's before Worker 1 is allowed more quantum, therefore preventing Worker 1

from monopolizing the scheduler in an unfriendly pattern.

Imagine a SQL Server configured with MaxDOP 8, and CPU Affinity is configured for 24 CPUs

(schedulers) across NUMA nodes 0 and 1. Schedulers 0 through 11 belong to NUMA node 0,

schedulers 12 through 23 belong to NUMA node 1. An application sends the following query

(request) to the Database Engine:

SQL

The execution plan shows a

Hash Join

between two tables, and each of the operators executed

in parallel, as indicated by the yellow circle with two arrows. Each Parallelism operator is a

different branch in the plan. Therefore, there are three branches in the following execution

plan.



Tip

The example query can be executed using the

database. The tables

and

were

enlarged 50 times and renamed to

and

.

### Showplan Logical and Physical Operators

### Reference

While there are three branches in the execution plan, at any point during execution only two

branches can execute concurrently in this execution plan:

1. The branch where a

Clustered Index Scan

is used on the

(build input of the join) executes alone.

2. Then, the branch where a

Clustered Index Scan

is used on the

(probe input of the join) executes concurrently with the branch where the

Bitmap

was

created and currently the

Hash Match

is executing.

The Showplan XML shows that 16 worker threads were reserved and used on NUMA node 0:

XML

Thread reservation ensures the Database Engine has enough worker threads to carry out all the

tasks that are needed for the request. Threads can be reserved across several NUMA nodes, or

be reserved in just one NUMA node. Thread reservation is done at runtime before execution

starts, and is dependent on scheduler load. The number of reserved worker threads is

generically derived from the formula

and excludes the

parent worker thread. Each branch is limited to a number of worker threads that's equal to

MaxDOP. In this example there are two concurrent branches and MaxDOP is set to 8, therefore

.

７

Note

If you think of an execution plan as a tree, a

branch

is an area of the plan that groups one

or more operators between Parallelism operators, also called Exchange Iterators. For more

information about plan operators, see

.

For reference, observe the live execution plan from

Live Query Statistics

, where one branch has

completed and two branches are executing concurrently.

The SQL Server Database Engine assigns a worker thread to execute an active task (1:1), which

can be observed during query execution by querying the

sys.dm_os_tasks

DMV, as seen in the

following example:

SQL

Here's the result set. Notice there are 17 active tasks for the branches that are currently

executing: 16 child tasks corresponding to the reserved threads, plus the parent task, or

coordinating task.

NULL

SUSPENDED

3

0x000001EFE6CB6160



Tip

The column

is always NULL for the parent task.



Tip

On a very busy SQL Server Database Engine, it's possible to see a number of active tasks

that's over the limit set by reserved threads. These tasks can belong to a branch that is not

being used anymore and are in a transient state, waiting for cleanup.

ﾉ

Expand table

0x000001EF4758ACA8

0x000001EFE43F3468

SUSPENDED

0

0x000001EF6DB70160

0x000001EF4758ACA8

0x000001EEB243A4E8

SUSPENDED

0

0x000001EF6DB7A160

0x000001EF4758ACA8

0x000001EC86251468

SUSPENDED

5

0x000001EEC05E8160

0x000001EF4758ACA8

0x000001EFE3023468

SUSPENDED

5

0x000001EF6B46A160

0x000001EF4758ACA8

0x000001EFE3AF1468

SUSPENDED

6

0x000001EF6BD38160

0x000001EF4758ACA8

0x000001EFE4AFCCA8

SUSPENDED

6

0x000001EF6ACB4160

0x000001EF4758ACA8

0x000001EFDE043848

SUSPENDED

7

0x000001EEA18C2160

0x000001EF4758ACA8

0x000001EF69038108

SUSPENDED

7

0x000001EF6AEBA160

0x000001EF4758ACA8

0x000001EFCFDD8CA8

SUSPENDED

8

0x000001EFCB6F0160

0x000001EF4758ACA8

0x000001EFCFDD88C8

SUSPENDED

8

0x000001EF6DC46160

0x000001EF4758ACA8

0x000001EFBCC54108

SUSPENDED

9

0x000001EFCB886160

0x000001EF4758ACA8

0x000001EC86279468

SUSPENDED

9

0x000001EF6DE08160

0x000001EF4758ACA8

0x000001EFDE901848

SUSPENDED

10

0x000001EFF56E0160

0x000001EF4758ACA8

0x000001EF6DB32108

SUSPENDED

10

0x000001EFCC3D0160

0x000001EF4758ACA8

0x000001EC8628D468

SUSPENDED

11

0x000001EFBFA4A160

0x000001EF4758ACA8

0x000001EFBD3A1C28

SUSPENDED

11

0x000001EF6BD72160

Observe that each of the 16 child tasks has a different worker thread assigned (seen in the

column), but all the workers are assigned to the same pool of eight schedulers

(0,5,6,7,8,9,10,11), and that the parent task is assigned to a scheduler outside this pool (3).

）

Important

Once the first set of parallel tasks on a given branch is scheduled, the Database Engine will

use that same pool of schedulers for any additional tasks on other branches. This means

the same set of schedulers will be used for all the parallel tasks in the entire execution

plan, only limited by MaxDOP.

The SQL Server Database Engine will always try to assign schedulers from the same NUMA

node for task execution, and assign them sequentially (in round-robin fashion) if

### sys.dm_os_waiting_tasks

```sql
SELECT
h.SalesOrderID,
h.OrderDate,
h.DueDate,
h.ShipDate
FROM
Sales.SalesOrderHeaderBulk
AS
h
INNER
JOIN
Sales.SalesOrderDetailBulk
AS
d
ON
h.SalesOrderID = d.SalesOrderID
WHERE
(h.OrderDate >=
'2014-3-28 00:00:00'
);
```

```sql
Sales.SalesOrderHeader
```

```sql
Sales.SalesOrderDetail
```

```sql
Sales.SalesOrderHeaderBulk
```

```sql
Sales.SalesOrderDetailBulk
```

```sql
Sales.SalesOrderHeaderBulk
```

```sql
Sales.SalesOrderDetailBulk
```

```sql
concurrent branches * runtime DOP
```

```sql
2 * 8 = 16
```

```sql
<ThreadStat
Branches
=
"2"
UsedThreads
=
"16"
>
<ThreadReservation
NodeId
=
"0"
ReservedThreads
=
"16"
/>
</ThreadStat>
```

```sql
0x000001EF4758ACA8
```

```sql
SELECT
parent_task_address, task_address,
task_state, scheduler_id, worker_address
FROM
sys.dm_os_tasks
WHERE
session_id = <insert_session_id>
ORDER
BY
parent_task_address, scheduler_id;
```

```sql
parent_task_address
```

```sql
worker_address
```
