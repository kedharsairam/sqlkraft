---
title: "Work with lock partitioning"
topic: "locking"
description: "Lock partitioning is enabled automatically on the Database Engine instances with a larger number"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Lock partitioning is enabled automatically on the Database Engine instances with a larger number

of logical CPUs. When lock partitioning is enabled, an informational message is recorded in the

error log.

When acquiring locks on a partitioned resource:

Only

,

,

,

, and

lock modes are acquired on a single partition.

Shared (

), exclusive (

), and other locks in modes other than

,

,

,

, and

must be acquired on all partitions starting with partition ID 0 and following in partition ID

order. These locks on a partitioned resource use more memory than locks in the same mode

on a nonpartitioned resource since each partition is effectively a separate lock. The memory

increase is determined by the number of partitions. The Database Engine lock performance

counters display information about memory used by partitioned and nonpartitioned locks.

A transaction is assigned to a lock partition when the transaction starts. For the transaction, all

lock requests that can be partitioned use the partition assigned to that transaction. By this

method, access to lock resources of the same object by different transactions is distributed across

different partitions.

The

column in the

Dynamic Management View

provides the lock partition ID for a lock partitioned resource. For more information, see

sys.dm_tran_locks (Transact-SQL).

Because more lock resources are acquired with lock partitioning, the likelihood of

deadlocks

might increase when this feature is enabled and a resource, such as a database or a table, is

accessed by multiple concurrent sessions. An increase in the number of deadlocks due to lock

partitioning is not common. As with all deadlocks, applications should follow best practices for

deadlock detection and resolution. For more information, see

Handle deadlocks.

The following code examples illustrate lock partitioning. In the examples, two transactions are

executed in two different sessions in order to show lock partitioning behavior on a computer

system with 16 CPUs.

These Transact-SQL statements create test objects that are used in the examples that follow.

`NL`

```sql
Sch-S
```

`IS`

`IU`

`IX`

```sql
S
```

```sql
X
```

`NL`

```sql
Sch-S
```

`IS`

`IU`

`IX`

`resource_lock_partition`

`sys.dm_tran_locks`

```sql
-- Create a test table.
CREATE
TABLE
TestTable
```
