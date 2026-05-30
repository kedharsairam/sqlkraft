---
title: "Integration Code Access Security"
topic: "clr-integration"
description: |
  07/23/2025

  Applies to:

  SQL Server

  The common language runtime (CLR) supports a security model called code access security for

  managed code. In this model, permissions are granted to assemblies bas
tags:
  - "clr-integration"
  - "integration-code-access-security"
pubDate: 2025-12-01
---

07/23/2025

Applies to:

SQL Server

The common language runtime (CLR) supports a security model called code access security for

managed code. In this model, permissions are granted to assemblies based on the identity of

the code. For more information, see

Code Access Security

.

The security policy that determines the permissions granted to assemblies is defined in three

different places:

: This policy is in effect for all managed code running in the machine on

which SQL Server is installed.

: This policy is in effect for managed code hosted by a process. For SQL Server,

the user policy is specific to the Windows account on which the SQL Server service is

running.

: This policy is set up by the host of the CLR (in this case, SQL Server) that is in

effect for managed code running in that host.

The code access security mechanism supported by the CLR is based on the assumption that the

runtime can host both fully trusted and partially trusted code. The resources that are protected

by CLR code access security are typically wrapped by managed application programming

interfaces that require the corresponding permission before allowing access to the resource.

The demand for the permission is satisfied only if all the callers (at the assembly level) in the

call stack have the corresponding resource permission.

The set of code access security permissions that are granted to managed code when running

inside SQL Server is the intersection of the set of permissions granted by the previous three

policy levels. Even if SQL Server grants a set of permissions to an assembly loaded in SQL

Server, the eventual set of permissions given to user code might be further restricted by the

user and machine-level policies.

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

```sql
PERMISSION_SET = SAFE
sp_configure
clr strict security
SAFE
```
