---
title: "Remove"
topic: "high-availability"
description: "ﾃ Summarize this article for me This article describes how to remove log shipping in SQL Server by using SQL Server Management Studio or Transact-SQL. 1."
tags: ["high-availability","remove"]
pubDate: 2025-12-01
---

ﾃ

This article describes how to remove log shipping in SQL Server by using SQL Server

Management Studio or Transact-SQL.

1. Connect to the instance of SQL Server that is currently the log shipping primary server,

and expand that instance.

2. Expand

, right-click the log shipping primary database, and then select.

3. Under

, select.

4. Clear the

check box.

5. Select

to remove log shipping from this primary database.

1. On the log shipping primary server, execute

sp_delete_log_shipping_primary_secondary

to delete the information about the secondary database from the primary server.

2. On the log shipping secondary server, execute

sp_delete_log_shipping_secondary_database

to delete the secondary database.

3. On the log shipping primary server, execute

to

delete information about the log shipping configuration from the primary server. This

also deletes the backup job.

７

Note

If there are no other secondary databases with the same secondary ID,

is invoked from

and deletes the entry for the secondary

ID and the copy and restore jobs.

```cmd
sp_delete_log_shipping_primary_database sp_delete_log_shipping_secondary_primary sp_delete_log_shipping_secondary_database
```
