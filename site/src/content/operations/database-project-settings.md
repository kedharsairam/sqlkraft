---
title: "Database Project Settings"
topic: "ssb-diagnose"
description: |
  SQL projects properties
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  In addition to the contents of the individual
  
  files, SQL database p
tags:
  - "ssb-diagnose"
  - "database-project-settings"
pubDate: 2025-12-01
---

SQL projects properties

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

In addition to the contents of the individual

files, SQL database projects contain properties that define the project's behavior and database-

level settings. These properties are stored in the

file and can be set by editing the

file directly. Some SQL projects tools, such

as Visual Studio and VS Code, provide access to edit a few or many of the project properties in a graphical user interface. This article provides an

overview of the properties that you can set for SQL database projects.

Commonly used SQL projects properties include:

Target platform (DSP)

Code analysis

DacApplicationName and DacVersion

Default schema

TreatTSqlWarningsAsErrors

During SQL project publish, changes to the database options are scripted based on the values defined in the project properties and default project

values. To prevent the database options from being modified during publish, using a tool like

SqlPackage CLI

or Visual Studio, set the publish

property to

to false. This setting can also be incorporated in a publish profile.

The

target platform

property specifies the version of SQL Server that the project targets. The

property is used to set the target platform for

the SQL project. More information on the target platform can be found in the

target platform

article.

Code analysis can dramatically improve the continuous integration and deployment process by catching potential issues early in the development

lifecycle. Learn more about enabling code analysis and including custom rules in the

SQL code analysis

article.

The following properties are used to define the data-tier application (DAC) that is created when the SQL project is built.

DacApplicationName

: The name of the data-tier application

. The default value is the project name.

DacDescription

: An optional description of the data-tier application

.

DacVersion

: The version of the data-tier application

. The default value is

.

The

property sets the default schema for the SQL project. This property applies to 1-part named objects. The default value is

.

The

and

properties control how T-SQL warnings are handled during project build. The

property suppresses T-SQL warnings during project build, specified as a comma-separated list of error numbers.

The

property treats T-SQL warnings as errors, causing any T-SQL warnings to fail the build. The default value for

is

.

The following example shows how to set the

,

, and

properties in a SQL project

file. The

property is set to

, the

property is set to

, and the

property is

set to

. The

property is only set to

on the

build configuration.

XML

Data-tier application properties

Default schema

T-SQL warnings

```cmd
.sql
.sqlproj
.sqlproj
ScriptDatabaseOptions
DSP
```