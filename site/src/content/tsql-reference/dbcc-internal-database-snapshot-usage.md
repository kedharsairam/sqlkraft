---
name: "DBCC internal database snapshot usage"
title: "DBCC internal database snapshot usage"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Transact-SQL programming language provides DBCC statements that act as Database

Console Commands for SQL Server.

Database Console Command statements are grouped into the following categories.

Maintenance

Maintenance tasks on a database, index, or filegroup.

Miscellaneous

Miscellaneous tasks such as enabling trace flags or removing a DLL from memory.

Informational

Tasks that gather and display various types of information.

Validation

Validation operations on a database, table, index, catalog, filegroup, or allocation of

database pages.

DBCC commands take input parameters and return values. All DBCC command parameters can

accept both Unicode and DBCS literals.

The following DBCC commands operate on an internal read-only database snapshot that the

Database Engine creates. The snapshot prevents blocking and concurrency problems when

these commands are executed. For more information, see

Database Snapshots (SQL Server).

When you execute one of these DBCC commands, the Database Engine creates a database

snapshot and brings it to a transactionally consistent state. The DBCC command then runs the

checks against this snapshot. After the DBCC command is completed, this snapshot is dropped.

Expand table

```sql
DBCC CHECKALLOC
DBCC CHECKCATALOG
DBCC CHECKDB
DBCC CHECKFILEGROUP
DBCC CHECKTABLE
```
