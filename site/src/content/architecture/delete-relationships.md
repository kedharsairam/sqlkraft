---
title: "Delete relationships"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  You can delete a foreign key constraint in SQL Server by usin
tags:
  - "tables"
  - "delete-relationships"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

You can delete a foreign key constraint in SQL Server by using SQL Server Management Studio

or Transact-SQL. Deleting a foreign key constraint removes the requirement to enforce

referential integrity.

Foreign keys reference keys in other tables, for more information, see

Primary and Foreign Key

Constraints

.

Requires ALTER permission on the table.

1. In

, expand the table with the constraint and then expand

.

2. Right-click the constraint and then select

.

3. In the

dialog box, select

.

1. In

, connect to an instance of Database Engine.

2. On the Standard bar, select

.

3. Copy and paste the following example into the query window and select

.

```sql
USE
AdventureWorks2022;
GO
ALTER
TABLE dbo.DocExe
```
