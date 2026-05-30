---
title: "Create a database"
topic: "collation"
description: |
  08/07/2025

  Applies to:

  SQL Server

  This article describes how to create a database in SQL Server by using SQL Server Management

  Studio or Transact-SQL.

  To create a database in Azure SQL Database u
tags:
  - "collation"
  - "create-a-database"
pubDate: 2025-12-01
---

08/07/2025

Applies to:

SQL Server

This article describes how to create a database in SQL Server by using SQL Server Management

Studio or Transact-SQL.

To create a database in Azure SQL Database using T-SQL, see

CREATE DATABASE

.

A maximum of 32,767 databases can be specified on an instance of SQL Server.

The

statement must run in autocommit mode (the default transaction

management mode) and isn't allowed in an explicit or implicit transaction.

The

master

database should be backed up whenever a user database is created, modified, or

dropped.

When you create a database, make the data files as large as possible based on the maximum

amount of data you expect in the database.

Requires

permission in the

database, or requires

,

or

permission.

To maintain control over disk use on an instance of SQL Server, permission to create databases

is typically limited to a few SQL Server logins.

1. In

, connect to an instance of the SQL Server Database Engine and then

expand that instance.

```sql
CREATE DATABASE
CREATE DATABASE master
CREATE ANY DATABASE
ALTER ANY DATABASE
```
