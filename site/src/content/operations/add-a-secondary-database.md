---
title: "Add a secondary database"
topic: "high-availability"
description: |
  ﾃ
  
  Summarize this article for me
  
  Applies to:
  
  SQL Server
  
  This article describes how to add a secondary database to an existing log shipping
  
  configuration in SQL Server by using SQL Server Managemen
tags:
  - "high-availability"
  - "add-a-secondary-database"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

This article describes how to add a secondary database to an existing log shipping

configuration in SQL Server by using SQL Server Management Studio or Transact-SQL.

1. Right-click the database you want to use as your primary database in the log shipping

configuration, and then select

.

2. Under

, select

.

3. Under

, select

.

4. Select

and connect to the instance of SQL Server that you want to use as your

secondary server.

5. In the

box, choose a database from the list or type the name of the

database you want to create.

6. On the

tab, choose the option that you want to use to

initialize the secondary database.

7. On the

, in the

box, type the path of the

folder into which the transaction logs backups should be copied. This folder is often

located on the secondary server.

8. Note the copy schedule listed in the

box under

. If you want to

customize the schedule for your installation, select

and then adjust the SQL

Server Agent schedule as needed. This schedule should approximate the backup

schedule.

9. On the

tab, under

, choose the

or

option.

10. If you chose the

option, choose if you want to disconnect users from the

secondary database while the restore operation is underway.