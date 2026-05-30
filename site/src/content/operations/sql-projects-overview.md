---
title: "SQL projects overview"
topic: "ssms"
description: |
  Applies to:

  SQL Server 2022 (16.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  A SQL database project is a local representation of SQL objec
tags:
  - "ssms"
  - "sql-projects-overview"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2022 (16.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

A SQL database project is a local representation of SQL objects that comprise the schema for a

single database, such as tables, stored procedures, or functions. The development cycle of a

SQL database project enables database development to be integrated into a continuous

integration and continuous deployment (CI/CD) workflows familiar as a development best

practice.

SQL projects are based in declarative T-SQL statements. In your SQL database project code,

you create each object once. If you need to change something about that object, such as

adding columns or changing a data type, you modify the singular file that declares the object

for the first and only time.

When a SQL database project is built, the output artifact is a

file. New and existing

databases can be updated to match the contents of the

by publishing the

to

a target database.

The SQL database projects framework around your database code that adds two foundational

capabilities to that set of files with its build process:

validation

of references between objects and the syntax against a specific version of SQL

deployment

of the build artifact to new or existing databases

```cmd
.dacpac
.dacpac
.dacpac
```
