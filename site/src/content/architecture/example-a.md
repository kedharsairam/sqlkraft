---
title: "Example A"
topic: "query-processing"
description: "statement is executed under a transaction."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Session 1:

A

statement is executed under a transaction. Because of the

lock hint, this

statement acquires and retains an Intent shared (

) lock on the table (for this illustration, row

and page locks are ignored). The

lock is acquired only on the partition assigned to the

transaction. For this example, it's assumed that the

lock is acquired on partition ID 7.

Session 2:

A transaction is started, and the

statement running under this transaction acquires and

retains a shared (

) lock on the table. The

lock is acquired on all partitions, which results in

multiple table locks, one for each partition. For example, on a 16-CPU system, 16

locks will be

issued across lock partition IDs 0-15. Because the

lock is compatible with the

lock being

held on partition ID 7 by the transaction in session 1, there's no blocking between transactions.

`SELECT`

`HOLDLOCK`

`IS`

`IS`

`IS`

`SELECT`

```sql
S
```

```sql
S
```

```sql
S
```

```sql
S
```

`IS`

```sql
(
col1 int
);
GO
-- Create a clustered index on the table.
CREATE
CLUSTERED
INDEX ci_TestTable
ON
TestTable (col1);
GO
-- Populate the table.
INSERT
INTO
TestTable
VALUES (1);
GO
```

```sql
-- Start a transaction.
BEGIN
TRANSACTION
;
-- This SELECT statement will acquire an IS lock on the table.
SELECT col1
FROM
TestTable
WITH (HOLDLOCK);
BEGIN
TRANSACTION
;
SELECT col1
```
