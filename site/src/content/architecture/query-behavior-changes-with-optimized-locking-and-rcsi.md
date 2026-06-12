---
title: "Query behavior changes with optimized locking and RCSI"
topic: "query-processing"
description: "Lock after qualification is not used in the following scenarios:"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Lock after qualification is not used in the following scenarios:

When disabled by

LAQ heuristics.

When conflicting locking hints, such as

,

,

, or

are used.

When the transaction isolation level is other than

, or when the

database option is disabled.

When the table being modified has a columnstore index.

When the DML statement includes variable assignment.

When the DML statement has an

clause that inserts data into a table variable or

## returns a result set.

When the DML statement uses more than one index seek or scan operator to read the

rows being modified.

In

statements.

Concurrent workloads under read committed snapshot isolation (RCSI) that rely on strict

execution order of transactions might experience differences in query behavior when

optimized locking is enabled.

Consider the following example where transaction T2 is updating table

based on column

that was updated during transaction T1.

ﾉ

Expand table

### Without LAQ

### With LAQ

Let's evaluate the outcome of the previous scenario with and without lock after qualification

(LAQ).

Without LAQ, the

statement in transaction T2 is blocked, waiting for transaction T1 to

complete. Once T1 completes, T2 updates the row setting column

to

because its predicate

is satisfied.

After both transactions commit, table

contains the following rows:

Output

With LAQ, transaction T2 uses the latest committed version of the row where column

equals

to

to evaluate its predicate (

). The row doesn't qualify; hence it's skipped and the

statement completes without having been blocked by transaction T1. In this example, LAQ

removes blocking but leads to different results.

After both transactions commit, table

contains the following rows:

Output

）

Important

### use stricter isolation levels

`UPDLOCK`

`READCOMMITTEDLOCK`

`XLOCK`

`HOLDLOCK`

```sql
READ COMMITTED
```

`READ_COMMITTED_SNAPSHOT`

`OUTPUT`

`MERGE`

`t4`

```sql
b
```

```sql
BEGIN TRANSACTION T1;
UPDATE t4
```

```sql
CREATE
TABLE t4 (
a int
NOT
NULL
,
b int
NULL
);
INSERT
INTO t4
VALUES (1,1);
GO
```

```sql
SET b = 2
WHERE a = 1;
BEGIN TRANSACTION T2;
UPDATE t4
SET b = 3
WHERE b = 2;
COMMIT TRANSACTION;
COMMIT TRANSACTION;
```

`UPDATE`

```sql
b
```

```sql
3
```

`t4`

```sql
b
```

```sql
1
```

```sql
b = 2
```

`t4`

```sql
a | b
1 | 3 a | b
1 | 2
```
