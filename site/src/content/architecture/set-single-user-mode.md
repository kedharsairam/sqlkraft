---
title: "Set single-user mode"
topic: "collation"
description: "This article describes how to set a user-defined database to single-user mode in SQL Server by using SQL Server Management Studio or Transact-SQL. Sin"
tags: ["collation","set-single-user-mode"]
pubDate: "2025-12-01"
---

This article describes how to set a user-defined database to single-user mode in SQL Server by

using SQL Server Management Studio or Transact-SQL. Single-user mode specifies that only

one user at a time can access the database and is generally used for maintenance actions.

If other users are connected to the database at the time that you set the database to

single-user mode, their connections to the database will be closed without warning.

The database remains in single-user mode even after the user that set the option is

disconnected. At that point, a different user, but only one, can connect to the database.

Before you set the database to SINGLE_USER, verify that the

AUTO_UPDATE_STATISTICS_ASYNC option is set to. When this option is set to

, the

background thread that is used to update statistics takes a connection against the

database, and you will be unable to access the database in single-user mode. For more

information, see

ALTER DATABASE SET Options (Transact-SQL).

Requires ALTER permission on the database.

To set a database to single-user mode:

1. In

, connect to an instance of the SQL Server Database Engine, and then

expand that instance.

2. Right-click the database to change, and then select.

3. In the

dialog box, select the

page.

4. From the

option, select.

```sql
OFF
ON
```
