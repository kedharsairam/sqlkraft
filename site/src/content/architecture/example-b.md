---
title: 'Example B'
topic: 'query-processing'
description: 'statement is executed under the transaction that is still active under session'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Session 1:

The following

statement is executed under the transaction that is still active under session

1. Because of the exclusive (

) table lock hint, the transaction attempts to acquire an

lock on

the table. However, the

lock that's being held by the transaction in session 2 blocks the

lock

at partition ID 0.

SQL

Session 1:

A

statement is executed under a transaction. Because of the

lock hint, this

statement acquires and retains an Intent shared (

) lock on the table (for this illustration, row

and page locks are ignored). The

lock is acquired only on the partition assigned to the

transaction. For this example, it's assumed that the

lock is acquired on partition ID 6.

SQL

Session 2:

A

statement is executed under a transaction. Because of the

lock hint, the

transaction tries to acquire an exclusive (

) lock on the table. Remember that the

lock must be

acquired on all partitions starting with partition ID 0. The

lock is acquired on all partitions IDs

0-5 but is blocked by the

lock that is acquired on partition ID 6.

On partition IDs 7-15 that the

lock hasn't yet reached, other transactions can continue to

acquire locks.

```sql
SELECT
```

```sql
X
```

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
SELECT
```

```sql
HOLDLOCK
```

```sql
IS
```

```sql
IS
```

```sql
IS
```

```sql
SELECT
```

```sql
TABLOCKX
```

```sql
X
```

```sql
X
```

```sql
X
```

```sql
IS
```

```sql
X
```

```sql
FROM
TestTable
WITH
(TABLOCK, HOLDLOCK);
SELECT
col1
FROM
TestTable
WITH
(TABLOCKX);
```

```sql
-- Start a transaction.
BEGIN
TRANSACTION
;
-- This SELECT statement will acquire an IS lock on the table.
SELECT
col1
FROM
TestTable
WITH
(HOLDLOCK);
```
