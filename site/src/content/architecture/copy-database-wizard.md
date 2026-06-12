---
title: "Copy Database Wizard"
topic: "collation"
description: |
  06/16/2025

  Applies to:

  SQL Server

  The Copy Database Wizard moves or copies databases and certain server objects easily from

  one instance of SQL Server to another instance, with no server downtime.
tags:
  - "collation"
  - "copy-database-wizard"
pubDate: 2025-12-01
---

06/16/2025

SQL Server

The Copy Database Wizard moves or copies databases and certain server objects easily from

one instance of SQL Server to another instance, with no server downtime. By using this wizard,

you can do the following actions:

Pick a source and destination server.

Select one or more databases to move or copy.

Specify the file location for one or more databases.

Copy logins to the destination server.

Copy supporting objects, jobs, user-defined stored procedures, and error messages.

Schedule when to move or copy the databases.

The Copy Database Wizard is not available in the Express edition.

The Copy Database Wizard cannot be used to copy or move databases that:

Are system databases (

,

,

,

).

Are marked for replication.

Are marked Inaccessible, Loading, Offline, Recovering, Suspect, or in Emergency Mode.

Have data or log files stored in Microsoft Azure storage.

When using

FileTables

, you can't use the Copy Database Wizard on the same server

because the wizard uses the same directory name.

A database cannot be moved or copied to an earlier version of SQL Server.

７

Note

Considering a migration to Azure SQL? Review the following tools instead of the Copy

Database Wizard:

```sql
master model msdb tempdb
```
