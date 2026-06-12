---
title: "Understand deadlocks"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This article discusses deadlocks in the Database Engine in depth. Deadlocks are caused by

competing, concurrent locks in the database, often in multi-step transactions. For more

information about transactions and locks, see

Transaction locking and row versioning guide.

For more specific information on identification and prevention of deadlocks in Azure SQL

Database and SQL database in Fabric, see

Analyze and prevent deadlocks in Azure SQL

Database and SQL database in Fabric.

A deadlock occurs when two or more tasks permanently block each other by each task having

a lock on a resource that the other tasks are trying to lock. For example:

Transaction A acquires a shared lock on row 1.

Transaction B acquires a shared lock on row 2.

Transaction A now requests an exclusive lock on row 2, and is blocked until transaction B

finishes and releases the shared lock it has on row 2.

Transaction B now requests an exclusive lock on row 1, and is blocked until transaction A

finishes and releases the shared lock it has on row 1.

Transaction A can't complete until transaction B completes, but transaction B is blocked by

transaction A. This condition is also called a cyclic dependency: Transaction A has a

dependency on transaction B, and transaction B closes the circle by having a dependency on

transaction A.

Both transactions in a deadlock wait forever, unless the deadlock is broken by an external

process. The Database Engine deadlock monitor periodically checks for tasks that are in a

deadlock. If the monitor detects a cyclic dependency, it chooses one of the tasks as a victim

and terminates its transaction with an error. This allows the other task to complete its

transaction. The application with the transaction that terminated with an error can retry the

transaction, which usually completes after the other deadlocked transaction finishes.

Deadlocking is often confused with normal blocking. When a transaction requests a lock on a

resource locked by another transaction, the requesting transaction waits until the lock is

released. By default, transactions in the Database Engine don't time out, unless

is

set. The requesting transaction is blocked, not deadlocked, because the requesting transaction

hasn't done anything to block the transaction owning the lock. Eventually, the owning

transaction completes and releases the lock, and then the requesting transaction is granted the

lock and proceeds. Deadlocks are resolved almost immediately, whereas blocking can, in

theory, persist indefinitely. Deadlocks are sometimes called a deadly embrace.

A deadlock can occur on any system with multiple threads, not just on a relational database

management system, and can occur for resources other than locks on database objects. For

example, a thread in a multithreaded operating system might acquire one or more resources,

such as blocks of memory. If the resource being acquired is currently owned by another thread,

the first thread might have to wait for the owning thread to release the target resource. The

waiting thread is said to have a dependency on the owning thread for that particular resource.

In an instance of the Database Engine, sessions can deadlock when acquiring non-database

resources, such as memory or threads.

In the illustration, transaction T1 has a dependency on transaction T2 for the

table lock

resource. Similarly, transaction T2 has a dependency on transaction T1 for the

table

lock resource. Because these dependencies form a cycle, there's a deadlock between

transactions T1 and T2.

Here's a more general illustration of a deadlock:

Task T1 has a lock on resource R1 (indicated by the arrow from R1 to T1), and has

requested a lock on resource R2 (indicated by the arrow from T1 to R2).

Task T2 has a lock on resource R2 (indicated by the arrow from R2 to T2), and has

requested a lock on resource R1 (indicated by the arrow from T2 to R1).

## Locks

## Worker threads

## Memory

## Parallel query execution-related resources

Because neither task can continue until a resource is available and neither resource can be

released until a task continues, a deadlock state exists.

Each user session might have one or more tasks running on its behalf where each task might

acquire or wait to acquire resources. The following types of resources can cause blocking that

could result in a deadlock. Waiting to acquire locks on resources, such as objects, pages, rows, metadata, and

applications can cause a deadlock. For example, transaction T1 has a shared (

) lock on

row r1 and is waiting to get an exclusive (

) lock on r2. Transaction T2 has a shared (

)

lock on r2 and is waiting to get an exclusive (

) lock on row r1. This results in a lock cycle

in which T1 and T2 wait for each other to release the locked resources. A queued task waiting for an available worker thread can cause a

deadlock. If the queued task owns resources that are blocking all worker threads, a

deadlock results. For example, session S1 starts a transaction and acquires a shared (

)

lock on row r1 and then goes to sleep. Active sessions running on all available worker

threads are trying to acquire exclusive (

) locks on row r1. Because session S1 can't

acquire a worker thread, it can't commit the transaction and release the lock on row r1.

This results in a deadlock. When concurrent requests are waiting for memory grants that can't be satisfied

with the available memory, a deadlock can occur. For example, two concurrent queries,

Q1 and Q2, execute as user-defined functions that acquire 10 MB and 20 MB of memory

respectively. If each query needs 30 MB and the total available memory is 20 MB, then Q1

and Q2 must wait for each other to release memory, which results in a deadlock. Coordinator, producer, or consumer threads

associated with an exchange port might block each other causing a deadlock usually

when including at least one other process that isn't a part of the parallel query. Also,

when a parallel query starts execution, the Database Engine determines the degree of

parallelism, and the number of required worker threads, based upon the current

workload. If the system workload unexpectedly changes, for example, where new queries

７

Note

The Database Engine automatically detects deadlock cycles. It chooses one of the

transactions as a deadlock victim and terminates it with an error to break the deadlock.

## Multiple Active Result Sets (MARS) resources

## User resource

## Session mutex

## Transaction mutex

start running on the server or the system runs out of worker threads, then a deadlock

could occur. These resources are used to control

interleaving of multiple active requests under MARS. For more information, see

Using

Multiple Active Result Sets (MARS) in SQL Server Native Client. When a thread is waiting for a resource that is potentially controlled by

a user application, the resource is considered to be an external or user resource and is

treated like a lock. The tasks running in one session are interleaved, meaning that only

one task can run under the session at a given time. Before the task can run, it must

have exclusive access to the session mutex. All tasks running in one transaction are interleaved, meaning that

only one task can run under the transaction at a given time. Before the task can run, it

must have exclusive access to the transaction mutex.

In order for a task to run under MARS, it must acquire the session mutex. If the task is

running under a transaction, it must then acquire the transaction mutex. This

guarantees that only one task is active at one time in a given session and a given

transaction. Once the required mutexes have been acquired, the task can execute.

When the task finishes, or yields in the middle of the request, it first releases the

transaction mutex, followed by the session mutex, in reverse order of acquisition.

However, deadlocks can occur with these resources. In the following pseudocode, two

tasks, user request U1 and user request U2, are running in the same session.

Output

The stored procedure executing from user request U1 has acquired the session mutex.

If the stored procedure takes a long time to execute, it's assumed by the Database

Engine that the stored procedure is waiting for input from the user. User request U2 is

waiting for the session mutex while the user is waiting for the result set from U2, and

U1 is waiting for a user resource. This is deadlock state logically illustrated as:

Deadlocks can also occur when a table is partitioned and the

setting of

is set to. When

is set to

, concurrency increases by allowing

the Database Engine to lock table partitions at the HoBT level instead of at the table level.

`LOCK_TIMEOUT`

`Part`

`Supplier`

```sql
S
```

```sql
X
```

```sql
S
```

```sql
X
```

```sql
S
```

```sql
X
```

`LOCK_ESCALATION`

```sql
ALTER
TABLE
```

`AUTO`

`LOCK_ESCALATION`

`AUTO`

```sql
U1: Rs1=Command1.Execute("insert sometable EXEC usp_someproc");
U2: Rs2=Command2.Execute("select colA from sometable");
```
