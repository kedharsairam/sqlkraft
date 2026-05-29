---
title: "Build from the Command Line"
topic: "profiler"
description: |
  While the SQL Database Project extension in
  
  provides a graphical user
  
  interface to build
  
  SQL database projects
  
  , a command line build experience is also available for
  
  Windows, macOS, and Linux en
tags:
  - "profiler"
  - "build-from-the-command-line"
pubDate: 2025-12-01
---

While the SQL Database Project extension in

provides a graphical user

interface to build

SQL database projects

, a command line build experience is also available for

Windows, macOS, and Linux environments. This article outlines the prerequisites and syntax

needed to build a

from a Microsoft.Build.Sql SDK-style SQL project at the command

line.

Using

Microsoft.Build.Sql

with

SDK-style SQL projects

is the preferred method for working

with SQL projects from the command line.

To build an SDK-style SQL project from the command line on Windows, macOS, or Linux, use

the following command:

Bash

Optionally, specify the project name. If you specify the project name, you can build a specific

project within a more complex folder structure.

Bash

Starting with Microsoft.Build.Sql 2.0.0-preview.3, you can build SDK-style SQL projects from the

command line using .NET Framework and msbuild. For SQLCLR objects, .NET Framework is

required to build the SQL project.

Bash

```cmd
.dacpac
dotnet build
dotnet build AdventureWorks/AdventureWorks.sqlproj
msbuild AdventureWorks/AdventureWorks.sqlproj
```