---
name: "sys.sp_tableoption"
title: "sp_tableoption"
category: "general"
description: "Sets option values for user-defined tables."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_tableoption
      [ @
      T
      able
      N
      ame
      P
      attern = ]
      N
      'TableNamePattern'
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

Sets option values for user-defined tables.

## Syntax

```sql
sp_tableoption
[ @
T able
N ame
P attern = ]
N
'TableNamePattern'
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
