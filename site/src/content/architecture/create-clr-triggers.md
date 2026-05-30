---
title: "Create CLR Triggers"
topic: "change-data-capture"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  You can create a database object inside SQL Server that is programmed in an assembly created

  in the .NET Framework common language runtime (CLR). Data
tags:
  - "change-data-capture"
  - "create-clr-triggers"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

You can create a database object inside SQL Server that is programmed in an assembly created

in the .NET Framework common language runtime (CLR). Database objects that can use the

rich programming model provided by the CLR include DML triggers, DDL triggers, stored

procedures, functions, aggregate functions, and types.

Creating a CLR trigger (DML or DDL) in SQL Server involves the following steps:

Define the trigger as a class in a .NET Framework-supported language. For more

information about how to program triggers in the CLR, see

CLR Triggers

. Then, compile

the class to build an assembly in the .NET Framework using the appropriate language

compiler.

Register the assembly in SQL Server using the

statement. For more

information about assemblies in SQL Server, see

Assemblies (Database Engine)

.

Create the trigger that references the registered assembly.

Executing CLR code is off by default in SQL Server. You can create, alter, and drop database

objects that reference managed code modules, but these references don't execute in SQL

Server, unless the

clr enabled

server configuration option is enabled by using

sp_configure

.

CREATE ASSEMBLY

ALTER ASSEMBLY

DROP ASSEMBLY

７

Note

Deploying a SQL Server Project in Visual Studio registers an assembly in the database that

was specified for the project. Deploying the project also creates CLR triggers in the

database for all methods annotated with the

attribute. For more information,

see

.

```sql
CREATE ASSEMBLY
SqlTrigger
```
