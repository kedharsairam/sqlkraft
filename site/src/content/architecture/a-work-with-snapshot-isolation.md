---
title: "A. Work with SNAPSHOT isolation"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

. Monitors the longest running time in seconds of any

transaction using row versioning. This can be used to determine if any transaction is running

for an unexpected amount of time.

. Monitors the total number of active transactions. This doesn't include system

transactions.

. Monitors the total number of active snapshot transactions.

. Monitors the total number of active snapshot transactions

that perform update operations.

. Monitors the total number of active nonsnapshot

transactions that generate version records.

The following examples show the differences in behavior between

isolation transactions

and

transactions that use row versioning.

In this example, a transaction running under

isolation reads data that is then modified

by another transaction. The

transaction doesn't block the update operation executed by

the other transaction, and it continues to read data from the versioned row, ignoring the data

modification. However, when the

transaction attempts to modify the data that has

already been modified by the other transaction, the

transaction generates an error and

is terminated.

On session 1:

７

Note

The sum of Update Snapshot Transactions and NonSnapshot Version Transactions

represents the total number of transactions that participate in version generation. The

difference of Snapshot Transactions and Update Snapshot Transactions represents the

number of read-only snapshot transactions.

On session 2:

On session 1:

`SNAPSHOT`

```sql
READ COMMITTED
```

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

```sql
USE
AdventureWorks2022;
GO
-- Enable snapshot isolation on the database.
ALTER
DATABASE
AdventureWorks2022
SET
ALLOW_SNAPSHOT_ISOLATION
ON
;
GO
-- Start a snapshot transaction
SET
TRANSACTION
ISOLATION
LEVEL
SNAPSHOT
;
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
-- under snapshot isolation shared locks are
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
-- Reissue the SELECT statement - this shows
-- the employee having 48 vacation hours. The
-- snapshot transaction is still reading data from
-- the older, versioned row.
SELECT
BusinessEntityID, VacationHours
```
