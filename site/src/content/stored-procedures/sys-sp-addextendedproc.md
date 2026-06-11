---
name: "sys.sp_addextendedproc"
title: "sp_addextendedproc"
category: "general"
description: "Registers the name of a new extended stored procedure to SQL Server. Transact-SQL syntax conventions The name of the function to call within the dynamic-link library (DLL). optionally can include the owner name in the form The name of the DLL that contains the function. should specify the complete path of the DLL. This feature will be removed in a future version of SQL Server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addextendedproc
  [ @functname = ]
  N
  'functname'
  , [ @dllname = ]
  'dllname'
  [ ; ]
---

## Description

Registers the name of a new extended stored procedure to SQL Server. Transact-SQL syntax conventions The name of the function to call within the dynamic-link library (DLL). optionally can include the owner name in the form The name of the DLL that contains the function. should specify the complete path of the DLL. This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
sp_addextendedproc
[ @functname = ]
N
'functname'
, [ @dllname = ]
'dllname'
[ ; ]
```
