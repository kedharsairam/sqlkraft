---
title: "Remove a secondary database"
topic: "high-availability"
description: |
  ﾃ

  Summarize this article for me

  Applies to:

  SQL Server

  This article describes how to remove a log shipping secondary database in SQL Server by using

  SQL Server Management Studio or Transact-SQL.

tags:
  - "high-availability"
  - "remove-a-secondary-database"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

SQL Server

This article describes how to remove a log shipping secondary database in SQL Server by using

Management Studio or Transact-SQL.

1. Connect to the instance of SQL Server that is currently the log shipping primary server

and expand that instance.

2. Expand

, right-click the log shipping primary database, and then select.

3. Under

, select.

4. Under

, select the database you want to

remove.

5. Select.

6. Select

to update the configuration.

1. On the primary server, execute

sp_delete_log_shipping_primary_secondary

to delete the

information about the secondary database from the primary server.

2. On the secondary server, execute

sp_delete_log_shipping_secondary_database

to delete

the secondary database.

７

Note

If there are no other secondary databases with the same secondary ID,

is invoked from

and deletes the entry for the secondary

ID and the copy and restore jobs.

```cmd
sp_delete_log_shipping_secondary_primary sp_delete_log_shipping_secondary_database
```
