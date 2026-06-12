---
title: "Lock after qualification (LAQ)"
topic: "locking"
description: "If optimized locking is enabled, the request holds only a single"
tags: ["locking","architecture"]
pubDate: 2026-05-29
---

If optimized locking is enabled, the request holds only a single

lock on the

(transaction)

resource.

If optimized locking isn't enabled, the same request holds four locks - one

(intent exclusive)

lock on the page containing the rows, and three

key locks on each row:

The

sys.dm_tran_locks

dynamic management view (DMV) is useful in examining or

troubleshooting locking issues. Here it is used to observe optimized locking in action.

Building on the TID infrastructure, the LAQ component of optimized locking changes how DML

statements such as

,

, and

acquire locks.

Without optimized locking, query predicates are checked row by row in a scan by first taking

an update (

) row lock. If the predicate is satisfied, an exclusive (

) row lock is taken before

updating the row and held until the end of transaction.

With optimized locking, and when the

snapshot isolation level (RCSI) is

enabled, predicates can be optimistically checked on the latest committed version of the row

without taking any locks. If the predicate doesn't satisfy, the query moves to the next row in

the scan. If the predicate is satisfied, an

row lock is taken to update the row.





In other words, the lock is taken

after qualification

of the row for modification. The

row lock

is released as soon as the row update is complete, before the end of the transaction.

Since predicate evaluation is performed without acquiring any locks, concurrent queries

modifying different rows don't block each other.

For example:

ﾉ

Expand table

Without optimized locking, session 2 is blocked because session 1 holds a

lock on the row

session 2 needs to update. However, with optimized locking, session 2 isn't blocked because

locks aren't taken, and because in the latest committed version of row 1, column

equals to 1,

which doesn't satisfy the predicate of session 2.

LAQ is performed optimistically on the assumption that a row isn't modified after checking the

predicate. If the predicate is satisfied and the row hasn't been modified after checking the

predicate, it's modified by the current transaction.

Because the

locks aren't taken, a concurrent transaction might modify the row after the

predicate has been evaluated. If there's an active transaction holding an

TID lock on the row,

the database engine waits for it to complete. If the row has changed after the predicate was

evaluated previously, the database engine reevaluates (requalifies) the predicate again before

modifying the row. If the predicate is still satisfied, the row is modified.

Predicate requalification is supported by a subset of the query engine operators. If predicate

reevaluation is needed, but the query plan uses an operator that doesn't support predicate

requalification, the database engine internally aborts statement processing and restarts it

without LAQ. When such an abort occurs, the

extended event

fires.

Some statements, for example

statements with variable assignment and statements

with the

OUTPUT

clause, can't be aborted and restarted without changing their semantics. For

such statements, LAQ isn't used.

In the following example, the predicate is re-evaluated because another transaction has

changed the row:

ﾉ

Expand table

```sql
X
```

`XACT`

`IX`

```sql
X
```

`INSERT`

`UPDATE`

`DELETE`

```sql
U
```

```sql
X
```

```sql
READ COMMITTED
```

```sql
X
```

```sql
BEGIN
TRANSACTION
;
UPDATE t0
SET b = b + 10;
SELECT
*
FROM sys.dm_tran_locks
WHERE request_session_id = @@SPID
AND resource_type
IN (
'PAGE'
,
'RID'
,
'KEY'
,
'XACT'
);
COMMIT
TRANSACTION
;
GO
DROP
TABLE
IF
EXISTS t0;
```

```sql
X
```

```sql
BEGIN TRANSACTION;
UPDATE t1
SET b = b + 10
WHERE a = 1;
BEGIN TRANSACTION;
UPDATE t1
SET b = b + 10
WHERE a = 2;
COMMIT TRANSACTION;
COMMIT TRANSACTION;
/* Confirm that optimized locking and read committed snapshot isolation (RCSI) are both enabled on this database. */
SELECT database_id,
name
,
is_accelerated_database_recovery_on,
is_optimized_locking_on,
is_read_committed_snapshot_on
FROM sys.databases
WHERE name
= DB_NAME();
CREATE
TABLE t1 (
a int
NOT
NULL
,
b int
NULL
);
INSERT
INTO t1
VALUES (1,10),(2,20),(3,30);
GO
```

```sql
U
```

```sql
U
```

```sql
a
```

```sql
U
```

```sql
X
```

`lock_after_qual_stmt_abort`

`UPDATE`

```sql
BEGIN TRANSACTION;
UPDATE t3
CREATE
TABLE t3 (
a int
NOT
NULL
,
b int
NULL
);
INSERT
INTO t3
VALUES (1,10),(2,20),(3,30);
GO
```
