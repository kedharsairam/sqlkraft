---
title: "Unique constraints and check constraints"
topic: "tables"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  constraints and

  constraints are two types of constraints that can be used to

  enforce data i
tags:
  - "tables"
  - "unique-constraints-and-check-constraints"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

constraints and

constraints are two types of constraints that can be used to

enforce data integrity in SQL Server tables. These are important database objects.

This article contains the following sections.

UNIQUE constraints

CHECK constraints

Constraints are rules that the SQL Server Database Engine enforces for you. For example, you

can use

constraints to make sure that no duplicate values are entered in specific

columns that don't participate in a primary key. Although both a

constraint and a

constraint enforce uniqueness, use a

constraint instead of a

constraint when you want to enforce the uniqueness of a column (or combination of columns)

that isn't the primary key.

Unlike

constraints,

constraints allow for the value. However, as with

any value participating in a

constraint, only one null value is allowed per column. A

constraint can be referenced by a

constraint.

When a

constraint is added to an existing column or columns in the table, by default,

the Database Engine examines the existing data in the columns to make sure all values are

unique. If a

constraint is added to a column that has duplicate values, the Database

Engine returns an error and doesn't add the constraint.

The Database Engine automatically creates a

index to enforce the uniqueness

requirement of the

constraint. Therefore, if an attempt to insert a duplicate row is

made, the Database Engine returns an error message that states the

constraint was

violated, and doesn't add the row to the table. Unless a clustered index is explicitly specified, a

unique, nonclustered index is created by default to enforce the

constraint.

```sql
UNIQUE
CHECK
UNIQUE
UNIQUE
PRIMARY KEY
UNIQUE
PRIMARY KEY
PRIMARY KEY
UNIQUE
NULL
UNIQUE
UNIQUE
FOREIGN KEY
UNIQUE
UNIQUE
UNIQUE
UNIQUE
UNIQUE
UNIQUE
```
