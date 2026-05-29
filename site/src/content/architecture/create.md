---
title: "Create"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  The only way to create a SQL Server database snapshot is to use Transact-SQL. SQL Server
  
  Management Studio doesn't support the creation of database snapshots.
  
  The source dat
tags:
  - "collation"
  - "create"
pubDate: 2025-12-01
---

Applies to:

SQL Server

The only way to create a SQL Server database snapshot is to use Transact-SQL. SQL Server

Management Studio doesn't support the creation of database snapshots.

The source database, which can use any recovery model, must meet the following

prerequisites:

The server instance must be running an edition of SQL Server that supports database

snapshot. For information about support for database snapshots in SQL Server, see

Editions and supported features of SQL Server 2022

.

The source database must be online, unless the database is a mirror database within a

database mirroring session.

To create a database snapshot on a mirror database, the database must be in the

synchronized

mirroring state

.

The source database can't be configured as a scalable shared database.

Prior to SQL Server 2019 (15.x), the source database couldn't contain a

filegroup. Support for in-memory database snapshots was added

in SQL Server 2019 (15.x).

This section discusses the following best practices:

Best practice: naming database snapshots

Best practice: limiting the number of database snapshots

Best practice: client connections to a database snapshot

）

Important

For information about other significant considerations, see

.

```sql
MEMORY_OPTIMIZED_DATA
```