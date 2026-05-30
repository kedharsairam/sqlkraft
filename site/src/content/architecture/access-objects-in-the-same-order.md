---
title: "Access objects in the same order"
topic: "query-processing"
description: "was involved in the deadlock)."
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

was involved in the deadlock).

The application should pause briefly before resubmitting its query. This gives the other

transaction involved in the deadlock a chance to complete and release its locks. Randomizing

the duration of the pause minimizes the likelihood of the deadlock reoccurring when the

resubmitted query requests its locks. For example, the error handler might be coded to pause

for a random duration between one and three seconds.

You can use

TRY...CATCH

to handle deadlocks. Error 1205 can be caught by the

block.

For more information, see

Handling Deadlocks

.

Although deadlocks can't be completely avoided, following certain coding conventions can

minimize the chance of generating a deadlock. Minimizing deadlocks can increase transaction

throughput and reduce system overhead because fewer transactions are:

Rolled back, undoing all the work performed by the transaction.

Resubmitted by applications because they were rolled back when deadlocked.

To help minimize deadlocks:

Access objects in the same order.

Avoid user interaction in transactions.

Keep transactions short and in one batch.

Avoid higher isolation levels such as

and

when not

required.

Use a row versioning-based isolation level.

Enable the

database option to use row versioning for

transactions using the

isolation level.

Use snapshot isolation transactions.

Use bound connections.

If all concurrent transactions access objects in the same order, deadlocks are less likely to

occur. For example, if two concurrent transactions obtain a lock on the

table and

then on the

table, one transaction is blocked on the

table until the other

```sql
CATCH
```

```sql
REPEATABLE READ
```

```sql
SERIALIZABLE
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
READ COMMITTED
```

```sql
Supplier
```

```sql
Part
```

```sql
Supplier
```
