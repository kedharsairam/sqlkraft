---
title: "Modify data"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  Data in a system-versioned temporal table is modified using r
tags:
  - "tables"
  - "modify-data"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Data in a system-versioned temporal table is modified using regular data manipulation

language (DML) statements, with one important difference: period column data can't be

directly modified. When data is updated, it is versioned, and the previous version of each

updated row is inserted into the history table. When data is deleted, the delete is logical, and

the row moved into the history table from the current table; the data isn't permanently deleted.

When you insert new data, you need to account for the

columns if they aren't

.

You can also use partition switching with temporal tables.

You can construct your

statement when you have visible

columns as follows, to

account for the

columns:

If you specify the column list in your

statement, you can omit the

columns

because the system generates values for these columns automatically.

SQL

If you do specify the

columns in the column list in your

statement, then you

need to specify

as their value.

SQL

```sql
PERIOD
HIDDEN
INSERT
PERIOD
PERIOD
INSERT
PERIOD
PERIOD
INSERT
DEFAULT
-- Insert with column list and without period columns
INSERT
INTO
[dbo].[Department] (
[DeptID],
[DeptName],
[ManagerID],
[ParentDeptID]
)
VALUES
(10,
'Marketing'
, 101, 1);
INSERT
INTO
[dbo].[Department] (
DeptID,
```
