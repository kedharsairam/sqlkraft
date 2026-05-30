---
title: "Alter"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  Assemblies that are registered in SQL Server can be updated from a more recent version using

  the

  statement. To update an assembly, use the

  statement
tags:
  - "clr-integration"
  - "alter"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

Assemblies that are registered in SQL Server can be updated from a more recent version using

the

statement. To update an assembly, use the

statement with

the following syntax:

doesn't disrupt currently running processes that are using the assembly; the

processes continue executing with the unaltered assembly.

can't be used to

change the signatures of common language runtime (CLR) functions, aggregate functions,

stored procedures, and triggers. You can add new public methods to the assembly, private

methods can be modified in any way, and public methods can be modified as long as

signatures or attributes aren't changed. Fields that are contained within a native-serialized

user-defined type, including data members or base classes, can't be changed by using

. All other changes are unsupported. For more information, see

ALTER ASSEMBLY

.

The permission set of an assembly can also be changed using the

statement.

The following statement changes the permission set of the

assembly to

.

If the permission set of an assembly is being changed from

to

or

, an asymmetric key and corresponding login with

permission

or

permission for the assembly must first be created. For more information,

see

Create an assembly

.

```sql
ALTER ASSEMBLY
ALTER ASSEMBLY
ALTER ASSEMBLY
ALTER ASSEMBLY
ALTER
ASSEMBLY
ALTER ASSEMBLY
SQLCLRTest
EXTERNAL_ACCESS
SAFE
EXTERNAL_ACCESS
UNSAFE
EXTERNAL ACCESS ASSEMBLY
UNSAFE ASSEMBLY
ALTER
ASSEMBLY
SQLCLRTest
FROM
'C:\MyDBApp\SQLCLRTest.dll'
;
ALTER
ASSEMBLY
SQLCLRTest
WITH
PERMISSION_SET = EXTERNAL_ACCESS;
```
