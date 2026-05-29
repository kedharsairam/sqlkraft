---
title: 'Behavior in summary'
topic: 'io-fundamentals'
description: 'The following table summarizes the differences between'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

The following table summarizes the differences between

isolation and

isolation using row versioning.

The database

option that

must be set to

to enable

the required

support.

How a session

requests the

specific type of

row versioning.

Use the default

isolation

level, or run the

statement to specify the

isolation level. This can be done

after the transaction starts.

Requires the execution of

to specify the

isolation level before the start of the

transaction.

The version of

data read by

statements.

All data that was committed before the

start of each statement.

All data that was committed before the

start of each transaction.

How updates

are handled.

Reverts from

row versions to actual data to select rows

to update and uses update locks on the

data rows selected. Acquires exclusive locks

on actual data rows to be modified. No

update conflict detection.

Rows are selected

based on the last committed version

without any locks being acquired. If rows

qualify for the update, exclusive row or

page locks are acquired. If update conflicts

are detected, they're handled and retried

automatically.

Uses row versions to select rows to update.

Tries to acquire an exclusive lock on the

actual data row to be modified, and if the

data has been modified by another

transaction, an update conflict occurs and

the snapshot transaction is terminated.

７

Note

For more information on behavior changes with the lock after qualification (LAQ) feature of

optimized locking, see

.

ﾉ

Expand table

```sql
SNAPSHOT
```

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

```sql
SNAPSHOT
```

```sql
ON
```

```sql
READ_COMMITTED_SNAPSHOT
ALLOW_SNAPSHOT_ISOLATION
```

```sql
READ COMMITTED
```

```sql
SET TRANSACTION ISOLATION
LEVEL
```

```sql
READ
COMMITTED
```

```sql
SET TRANSACTION
ISOLATION LEVEL
```

```sql
SNAPSHOT
```
