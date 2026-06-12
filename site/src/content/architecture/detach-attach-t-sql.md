---
title: "Detach & attach (T-SQL)"
topic: "collation"
description: |
  Article

  •

  08/10/2023

  Applies to:

  SQL Server

  This topic describes how to move a detached database to another location and re-attach it to

  the same or a different server instance in SQL Server. Ho
tags:
  - "collation"
  - "detach-attach-t-sql"
pubDate: 2025-12-01
---

Article

•

08/10/2023

SQL Server

This topic describes how to move a detached database to another location and re-attach it to

the same or a different server instance in SQL Server. However, we recommend that you move

databases by using the ALTER DATABASE planned relocation procedure, instead of using

detach and attach. For more information, see

Move User Databases.

1. Detach the database. For more information, see

Detach a Database.

2. In a Windows Explorer or Windows Command Prompt window, move the detached

database file or files and log file or files to the new location.

You should move the log files even if you intend to create new log files. In some cases,

reattaching a database requires its existing log files. Therefore, always keep all the

detached log files until the database has been successfully attached without them.

）

Important

We recommend that you do not attach or restore databases from unknown or untrusted

sources. Such databases could contain malicious code that might execute unintended

Transact-SQL code or cause errors by modifying the schema or the physical database

structure. Before you use a database from an unknown or untrusted source, run

on the database on a nonproduction server and also examine the code, such as

stored procedures or other user-defined code, in the database.

７

Note

If you try to attach the database without specifying the log file, the attach operation

will look for the log file in its original location. If a copy of the log still exists in the

original location, that copy is attached. To avoid using the original log file, either
