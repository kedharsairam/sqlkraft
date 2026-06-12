---
title: "Resolve indexes on views"
topic: "index-architecture"
description: "is defined as shown in the following:"
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

And

is defined as shown in the following:

The join order in the query plan is

,

,

,

,.

As with any index, SQL Server chooses to use an indexed view in its query plan only if the

Query Optimizer determines it is beneficial to do so.

Indexed views can be created in any edition of SQL Server. In some editions of some older

versions of SQL Server, the Query Optimizer automatically considers the indexed view. In some

editions of some older versions of SQL Server, to use an indexed view, the

table hint

must be used. Automatic use of an indexed view by the query optimizer is supported only in

specific editions of SQL Server. Azure SQL Database and Azure SQL Managed Instance also

support automatic use of indexed views without specifying the

hint.

The SQL Server Query Optimizer uses an indexed view when the following conditions are met:

These session options are set to

:

The

session option is set to OFF.

The Query Optimizer finds a match between the view index columns and elements in the

query, such as the following:

Search condition predicates in the WHERE clause

Join operations

Aggregate functions

`View1`

`Table1`

`Table2`

`TableA`

`TableB`

`Table3`

`NOEXPAND`

`NOEXPAND`

`ON`

```sql
ANSI_NULLS
ANSI_PADDING
ANSI_WARNINGS
ARITHABORT
CONCAT_NULL_YIELDS_NULL
QUOTED_IDENTIFIER
```

`NUMERIC_ROUNDABORT`

```sql
SELECT
*
FROM
Table1, Table2, View1, Table3
WHERE
Table1.Col1 = Table2.Col1
AND
Table2.Col1 = View1.Col1
AND
View1.Col2 = Table3.Col2;
OPTION (FORCE ORDER);
CREATE
VIEW
View1
AS
SELECT
Colx, Coly
FROM
TableA, TableB
WHERE
TableA.ColZ = TableB.Colz;
```
