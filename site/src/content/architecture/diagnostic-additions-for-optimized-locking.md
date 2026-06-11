---
title: "Diagnostic additions for optimized locking"
topic: "locking"
description: ""
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

The following improvements help you monitor and troubleshoot blocking and deadlocks when

optimized locking is enabled:

Wait types for optimized locking

wait types for the

lock on the TID, and resource descriptions in

sys.dm_os_wait_stats

:

- Occurs when a task is waiting for a shared lock on an

type, with an intent to read.

- Occurs when a task is waiting for a shared lock on an

type, with an intent to modify.

- Occurs when a task is waiting for a shared lock on an

type, where the intent can't be inferred. This scenario isn't common.

Locking resources visibility

locking resources. For more information, see

in

sys.dm_tran_locks

.

Wait resource visibility

wait resources. For more information, see

in

sys.dm_exec_requests

.

Deadlock graph

Under each resource in the deadlock report

, each

element reports the underlying resources and specific information for locks of each

member of a deadlock. For more information and an example, see

Optimized locking

and deadlocks

.

Extended events

The

event fires when a statement is internally reprocessed

because of a conflict with another transaction. For more information, see

Lock after

qualification (LAQ)

.

The

event fires for every database every several minutes and provides

aggregate locking statistics for the time interval, such as the number of lock

escalations, whether TID locking and LAQ components of optimized locking are

Even without LAQ, applications shouldn't assume that the database engine guarantees

strict ordering without using locking hints when row versioning based isolation levels are

used. Our general recommendation for customers running concurrent workloads under

RCSI that rely on strict execution order of transactions (as shown in the previous example)

is to

such as

and

.

`XACT`

```sql
S
```

`LCK_M_S_XACT_READ`

```sql
XACT wait_resource
```

`LCK_M_S_XACT_MODIFY`

```sql
XACT wait_resource
```

`LCK_M_S_XACT`

```sql
XACT wait_resource
```

`XACT`

`resource_description`

`XACT`

`wait_resource`

```sql
<resource-list>
```

```sql
<xactlock>
```

`lock_after_qual_stmt_abort`

`locking_stats`

```sql
REPEATABLE READ
```

`SERIALIZABLE`
