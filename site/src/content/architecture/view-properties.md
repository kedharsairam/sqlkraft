---
title: "View properties"
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

  You
tags:
  - "tables"
  - "view-properties"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

You can view the foreign key attributes of a relationship in SQL Server by using SQL Server

Management Studio or Transact-SQL.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

1. Open the Table Designer for the table containing the foreign key you want to view, right-

click in the Table Designer, and choose

from the shortcut menu.

2. In the

dialog box, select the relationship with properties you

want to view.

If the foreign key columns are related to a primary key, the primary key columns are identified

in

by a primary key symbol in the row selector.

1. In

, connect to an instance of Database Engine.

2. On the Standard bar, select

.

3. Copy and paste the following example into the query window and select

. The

example returns all foreign keys and their properties for the table

in the sample database.

SQL

```sql
HumanResources.Employee
USE
AdventureWorks2022;
GO
SELECT
f.name
AS
foreign_key_name,
OBJECT_NAME(f.parent_object_id)
AS
table_name,
COL_NAME(fc.parent_object_id, fc.parent_column_id)
AS
```
