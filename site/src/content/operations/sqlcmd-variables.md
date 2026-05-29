---
title: "SQLCMD variables"
topic: "ssms"
description: |
  SQLCMD variables overview

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  SQLCMD variables are used in SQL projects to create dynamically re
tags:
  - "ssms"
  - "sqlcmd-variables"
pubDate: 2025-12-01
---

SQLCMD variables overview

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

SQLCMD variables are used in SQL projects to create dynamically replaceable tokens in SQL

objects and scripts. The values of these variables are set at deployment time and can be used

to dynamically set values in a SQL project. Values for SQLCMD variables can be set in the

publish action or through a publish profile.

SQLCMD variables are defined in the

file under an

item. In this example,

the variable

is defined with a default value of

:

The

element is optional. When a default value is provided, it's only used to load

in the publish dialog of graphical tools for SQL projects. The default value isn't compiled into

SQL project file sample and syntax

```cmd
.sqlproj
<ItemGroup>
EnvironmentName
testing
DefaultValue
```
