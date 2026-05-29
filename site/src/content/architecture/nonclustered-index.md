---
title: "Nonclustered index"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  You can create nonclustered indexes in SQL Server by using SQL Server Management Studio or

  T
tags:
  - "filestream"
  - "nonclustered-index"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

You can create nonclustered indexes in SQL Server by using SQL Server Management Studio or

Transact-SQL. A nonclustered index is an index structure separate from the data stored in a

table that reorders one or more selected columns. Nonclustered indexes can often help you

find data more quickly than searching the underlying table; queries can sometimes be

answered entirely by the data in the nonclustered index, or the nonclustered index can point

the Database Engine to the rows in the underlying table. Generally, nonclustered indexes are

created to improve the performance of frequently used queries not covered by the clustered

index or to locate rows in a table without a clustered index (called a heap). You can create

multiple nonclustered indexes on a table or indexed view.

Nonclustered indexes are implemented in the following ways:

constraints\*\*

When you create a

constraint, a unique nonclustered index is created to enforce a

constraint by default. You can specify a unique clustered index if a clustered index

on the table doesn't already exist. For more information, see

Unique constraints and

check constraints

.

By default, a nonclustered index is created if clustered isn't specified. The maximum

number of nonclustered indexes that can be created per table is 999. This includes any

indexes created by

or

constraints, but doesn't include XML indexes.

After a unique clustered index has been created on a view, nonclustered indexes can be

created. For more information, see

Create indexed views

.

```sql
UNIQUE
UNIQUE
UNIQUE
PRIMARY KEY
UNIQUE
```
