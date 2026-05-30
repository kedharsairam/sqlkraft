---
title: "What is optimized locking?"
topic: "locking"
description: "SQL Server 2025 (17.x)"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

SQL database in Microsoft Fabric

Optimized locking offers an improved transaction locking mechanism to reduce lock blocking

and lock memory consumption for concurrent transactions.

Optimized locking helps to reduce lock memory as very few locks are held even for large

transactions. In addition, optimized locking avoids lock escalations and can avoid certain types

of deadlocks. This allows more concurrent access to the table.

Optimized locking is composed of two primary components:

and

.

A transaction ID (TID) is a unique identifier of a transaction. Each row is labeled with the

last TID that modified it. Instead of potentially many key or row identifier locks, a single

lock on the TID is used to protect all modified rows. For more information, see

Transaction ID (TID) locking

.

Lock after qualification (LAQ) is an optimization that evaluates query predicates using the

latest committed version of the row without acquiring a lock, thus improving concurrency.

LAQ requires

read committed snapshot isolation (RCSI)

. For more information, see

Lock

after qualification (LAQ)

.

For example:

Without optimized locking, updating 1,000 rows in a table might require 1,000 exclusive

(

) row locks held until the end of the transaction.

With optimized locking, updating 1,000 rows in a table might require 1,000

row locks

but each lock is released as soon as each row is updated, and only one

TID lock is held

until the end of the transaction. Because locks are released quickly, lock memory usage is

reduced and

lock escalation

is much less likely to occur, improving workload concurrency.

７

Note

Enabling optimized locking reduces or eliminates row and page locks acquired by the

Data Modification Language (DML) statements such as

,

,

,

. It

has no effect on other kinds of database and object locks, such as schema locks.

```sql
X
```

```sql
X
```

```sql
X
```

`INSERT`

`UPDATE`

`DELETE`

`MERGE`
