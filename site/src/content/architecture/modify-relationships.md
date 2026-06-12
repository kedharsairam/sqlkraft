---
title: "Modify relationships"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  You can modify the foreign key side of a relationship in SQL
tags:
  - "tables"
  - "modify-relationships"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

You can modify the foreign key side of a relationship in SQL Server by using SQL Server

Management Studio or Transact-SQL. Modifying a table's foreign key changes which columns

are related to columns in the primary key table.

Limitations and Restrictions

Security

Management Studio

Transact-SQL

The new foreign key column must match the data type and size of the primary key column to

which it relates, with these exceptions:

A

column or

column can relate to a

column.

A

column can relate to a

column.

An alias data type can relate to its base type.

Requires ALTER permission on the table.
