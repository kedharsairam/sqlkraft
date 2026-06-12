---
title: "Programming model restrictions"
topic: "clr-integration"
description: ""
tags: ["clr-integration","programming-model-restrictions"]
pubDate: 2025-12-01
---

When you build a managed stored procedure or other managed database object, SQL Server

performs certain code checks that need to be considered. These checks are performed on the

managed code assembly when first registered in the database, using the

statement, and also at runtime. The managed code is also checked at runtime because in an

assembly there might be code paths that might never actually be reached at runtime.

These code checks provide flexibility for registering third-party assemblies especially, so that an

assembly isn't blocked where there's

unsafe

code designed to run in a client environment, but

would never be executed in the hosted common language runtime (CLR). The requirements

that the managed code must meet depend on whether the assembly is registered as

,

, or.

is the strictest security level.

In addition to restrictions being placed on the managed code assemblies, there are also code

security permissions that are granted. The CLR supports a security model called code access

security (CAS) for managed code. In this model, permissions are granted to assemblies based

on the identity of the code.

,

, and

assemblies have different CAS

permissions. For more information, see

CLR integration code access security.

If the

publisher policy

is set,

fails.

CLR uses Code Access Security (CAS) in the.NET Framework, which is no longer supported as a

security boundary. A CLR assembly created with

might be able to

access external system resources, call unmanaged code, and acquire sysadmin privileges. In

2017 (14.x) and later versions, the

option,

clr strict security

, enhances

the security of CLR assemblies.

is enabled by default, and treats

and

assemblies as if they were marked. The

option

can be disabled for backward compatibility, but isn't recommended.

We recommend that you sign all assemblies by a certificate or asymmetric key, with a

corresponding login that has been granted

permission in the

database. SQL Server administrators can also add assemblies to a list of assemblies, which the

Database Engine should trust. For more information, see

sys.sp_add_trusted_assembly.

```sql
CREATE ASSEMBLY
SAFE
EXTERNAL_ACCESS
UNSAFE
SAFE
SAFE
EXTERNAL_ACCESS
UNSAFE
CREATE ASSEMBLY
PERMISSION_SET = SAFE sp_configure clr strict security
SAFE
EXTERNAL_ACCESS
UNSAFE clr strict security
UNSAFE ASSEMBLY master
```
