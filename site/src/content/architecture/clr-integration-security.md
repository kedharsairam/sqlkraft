---
title: "CLR Integration Security"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  The security model of the SQL Server integration with the .NET Framework common language

  runtime (CLR) manages and secures access between different ty
tags:
  - "clr-integration"
  - "clr-integration-security"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

The security model of the SQL Server integration with the .NET Framework common language

runtime (CLR) manages and secures access between different types of CLR and non-CLR

objects running within SQL Server. These objects can be called from a Transact-SQL statement,

or another CLR object running in the server. The calls between objects are referred to as links.

The types of security checks performed on these objects depend on the types of links involved.

The CLR integration security model has the following goals:

By default, running managed user code on SQL Server shouldn't compromise the integrity

and stability of SQL Server. Performing operations that potentially compromise the

robustness of SQL Server should be protected by appropriate high-level permissions.

Managed user code shouldn't gain unauthorized access to user data or other user code in

the database. User-defined code should run under the security context of the user-

session that invoked it, and with the correct privileges for that security context.

There should be controls for restricting user code from accessing any resources outside

the server, using it strictly for local data access and computation.

User-defined code shouldn't be able to gain unauthorized access to system resources by

virtue of running in the SQL Server process.

SQL Server now integrates the user-based security model of SQL Server with the code access-

based security model of the CLR. Some of the advantages of this combined approach to

security are discussed in this section.

The following table lists the articles in this section.

Description

CLR integration Code Access

Security

Discusses the code access security (CAS) model for managed code

Host protection attributes and CLR

integration programming

Provides information about the host protection attribute (HPA)

values that are disallowed in

and

assemblies

ﾉ

Expand table

```sql
SAFE
EXTERNAL_ACCESS
```
