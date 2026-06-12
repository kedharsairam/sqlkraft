---
title: "Restore the master database"
topic: "linux-operations"
description: "on Linux Under certain circumstances, you might need to restore the database on an instance of SQL Server in single-user mode on Linux."
tags: ["linux-operations","restore-the-master-database"]
pubDate: 2025-12-01
---

on Linux

Under certain circumstances, you might need to restore the

database on an instance of

in single-user mode on Linux. Scenarios include migrating to a new instance, or

recovering from inconsistencies.

To restore the

database, you must start SQL Server in single-user mode, by using the

startup option

from the command line.

For starting a SQL Server instance in single-user mode on Windows, see

Single-user mode for.

Starting SQL Server in single-user mode enables any member of the local administrator group to

connect to SQL Server as a member of the

fixed server role. For more information, see

Connect to SQL Server when system administrators are locked out.

When you start an instance of SQL Server in single-user mode:

Only one user can connect to the server.

The

process isn't executed. By default, it runs automatically at startup.

1. The following command stops the SQL Server instance if it's currently running:

７

Note

will automatically shut down after the restore is complete. This behavior is by

design.

```cmd
master master
-m
CHECKPOINT systemctl stop mssql-server
```
