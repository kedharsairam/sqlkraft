---
title: 'B. Work with READ COMMITTED isolation using row versioning'
topic: 'io-fundamentals'
description: 'transaction using row versioning runs concurrently with'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

On session 2:

SQL

On session 1:

SQL

In this example, a

transaction using row versioning runs concurrently with

another transaction. The

transaction behaves differently than a

transaction. Like a

transaction, the

transaction will read versioned rows

even after the other transaction has modified data. However, unlike a

transaction, the

transaction:

Reads the modified data after the other transaction commits the data changes.

Is able to update the data modified by the other transaction where the

transaction

couldn't.

On session 1:

SQL

On session 2:

SQL

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

```sql
SNAPSHOT
```

```sql
SNAPSHOT
```

```sql
READ COMMITTED
```

```sql
SNAPSHOT
```

```sql
READ COMMITTED
```

```sql
FROM
HumanResources.Employee
WHERE
BusinessEntityID = 4;
-- Commit the transaction; this commits the data
-- modification.
COMMIT
TRANSACTION
;
GO
-- Reissue the SELECT statement - this still
-- shows the employee having 48 vacation hours
-- even after the other transaction has committed
-- the data modification.
SELECT
BusinessEntityID, VacationHours
FROM
HumanResources.Employee
WHERE
BusinessEntityID = 4;
-- Because the data has been modified outside of the
-- snapshot transaction, any further data changes to
-- that data by the snapshot transaction will cause
-- the snapshot transaction to fail. This statement
-- will generate a 3960 error and the transaction will
-- terminate.
UPDATE
HumanResources.Employee
SET
SickLeaveHours = SickLeaveHours - 8
WHERE
BusinessEntityID = 4;
-- Undo the changes to the database from session 1.
-- This will not undo the change from session 2.
ROLLBACK
TRANSACTION
;
GO
```

```sql
SNAPSHOT
```

```sql
USE
AdventureWorks2022;
GO
-- Enable READ_COMMITTED_SNAPSHOT on the database.
-- For this statement to succeed, this session
-- must be the only connection to the AdventureWorks2022
-- database.
ALTER
DATABASE
AdventureWorks2022
SET
READ_COMMITTED_SNAPSHOT
ON
;
GO
-- Start a read-committed transaction
SET
TRANSACTION
ISOLATION
LEVEL
READ
COMMITTED;
GO
BEGIN
TRANSACTION
;
-- This SELECT statement will return
-- 48 vacation hours for the employee.
SELECT
BusinessEntityID, VacationHours
FROM
HumanResources.Employee
WHERE
BusinessEntityID = 4;
USE
AdventureWorks2022;
GO
-- Start a transaction.
BEGIN
TRANSACTION
;
-- Subtract a vacation day from employee 4.
-- Update is not blocked by session 1 since
-- under read-committed using row versioning shared locks are
-- not requested.
UPDATE
HumanResources.Employee
SET
VacationHours = VacationHours - 8
WHERE
BusinessEntityID = 4;
-- Verify that the employee now has 40 vacation hours.
SELECT
VacationHours
FROM
HumanResources.Employee
WHERE
BusinessEntityID = 4;
```
