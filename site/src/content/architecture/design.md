---
title: "Design"
topic: "clr-integration"
description: |
  07/23/2025

  Applies to:

  SQL Server

  This article describes the following factors you should consider when you design assemblies:

  Packaging assemblies

  Managing assembly security

  Restrictions on ass
tags:
  - "clr-integration"
  - "design"
pubDate: 2025-12-01
---

07/23/2025

Applies to:

SQL Server

This article describes the following factors you should consider when you design assemblies:

Packaging assemblies

Managing assembly security

Restrictions on assemblies

An assembly can contain functionality for more than one SQL Server routine or type in its

classes and methods. Most of the time, it makes sense to package the functionality of routines

that perform related functions within the same assembly, especially if these routines share

classes whose methods call one another. For example, classes that perform data entry

management tasks for common language runtime (CLR) triggers and CLR stored procedures

can be packaged in the same assembly. This is because the methods for these classes are more

likely to call each other than methods of less related tasks.

When you're packaging code into assembly, consider:

CLR user-defined types and indexes that depend on CLR user-defined functions can cause

persisted data to be in the database that depends on the assembly. Modifying the code

of an assembly is frequently more complex when there's persisted data that depends on

the assembly in the database. Therefore, it's better to separate code on which persisted

data dependencies rely (such as user-defined types and indexes using user-defined

functions) from code that doesn't have these persisted data dependencies. For more

information, see

Implement assemblies

and

ALTER ASSEMBLY

.

If a piece of managed code requires higher permission, it's better to separate that code

into a separate assembly from code that doesn't require higher permission.

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
PERMISSION_SET = SAFE sp_configure clr strict security
SAFE
```
