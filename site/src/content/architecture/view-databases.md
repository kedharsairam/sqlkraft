---
title: "View databases"
topic: "collation"
description: "This article describes how to view a list of databases on an instance of SQL Server by using SQL Serve"
tags: ["collation","view-databases"]
pubDate: "2025-12-01"
---

This article describes how to view a list of databases on an instance of SQL Server by using SQL

Server Management Studio or Transact-SQL.

If the caller of

is not the owner of the database and the database is not

or

, the minimum permissions required to see the corresponding row are ALTER ANY

DATABASE or VIEW ANY DATABASE server-level permission, or CREATE DATABASE permission in

the

database. The database to which the caller is connected can always be viewed in.

1. In

, connect to an instance of the SQL Server Database Engine, and then

expand that instance.

2. To see a list of all databases on the instance, expand.

1. Connect to the Database Engine.

2. From the Standard bar, select.

3. Copy and paste the following example into the query window and select. This

example returns a list of databases on the instance of SQL Server. The list includes the

names of the databases, their database IDs, and the dates when the databases were

created.

```sql
sys.databases master tempdb master sys.databases
```
