---
title: "Copy Columns"
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
  - "copy-columns"
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

This topic describes how to copy columns from one table to another, copying either just the

column definition, or the definition and data in SQL Server by using SQL Server Management

Studio or Transact-SQL.

Limitations and Restrictions

Security

SQL Server Management Studio

Transact-SQL

When you copy a column that has an alias data type from one database to another, the alias

data type may not be available in the destination database. In such a case, the column will be

assigned the nearest matching base data type available in that database.

Requires ALTER permission on the table.
