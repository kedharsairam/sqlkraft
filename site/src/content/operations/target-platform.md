---
title: "Target platform"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The target platform setting is a project property that is used during project build to valida
tags:
  - "ssms"
  - "target-platform"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The target platform setting is a project property that is used during project build to validate

support for features included in the project, such as T-SQL syntax and system functions. The

target platform setting is incorporated into the

build artifact and during deployment

the target platform setting is checked against the target database to ensure compatibility. If

the target platform doesn't match the database, the deployment doesn't begin unless the

publish property

is specified.

The target platform project property is contained in the

tag in the

file under the

item:

Valid values for the target platform in the

tag include:

(SQL Server 2014)

(SQL Server 2016)

(SQL Server 2017)

(SQL Server 2019)

(SQL Server 2022)

(Azure SQL

Database)

(SQL database in

Fabric or Fabric Mirrored SQL Database, preview)

(Azure Synapse SQL Pool)

(Azure Synapse

Serverless SQL Pool)

SQL project file sample and syntax

```cmd
.dacpac
/p:AllowIncompatiblePlatform=true
DSP
.sqlproj
<PropertyGroup>
```
