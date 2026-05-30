---
title: "Project references"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  With project references in SQL database projects, you can create dependencies between your

  S
tags:
  - "ssms"
  - "project-references"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

With project references in SQL database projects, you can create dependencies between your

SQL project and other projects. There are two primary types of project references:

- Dependencies between SQL projects or references to

files

and NuGet packages that provide database object definitions.

- References from .NET projects to SQL projects for scenarios like

integration testing, deployment automation, and code generation.

When you understand when and how to use each type of reference, you can structure your

database development workflow effectively.

Database references allow a SQL project to incorporate objects from another SQL project, a

file, or a published NuGet package. These references are used when your database

objects depend on objects defined elsewhere, such as tables in a shared schema or system

database objects.

A basic database reference to another SQL project in the same solution looks like this:

XML

Database references support three relationship types:

- Objects from the referenced project become part of the same database

model.

- Reference objects using three-part naming with a

SQLCMD variable for the database name.

- Reference objects using four-part naming with

SQLCMD variables for both server and database names.

For detailed information about configuring database references, including examples for each

relationship type and guidance on building and publishing projects with references, see

Database references overview

.

```cmd
.dacpac
.dacpac
<ItemGroup>
<ProjectReference
Include
=
"..\Database1\Database1.sqlproj"
/>
</ItemGroup>
```
