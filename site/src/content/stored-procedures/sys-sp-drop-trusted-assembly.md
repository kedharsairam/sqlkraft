---
name: "sys.sp_drop_trusted_assembly"
title: "sp_drop_trusted_assembly"
category: "general"
description: "2017 (14.x) and later Drops an assembly from the list of trusted assemblies on the server. The SHA2_512 hash value of the assembly to drop from the list of trusted assemblies for the server. Trusted assemblies might load when CLR strict security is enabled, even if the assembly is unsigned or the database isn't marked as trustworthy. This procedure remove"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_drop_trusted_assembly
  [ @hash = ]
  'value'
  [ ; ]
---

## Description

2017 (14.x) and later Drops an assembly from the list of trusted assemblies on the server. The SHA2_512 hash value of the assembly to drop from the list of trusted assemblies for the server. Trusted assemblies might load when CLR strict security is enabled, even if the assembly is unsigned or the database isn't marked as trustworthy.

## Syntax

```sql
sp_drop_trusted_assembly
[ @hash = ]
'value'
[ ; ]
```

## Permissions

SQL) 06/23/2025 x) and later Azure SQL Managed Instance Drops an assembly from the list of trusted assemblies on the server. syntaxsql The SHA2_512 hash value of the assembly to drop from the list of trusted assemblies for the server. Trusted assemblies might load when CLR strict security is enabled, even if the assembly is unsigned or the database isn't marked as trustworthy. This procedure removes an assembly from sys.trusted_assemblies. ） Important Arguments for extended stored procedures must be entered in the specific order as described in the section. If the parameters are entered out of order, an error message occurs.

## Examples

### Example 1

```sql
EXECUTE sp_drop_trusted_assembly
0x8893AD6D78D14EE43DF482E2EAD44123E3A0B684A8873C3F7BF3B5E8D8F09503F3E62370CE742BBC
96FE3394477214B84C7C1B0F7A04DCC788FA99C2C09DFCCC;
```
