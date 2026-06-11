---
title: "Modify data with optimized locking"
topic: "locking"
description: ""
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

With optimized locking enabled and with the

(RCSI) database option

enabled, and using the default

isolation level, readers don't acquire any locks,

and writers acquire short duration low-level locks, instead of locks that expire at the end of the

transaction.

Enabling RCSI is recommended for most efficiency with optimized locking. When using stricter

isolation levels such as

or

, the Database Engine holds row and

page locks until the end of the transaction, for both readers and writers, resulting in increased

blocking and lock memory.

With RCSI enabled, and when using the default

isolation level, writers qualify

rows per the predicate based on the latest committed version of the row, without acquiring

locks. A query waits only if the row qualifies and there's another active write transaction on that

row or page. Qualifying based on the latest committed version and locking only the qualified

rows reduces blocking and increases concurrency.

If update conflicts are detected with RCSI and in the default

isolation level,

they're handled and retried automatically without any impact to customer workloads.

With optimized locking enabled and when using the

isolation level, the behavior of

update conflicts is the same as without optimized locking. Update conflicts must be handled and

retried by the application.

７

Note

Update operations running under

isolation internally execute under

isolation when the

transaction accesses any of the following:

A table with a foreign key constraint.

A table that is referenced in the foreign key constraint of another table.

An indexed view referencing more than one table.

However, even under these conditions the update operation continues to verify that the data

hasn't been modified by another transaction. If data has been modified by another

transaction, the

transaction encounters an update conflict and is terminated.

Update conflicts must be handled and retried by the application.

### Query behavior changes with optimized locking and RCSI

`READ_COMMITTED_SNAPSHOT`

```sql
READ COMMITTED
```

```sql
REPEATABLE READ
```

`SERIALIZABLE`

```sql
READ COMMITTED
```

```sql
U
```

```sql
READ COMMITTED
```

`SNAPSHOT`

`SNAPSHOT`

```sql
READ
COMMITTED
```

`SNAPSHOT`

`SNAPSHOT`
