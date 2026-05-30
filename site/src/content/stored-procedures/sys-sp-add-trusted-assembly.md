---
name: "sys.sp_add_trusted_assembly"
title: "sp_add_trusted_assembly"
category: "general"
description: "SQL Server 2017 (14.x) and later Adds an assembly to the list of trusted assemblies for the server. Transact-SQL syntax conventions This procedure adds an assembly to The SHA2_512 hash value of the assembly to add to the list of trusted assemblies for the server. Trusted assemblies might load when Server configuration: clr strict security even if the assembly is unsigned or the database isn't mark"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_trusted_assembly
  [ @hash = ]
  'value'
  [ , [ @description = ]
  'description'
  ]
  [ ; ]
---

## Description

SQL Server 2017 (14.x) and later Adds an assembly to the list of trusted assemblies for the server. Transact-SQL syntax conventions This procedure adds an assembly to The SHA2_512 hash value of the assembly to add to the list of trusted assemblies for the server. Trusted assemblies might load when Server configuration: clr strict security even if the assembly is unsigned or the database isn't marked as trustworthy.

## Syntax

```sql
sp_add_trusted_assembly
[ @hash = ]
'value'
[ , [ @description = ]
'description'
]
[ ; ]
```
