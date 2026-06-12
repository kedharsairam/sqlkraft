---
title: "Cause a deadlock"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: 2026-05-29
---

shorter duration than a higher isolation level, such as. This reduces lock

contention.

When the

database option is set

, a transaction running under the

isolation level uses row versioning rather than shared locks during read

operations.

Snapshot isolation also uses row versioning, which doesn't use shared locks during read

operations. Before a transaction can run under snapshot isolation, the

database option must be set.

Use row versioning-based isolation levels to minimize deadlocks that can occur between read

and write operations.

Using bound connections, two or more connections opened by the same application can

cooperate with each other. Any locks acquired by the secondary connections are held as if they

were acquired by the primary connection, and vice versa. Therefore, they don't block each

other.

You might need to cause a deadlock for learning or demonstration purposes.

The following example works in the

sample database with the default

schema and data when

READ_COMMITTED_SNAPSHOT has been enabled. To download this

sample, visit

AdventureWorks sample databases.

For an example that causes a deadlock when optimized locking is enabled, see

Optimized

locking and deadlocks.



Tip

Microsoft recommends the row versioning-based

isolation level for all

applications, unless an application relies upon the blocking behavior of the lock-based

isolation level.

## Session A

## Session B

## Session A

## Session B

## Session B

## Session A

## Session B

## Session A

To cause a deadlock, you need to connect two sessions to the

database.

We refer to these sessions as

and. You can create these two sessions by

creating two query windows in SQL Server Management Studio (SSMS).

In

, run the following batch. This code begins an

explicit transaction

and executes a

statement that updates the

table. To do this, the transaction acquires an

update (U) lock

on the qualifying rows in table

which are then converted to

exclusive (

) locks. We leave the transaction open.

Now, in

, run the following batch. This code doesn't explicitly begin a transaction.

Instead, it operates in

autocommit transaction mode. This statement updates the

table. The update takes an update (

) lock on the qualifying rows

in the

table. The query joins to other tables, including the

table.

To complete this update,

needs shared (

) locks on rows in table

,

including the rows that are locked by.

is blocked on.

Return to. Run the following

statement. This statement executes as a part of

the previously open transaction.

`SERIALIZABLE`

`READ_COMMITTED_SNAPSHOT`

`ON`

```sql
READ COMMITTED
```

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`AdventureWorksLT2019`

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

`AdventureWorksLT2019`

`SalesLT.Product`

`SalesLT.Product`

```sql
X
```

`SalesLT.ProductDescription`

```sql
U
```

`SalesLT.ProductDescription`

`SalesLT.Product`

```sql
S
```

`SalesLT.Product`

`SalesLT.Product`

`UPDATE`

```sql
BEGIN
TRANSACTION
;
UPDATE
SalesLT.Product
SET
SellEndDate = SellEndDate + 1
WHERE
Color =
'Red'
;
UPDATE
SalesLT.ProductDescription
SET
Description = Description
FROM
SalesLT.ProductDescription
AS pd
INNER
JOIN
SalesLT.ProductModelProductDescription
AS pmpd
ON pd.ProductDescriptionID = pmpd.ProductDescriptionID
INNER
JOIN
SalesLT.ProductModel
AS pm
ON pmpd.ProductModelID = pm.ProductModelID
INNER
JOIN
SalesLT.Product
AS p
ON pm.ProductModelID = p.ProductModelID
WHERE p.Color =
'Silver'
;
UPDATE
SalesLT.ProductDescription
SET
Description = Description
```
