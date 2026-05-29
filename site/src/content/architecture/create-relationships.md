---
title: "Create relationships"
topic: "tables"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  This article describes how to create foreign key relationship
tags:
  - "tables"
  - "create-relationships"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

This article describes how to create foreign key relationships in SQL Server by using SQL Server

Management Studio or Transact-SQL. You create a relationship between two tables when you

want to associate rows of one table with rows of another.

Creating a new table with a foreign key requires

CREATE TABLE

permission in the database, and

ALTER SCHEMA

permission on the schema in which the table is being created.

Creating a foreign key in an existing table requires

ALTER TABLE

permission on the table.

A foreign key constraint doesn't have to be linked only to a primary key constraint in

another table. Foreign keys can also be defined to reference the columns of a

constraint in another table.

When a value other than

is entered into the column of a

constraint, the

value must exist in the referenced column. Otherwise, a foreign key violation error

message is returned. To make sure that all values of a composite foreign key constraint

are verified, specify

on all the participating columns.

constraints can reference only tables within the same database on the same

server. Cross-database referential integrity must be implemented through triggers. For

more information, see

CREATE TRIGGER (Transact-SQL)

.

constraints can reference another column in the same table, and is referred

to as a self-reference.

A

constraint specified at the column level can list only one reference column.

This column must have the same data type as the column on which the constraint is

defined.

A

constraint specified at the table level must have the same number of

reference columns as the number of columns in the constraint column list. The data type

of each reference column must also be the same as the corresponding column in the

column list.

```sql
UNIQUE
NULL
FOREIGN KEY
NOT NULL
FOREIGN KEY
FOREIGN KEY
FOREIGN KEY
FOREIGN KEY
```