---
title: "Collation & data types"
topic: "clr-integration"
description: |
  Article
  
  •
  
  12/30/2024
  
  Applies to:
  
  SQL Server
  
  In the .NET Framework, the
  
  object handles collations. The .NET Framework string
  
  application programming interfaces (APIs) use the
  
  property associate
tags:
  - "clr-integration"
  - "collation-data-types"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

In the .NET Framework, the

object handles collations. The .NET Framework string

application programming interfaces (APIs) use the

property associated with the

object of the current thread to perform string comparisons. The default setting of

the

object is based on the Windows locale setting for the computer on which SQL

Server is running. This determines the default comparison semantics, if no explicit

is specified, for comparisons of

values. SQL Server doesn't explicitly change the

property to the database or server collation. If necessary, you must set the

appropriate

property in your routines.

When you create a common language runtime (CLR) routine, and a parameter of a CLR method

bound to the routine is of type

, SQL Server creates an instance of the parameter

with the default collation of the database containing the calling routine. If a parameter isn't a

(for example,

rather than

), the collation information from the

database isn't associated with the parameter.

SQL Server data types in the .NET Framework

```sql
CompareInfo
CompareInfo
CultureInfo
CultureInfo
CultureInfo
System.String
CompareInfo
CompareInfo
SQLString
SqlType
String
SQLString
```