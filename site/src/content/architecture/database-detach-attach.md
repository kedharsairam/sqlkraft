---
title: "Database Detach & Attach"
topic: "collation"
description: |
  Article
  
  •
  
  04/01/2024
  
  Applies to:
  
  SQL Server
  
  The data and transaction log files of a database can be detached and then reattached to the
  
  same or another instance of SQL Server. Detaching and atta
tags:
  - "collation"
  - "database-detach-attach"
pubDate: 2025-12-01
---

Article

•

04/01/2024

Applies to:

SQL Server

The data and transaction log files of a database can be detached and then reattached to the

same or another instance of SQL Server. Detaching and attaching a database is useful if you

want to change the database to a different instance of SQL Server on the same computer or to

move the database.

File access permissions are set during several database operations, including detaching or

attaching a database.

Detaching a database removes it from the instance of SQL Server but leaves the database

intact within its data files and transaction log files. These files can then be used to attach the

database to any instance of SQL Server, including the server from which the database was

detached.

You can't detach a database if any of the following are true:

The database is replicated and published. If replicated, the database must be

unpublished. Before you can detach it, you must disable publishing by running

sp_replicationdboption

.

）

Important

We recommend that you don't attach or restore databases from unknown or untrusted

sources. Such databases could contain malicious code that might execute unintended

Transact-SQL code or cause errors by modifying the schema or the physical database

structure. Before you use a database from an unknown or untrusted source, run

on the database on a nonproduction server and also examine

the code, such as stored procedures or other user-defined code, in the database.

７

Note