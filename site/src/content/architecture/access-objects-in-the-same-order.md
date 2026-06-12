---
title: "Access objects in the same order"
topic: "query-processing"
description: "Access objects in consistent order to minimize deadlocks in concurrent transactions."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

If all concurrent transactions access objects in the same order, deadlocks are less likely to occur. For example, if two concurrent transactions obtain a lock on the `Supplier` table and then on the `Part` table, one transaction is blocked on the `Part` table until the other completes.

## Minimizing deadlocks

To help minimize deadlocks:

- **Access objects in the same order.** If all concurrent transactions access objects in the same order, deadlocks are less likely to occur.
- **Avoid user interaction in transactions.** User interaction during a transaction significantly increases lock duration and deadlock probability.
- **Keep transactions short and in one batch.** Short transactions reduce lock contention.
- **Avoid higher isolation levels** such as `REPEATABLE READ` and `SERIALIZABLE` when not required. Use row versioning-based isolation levels when possible.
- **Enable `READ_COMMITTED_SNAPSHOT`** database option to use row versioning for transactions using the `READ COMMITTED` isolation level.
- **Use snapshot isolation transactions.**
- **Use bound connections.**

## Deadlock handling

Although deadlocks cannot be completely avoided, following certain coding conventions can minimize the chance of generating a deadlock. Minimizing deadlocks can increase transaction throughput and reduce system overhead because fewer transactions are:

- Rolled back, undoing all the work performed by the transaction.
- Resubmitted by applications because they were rolled back when deadlocked.

When a deadlock occurs (error 1205), the application should pause briefly before resubmitting its query. This gives the other transaction involved in the deadlock a chance to complete and release its locks. Randomizing the duration of the pause minimizes the likelihood of the deadlock reoccurring when the resubmitted query requests its locks. For example, the error handler might be coded to pause for a random duration between one and three seconds.

You can use `TRY.CATCH` to handle deadlocks. Error 1205 can be caught by the `CATCH` block.
