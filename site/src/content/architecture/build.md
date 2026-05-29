---
title: "Build"
topic: "clr-integration"
description: |
  Article
  
  •
  
  12/30/2024
  
  Applies to:
  
  SQL Server
  
  You can build database objects using the SQL Server integration with the .NET Framework
  
  common language runtime (CLR). Managed code that runs inside o
tags:
  - "clr-integration"
  - "build"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

You can build database objects using the SQL Server integration with the .NET Framework

common language runtime (CLR). Managed code that runs inside of SQL Server is called a

CLR

routine

. These routines include:

Scalar-valued user-defined functions (scalar UDFs)

Table-valued user-defined functions (TVFs)

User-defined procedures (UDPs)

User-defined triggers

CLR routines have the same structure in managed code. They're mapped to public, static

(shared in Visual Basic .NET) methods of a class. In addition to routines, user-defined types

(UDTs) and user-defined aggregate functions can also be defined using the .NET Framework.

UDTs and user-defined aggregates are mapped to entire .NET Framework classes.

Each type of .NET Framework routine has a Transact-SQL declaration and can be used

anywhere in SQL Server that the Transact-SQL equivalent can be used. For instance, scalar UDFs

can be used in any scalar expression. A TVF can be used in any

clause. A procedure can

be invoked in an

statement or invoked from a client application.

Execution of a CLR object (user-defined function, user-defined type, or trigger) on the common

language runtime can take place on multiple threads (parallel plan), if the query optimizer

decides it's beneficial. However, if a user-defined function accesses data, execution is on a

serial plan.

The following table lists the articles covered in this section.

Description

Get started with CLR

integration

Provides a brief overview of the libraries and namespaces required to

compile object using CLR integration with SQL Server. Includes an example

"Hello World" CLR stored procedure.

Supported .NET Framework

libraries

Provides information on the .NET Framework libraries supported by CLR

integration.

ﾉ

Expand table

```sql
FROM
EXEC
```