---
name: "sys.sp_procoption"
title: "sp_procoption"
category: "general"
description: "Sets or clears a stored procedure for automatic execution. A stored procedure that is set to automatic execution runs every time an instance of SQL Server is started. Transact-SQL syntax conventions The name of the procedure for which to set an option."
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

Sets or clears a stored procedure for automatic execution. A stored procedure that is set to automatic execution runs every time an instance of SQL Server is started. Transact-SQL syntax conventions The name of the procedure for which to set an option. The name of the option to set. , and the only value possible is Whether to set the option on (

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
