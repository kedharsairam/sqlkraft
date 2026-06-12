---
name: "PRIMARY KEY constraints"
title: "PRIMARY KEY constraints"
category: "statements"
description: "statement that creates the temp table. For example, if a stored procedure creates a temporary"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

statement that creates the temp table. For example, if a stored procedure creates a temporary

table with a named primary key constraint, the stored procedure can't be executed

simultaneously by multiple users.

Global temporary tables in SQL Server (table names prefixed with

) are stored in

and

shared among all user sessions across the entire SQL Server instance.

supports global temporary tables that are also stored in

but are

scoped to the database level. This means that global temporary tables are shared among all

user sessions within the same database. User sessions from other databases can't access global

temporary tables. Otherwise, global temporary tables for Azure SQL Database follow the same

## syntax and semantics that SQL Server uses.

Similarly, global temporary stored procedures are also scoped to the database level in Azure

SQL Database.

Local temporary tables (table names prefixed with

) are also supported for Azure SQL

Database and follow the same syntax and semantics that SQL Server uses. For more

information, see

Temporary tables.

Any user can create and access temporary objects.

Before creating a partitioned table by using CREATE TABLE, you must first create a partition

function to specify how the table becomes partitioned. A partition function is created by using

CREATE PARTITION FUNCTION. Second, you must create a partition scheme to specify the

filegroups to hold the partitions indicated by the partition function. A partition scheme is

created by using

CREATE PARTITION SCHEME. Placement of PRIMARY KEY or UNIQUE

constraints to separate filegroups can't be specified for partitioned tables. For more

information, see

Partitioned tables and indexes.

A table can contain only one PRIMARY KEY constraint.

```sql
##
```

`tempdb`

`tempdb`

```sql
#
```
