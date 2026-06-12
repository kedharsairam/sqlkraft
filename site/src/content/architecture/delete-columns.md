---
title: "Delete Columns"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft Fabric

  Thi
tags:
  - "tables"
  - "delete-columns"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

This article describes how to delete table columns in SQL Server using

Management

Studio (SSMS)

or Transact-SQL.

You can't delete a column that has a

constraint. You must first delete the constraint.

You can't delete a column that has

or

constraints or other

dependencies except when using the

Table Designer

in SSMS. When using

Object Explorer

in

SSMS or Transact-SQL, you must first remove all dependencies on the column.

Requires

permission on the table.

You can delete columns in SSMS using Object Explorer or Table Designer.

The following steps explain how to delete columns with Object Explorer in SSMS:

1. Connect to an instance of Database Engine.

2. In

, locate the table from which you want to delete columns, and expand

the table to expose the column names.

Ｕ

Caution

When you delete a column from a table, the column and all the data it contains are

deleted.

```sql
CHECK
PRIMARY KEY
FOREIGN KEY
ALTER
```
