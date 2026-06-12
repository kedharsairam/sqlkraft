---
name: "ONLINE option"
title: "ONLINE option"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

## Resumable index operations

index is disabled, the

operation must be performed with

set to. If a nonclustered index is disabled and isn't associated with a disabled

clustered index, the

operation can be performed with

set to

or.

The following guidelines apply for performing index operations online:

The underlying table can't be altered, truncated, or dropped while an online index

operation is in process.

Additional temporary disk space is required during the index operation.

Online operations can be performed on partitioned indexes and indexes that contain

persisted computed columns, or included columns.

The

argument option allows you to decide how the index

operation proceeds when it waits for a

lock. For more information, see

WAIT_AT_LOW_PRIORITY

For more information, see

Perform index operations online.

: SQL Server 2019 (15.x) and later versions, Azure SQL Database, SQL database in

Microsoft Fabric, and Azure SQL Managed Instance

You can make an online index create operation resumable. That means that the index build can

be stopped and later restarted from the point where it stopped. To run an index build as

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

７

Note

When indexes with 128 extents or more are dropped or rebuilt, the Database Engine

defers the actual page deallocations, and their associated locks, until after the transaction

commits. For more information, see.

The

option can be specified in two contexts:

for the

option specifies the time interval for an index being

rebuilt. After this time elapses, and if the index rebuild is still running, it is paused. You

decide when the rebuild for a paused index can be resumed. The

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

statement with the same parameters resumes a

paused index build operation. You can also resume a paused index build operation by

executing the

statement.

The

command kills the session that is running an index build and cancels the index

operation. You cannot resume an index operation that has been aborted.

A resumable index operation runs until it completes, pauses, or fails. In case the operation

pauses, an error is issued indicating that the operation was paused and that the index creation

did not complete. In case the operation fails, an error is issued as well.

To see if an index operation is executed as a resumable operation and to check its current

execution state, use the

sys.index_resumable_operations

catalog view.

The following resources are required for resumable index operations:

Additional space required to keep the index being built, including the time when build is

paused.

Additional log throughput during the sorting phase. The overall log space usage for

resumable index is less compared to regular online index create and allows log truncation

during this operation.

DDL statements attempting to modify the table associated with the index being created

while the index operation is paused aren't allowed.

Ghost cleanup is blocked on the in-build index for the duration of the operation both

while paused and while the operation is running.

### Applies to

## Current functional limitations

## WAIT_AT_LOW_PRIORITY with online index operations

If the table contains LOB columns, a resumable clustered index build requires a schema

modification (

) lock at the start of the operation.

Resumable index create operations have the following limitations:

After a resumable online index create operation is paused, the initial value of

can't

be changed.

The

option isn't supported for resumable index operations.

The DDL command with

can't be executed inside an explicit transaction.

You cannot create an index using a resumable index operation if the index contains:

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

Filtered indexes

Disabled indexes

: SQL Server 2022 (16.x) and later versions, Azure SQL Database, SQL database in

Microsoft Fabric, and Azure SQL Managed Instance

When you don't use the

option, all active blocking transactions holding

locks on the table or index must complete for the index create operation to start and to

complete. When the online index operation starts and before it completes, it needs to acquire

a shared (

) or a schema modification (

) lock on the table and hold it for a short time.

Even though the lock is held for a short time only, it might significantly affect workload

throughput, increase query latency, or cause execution timeouts.

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

```sql
CREATE INDEX WITH DROP_EXISTING
```

`ONLINE`

`OFF`

```sql
CREATE INDEX WITH DROP_EXISTING
```

`ONLINE`

`OFF`

`ON`

`WAIT_AT_LOW_PRIORITY`

```sql
Sch-M
```

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
CREATE INDEX
```

```sql
ALTER INDEX RESUME
```

`ABORT`

```sql
Sch-M
```

`MAXDOP`

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
