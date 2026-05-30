---
title: "Supported .NET Framework Libraries"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  With the common language runtime (CLR) hosted in SQL Server, you can author stored

  procedures, triggers, user-defined functions, user-defined types, a
tags:
  - "clr-integration"
  - "supported-net-framework-libraries"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

With the common language runtime (CLR) hosted in SQL Server, you can author stored

procedures, triggers, user-defined functions, user-defined types, and user-defined aggregates

in managed code. With the functionality found in the .NET Framework class libraries, you have

access to prebuilt classes that provide functionality for string manipulation, advanced math

operations, file access, cryptography, and more. These classes can be accessed from any

managed stored procedure, user-defined type, trigger, user-defined function, or user-defined

aggregate.

If you service or upgrade unsupported assemblies in the global assembly cache (GAC), your

SQL Server application can stop working. This is because servicing or upgrading libraries in the

GAC doesn't update those assemblies inside SQL Server. If an assembly exists both in a SQL

Server database and in the GAC, the two copies of the assembly must exactly match. If they

don't match, an error occurs when the assembly is used by SQL Server CLR integration. If you

service or upgrade any assemblies in the GAC that are also registered in the database,

including unsupported .NET Framework assemblies, make sure to also service or upgrade the

copy of the assembly inside your SQL Server databases with the

statement. For

more information, see

MSSQLSERVER_6522

.

SQL Server has a list of supported .NET Framework libraries that are tested to ensure that they

meet reliability and security standards for interaction with SQL Server. Supported libraries don't

need to be explicitly registered on the server before they can be used in your code; SQL Server

loads them directly from the Global Assembly Cache (GAC).

The libraries/namespaces supported by CLR integration in SQL Server are:

```sql
ALTER ASSEMBLY mscorlib.dll
CustomMarshalers.dll
Microsoft.VisualBasic.dll
Microsoft.VisualC.dll
System.Configuration.dll
System.Core.dll
System.Data.OracleClient.dll
System.Data.SqlXml.dll
System.Data.dll
```
