---
title: "Add Database Reference Dialog Box"
topic: "ssb-diagnose"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Database references in SQL projects enable you to incorporate objects that aren't included in
tags:
  - "ssb-diagnose"
  - "add-database-reference-dialog-box"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Database references in SQL projects enable you to incorporate objects that aren't included in a

project by linking to another project,

file, or published NuGet package. The database

objects added to a project can be part of the same database, a different database on the same

server, or a different database on a different server. For SQL Server development, database

references can be used to link to another database on the same server for three-part naming,

or to link to a different database on a different server for cross-database queries. For databases

with a large number of objects in distinct groups, database references can be used to break up

a database into smaller, more manageable projects. Smaller project size can help to improve

performance and reduce the time required to build a project during iterative local

development.



７

Note

```cmd
.dacpac
```
