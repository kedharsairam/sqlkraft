---
name: "Online index operations"
title: "Online index operations"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: 2026-05-29
---

If

is specified when the row or page lock options are set, the settings are applied to all

indexes. When the underlying table is a heap, the settings are applied in the following ways:

or

The heap and all associated nonclustered indexes.

The heap and all associated nonclustered indexes.

The nonclustered indexes, where all page locks aren't allowed. For the heap, only

the shared (

), update (

) and exclusive (

) page locks aren't allowed. The

Database Engine can still acquire intent page locks (

,

, or

) for internal

purposes.

When rebuilding an index and the

option is set to

, data in the index, its associated

table, and other indexes on the same table is available for queries and modification. You can

also rebuild online a portion of an index residing on a single partition. Exclusive table locks are

held only for a short amount of time at the end of the index rebuild.

Reorganizing an index is always performed online. The process holds locks only for short

periods of time and is unlikely to block queries or updates.

You can perform concurrent online index operations on the same table or table partition only

when doing the following operations:

Creating multiple nonclustered indexes.

Reorganizing different indexes on the same table.

Reorganizing different indexes while rebuilding nonoverlapping indexes on the same

table.

Expand table

２

Warning

It is not recommended to disable row or page locks on an index. Concurrency-related

problems might occur, and certain functionality might be unavailable. For example, an

index can't be reorganized when

is set to.

### Applies to

## Resumable index operations

All other online index operations performed at the same time fail. For example, you can't

rebuild two or more indexes on the same table concurrently, or create a new index while

rebuilding an existing index on the same table.

For more information, see

Perform index operations online.

: SQL Server 2017 (14.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

You can make an online index rebuild resumable. That means that the index rebuild can be

stopped and later restarted from the point where it stopped. To run an index rebuild as

resumable, specify the

option.

The following guidelines apply to resumable index operations:

To use the

option you must also use the

option.

The

option isn't persisted in the metadata for a given index and applies only to

the duration of the current DDL statement. Therefore, the

clause must be

specified explicitly to enable resumability.

The

option can be specified in two contexts:

for the

option specifies the time interval for an index being

built. After this time elapses, and if the index build is still running, it is paused. You

decide when the build for a paused index can be resumed. The

in minutes for

must be greater than 0 minutes and less than or equal to one week (7 \*

24 \* 60 = 10080 minutes). A long pause in an index operation might noticeably impact

the DML performance on a specific table as well as the database disk capacity since

both the original index and the newly created index require disk space and need to be

updated by DML operations. If

option is omitted, the index operation

continues until completion or until a failure occurs.

for the

option specifies the time to wait using low

priority locks if the index operation is blocked, before taking action. For more

information, see

WAIT_AT_LOW_PRIORITY with online index operations.

To pause the index operation immediately, you can execute the

command, or execute the

command.

Re-executing the original

statement with the same parameters

resumes a paused index rebuild operation. You can also resume a paused index rebuild

operation by executing the

statement.

The

command kills the session that is running an index build and cancels the index

operation. You cannot resume an index operation that has been aborted.

## Current functional limitations

When resuming an index rebuild operation that is paused, you can change the

value to a new value. If

isn't specified when resuming an index operation that is

paused, the

value used for the last resume is used. If the

option isn't

specified at all for an index rebuild operation, then the default value is used.

A resumable index operation runs until it completes, pauses, or fails. In case the operation

pauses, an error is issued indicating that the operation was paused and that the index rebuild

did not complete. In case the operation fails, an error is issued as well.

To see if an index operation is executed as a resumable operation and to check its current

execution state, use the

sys.index_resumable_operations

catalog view.

The following resources are required for resumable index operations:

Additional space required to keep the index being built, including the time when build is

paused.

Additional log throughput during the sorting phase. The overall log space usage for

resumable index is less compared to regular online index rebuild and allows log

truncation during this operation.

DDL statements attempting to modify an index that is being rebuild or its associated

table while the index operation is paused aren't allowed.

Ghost cleanup is blocked on the in-build index for the duration of the operation both

while paused and while the operation is running.

If the table contains LOB columns, a resumable clustered index build requires a schema

modification (

) lock at the start of the operation.

Resumable index rebuild operations have the following limitations:

The

option isn't supported for resumable index operations.

The DDL command with

can't be executed inside an explicit transaction.

You cannot rebuild an index using a resumable index operation if the index contains:

A computed or

(

) column as a key column.

A computed or LOB column as an included column.

Resumable index operations aren't supported for:

The

command

The

command

Columnstore indexes

### Applies to

## WAIT_AT_LOW_PRIORITY with online index operations

Filtered indexes

Disabled indexes

: SQL Server 2014 (12.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

When you don't use the

option, all active blocking transactions holding

locks on the table or index must complete for the index rebuild operation to start and to

complete. When the online index operation starts and before it completes, it needs to acquire

a shared (

) or a schema modification (

) lock on the table and hold it for a short time.

Even though the lock is held for a short time only, it might significantly affect workload

throughput, increase query latency, or cause execution time-outs.

To avoid these problems, the

option allows you to manage the behavior

of

or

locks required for an online index operation to start and complete, selecting

from three options. In all cases, if during the wait time specified by

there is no blocking that involves the index operation, the index operation proceeds

immediately.

makes the online index operation wait using low priority locks, allowing

other operations using normal priority locks to proceed in the meantime. Omitting the

option is equivalent to.

=

time

[

]

The wait time (an integer value specified in minutes) that the online index operation waits

using low priority locks. If the operation is blocked for the

time, the specified

action is executed.

time is always in minutes, and the word

can be omitted.

= [

|

|

]

: Continue waiting for the lock with normal priority.

: Exit the online index operation currently being executed, without taking any action.

The option

can't be used when

is 0.

: Kill all user transactions that block the online index operation so that the

operation can continue. The

option requires the principal executing the

or

statement to have the

permission.

`ALL`

```sql
ALLOW_ROW_LOCKS =
ON
```

`OFF`

```sql
ALLOW_PAGE_LOCKS =
ON
```

```sql
ALLOW_PAGE_LOCKS =
OFF
```

```sql
S
```

```sql
U
```

```sql
X
```

`IS`

`IU`

`IX`

`ONLINE`

`ON`

`ALLOW_PAGE_LOCKS`

`OFF`

```sql
RESUMABLE = ON
```

`RESUMABLE`

`ONLINE`

`RESUMABLE`

```sql
RESUMABLE = ON
```

`MAX_DURATION`

`MAX_DURATION`

`RESUMABLE`

`MAX_DURATION`

`MAX_DURATION`

`MAX_DURATION`

`WAIT_AT_LOW_PRIORITY`

```sql
ALTER INDEX PAUSE
```

```sql
KILL <session_id>
```

```sql
ALTER INDEX REBUILD
```

```sql
ALTER INDEX RESUME
```

`ABORT`

`MAXDOP`

`MAXDOP`

`MAXDOP`

`MAXDOP`

```sql
Sch-M
```

```sql
SORT_IN_TEMPDB = ON
```

```sql
RESUMABLE = ON
```

`timestamp`

`rowversion`

```sql
ALTER INDEX REBUILD ALL
```

```sql
ALTER TABLE REBUILD
```

`WAIT_AT_LOW_PRIORITY`

```sql
S
```

```sql
Sch-M
```

`WAIT_AT_LOW_PRIORITY`

```sql
S
```

```sql
Sch-M
```

```sql
MAX_DURATION = n
[minutes]
```

`WAIT_AT_LOW_PRIORITY`

`WAIT_AT_LOW_PRIORITY`

```sql
WAIT_AT_LOW_PRIORITY (MAX_DURATION = 0 minutes, ABORT_AFTER_WAIT = NONE)
```

`MAX_DURATION`

`MINUTES`

`MAX_DURATION`

`ABORT_AFTER_WAIT`

`MAX_DURATION`

`MINUTES`

`ABORT_AFTER_WAIT`

`NONE`

`SELF`

`BLOCKERS`

`NONE`

`SELF`

`SELF`

`MAX_DURATION`

`BLOCKERS`

`BLOCKERS`

```sql
CREATE
INDEX
```

```sql
ALTER INDEX
```

```sql
ALTER ANY CONNECTION
```
