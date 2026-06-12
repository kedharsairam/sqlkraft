---
title: "SQL Server Data Tools, SDK-style"
topic: "data-tools"
description: |
  SQL Server Data Tools, SDK-style (preview)

  SQL Server Data Tools (SSDT)

  is a set of development tools in Visual Studio with focused on

  building SQL Server databases and Azure SQL databases. SDK-sty
tags:
  - "data-tools"
  - "sql-server-data-tools-sdk-style"
pubDate: 2025-12-01
---

Data Tools, SDK-style (preview)

Data Tools (SSDT)

is a set of development tools in Visual Studio with focused on

building SQL Server databases and Azure SQL databases. SDK-style SQL projects in Visual

Studio enable the next generation of SQL projects as part of the

Data Tools, SDK-

feature available for Visual Studio 2022. The

SQL projects

capability extends to

CI/CD pipelines, enabling you to automate the build and deployment of your database projects

with the

SqlPackage.

The original SQL project format is based on MSBuild (.NET Framework) and is the format used

by SQL Server Data Tools in Visual Studio. The SDK-style project format is based on the new

SDK-style projects (Microsoft.Build.Sql) and is the format used by the SQL Database Projects

extension for Visual Studio Code. The Microsoft.Build.Sql project SDK is more flexible than the

original SQL projects and contains new features:.NET 8 support (cross platform)

NuGet

package references

for database references

Default globbing pattern for

files in the project

Visual Studio 2026 doesn't support SDK-style SQL projects, and the original SQL projects are

the only SQL project format available in that version of Visual Studio. Visual Studio 2022 is the

only version of Visual Studio that contains SDK-style SQL projects in the

Data

component.

For more information about SQL projects, see

What are SQL database projects?. The

Microsoft.Build.Sql SDK is available on

GitHub

and on

NuGet.org.

To install the SDK-style SQL projects in Visual Studio 2022, follow these steps:

1. Download and install Visual Studio 2022 (17.12 or later) from the

Visual Studio download

page.

２

Warning

The SDK-style SQL projects feature is in preview and side-by-side install with the original

SQL projects isn't supported. Installing the SDK-style SQL projects in a standalone Visual

Studio instance is advised.

```cmd.sql
```
