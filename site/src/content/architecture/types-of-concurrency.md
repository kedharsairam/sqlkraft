---
title: "Types of concurrency"
topic: "query-processing"
description: "Missing an updated row or seeing an updated row multiple times"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Missing an updated row or seeing an updated row multiple times

Transactions that are running at the

level (or statements using the

table hint) don't issue shared locks to prevent other transactions from modifying

data read by the current transaction. Transactions that are running at the

level do issue shared locks, but the row or page locks are released after the row is read.

In either case, when you're scanning an index, if another user changes the index key

column of the row during your read, the row might appear again if the key change

moved the row to a position ahead of your scan. Similarly, the row might not be read at

all if the key change moved the row to a position in the index that you had already read.

To avoid this, use the

or

hint, or row versioning. For more

information, see

Table Hints (Transact-SQL)

.

Missing one or more rows that weren't the target of update

When you're using

, if your query reads rows using an allocation order

scan (using IAM pages), you might miss rows if another transaction is causing a page

split. This doesn't occur when you're using the

isolation level.

### Pessimistic

### Optimistic

```sql
READ UNCOMMITTED
```

`NOLOCK`

```sql
READ COMMITTED
```

`SERIALIZABLE`

`HOLDLOCK`

```sql
READ UNCOMMITTED
```

```sql
READ COMMITTED
```

```sql
SELECT
ID
FROM dbo.employee
WHERE
ID
> 5
AND
ID
< 10;
--The INSERT statement from the second transaction occurs here.
SELECT
ID
FROM dbo.employee
WHERE
ID
> 5 and
ID
< 10;
COMMIT
;
--Transaction 2
BEGIN
TRAN;
INSERT
INTO dbo.employee (
Id
,
Name
)
VALUES (6 ,
'New'
);
COMMIT
;
```
