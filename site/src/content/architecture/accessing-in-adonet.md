---
title: "Accessing in ADO.NET"
topic: "clr-integration"
description: |
  Applies to:
  
  SQL Server
  
  User-defined types (UDTs) are written using any of the languages supported by the .NET
  
  Framework common language runtime (CLR) that produce verifiable code. This includes C# 
tags:
  - "clr-integration"
  - "accessing-in-adonet"
pubDate: 2025-12-01
---

Applies to:

SQL Server

User-defined types (UDTs) are written using any of the languages supported by the .NET

Framework common language runtime (CLR) that produce verifiable code. This includes C# and

Visual Basic .NET. UDTs allow objects and custom data structures to be stored in a SQL Server

database.

The data is exposed as public members of a .NET Framework class or structure, and behaviors

are defined by methods of the class or structure. A UDT can be used as the column definition

of a table, as a variable in a Transact-SQL batch, or as an argument of a Transact-SQL function

or stored procedure.

In ADO.NET, the

provider exposes UDTs in the following ways:

Through the

as an object.

Through the

as raw bytes.

As a parameter of a

object.

Description

Retrieve user-defined type (UDT) data in

ADO.NET

Describes how to retrieve UDT data and how to specify

parameters.

Update user-defined type (UDT) columns

with DataAdapters

Describes how to work with UDTs in a

and how to

update UDT data using a

.

CLR user-defined types

Last updated on 03/23/2026

ﾉ

Expand table

```sql
Microsoft.Data.SqlClient
Microsoft.Data.SqlClient.SqlDataReader
SqlDataReader
Microsoft.Data.SqlClient.SqlParameter
DataSet
DataAdapter
```