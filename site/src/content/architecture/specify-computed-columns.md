---
title: "Specify Computed Columns"
topic: "tables"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  A computed column is a virtual column that isn't physically stored in the table, unless the

tags:
  - "tables"
  - "specify-computed-columns"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

A computed column is a virtual column that isn't physically stored in the table, unless the

column is marked. A computed column expression can use data from other columns

to calculate a value for the column to which it belongs. You can specify an expression for a

computed column in SQL Server by using SQL Server Management Studio (SSMS) or Transact-

SQL (T-SQL).

A computed column can't be used as a

or

constraint definition or

with a

constraint definition. However, if the computed column value is defined

by a deterministic expression and the data type of the result is allowed in index columns,

a computed column can be used as a key column in an index or as part of any

or

constraint.

For example, if the table has integer columns

and

, a computed column defined as

might be indexed, but computed column defined as

can't be indexed, because the value might change in subsequent invocations.

A computed column can't be the target of an INSERT or UPDATE statement.

must be

when you're creating or changing indexes on

computed columns or indexed views. For more information, see

SET QUOTED_IDENTIFIER

(Transact-SQL).

Requires ALTER permission on the table.

1. In

, expand the table for which you want to add the new computed

column. Right-click

and select.

```sql
PERSISTED
DEFAULT
FOREIGN KEY
NOT NULL
PRIMARY
KEY
UNIQUE a b a
+ b a + DATEPART(dd, GETDATE())
SET QUOTED_IDENTIFIER
ON
```
