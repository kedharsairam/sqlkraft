---
title: "Considerations & limitations"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  There are some considerations and limitations to be aware of
tags:
  - "tables"
  - "considerations-limitations"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

There are some considerations and limitations to be aware of when working with temporal

tables, due to the nature of system-versioning:

A temporal table must have a primary key defined, in order to correlate records between

the current table and the history table. The history table can't have a primary key defined.

The

period columns used to record the

and

values must

be defined with a data type of

.

Temporal syntax works on tables or views that are

stored locally

in the database. With

remote objects such as tables on a linked server, or external tables, you can't use the

clause or period predicates directly in the query.

If the name of a history table is specified during history table creation, you must specify

the schema and table name.

By default, the history table is

compressed.

If current table is partitioned, the history table is created on default file group because

partitioning configuration isn't replicated automatically from the current table to the

history table.

Temporal and history tables can't use FileTable or FILESTREAM. FileTable and FILESTREAM

allow data manipulation outside of SQL Server, so system versioning can't be guaranteed.

A node or edge table can't be created as or altered to a temporal table.

While temporal tables support blob data types, such as

,

,

, and

, they incur significant storage costs and have performance

implications due to their size. As such, when designing your system, care should be taken

when using these data types.

The history table must be created in the same database as the current table. Temporal

querying over linked servers isn't supported.

The history table can't have constraints (primary key, foreign key, table, or column

constraints).

```sql
SYSTEM_TIME
ValidFrom
ValidTo
FOR
PAGE
```
