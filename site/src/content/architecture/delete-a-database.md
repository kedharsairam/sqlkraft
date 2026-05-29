---
title: "Delete a database"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  This article describes how to delete a user-defined database in SQL Server by using SQL Server
  
  Management Studio or Transact-S
tags:
  - "collation"
  - "delete-a-database"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article describes how to delete a user-defined database in SQL Server by using SQL Server

Management Studio or Transact-SQL.

Delete any database snapshots that exist on the database. For more information, see

Drop a Database Snapshot

.

If the database is involved in log shipping, remove log shipping.

If the database is published for transactional replication, or published or subscribed to

merge replication, remove replication from the database.

To run

, you need

permission on the database.

1. In

, connect to an instance of the SQL Server Database Engine, and then

expand that instance.

2. Expand

, right-click the database to delete, and then select

.

3. Confirm the correct database is selected, and then select

.

For more information, see

DROP DATABASE

.

1. Connect to the Database Engine.

２

Warning

Consider taking a full backup of the database before dropping it. You can recreate a

deleted database only by restoring a full backup. For more information, see

Quickstart:

.

```sql
DROP DATABASE
CONTROL
```