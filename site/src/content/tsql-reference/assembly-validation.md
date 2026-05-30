---
name: "Assembly Validation"
title: "Assembly Validation"
category: "statements"
description: "If any dependent assemblies referenced by the root assembly aren't already in the database"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

If any dependent assemblies referenced by the root assembly aren't already in the database

and are implicitly loaded together with the root assembly, they have the same permission set

as the root level assembly. If the dependent assemblies must be created by using a different

permission set than the root-level assembly, they must be uploaded explicitly before the root

level assembly with the appropriate permission set.

SQL Server scans the assembly binaries uploaded by the

statement to

guarantee the following checks:

The assembly binary is well formed with valid metadata and code segments, and the code

segments have valid Microsoft Intermediate language (MSIL) instructions.

The set of system assemblies it references is one of the following supported assemblies in

SQL Server:

,

,

,

,

,

,

,

,

,

,

, and

. Other system assemblies can be referenced, but they must be

explicitly registered in the database.

For assemblies created by using

or

permission sets:

The assembly code should be type-safe. Type safety is established by running the

common language runtime verifier against the assembly.

The assembly shouldn't contain any static data members in its classes unless they're

marked as read-only.

The classes in the assembly can't contain finalizer methods.

The classes or methods of the assembly should be annotated only with allowed code

attributes. For more information, see

CLR integration: custom attributes for CLR

routines

.

Besides the previous checks that are performed when

executes, there are

extra checks that are performed at execution time of the code in the assembly:

Calling certain .NET Framework APIs that require a specific Code Access Permission might

fail if the permission set of the assembly doesn't include that permission.

For

and

assemblies, any attempt to call .NET Framework APIs that

are annotated with certain HostProtectionAttributes fails.

### sysadmin

```sql
CREATE ASSEMBLY
```

`Microsoft.VisualBasic.dll`

`mscorlib.dll`

`System.Data.dll`

`System.dll`

`System.Xml.dll`

`Microsoft.VisualC.dll`

`CustomMarshallers.dll`

`System.Security.dll`

`System.Web.Services.dll`

`System.Data.SqlXml.dll`

`System.Core.dll`

`System.Xml.Linq.dll`

`SAFE`

```sql
EXTERNAL ACCESS
```

```sql
CREATE ASSEMBLY
```

`SAFE`

`EXTERNAL_ACCESS`
