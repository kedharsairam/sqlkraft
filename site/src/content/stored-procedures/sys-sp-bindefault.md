---
name: "sys.sp_bindefault"
title: "sp_bindefault"
category: "general"
description: "Binds a default to a column or to an alias data type."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_bindefault
      [ @defname = ]
      N
      'defname'
      , [ @objname = ]
      N
      'objname'
      [ , [ @futureonly = ]
      'futureonly'
      ]
      [ ; ]
---

## Description

Binds a default to a column or to an alias data type.

## Syntax

```sql
sp_bindefault
[ @defname = ]
N
'defname'
, [ @objname = ]
N
'objname'
[ , [ @futureonly = ]
'futureonly'
]
[ ; ]
```
