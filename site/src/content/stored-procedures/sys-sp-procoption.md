---
name: "sys.sp_procoption"
title: "sp_procoption"
category: "general"
description: "Sets or clears a stored procedure for automatic execution. A stored procedure that is set to automatic execution runs every time an instance of SQL Server is started."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_procoption
  [ @
  P
  roc
  N
  ame = ]
  N
  'ProcName'
  , [ @
  O
  ption
  N
  ame = ]
  'OptionName'
  , [ @
  O
  ption
  V
  alue = ]
  'OptionValue'
  [ ; ]
---

## Description

Sets or clears a stored procedure for automatic execution. A stored procedure that is set to automatic execution runs every time an instance of SQL Server is started.

## Syntax

```sql
sys.sp_procoption
[ @
P roc
N ame = ]
N
'ProcName'
, [ @
O ption
N ame = ]
'OptionName'
, [ @
O ption
V alue = ]
'OptionValue'
[ ; ]
```
