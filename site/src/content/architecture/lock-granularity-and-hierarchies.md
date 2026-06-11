---
title: "Lock granularity and hierarchies"
topic: "locking"
description: ""
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Locking is a mechanism used by the Database Engine to synchronize access by multiple users to

the same piece of data at the same time.

Before a transaction acquires a dependency on the current state of a piece of data, such as by

reading or modifying the data, it must protect itself from the effects of another transaction

modifying the same data. The transaction does this by requesting a lock on the piece of data.

Locks have different modes, such as shared (

) or exclusive (

). The lock mode defines the level

of dependency the transaction has on the data. No transaction can be granted a lock that would

conflict with the mode of a lock already granted on that data to another transaction. If a

transaction requests a lock mode that conflicts with a lock that has already been granted on the

same data, the Database Engine will pause the requesting transaction until the first lock is

released.

When a transaction modifies a piece of data, it holds certain locks protecting the modification

until the end of the transaction. How long a transaction holds the locks acquired to protect read

operations depends on the transaction isolation level setting and whether or not

optimized

locking

is enabled.

When optimized locking isn't enabled, row and page locks necessary for writes are held

until the end of the transaction.

When optimized locking is enabled, only a Transaction ID (TID) lock is held until the end of

the transaction. Under the default

isolation level, transactions won't hold

row and page locks necessary for writes until the end of the transaction. This reduces lock

memory required and reduces the need for lock escalation. Further, when optimized locking

is enabled, the

lock after qualification (LAQ)

optimization evaluates predicates of a query on

the latest committed version of the row without acquiring a lock, improving concurrency.

All locks held by a transaction are released when the transaction completes (either commits or

rolls back).

Applications don't typically request locks directly. Locks are managed internally by a part of the

Database Engine called the lock manager. When an instance of the Database Engine processes a

Transact-SQL statement, the Database Engine query processor determines which resources are to

be accessed. The query processor determines what types of locks are required to protect each

resource based on the type of access and the transaction isolation level setting. The query

processor then requests the appropriate locks from the lock manager. The lock manager grants

the locks if there are no conflicting locks held by other transactions.

The Database Engine has multigranular locking that allows different types of resources to be

locked by a transaction. To minimize the cost of locking, the Database Engine locks resources

automatically at a level appropriate to the task. Locking at a smaller granularity, such as rows,

increases concurrency but has a higher overhead because more locks must be held if many rows

are locked. Locking at a larger granularity, such as tables, are expensive in terms of concurrency

because locking an entire table restricts access to any part of the table by other transactions.

However, it has a lower overhead because fewer locks are being maintained.

The Database Engine often has to acquire locks at multiple levels of granularity to fully protect a

resource. This group of locks at multiple levels of granularity is called a lock hierarchy. For

example, to fully protect a read of an index, an instance of the Database Engine might have to

acquire shared locks on rows and intent shared locks on the pages and table.

The following table shows the resources that the Database Engine can lock.

## Description

A row identifier used to lock a single row within a heap.

A row lock to lock a single row in a B-tree index.

An 8 kilobyte (KB) page in a database, such as data or index pages.

A contiguous group of eight pages, such as data or index pages.

A heap or B-tree. A lock protecting a B-tree (index) or the heap data pages in a table that

doesn't have a clustered index.

The entire table, including all data and indexes.

A database file.

An application-specified resource.

Metadata locks.

An allocation unit.

The entire database.

Transaction ID (TID) lock used in

Optimized locking

. For more information, see

Transaction ID (TID) locking

.

and

locks can be affected by the

option of

ALTER TABLE

.

ﾉ

Expand table

1

1

2

1

```sql
S
```

```sql
X
```

```sql
READ COMMITTED
```

`RID`

`KEY`

`PAGE`

`EXTENT`

`HoBT`

`TABLE`

`FILE`

`APPLICATION`

`METADATA`

`ALLOCATION_UNIT`

`DATABASE`

`XACT`

`HoBT`

`TABLE`

`LOCK_ESCALATION`
