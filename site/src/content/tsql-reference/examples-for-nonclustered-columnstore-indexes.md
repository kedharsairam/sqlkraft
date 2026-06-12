---
name: "Examples for nonclustered columnstore indexes"
title: "Examples for nonclustered columnstore indexes"
category: "statements"
description: "There are two ways to maintain the clustered columnstore index, and both methods achieved"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## A. Create a columnstore index as a secondary index on a

## rowstore table

There are two ways to maintain the clustered columnstore index, and both methods achieved

the same results:

Starting with SQL Server 2016 (13.x), use

instead of.

For more information, see

Columnstore index rowgroup.

In previous versions of SQL Server, you can use

with

, or

ALTER INDEX

and the

option.

Start by determining the clustered columnstore index name in.

Remove fragmentation by performing a REORGANIZE on the columnstore index.

This example creates a nonclustered columnstore index on a rowstore table. Only one

columnstore index can be created in this situation. The columnstore index requires extra

## B. Create a basic nonclustered columnstore index by using all

## options

## C. Create a nonclustered columnstore index with a filtered

## predicate

storage, because it contains a copy of the data in the rowstore table. This example creates a

simple table and a rowstore clustered index, and then demonstrates the syntax of creating a

nonclustered columnstore index.

The following example demonstrates the syntax of creating a nonclustered columnstore index

on the DEFAULT filegroup, specifying the maximum degrees of parallelism (MAXDOP) as 2.

The following example creates a filtered, nonclustered columnstore index on the

table in the

sample database. The filter

predicate can include columns that aren't key columns in the filtered index. The predicate in

this example selects only the rows where

is non-NULL.

## D. Change the data in a nonclustered columnstore index

In SQL Server 2014 (12.x) and earlier versions, after you create a nonclustered columnstore

index on a table, you can't directly modify the data in that table. A query with INSERT, UPDATE,

DELETE, or MERGE fails and returns an error message. Here are options you can use to add or

modify the data in the table:

Disable or drop the columnstore index. You can then update the data in the table. If you

disable the columnstore index, you can rebuild the columnstore index when you finish

updating the data. For example:

Load data into a staging table that doesn't have a columnstore index. Build a columnstore

index on the staging table. Switch the staging table into an empty partition of the main

table.

Switch a partition from the table with the columnstore index into an empty staging table.

If there's a columnstore index on the staging table, disable the columnstore index.

Perform any updates. Build (or rebuild) the columnstore index. Switch the staging table

back into the (now empty) partition of the main table.

```sql
ALTER INDEX.REORGANIZE
```

`REBUILD`

```sql
CREATE CLUSTERED COLUMNSTORE INDEX
```

```sql
DROP_EXISTING=ON
```

`REBUILD`

`MyFactTable`

```sql
DROP
INDEX
[IDX_CL_MyFactTable]
ON dbo.[MyFactTable];
```

```sql
SELECT i.object_id,
i.name,
t.object_id,
t.name
FROM sys.indexes
AS i
INNER
JOIN sys.tables
AS t
ON i.object_id = t.object_id
WHERE i.type_desc =
'CLUSTERED COLUMNSTORE'
AND t.name =
'MyFactTable'
;
--Rebuild the entire index by using ALTER INDEX and the REBUILD option.
ALTER
INDEX
IDX_CL_MyFactTable
ON dbo.[MyFactTable] REORGANIZE;
```

`Production.BillOfMaterials`

`AdventureWorks2025`

`EndDate`

```sql
CREATE
TABLE dbo.SimpleTable (
ProductKey
INT
NOT
NULL
,
OrderDateKey
INT
NOT
NULL
,
DueDateKey
INT
NOT
NULL
,
ShipDateKey
INT
NOT
NULL
);
GO
CREATE
CLUSTERED
INDEX cl_simple
ON dbo.SimpleTable(ProductKey);
GO
CREATE
NONCLUSTERED COLUMNSTORE
INDEX csindx_simple
ON dbo.SimpleTable(OrderDateKey, DueDateKey, ShipDateKey);
GO
```

```sql
CREATE
NONCLUSTERED COLUMNSTORE
INDEX csindx_simple
ON
SimpleTable(OrderDateKey, DueDateKey, ShipDateKey)
WITH (DROP_EXISTING =
ON
,
MAXDOP = 2)
ON
"DEFAULT"
;
GO
```

```sql
IF EXISTS (
SELECT name
FROM sys.indexes
WHERE name
= N
'FIBillOfMaterialsWithEndDate'
AND object_id = OBJECT_ID(N
'Production.BillOfMaterials'
))
DROP
INDEX
FIBillOfMaterialsWithEndDate
ON
Production.BillOfMaterials;
GO
CREATE
NONCLUSTERED COLUMNSTORE
INDEX
"FIBillOfMaterialsWithEndDate"
ON
Production.BillOfMaterials(ComponentID, StartDate)
WHERE
EndDate
IS
NOT
NULL
;
```

```sql
ALTER
INDEX mycolumnstoreindex
ON dbo.mytable
DISABLE
;
-- update the data in mytable as necessary
ALTER
INDEX mycolumnstoreindex
ON dbo.mytable
REBUILD
;
```
