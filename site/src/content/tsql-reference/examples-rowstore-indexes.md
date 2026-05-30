---
name: "Examples: Rowstore indexes"
title: "Examples: Rowstore indexes"
category: "statements"
description: "This sample removes the archive compression, and only uses columnstore compression."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## A. Rebuild an index

## B. Rebuild all indexes on a table and specify options

This sample removes the archive compression, and only uses columnstore compression.

The following example rebuilds a single index on the

table in the

database.

The following example specifies the keyword

. This rebuilds all indexes associated with the

table

in the

database. Three options are specified.

The following example adds the ONLINE option including the low priority lock option, and

adds the row compression option.

: SQL Server 2014 (12.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

## C. Reorganize an index with LOB compaction

## D. Set options on an index

## E. Disable an index

The following example reorganizes a single clustered index in the

database. Because the index contains a LOB data type in the leaf level, the statement also

compacts all pages that contain the large object data. Specifying the

option isn't required because the default value is ON.

The following example sets several options on the index

in the

database.

The following example disables a nonclustered index on the

table in the

database.

## F. Disable constraints

## G. Enable constraints

## H. Rebuild a partitioned index

The following example disables a

constraint by disabling the

index in

the

database. The

constraint on the underlying table is

automatically disabled and warning message is displayed.

The result set returns this warning message.

Output

The following example enables the

and

constraints that were

disabled in Example F.

The

constraint is enabled by rebuilding the

index.

The

constraint is then enabled.

### Applies to

### Applies to

## I. Change the compression setting of an index

## J. Change the setting of an index with XML compression

The following example rebuilds a single partition, partition number

, of the partitioned index

in the

database. Partition 5 is

rebuilt with

and the 10 minutes wait time for the low priority lock applies separately

to every lock acquired by index rebuild operation. If during this time the lock can't be obtained

to complete index rebuild, the rebuild operation statement itself is aborted, due to

.

: SQL Server 2014 (12.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

The following example rebuilds an index on a nonpartitioned rowstore table.

: SQL Server 2022 (16.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance.

The following example rebuilds an index on a nonpartitioned rowstore table.

### Applies to

## K. Online resumable index rebuild

For more data compression examples, see

Data compression

.

: SQL Server 2017 (14.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

The following examples show how to use online resumable index rebuild.

Execute an online index rebuild as resumable operation with

. Executing the same

command again after an index operation was paused, automatically resumes the index rebuild

operation.

Execute an online index rebuild as resumable operation with

set to 240 minutes.

Pause a running resumable online index rebuild.

Resume an online index rebuild for an index rebuild that was executed as resumable operation

specifying a new value for

set to 4.

Resume an online index rebuild operation for an index online rebuild that was executed as

resumable. Set

to 2, set the execution time for the index being running as resumable to

240 minutes, and if an index is being blocked on the lock, wait 10 minutes and after that kill all

blockers.

Abort resumable index rebuild operation that is running or paused.

Index architecture and design guide

Perform index operations online

CREATE INDEX (Transact-SQL)

CREATE SPATIAL INDEX (Transact-SQL)

CREATE XML INDEX (Transact-SQL)

DROP INDEX (Transact-SQL)

Disable indexes and constraints

XML indexes (SQL Server)

Optimize index maintenance to improve query performance and reduce resource

consumption

sys.dm_db_index_physical_stats (Transact-SQL)

EVENTDATA (Transact-SQL)

Last updated on 02/05/2026

Related content

`Employee`

`AdventureWorks2025`

`ALL`

`Production.Product`

`AdventureWorks2025`

```sql
WITH (DROP_EXISTING =
ON
);
--Compress the table further by using archival compression.
ALTER
INDEX cci_SimpleTable
ON
SimpleTable
REBUILD
WITH (DATA_COMPRESSION = COLUMNSTORE_ARCHIVE);
GO
ALTER
INDEX cci_SimpleTable
ON
SimpleTable
REBUILD
WITH (DATA_COMPRESSION = COLUMNSTORE);
GO
```

```sql
ALTER
INDEX
PK_Employee_EmployeeID
ON
HumanResources.Employee
REBUILD
;
```

```sql
ALTER
INDEX
ALL
ON
Production.Product
REBUILD
WITH (FILLFACTOR = 80, SORT_IN_TEMPDB =
ON
, STATISTICS_NORECOMPUTE =
ON
);
```

`AdventureWorks2025`

```sql
WITH (LOB_COMPACTION =
ON)
```

`AK_SalesOrderHeader_SalesOrderNumber`

`AdventureWorks2025`

`Employee`

`AdventureWorks2025`

```sql
ALTER
INDEX
ALL
ON
Production.Product
REBUILD
WITH (
FILLFACTOR = 80,
SORT_IN_TEMPDB =
ON
,
STATISTICS_NORECOMPUTE =
ON
,
ONLINE
=
ON ( WAIT_AT_LOW_PRIORITY ( MAX_DURATION = 4
MINUTES
, ABORT_AFTER_WAIT
= BLOCKERS ) ),
DATA_COMPRESSION =
ROW
);
```

```sql
ALTER
INDEX
PK_ProductPhoto_ProductPhotoID
ON
Production.ProductPhoto REORGANIZE
WITH (LOB_COMPACTION =
ON
);
```

```sql
ALTER
INDEX
AK_SalesOrderHeader_SalesOrderNumber
ON
Sales.SalesOrderHeader
SET (
STATISTICS_NORECOMPUTE =
ON
,
IGNORE_DUP_KEY =
ON
,
ALLOW_PAGE_LOCKS =
ON
) ;
GO
```

```sql
PRIMARY KEY
```

```sql
PRIMARY KEY
```

`AdventureWorks2025`

```sql
FOREIGN KEY
```

```sql
PRIMARY KEY
```

```sql
FOREIGN KEY
```

```sql
PRIMARY KEY
```

```sql
PRIMARY KEY
```

```sql
FOREIGN KEY
```

```sql
ALTER
INDEX
IX_Employee_ManagerID
ON
HumanResources.Employee
DISABLE
;
```

```sql
ALTER
INDEX
PK_Department_DepartmentID
ON
HumanResources.Department
DISABLE
;
Warning: Foreign key 'FK_EmployeeDepartmentHistory_Department_DepartmentID'
on table 'EmployeeDepartmentHistory' referencing table 'Department'
was disabled as a result of disabling the index 'PK_Department_DepartmentID'.
```

```sql
ALTER
INDEX
PK_Department_DepartmentID
ON
HumanResources.Department
REBUILD
;
ALTER
TABLE
HumanResources.EmployeeDepartmentHistory
CHECK
CONSTRAINT
FK_EmployeeDepartmentHistory_Department_DepartmentID;
GO
```

```sql
5
```

`IX_TransactionHistory_TransactionDate`

`AdventureWorks2025`

```sql
ONLINE=ON
```

```sql
ABORT_AFTER_WAIT = SELF
```

```sql
-- Verify the partitioned indexes.
SELECT
*
FROM sys.dm_db_index_physical_stats (DB_ID(),OBJECT_ID(N
'Production.TransactionHistory'
),
NULL
,
NULL
,
NULL
);
GO
--Rebuild only partition 5.
ALTER
INDEX
IX_TransactionHistory_TransactionDate
ON
Production.TransactionHistory
REBUILD
Partition
= 5
WITH (
ONLINE
=
ON (WAIT_AT_LOW_PRIORITY (MAX_DURATION = 10 minutes
,
ABORT_AFTER_WAIT =
SELF
)));
GO
```

```sql
ALTER
INDEX
IX_INDEX1
ON
T1
REBUILD
WITH (DATA_COMPRESSION = PAGE);
GO
```

```sql
MAXDOP = 1
```

`MAX_DURATION`

`MAXDOP`

```sql
ALTER
INDEX
IX_INDEX1
ON
T1
REBUILD
WITH (XML_COMPRESSION =
ON
);
GO
```

```sql
ALTER
INDEX test_idx on test_table
REBUILD
WITH (
ONLINE
=
ON
, MAXDOP = 1,
RESUMABLE
=
ON
);
ALTER
INDEX test_idx on test_table
REBUILD
WITH (
ONLINE
=
ON
,
RESUMABLE
=
ON
,
MAX_DURATION = 240);
ALTER
INDEX test_idx on test_table PAUSE;
ALTER
INDEX test_idx on test_table
RESUME
WITH (MAXDOP = 4);
```

`MAXDOP`

```sql
ALTER
INDEX test_idx on test_table
RESUME
WITH (MAXDOP = 2, MAX_DURATION = 240
MINUTES
,
WAIT_AT_LOW_PRIORITY (MAX_DURATION = 10, ABORT_AFTER_WAIT = BLOCKERS));
ALTER
INDEX test_idx on test_table
ABORT
;
```
