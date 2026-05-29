---
title: "Attach a Database"
topic: "collation"
description: |
  Article
  
  •
  
  08/10/2023
  
  Applies to:
  
  SQL Server
  
  This article describes how to attach a database in SQL Server with SQL Server Management
  
  Studio or Transact-SQL. You can use this feature to copy, mov
tags:
  - "collation"
  - "attach-a-database"
pubDate: 2025-12-01
---

Article

•

08/10/2023

Applies to:

SQL Server

This article describes how to attach a database in SQL Server with SQL Server Management

Studio or Transact-SQL. You can use this feature to copy, move, or upgrade a SQL Server

database.

For a list of limitations and restrictions, see

Database Detach and Attach (SQL Server)

.

Review all of the following prerequisites before proceeding:

In the case where you are moving a database from one instance to another, the database

must first be detached from any existing SQL instance. If you attempt to attach a

database that has not been detached returns an error. For more information, see

Detach a

Database

.

When you attach a database, all data files for the database must be available. Often, these

files have extensions .mdf or .ndf (for data files) and .ldf (for transaction log files).

Additionally, any filegroups for FILESTREAM data must be present and available. For more

information to attach a FILESTREAM-enabled database, see

Move a FILESTREAM-Enabled

Database

.

If any data file has a different path from when the database was first created or last

attached, you must specify the current path of the file.

The Database Engine service account must have permissions to read the files in their new

location.

If MDF and LDF files are in different directories and one of the paths includes

, when you attach a database the operation will fail.

We recommend that you move databases within an instance with the

planned

relocation procedure instead of detach and attach, when moving database files within the

same instance. For more information, see

Move User Databases

.

```sql
\\?
\GlobalRoot
ALTER DATABASE
```