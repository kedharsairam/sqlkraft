---
title: "Clustered index"
topic: "filestream"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  You can create clustered indexes on tables by using SQL Server Management Studio or
  
  Transact
tags:
  - "filestream"
  - "clustered-index"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

You can create clustered indexes on tables by using SQL Server Management Studio or

Transact-SQL. With few exceptions, every table should have a clustered index. Besides

improving query performance, a clustered index can be rebuilt or reorganized on demand to

control table fragmentation. A clustered index can also be created on a view. (Clustered

indexes are defined in the article

Clustered and nonclustered indexes

.)

Clustered indexes are implemented in the following ways:

and

constraints**

When you create a

constraint, a unique clustered index on the column or

columns is automatically created if a clustered index on the table doesn't already exist

and you don't specify a unique nonclustered index. The primary key column can't allow

values.

When you create a

constraint, a unique nonclustered index is created to enforce a

constraint by default. You can specify a unique clustered index if a clustered index

on the table doesn't already exist.

An index created as part of the constraint is automatically given the same name as the

constraint name. For more information, see

Primary and foreign key constraints

and

Unique constraints and check constraints

.

You can create a clustered index on a column other than primary key column if a

nonclustered primary key constraint was specified.

When a clustered index structure is created, disk space for both the old (source) and new

(target) structures is required in their respective files and filegroups. The old structure isn't

deallocated until the complete transaction commits. Additional temporary disk space for

sorting might also be required. For more information, see

Disk Space Requirements for

Index DDL Operations

.

```sql
PRIMARY KEY
UNIQUE
PRIMARY KEY
NULL
UNIQUE
UNIQUE
```