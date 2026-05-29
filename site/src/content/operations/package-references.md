---
title: "Package references"
topic: "ssms"
description: |
  SQL projects package references
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  Package references in SQL projects allow you to reference da
tags:
  - "ssms"
  - "package-references"
pubDate: 2025-12-01
---

SQL projects package references

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Package references in SQL projects allow you to reference database objects from other projects

or NuGet packages. The database objects added to a project through package references can

be part of the same database, a different database on the same server, or a different database

on a different server.

Package references are one of several methods for adding database objects to a SQL project as

a

database reference

. Package references can contain objects for the same database, a

different database on the same server, or a different database on a different server. Package

references can be used to break up a database into smaller, more manageable projects, which

can help to reduce the time required to build a project during iterative local development.

７

Note

Package references are the recommended method for referencing database objects in

new development. Referencing NuGet packages is only supported in SDK-style SQL

projects.