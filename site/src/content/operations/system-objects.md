---
title: "System objects"
topic: "ssms"
description: |
  SQL projects system objects
  
  10/16/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric Preview
  
  SQL projects validate database object refere
tags:
  - "ssms"
  - "system-objects"
pubDate: 2025-12-01
---

SQL projects system objects

10/16/2025

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric Preview

SQL projects validate database object references during the project build process. By default,

SQL projects don't include system objects in the database model, which can lead to validation

errors if your project contains references to system objects. To resolve these validation errors,

you would include a database reference to the

for the target platform of your

project.

The

database reference can be added as a

package reference

in

Microsoft.Build.Sql SDK-style SQL projects or as an

artifact reference

in both SDK-style and

original SQL projects.

The available system database packages are:

SQL Server master system database

SQL Server msdb system database

Azure SQL Database master system database

SQL database in Fabric system objects

Azure Synapse Analytics master system database

Azure Synapse Analytics serverless pools master system database

The most direct method for adding a package reference to a SQL project is to use the .NET

command-line interface (CLI). The following example adds a package reference to the Azure

SQL Database

system database to a SQL project:

Bash

This command adds the following entry to the

file (the package version will reflect

the latest version available at the time the command is run):

XML

```cmd
master.dacpac
master.dacpac
master
.sqlproj
dotnet add <path-to-sqlproj> package Microsoft.SqlServer.Dacpacs.Azure.Master
...
<ItemGroup>
```