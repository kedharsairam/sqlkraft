---
name: "Use NOEXPAND"
title: "Use NOEXPAND"
category: "statements"
description: "Isolation level hints:"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

Granularity hints:

,

,

,

,

, or.

Isolation level hints:

,

,

,

,.

A filtered index can be used as a table hint, but causes the query optimizer to generate error

8622 if it doesn't cover all of the rows that the query selects. The following is an example of an

invalid filtered index hint. The example creates the filtered index

and then uses it as an index hint for a

statement.

The filtered index predicate includes data rows for ComponentIDs 533, 324, and 753. The query

predicate also includes data rows for ComponentIDs 533, 324, and 753 but extends the result

set to include ComponentIDs 855 and 924, which aren't in the filtered index. Therefore, the

query optimizer can't use the filtered index hint and generates error 8622. For more

information, see

Create filtered indexes.

The query optimizer doesn't consider an index hint if the

options don't have the required

values for filtered indexes. For more information, see

CREATE INDEX.

applies only to

indexed views. An indexed view is a view with a unique clustered index

created on it. If a query contains references to columns that are present both in an indexed

view and base tables, and the query optimizer determines that using the indexed view provides

the best method for executing the query, the query optimizer uses the index on the view. This

functionality is called

indexed view matching. Automatic use of an indexed view by the query

optimizer is supported only in specific editions of SQL Server. Azure SQL Database and Azure

SQL Managed Instance also support automatic use of indexed views without specifying the

hint.

For more information, see

Query processing architecture guide.

For a list of features supported by the editions of SQL Server on Windows, see:

Editions and supported features of SQL Server 2025

Editions and supported features of SQL Server 2022

Editions and supported features of SQL Server 2019

Editions and supported features of SQL Server 2017

Editions and supported features of SQL Server 2016

However, for the query optimizer to consider indexed views for matching, or use an indexed

view that is referenced with the

hint, the following

options must be set to.

ANSI_NULLS

ANSI_PADDING

ANSI_WARNINGS

ARITHABORT

CONCAT_NULL_YIELDS_NULL

QUOTED_IDENTIFIER

is implicitly set to

when

is set to. Therefore, you don't have

to manually adjust this setting.

Also, the

option must be set to.

To force the query optimizer to use an index for an indexed view, specify the

option.

This hint can be used only if the view is also named in the query. SQL Server doesn't provide a

hint to force a particular indexed view to be used in a query that doesn't name the view directly

in the

clause. However, the query optimizer considers using indexed views, even if they

aren't referenced directly in the query. The SQL Server Database Engine only automatically

creates statistics on an indexed view when a

table hint is used. Omitting this hint can

lead to execution plan warnings about missing statistics that can't be resolved by creating

statistics manually.

During query optimization, the Database Engine uses view statistics that were created

automatically or manually when the query references the view directly and the

hint is

used.

1

1

`PAGLOCK`

`NOLOCK`

`READCOMMITTEDLOCK`

`ROWLOCK`

`TABLOCK`

`TABLOCKX`

`HOLDLOCK`

`NOLOCK`

`READCOMMITTED`

`REPEATABLEREAD`

`SERIALIZABLE`

`FIBillOfMaterialsWithComponentID`

`SELECT`

`SET`

`NOEXPAND`

```sql
IF EXISTS (
SELECT name
FROM sys.indexes
WHERE name
= N
'FIBillOfMaterialsWithComponentID'
AND object_id = OBJECT_ID(N
'Production.BillOfMaterials'
))
DROP
INDEX
FIBillOfMaterialsWithComponentID
ON
Production.BillOfMaterials;
GO
CREATE
NONCLUSTERED
INDEX
[FIBillOfMaterialsWithComponentID]
ON
Production.BillOfMaterials(ComponentID, StartDate, EndDate)
WHERE
ComponentID
IN (533, 324, 753);
GO
SELECT
StartDate, ComponentID
FROM
Production.BillOfMaterials
WITH (
INDEX (FIBillOfMaterialsWithComponentID))
WHERE
ComponentID
IN (533, 324, 753, 855, 924);
GO
```

`NOEXPAND`

`NOEXPAND`

`SET`

`ON`

`ARITHABORT`

`ON`

`ANSI_WARNINGS`

`ON`

`NUMERIC_ROUNDABORT`

`OFF`

`NOEXPAND`

`FROM`

`NOEXPAND`

`NOEXPAND`
