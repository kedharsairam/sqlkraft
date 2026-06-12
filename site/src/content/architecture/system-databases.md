---
title: "System Databases"
topic: "collation"
description: "This article describes how to move system databases in SQL Server."
tags: ["collation","system-databases"]
pubDate: "2025-12-01"
---

This article describes how to move system databases in SQL Server. Moving system databases

might be useful in the following situations:

Failure recovery. For example, the database is in suspect mode or has shut down because

of a hardware failure.

Planned relocation.

Relocation for scheduled disk maintenance.

The following procedures apply to moving database files within the same instance of SQL

Server. To move a database to another instance of SQL Server or to another server, use the

backup and restore

operation.

The procedures in this article require the logical name of the database files. To obtain the

name, query the name column in the

sys.master_files

catalog view.

To move a system database data or log file as part of a planned relocation or scheduled

maintenance operation, follow these steps. This includes the

,

, and

system

databases.

）

Important

If you move a system database and later rebuild the

database, you must move the

system database again because the rebuild operation installs all system databases to their

default location.

）

Important

This procedure applies to all system databases except the

and

databases. See later in this article for steps to move the

database. The

database can't be moved.

```sql
model msdb tempdb master master
Resource master
Resource
```
