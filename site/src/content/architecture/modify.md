---
title: "Modify"
topic: "filestream"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  This topic describes how to modify an index in SQL Server by using SQL Server Management
  
  Stu
tags:
  - "filestream"
  - "modify"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This topic describes how to modify an index in SQL Server by using SQL Server Management

Studio or Transact-SQL.

SQL Server Management Studio

Transact-SQL

1. In Object Explorer, connect to an instance of the SQL Server Database Engine and then

expand that instance.

2. Expand

, expand the database in which the table belongs, and then expand

.

3. Expand the table in which the index belongs and then expand

.

4. Right-click the index that you want to modify and then click

.

5. In the

dialog box, make the desired changes. For example, you can add

or remove a column from the index key, or change the setting of an index option.

1. To add, remove, or change the position of an index column, select the

page from

the

dialog box.

）

Important

Indexes created as the result of a PRIMARY KEY or UNIQUE constraint cannot be modified

by using this method. Instead, the constraint must be modified.