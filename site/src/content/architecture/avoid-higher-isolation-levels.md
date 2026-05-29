---
title: 'Avoid higher isolation levels'
topic: 'io-fundamentals'
description: 'transaction is completed. After the first transaction commits or rolls back, the second'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

transaction is completed. After the first transaction commits or rolls back, the second

continues, and a deadlock doesn't occur. Using stored procedures for all data modifications

can standardize the order of accessing objects.

Avoid transactions that include user interaction, because the speed of batches running without

user intervention is much faster than the speed at which a user must manually respond to

queries, such as replying to a prompt for a parameter requested by an application. This

degrades system throughput because any locks held by the transaction are released only when

the transaction is committed or rolled back. Even if a deadlock doesn't occur, other

transactions accessing the same resources are blocked while waiting for the transaction to

complete.

A deadlock typically occurs when several long-running transactions execute concurrently in the

same database. The longer the transaction, the longer the exclusive or update locks are held,

blocking other activity and leading to possible deadlock situations.

Keeping transactions in one batch minimizes network roundtrips during a transaction, reducing

possible delays in completing the transaction due to client processing.

Determine whether a transaction can run at a lower isolation level. Using

allows a transaction to read data previously read (but not modified) by another transaction

without waiting for the transaction to complete.

holds shared locks for a

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```
