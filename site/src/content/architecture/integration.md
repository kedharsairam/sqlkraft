---
title: "Integration"
topic: "clr-integration"
description: |
  Article
  
  •
  
  12/30/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  The common language runtime (CLR) is the heart of the .NET Framework and provides the
  
  execution environment for all .NET F
tags:
  - "clr-integration"
  - "integration"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

Azure SQL Managed Instance

The common language runtime (CLR) is the heart of the .NET Framework and provides the

execution environment for all .NET Framework code. Code that runs within the CLR is referred

to as

managed code

. The CLR provides various functions and services required for program

execution, including just-in-time (JIT) compilation, allocating and managing memory, enforcing

type safety, exception handling, thread management, and security. For more information, see

.NET Framework development guide

.

With the CLR hosted in SQL Server (called CLR integration), you can author stored procedures,

triggers, user-defined functions, user-defined types, and user-defined aggregates in managed

code. Because managed code compiles to native code before execution, you can achieve

significant performance increases in some scenarios.

In SQL Server 2016 (13.x) and earlier versions, Code Access Security (CAS) prevented

assemblies from performing certain operations.

CLR uses Code Access Security (CAS) in the .NET Framework, which is no longer supported as a

security boundary. A CLR assembly created with

might be able to

access external system resources, call unmanaged code, and acquire sysadmin privileges. In

SQL Server 2017 (14.x) and later versions, the

option,

clr strict security

, enhances

the security of CLR assemblies.

is enabled by default, and treats

and

assemblies as if they were marked

. The

option

can be disabled for backward compatibility, but isn't recommended.

We recommend that you sign all assemblies by a certificate or asymmetric key, with a

corresponding login that has been granted

permission in the

database. SQL Server administrators can also add assemblies to a list of assemblies, which the

Database Engine should trust. For more information, see

sys.sp_add_trusted_assembly

.

７

Note

For more information about using the new .NET with SQL Server Language Extensions, see

.

```sql
PERMISSION_SET = SAFE
sp_configure
clr strict security
SAFE
EXTERNAL_ACCESS
UNSAFE
clr strict security
UNSAFE ASSEMBLY
master
```