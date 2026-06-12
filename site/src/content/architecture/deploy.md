---
title: "Deploy"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  Deployment is the process by which you distribute a finished application or module to be

  installed and run on another computer. Using Visual Studio, y
tags:
  - "clr-integration"
  - "deploy"
pubDate: 2025-12-01
---

Article

•

12/30/2024

SQL Server

Deployment is the process by which you distribute a finished application or module to be

installed and run on another computer. Using Visual Studio, you can develop common

language runtime (CLR) database objects and deploy them to a test server. Alternatively, the

managed database objects can also be compiled with the.NET Framework redistribution files,

instead of Visual Studio. Once compiled, the assemblies containing the CLR database objects

can then be deployed to a test server using Visual Studio or Transact-SQL statements.

Once the CLR methods are tested and verified on the test server, they can be distributed to

production servers using a deployment script. The deployment script can be generated

manually, or by using SQL Server Management Studio (covered later in this article).

The CLR integration feature is turned off by default in SQL Server and must be enabled in order

to use CLR assemblies. For more information, see

Enable CLR integration.

Using Visual Studio, you can develop CLR functions, procedures, triggers, user-defined types

(UDTs), or user-defined aggregates (UDAs), and deploy them to a test server. These managed

database objects can also be compiled with the command line compilers, such as csc.exe and

vbc.exe, included with the.NET Framework redistribution files. The Visual Studio Integrated

Development Environment isn't required to develop managed database objects for SQL Server.

Make sure that all compiler errors and warnings are resolved. The assemblies containing the

CLR routines can then be registered in a SQL Server database using Visual Studio or Transact-

SQL statements.

1. Build the project by selecting

from the

menu.

７

Note

The TCP/IP network protocol must be enabled on the SQL Server instance in order to use

Visual Studio for remote development, debugging, and development. For more

information about enabling TCP/IP protocol on the server, see.
