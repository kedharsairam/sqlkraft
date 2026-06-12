---
title: "Skip index locks (SIL)"
topic: "index-architecture"
description: "With TID locking, short-duration exclusive ("
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

With TID locking, short-duration exclusive (

) row locks and intent-exclusive (

) page locks

are used to modify rows. When RCSI and LAQ are used, these locks are only necessary if there

could be other queries accessing the row and expecting it to be stable. Examples of such

queries are those running under the

or

isolation levels, or using

the corresponding locking hints. Such queries are known as

row locking queries

(RLQ).

When there are no RLQ queries accessing a row, the database engine can skip taking row and

page locks when modifying a row, and use only an exclusive page

latch. This optimization

reduces the locking overhead while preserving ACID transaction semantics. Skipping row and

page locks particularly benefits transactions modifying a large number of rows.

Currently, the SIL optimization is used in the following cases only:

statements on heaps.

page locks are skipped.

statements on clustered indexes, nonclustered indexes, and heaps.

page locks and

row locks are skipped.

The SIL optimization isn't currently used in the following cases:

statements.

statements on heaps if the row contains existing forwarding pointers or if new

forwarding pointers are added by the update.

If the modified row has any columns using the LOB data types, such as

,

,

, and.

For rows on pages that were split in the same transaction.

### query plan

### database

```sql
SET b = b + 10
WHERE a = 1;
BEGIN TRANSACTION;
UPDATE t3
SET b = b + 10
WHERE a = 1;
COMMIT TRANSACTION;
COMMIT TRANSACTION;
```

```sql
X
```

`IX`

```sql
REPEATABLE READ
```

`SERIALIZABLE`

`INSERT`

`IX`

`UPDATE`

`IX`

```sql
X
```

`DELETE`

`UPDATE`

`varchar(max)`

`nvarchar(max)`

`varbinary(max)`

`json`
