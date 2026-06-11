---
title: "Enable row versioning-based isolation levels"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

On session 1:

On session 2:

On session 1:

Database administrators control the database-level settings for row versioning by using the

and

database options in the

statement.

When the

database option is set to

, the mechanisms used to

support the option are activated immediately. When setting the

option,

only the connection executing the

command is allowed in the database. There

must be no other open connection in the database until

is complete. The

database doesn't have to be in single-user mode.

The following Transact-SQL statement enables

:

When the

database option is set to

, the instance of the Database

Engine doesn't start generating row versions for modified data until all active transactions that

have modified data in the database complete. If there are active modification transactions, the

Database Engine sets the state of the option to

. After all of the modification

transactions complete, the state of the option is changed to

. Users can't start a

transaction in the database until the option is

. Similarly, the database passes through a

state when the database administrator sets the

option to

.

The following Transact-SQL statement enables

:

The following table lists and describes the states of the

option. Using

with the

option doesn't block users who are currently

accessing the database data.

ﾉ

Expand table

```sql
-- Reissue the SELECT statement - this still shows
-- the employee having 48 vacation hours. The
-- read-committed transaction is still reading data
-- from the versioned row and the other transaction
-- has not committed the data changes yet.
SELECT
BusinessEntityID, VacationHours
FROM
HumanResources.Employee
WHERE
BusinessEntityID = 4;
-- Commit the transaction.
COMMIT
TRANSACTION
;
GO
-- Reissue the SELECT statement which now shows the
-- employee having 40 vacation hours. Being
-- read-committed, this transaction is reading the
-- committed data. This is different from snapshot
-- isolation which reads from the versioned row.
SELECT
BusinessEntityID, VacationHours
FROM
HumanResources.Employee
WHERE
BusinessEntityID = 4;
-- This statement, which caused the snapshot transaction
-- to fail, will succeed with read-committed using row versioning.
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

`READ_COMMITTED_SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

```sql
ALTER DATABASE
```

`READ_COMMITTED_SNAPSHOT`

`ON`

`READ_COMMITTED_SNAPSHOT`

```sql
ALTER DATABASE
```

```sql
ALTER DATABASE
```

`READ_COMMITTED_SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`PENDING_ON`

`ON`

`SNAPSHOT`

`ON`

`PENDING_OFF`

`ALLOW_SNAPSHOT_ISOLATION`

`OFF`

`ALLOW_SNAPSHOT_ISOLATION`

`ALLOW_SNAPSHOT_ISOLATION`

```sql
ALTER DATABASE
```

`ALLOW_SNAPSHOT_ISOLATION`

```sql
ALTER
DATABASE
AdventureWorks2022
SET
READ_COMMITTED_SNAPSHOT
ON
;
ALTER
DATABASE
AdventureWorks2022
SET
ALLOW_SNAPSHOT_ISOLATION
ON
;
```
