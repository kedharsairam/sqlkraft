---
title: "Transaction ID (TID) locking"
topic: "locking"
description: ""
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

In the database engine, locking is a mechanism that prevents multiple transactions from

updating the same data simultaneously in order to guarantee the

ACID

properties of

transactions.

When a transaction needs to modify data, it requests a lock on the data. The lock is granted if

no other conflicting locks are held on the data, and the transaction can proceed with the

modification. If another conflicting lock is held on the data, the transaction must wait for the

lock to be released before it can proceed.

When multiple transactions attempt to access the same data concurrently, the database engine

must resolve potentially complex conflicts with concurrent reads and writes. Locking is one of

the mechanisms by which the engine can provide the semantics for the ANSI SQL transaction

isolation levels

. Although locking in databases is essential, reduced concurrency, deadlocks,

complexity, and lock overhead can affect performance and scalability.

When

row versioning

based isolation levels are in use or when ADR is enabled, every row in the

database internally contains a transaction ID (TID). TID is persisted with the row. Every

transaction modifying a row stamps the row with its TID.

With TID locking, instead of taking the lock on the key of the row, a lock is taken on the TID of

the row. The modifying transaction holds an

lock on its TID. Other transactions acquire an

lock on the TID to wait until the first transaction completes. With TID locking, page and row

locks continue to be taken for modifications, but each page and row lock is released as soon as

each row is modified. The only lock held until the end of transaction is the single

lock on the

TID resource, replacing multiple page and row (key) locks.

Consider the following example that shows locks for the current session while a write

transaction is active:

```sql
X
```

```sql
S
```

```sql
X
```

```sql
/* Is optimized locking is enabled? */
SELECT
DATABASEPROPERTYEX(DB_NAME(),
'IsOptimizedLockingOn'
)
AS is_optimized_locking_enabled;
CREATE
TABLE t0 (
a int
PRIMARY
KEY
,
b int
NULL
);
INSERT
INTO t0
VALUES (1,10),(2,20),(3,30);
GO
```
