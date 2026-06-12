---
title: "Escalation threshold for a Transact-SQL statement"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Optimized locking helps to reduce lock memory as very few locks are held for the duration of the

transaction. As the Database Engine acquires row and page locks, lock escalation can occur

similarly, but far less frequently. Optimized locking typically succeeds in avoiding lock escalations,

lowering the number of locks and amount of lock memory necessary.

When optimized locking is enabled, and in the default

isolation level, the

Database Engine releases row and page locks as soon as the row is modified. No row and page

locks are held for the duration of the transaction, except for a single Transaction ID (TID) lock.

This reduces the likelihood of lock escalation.

Lock escalation is triggered when lock escalation isn't disabled on the table by using the

option, and when either of the following conditions exists:

A single Transact-SQL statement acquires at least 5,000 locks on a single nonpartitioned

table or index.

A single Transact-SQL statement acquires at least 5,000 locks on a single partition of a

partitioned table and the

option is set to AUTO.

The number of locks in an instance of the Database Engine exceeds memory or

configuration thresholds.

If locks can't be escalated because of lock conflicts, the Database Engine periodically triggers lock

escalation at every 1,250 new locks acquired.

When the Database Engine checks for possible escalations at every 1,250 newly acquired locks, a

lock escalation will occur if and only if a Transact-SQL statement has acquired at least 5,000 locks

on a single reference of a table. Lock escalation is triggered when a Transact-SQL statement

acquires at least 5,000 locks on a single reference of a table. For example, lock escalation isn't

triggered if a statement acquires 3,000 locks in one index and 3,000 locks in another index of the

same table. Similarly, lock escalation isn't triggered if a statement has a self join on a table, and

each reference to the table only acquires 3,000 locks in the table.

Lock escalation only occurs for tables that have been accessed at the time the escalation is

triggered. Assume that a single

statement is a join that accesses three tables in this

sequence:

,

, and. The statement acquires 3,000 row locks in the clustered

```sql
READ COMMITTED
```

```sql
ALTER
TABLE SET LOCK_ESCALATION
```

```sql
ALTER TABLE SET LOCK_ESCALATION
```

`SELECT`

`TableA`

`TableB`

`TableC`
