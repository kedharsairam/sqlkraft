---
name: "database in Fabric"
title: "Database in Fabric"
category: "predicates"
description: "The following example creates a nonclustered composite index on the"
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

The following example creates a nonclustered composite index on the

and

columns of the

table.

The following example creates a clustered index on the

column of the

table in the

database.

The following example creates index IX_FF with two columns from the dbo.FactFinance table.

The next statement rebuilds the index with one more column and keeps the existing name.

## E. Create a unique nonclustered index

## F. Use the IGNORE_DUP_KEY option

The following example creates a unique nonclustered index on the

column of the

table in the

database. The index will enforce

uniqueness on the data inserted into the

column.

The following query tests the uniqueness constraint by attempting to insert a row with the

same value as that in an existing row.

The resulting error message is:

Output

The following example demonstrates the effect of the

option by inserting

multiple rows into a temporary table first with the option set to

and again with the option

set to

. A single row is inserted into the

table that will intentionally cause a duplicate

value when the second multiple-row

statement is executed. A count of rows in the

table returns the number of rows inserted.

Here are the results of the second

statement.

Output

Notice that the rows inserted from the

table that did not violate the

uniqueness constraint were successfully inserted. A warning was issued and the duplicate row

ignored, but the entire transaction was not rolled back.

The same statements are executed again, but with

set to

.

Here are the results of the second

statement.

## G. Using DROP_EXISTING to drop and re-create an index

## H. Create an index on a view

Output

Notice that none of the rows from the

table were inserted into the

table even though only one row in the table violated the

index constraint.

The following example drops and re-creates an existing index on the

column of the

table in the

database by using the

option. The options

and

are also set.

The following example creates a view and an index on that view. Two queries are included that

use the indexed view.

### Query

### Display Actual Execution Plan

## I. Create an index with included (non-key) columns

The following example creates a nonclustered index with one key column (

) and

four non-key columns (

,

,

,

). A query that is

covered by the index follows. To display the index that is selected by the query optimizer, on

the

menu in SQL Server Management Studio, select

before executing the query.

## J. Create a partitioned index

## K. Creating a filtered index

## L. Create a compressed index

The following example creates a nonclustered partitioned index on

, an

existing partition scheme in the

database. This example assumes the

partitioned index sample has been installed.

The following example creates a filtered index on the Production.BillOfMaterials table in the

database. The filter predicate can include columns that are not key

columns in the filtered index. The predicate in this example selects only the rows where

EndDate is non-NULL.

The following example creates an index on a nonpartitioned table by using row compression.

The following example creates an index on a partitioned table by using row compression on all

partitions of the index.

### Applies to

## M. Create an index with XML compression

The following example creates an index on a partitioned table by using page compression on

partition

of the index and row compression on partitions

through

of the index.

: SQL Server 2022 (16.x) and later versions, Azure SQL Database, SQL database in

Microsoft Fabric, and Azure SQL Managed Instance.

The following example creates an index on a nonpartitioned table by using XML compression.

At least one column in the index must be the

data type.

The following example creates an index on a partitioned table by using XML compression on all

partitions of the index.

### Applies to

## N. Create, resume, pause, and abort resumable index

## operations

## O. CREATE INDEX with different low priority lock options

: SQL Server 2019 (15.x) and later versions, Azure SQL Database, SQL database in

Microsoft Fabric, and Azure SQL Managed Instance

The following examples use the

option to specify different strategies for

dealing with blocking.

### Applies to

`SalesQuota`

`SalesYTD`

`Sales.SalesPerson`

`VendorID`

`ProductVendor`

`Purchasing`

```sql
CREATE
INDEX
IX_VendorID
ON
ProductVendor (VendorID);
CREATE
INDEX
IX_VendorID
ON dbo.ProductVendor (VendorID
DESC
,
Name
ASC
, Address
DESC
);
CREATE
INDEX
IX_VendorID
ON
Purchasing..ProductVendor (VendorID);
```

```sql
CREATE
NONCLUSTERED
INDEX
IX_SalesPerson_SalesQuota_SalesYTD
ON
Sales.SalesPerson (SalesQuota, SalesYTD);
```

```sql
CREATE
CLUSTERED
INDEX
IX_ProductVendor_VendorID
ON
Purchasing..ProductVendor (VendorID);
```

```sql
CREATE
INDEX
IX_FF
ON dbo.FactFinance (FinanceKey
ASC
, DateKey
ASC
);
-- Rebuild and add the OrganizationKey
CREATE
INDEX
IX_FF
ON dbo.FactFinance (FinanceKey, DateKey, OrganizationKey
DESC
)
WITH (DROP_EXISTING =
ON
);
```

`Name`

`Production.UnitMeasure`

`AdventureWorks2025`

`Name`

`IGNORE_DUP_KEY`

`ON`

`OFF`

```sql
#Test
```

`INSERT`

```sql
CREATE
UNIQUE
INDEX
AK_UnitMeasure_Name
ON
Production.UnitMeasure(
Name
);
-- Verify the existing value.
SELECT
Name
FROM
Production.UnitMeasure
WHERE
Name
= N
'Ounces'
;
GO
INSERT
INTO
Production.UnitMeasure (UnitMeasureCode,
Name
, ModifiedDate)
VALUES (
'OC'
,
'Ounces'
,
GETDATE ());
Server: Msg 2601, Level 14, State 1, Line 1
Cannot insert duplicate key row in object 'UnitMeasure' with unique index
'AK_UnitMeasure_Name'. The statement has been terminated.
```

```sql
CREATE
TABLE
#
Test (C1
NVARCHAR (10), C2
NVARCHAR (50), C3 DATETIME);
GO
CREATE
UNIQUE
INDEX
AK_Index
ON
#
Test (C2)
```

`INSERT`

`Production.UnitMeasure`

`IGNORE_DUP_KEY`

`OFF`

`INSERT`

```sql
WITH (IGNORE_DUP_KEY =
ON
);
GO
INSERT
INTO
#
Test
VALUES (N
'OC'
, N
'Ounces'
,
GETDATE ());
INSERT
INTO
#
Test
SELECT
*
FROM
Production.UnitMeasure;
GO
SELECT
COUNT (*)
AS
[
Number of rows
]
FROM
#
Test
;
GO
DROP
TABLE
#
Test
;
GO
Server: Msg 3604, Level 16, State 1, Line 5 Duplicate key was ignored.
Number of rows
--------------
38
CREATE
TABLE
#
Test (C1
NVARCHAR (10), C2
NVARCHAR (50), C3 DATETIME);
GO
CREATE
UNIQUE
INDEX
AK_Index
ON
#
Test (C2)
WITH (IGNORE_DUP_KEY =
OFF
);
GO
INSERT
INTO
#
Test
VALUES (N
'OC'
, N
'Ounces'
,
GETDATE ());
INSERT
INTO
#
Test
SELECT
*
FROM
Production.UnitMeasure;
GO
SELECT
COUNT (*)
AS
[
Number of rows
]
FROM
#
Test
;
GO
DROP
TABLE
#
Test
;
GO
```

`Production.UnitMeasure`

`UNIQUE`

`ProductID`

`Production.WorkOrder`

`AdventureWorks2025`

`DROP_EXISTING`

`FILLFACTOR`

`PAD_INDEX`

```sql
Server: Msg 2601, Level 14, State 1, Line 5
Cannot insert duplicate key row in object '#Test' with unique index
'AK_Index'. The statement has been terminated.
Number of rows
--------------
1
```

```sql
CREATE
NONCLUSTERED
INDEX
IX_WorkOrder_ProductID
ON
Production.WorkOrder(ProductID)
WITH (FILLFACTOR = 80,
PAD_INDEX =
ON
,
DROP_EXISTING =
ON
);
GO
```

```sql
-- Set the options to support indexed views
SET
NUMERIC_ROUNDABORT
OFF
;
SET
ANSI_PADDING, ANSI_WARNINGS, CONCAT_NULL_YIELDS_NULL, ARITHABORT,
QUOTED_IDENTIFIER, ANSI_NULLS
ON
;
GO
-- Create view with schemabinding
IF OBJECT_ID ('Sales.vOrders', 'view') IS NOT NULL
DROP
VIEW
Sales.vOrders;
GO
CREATE
VIEW
Sales.vOrders
WITH
SCHEMABINDING
```

`PostalCode`

`AddressLine1`

`AddressLine2`

`City`

`StateProvinceID`

```sql
AS
SELECT
SUM (UnitPrice * OrderQty * (1.00 - UnitPriceDiscount))
AS
Revenue,
OrderDate, ProductID,
COUNT_BIG (*)
AS
COUNT
FROM
Sales.SalesOrderDetail
AS od, Sales.SalesOrderHeader
AS o
WHERE od.SalesOrderID = o.SalesOrderID
GROUP
BY
OrderDate, ProductID;
GO
-- Create an index on the view
CREATE
UNIQUE
CLUSTERED
INDEX
IDX_V1
ON
Sales.vOrders (OrderDate, ProductID);
GO
-- This query can use the indexed view even though the view is
-- not specified in the FROM clause.
SELECT
SUM (UnitPrice * OrderQty * (1.00 - UnitPriceDiscount))
AS
Rev,
OrderDate, ProductID
FROM
Sales.SalesOrderDetail
AS od
JOIN
Sales.SalesOrderHeader
AS o
ON od.SalesOrderID = o.SalesOrderID
AND
ProductID
BETWEEN
700
AND
800
AND
OrderDate >=
CONVERT (DATETIME,
'05/01/2002'
, 101)
GROUP
BY
OrderDate, ProductID
ORDER
BY
Rev
DESC
;
GO
-- This query can use the above indexed view
SELECT
OrderDate,
SUM (UnitPrice * OrderQty * (1.00 - UnitPriceDiscount))
AS
Rev
FROM
Sales.SalesOrderDetail
AS od
JOIN
Sales.SalesOrderHeader
AS o
ON od.SalesOrderID = o.SalesOrderID
AND
DATEPART (mm, OrderDate) = 3
AND
DATEPART (yy, OrderDate) = 2002
GROUP
BY
OrderDate
ORDER
BY
OrderDate
ASC
;
GO
```

```sql
CREATE
NONCLUSTERED
INDEX
IX_Address_PostalCode
ON
Person.Address (PostalCode)
INCLUDE (AddressLine1, AddressLine2, City, StateProvinceID);
GO
SELECT
AddressLine1, AddressLine2, City, StateProvinceID, PostalCode
```

`TransactionsPS1`

`AdventureWorks2025`

`AdventureWorks2025`

```sql
FROM
Person.Address
WHERE
PostalCode
BETWEEN
N
'98000'
and
N
'99999'
;
GO
```

```sql
CREATE
NONCLUSTERED
INDEX
IX_TransactionHistory_ReferenceOrderID
ON
Production.TransactionHistory (ReferenceOrderID)
ON
TransactionsPS1 (TransactionDate);
GO
```

```sql
CREATE
NONCLUSTERED
INDEX
"FIBillOfMaterialsWithEndDate"
ON
Production.BillOfMaterials (ComponentID, StartDate)
WHERE
EndDate
IS
NOT
NULL
;
```

```sql
CREATE
NONCLUSTERED
INDEX
IX_INDEX_1
ON
T1 (C2)
WITH (DATA_COMPRESSION =
ROW
);
GO
```

```sql
1
```

```sql
2
```

```sql
4
```

```sql
CREATE
CLUSTERED
INDEX
IX_PartTab2Col1
ON
PartitionTable1 (Col1)
WITH (DATA_COMPRESSION =
ROW
);
GO
CREATE
CLUSTERED
INDEX
IX_PartTab2Col1
ON
PartitionTable1 (Col1)
WITH (
DATA_COMPRESSION = PAGE
ON
PARTITIONS (1),
DATA_COMPRESSION =
ROW
ON
PARTITIONS (2
TO
4)
);
GO
```

```sql
CREATE
NONCLUSTERED
INDEX
IX_INDEX_1
ON
T1 (C2)
WITH (XML_COMPRESSION =
ON
);
GO
CREATE
CLUSTERED
INDEX
IX_PartTab2Col1
ON
PartitionTable1 (Col1)
WITH (XML_COMPRESSION =
ON
);
GO
```

`WAIT_AT_LOW_PRIORITY`

```sql
-- Execute a resumable online index create statement with MAXDOP=1
CREATE
INDEX test_idx1
ON test_table (col1)
WITH (
ONLINE
=
ON
, MAXDOP = 1,
RESUMABLE
=
ON
);
-- Executing the same command again (see above) after an index operation was paused,
resumes automatically the index create operation.
-- Execute a resumable online index creates operation with MAX_DURATION set to 240 minutes. After the time expires, the resumable index create operation is paused.
CREATE
INDEX test_idx2
ON test_table (col2)
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
-- Pause a running resumable online index creation
ALTER
INDEX test_idx1
ON test_table PAUSE;
ALTER
INDEX test_idx2
ON test_table PAUSE;
-- Resume a paused online index creation
ALTER
INDEX test_idx1
ON test_table
RESUME
;
ALTER
INDEX test_idx2
ON test_table
RESUME
;
-- Abort resumable index create operation which is running or paused
ALTER
INDEX test_idx1
ON test_table
ABORT
;
ALTER
INDEX test_idx2
ON test_table
ABORT
;
```

```sql
--Kill this session after waiting 5 minutes
CREATE
CLUSTERED
INDEX idx_1
ON dbo.T2 (a)
WITH (
ONLINE
=
ON (WAIT_AT_LOW_PRIORITY (MAX_DURATION = 5
MINUTES
, ABORT_AFTER_WAIT =
SELF
)));
GO
--Kill blocker sessions
CREATE
CLUSTERED
INDEX idx_1
ON dbo.T2 (a)
WITH (
ONLINE
=
ON (WAIT_AT_LOW_PRIORITY
```
