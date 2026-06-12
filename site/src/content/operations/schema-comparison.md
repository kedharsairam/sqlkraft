---
title: "Schema comparison"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The schema comparison tooling enables you to compare two database definitions, where the

  sou
tags:
  - "ssms"
  - "schema-comparison"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The schema comparison tooling enables you to compare two database definitions, where the

source and target of the comparison can be any combination of connected database, SQL

database project or

file. Once the comparison is complete, the results of the

comparison appear as a set of actions that make the target the same as the source. Differences

between the database models are presented in a similar manner as a source control diff. If the

schema compare target is a SQL project or a database, you can update the target directly from

the schema compare interface, or generate an update script that has the same effect.

Schema compare provides the following features:

Compare schemas between two

files, databases, or SQL projects.

View results as a set of actions to match a target against the source.

Selectively exclude actions listed in results.

Set options that control the scope of the comparison.

Apply changes directly to the target, or generate a script to apply changes at a later time.

Save the comparison.



```cmd.dacpac.dacpac
```
