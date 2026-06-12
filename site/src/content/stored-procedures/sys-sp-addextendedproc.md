---
name: "sys.sp_addextendedproc"
title: "sp_addextendedproc"
category: "general"
description: "Registers the name of a new extended stored procedure to SQL Server."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
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

Registers the name of a new extended stored procedure to SQL Server.

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
