---
title: "Convert an original SQL project"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Creating a new SDK-style SQL project is a

  quick task

  . However, if you have existing SQL

  p
tags:
  - "ssms"
  - "convert-an-original-sql-project"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Creating a new SDK-style SQL project is a

quick task

. However, if you have existing SQL

projects you can convert them to SDK-style SQL projects in place to take advantage of the new

features.

Once you convert the project, you can use the new features of the SDK-style project, such as:

cross-platform build support

simplified project file format

package references

To complete the conversion carefully, we will:

1. Create a backup of the original project file.

2. Build a

file from the original project for comparison.

3. Modify the project file to an SDK-style project.

4. Build a

file from the modified project for comparison.

5. Verify that the

files are the same.

SDK-style projects aren't supported in SQL Server Data Tools (SSDT) in Visual Studio. Once

converted, you must use one of the following to build or edit the project:

the command line

the SQL Database Projects extension in Visual Studio Code

the SQL Server Data Tools, SDK-style (preview) in Visual Studio 2022

.NET 8 SDK

７

Note

You might find that your SQL project contains customization that extends the changes

required beyond these steps. In addition to this article, the

can be used to understand the changes necessary to upgrade from an original SQL project

to SDK-style SQL projects.

```cmd
.dacpac
.dacpac
.dacpac
```
