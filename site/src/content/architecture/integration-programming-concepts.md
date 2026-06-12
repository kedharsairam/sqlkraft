---
title: "Integration programming concepts"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  SQL Server features the integration of the common language runtime (CLR) component of the

  .NET Framework for Windows.

  You
tags:
  - "clr-integration"
  - "integration-programming-concepts"
pubDate: 2025-12-01
---

Article

•

12/30/2024

SQL Server

Azure SQL Managed Instance

features the integration of the common language runtime (CLR) component of the.NET Framework for Windows.

You can write stored procedures, triggers, user-defined types, user-defined functions, user-

defined aggregates, and streaming table-valued functions, using any language, including C#

and Visual Basic.NET.

CLR integration doesn't support.NET Core, or.NET 5 and later versions.

You can load CLR database objects for SQL Server 2017 (14.x) and later versions on Linux,

but they must be built with the.NET Framework. Also, CLR assemblies with the

or

permission set aren't supported on Linux.

By default, the.NET Framework

runtime

is installed with SQL Server, but the.NET

Framework SDK isn't. To install the latest version of the.NET Framework SDK, see

Download.NET Framework Developer Pack.

The

namespace includes core functionality for CLR

programming in SQL Server. For documentation on the

namespace, see

Microsoft.SqlServer.Server Namespace (.NET Framework 4.8).

CLR functionality, such as CLR user functions, aren't supported for Azure SQL Database.

The following table lists the articles in this section.

Description

Common language

runtime (CLR) integration

Provides a brief overview of the CLR, and describes how and why this

technology is used in SQL Server. Describes the benefits of using the CLR to

create database objects.

ﾉ

Expand table

```sql
EXTERNAL_ACCESS
UNSAFE
Microsoft.SqlServer.Server
Microsoft.SqlServer.Server
```
