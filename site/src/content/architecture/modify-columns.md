---
title: "Modify Columns"
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
  - "modify-columns"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

You can modify the data type of a column in SQL Server by using SQL Server Management

Studio or Transact-SQL.

Requires ALTER permission on the table.

1. In

, right-click the table with columns for which you want to change the

scale and select.

2. Select the column for which you want to modify the data type.

3. In the

tab, select the grid cell for the

property and choose

a new data type from the dropdown list.

4. On the

menu, select

table name.

２

Warning

Modifying the data type of a column that already contains data can result in the

permanent loss of data when the existing data is converted to the new type. In addition,

code and applications that depend on the modified column can fail. These include queries,

views, stored procedures, user-defined functions, and client applications. These failures

will cascade. For example, a stored procedure that calls a user-defined function that

depends on the modified column can fail. Carefully consider any changes you want to

make to a column before making it.

７

Note
