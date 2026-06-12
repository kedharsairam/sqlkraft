---
title: "User-defined types"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  SQL Server gives you the ability to create database objects that are programmed against an

  assembly created in the .NET Framework common language runt
tags:
  - "clr-integration"
  - "user-defined-types"
pubDate: 2025-12-01
---

Article

•

12/30/2024

SQL Server

gives you the ability to create database objects that are programmed against an

assembly created in the.NET Framework common language runtime (CLR). Database objects

that can take advantage of the rich programming model provided by the CLR include triggers,

stored procedures, functions, aggregate functions, and types.

You can use user-defined types (UDTs) to extend the scalar type system of the server, enabling

storage of CLR objects in a SQL Server database. UDTs can contain multiple elements and can

have behaviors, differentiating them from the traditional alias data types which consist of a

single SQL Server system data type.

Because UDTs are accessed by the system as a whole, their use for complex data types might

negatively affect performance. Complex data is generally best modeled using traditional rows

and tables. UDTs in SQL Server are well suited to the following type of data:

Date, time, currency, and extended numeric types

Geospatial applications

Encoded or encrypted data

The process of developing UDTs in SQL Server consists of the following steps:

1.

UDTs are defined using any of the

languages supported by the.NET Framework common language runtime (CLR) that

produce verifiable code. This includes C# and Visual Basic.NET. The data is exposed as

fields and properties of a.NET Framework class or structure, and behaviors are defined by

methods of the class or structure.

2.

UDTs can be deployed through the Visual Studio user interface in

a database project, or by using the Transact-SQL

statement, which

copies the assembly containing the class or structure into a database.

3.

Once an assembly is loaded into a host database, you use

the Transact-SQL CREATE TYPE statement to create a UDT and expose the members of the

class or structure as members of the UDT. UDTs exist only in the context of a single

７

Note

The ability to execute CLR code is set to OFF by default in SQL Server. The CLR can be

enabled by using the

system stored procedure.

```sql
CREATE ASSEMBLY sp_configure
```
