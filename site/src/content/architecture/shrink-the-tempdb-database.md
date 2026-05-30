---
title: "Shrink the tempdb database"
topic: "collation"
description: |
  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article discusses various methods that you can use to shrink the

  database in SQL

  Server.

  You can use any of the following methods to change
tags:
  - "collation"
  - "shrink-the-tempdb-database"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Managed Instance

This article discusses various methods that you can use to shrink the

database in SQL

Server.

You can use any of the following methods to change the size of

. The first three options

are described in this article. If you want to use SQL Server Management Studio (SSMS), follow

the instructions in

Shrink a database

.

Yes

Gives complete control on the size of the default

files (

and

).

No

Operates at database level.

No

Lets you shrink individual files.

SQL Server Management

Studio

No

Shrink database files through a graphical user interface.

By default, the

database is configured to autogrow as needed. Therefore, this database

might unexpectedly grow over time to a size larger than the desired size. Larger

database sizes don't adversely affect the performance of SQL Server.

When SQL Server starts, it recreates

by using a copy of the

database, and resets

to its last configured size. The configured size is the last explicit size that you set using

a file size changing operation such as

with the

option, or the

or

statements. Therefore, unless you need to use different

values or want to immediately resolve a large

database, you can wait for the next

restart of the SQL Server service for the size to decrease.

You can shrink

while

activity is ongoing. However, you might encounter other

errors such as blocking, deadlocks, and so on, that can prevent shrink from completing. To

make sure that a shrink of

succeeds, perform this operation while the server is in

single-user mode, or when you stop all

activity.

ﾉ

Expand table

```sql
tempdb tempdb
ALTER DATABASE tempdb tempdev templog
DBCC SHRINKDATABASE
DBCC SHRINKFILE tempdb tempdb tempdb model tempdb
ALTER DATABASE
MODIFY FILE
DBCC
SHRINKFILE
DBCC SHRINKDATABASE tempdb tempdb tempdb tempdb tempdb
```
