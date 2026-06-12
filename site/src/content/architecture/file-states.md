---
title: "File states"
topic: "collation"
description: |
  Article

  •

  04/04/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  In SQL Server, the state of a database file i
tags:
  - "collation"
  - "file-states"
pubDate: 2025-12-01
---

Article

•

04/04/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

In SQL Server, the state of a database file is maintained independently from the state of the

database. A file is always in one specific state, such as ONLINE or OFFLINE. To view the current

state of a file, use the

sys.master_files

or

sys.database_files

catalog view. If the database is

offline, the state of the files can be viewed from the

sys.master_files

catalog view.

The state of the files in a filegroup determines the availability of the whole filegroup. For a

filegroup to be available, all files within the filegroup must be online. To view the current state

of a filegroup, use the

sys.filegroups

catalog view. If a filegroup is offline and you try to access

the filegroup by a Transact-SQL statement, it will fail with an error. When the query optimizer

builds query plans for SELECT statements, it avoids nonclustered indexes and indexed views

that reside in offline filegroups, letting these statements to succeed. However, if the offline

filegroup contains the heap or clustered index of the target table, the SELECT statements fail.

Additionally, any INSERT, UPDATE, or DELETE statement that modifies a table with any index in

an offline filegroup will fail.

The following table defines the file states.

ONLINE

The file is available for all operations. Files in the primary filegroup are always online if the

database itself is online. If a file in the primary filegroup is not online, the database is not

online and the states of the secondary files are undefined.

OFFLINE

The file is not available for access and may not be present on the disk. Files become

offline by explicit user action and remain offline until additional user action is taken.

A file state can be set offline when the file is corrupted, but it can be

restored. A file set to offline can only be set online by restoring the file from backup. For

more information about restoring a single file, see

RESTORE (Transact-SQL).

A database file is also set OFFLINE when a database is in full or bulk logged recovery and

a file is dropped. The entry in sys.master_files persists until a transaction log is truncated

past the drop_lsn value. For more information, see

Transaction Log Truncation.

ﾉ

Expand table
