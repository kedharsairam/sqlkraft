---
title: "Backup & Restore"
topic: "collation"
description: |
  Article

  •

  08/27/2024

  Applies to:

  SQL Server

  In SQL Server, you can create a new database by restoring a backup of a user database created

  by using SQL Server 2005 (9.x) or a later version. Howev
tags:
  - "collation"
  - "backup-restore"
pubDate: 2025-12-01
---

Article

•

08/27/2024

SQL Server

In SQL Server, you can create a new database by restoring a backup of a user database created

by using SQL Server 2005 (9.x) or a later version. However, backups of

,

and

that were created by using an earlier version of SQL Server cannot be restored by SQL

Server. Also, SQL Server backups cannot be restored by any earlier version of SQL Server.

When you use backup and restore to copy a database to another instance of SQL Server, the

source and destination computers can be any platform on which SQL Server runs.

The general steps are:

1. Back up the source database, which can reside on an instance of SQL Server 2005 (9.x) or

later. The computer on which this instance of SQL Server is running is the.

2. On the computer to which you want to copy the database (the

),

connect to the instance of SQL Server on which you plan to restore the database. If

needed, on the

server instance, create the same backup devices as used to

the backup of the

databases.

3. Restore the backup of the

database on the

computer. Restoring the

database automatically creates all of the database files.

Some additional considerations that may affect this process:

）

Important

2016 uses a different default path than earlier versions. Therefore, to restore

backups of a database created in the default location of earlier versions you must use the

MOVE option. For information about the new default path see. For more information about moving database files,

see "Moving the Database Files," later in this topic.
