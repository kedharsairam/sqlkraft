---
title: "Rename a database"
topic: "collation"
description: "08/07/2025 This article describes how to rename a user-defined database in SQL Server, Azure SQL Database, or Azure SQL Manag"
tags: ["collation","rename-a-database"]
pubDate: 2025-12-01
---

This article describes how to rename a user-defined database in SQL Server, Azure SQL

Database, or Azure SQL Managed Instance, by using SQL Server Management Studio (SSMS) or

Transact-SQL (T-SQL). The name of the database can include any characters that follow the

rules for identifiers.

System databases can't be renamed.

The database name can't be changed while other users are accessing the database.

Use SSMS Activity Monitor to find other connections to the database, and close them.

For more information, see

Open Activity Monitor in SQL Server Management Studio

(SSMS).

In SQL Server, you can set a database in single user mode to close any open

connections. For more information, see

set the database to single-user mode.

In Azure SQL Database, you must make sure no other users have an open connection

to the database to be renamed.

Renaming a database doesn't change the physical name of the database files on disk, or

the logical names of the files. For more information, see

Database Files and Filegroups.

It isn't possible to rename an Azure SQL database configured in an

active geo-replication

relationship.

Requires

permission on the database.

７

Note

To rename a database in Azure Synapse Analytics or Parallel Data Warehouse, use the

statement.

`ALTER`
