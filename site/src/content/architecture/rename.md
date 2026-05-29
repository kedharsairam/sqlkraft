---
title: "Rename"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This topic describes how to rename an index in SQL Server by using SQL Server Management

  Stu
tags:
  - "filestream"
  - "rename"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This topic describes how to rename an index in SQL Server by using SQL Server Management

Studio or Transact-SQL. Renaming an index replaces the current index name with the new

name that you provide. The specified name must be unique within the table or view. For

example, two tables can have an index named

, but the same table cannot have two

indexes named

. You cannot create an index with the same name as an existing disabled

index. Renaming an index does not cause the index to be rebuilt.

Limitations and Restrictions

Security

SQL Server Management Studio

Transact-SQL

When you create a PRIMARY KEY or UNIQUE constraint on a table, an index with the same

name as the constraint is automatically created for the table. Because index names must be

unique within the table, you cannot create or rename an index to have the same name as an

existing PRIMARY KEY or UNIQUE constraint on the table.

Requires ALTER permission on the index.
