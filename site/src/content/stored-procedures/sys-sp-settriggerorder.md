---
name: "sys.sp_settriggerorder"
title: "sp_settriggerorder"
category: "general"
description: "triggers that are fired first or last. The triggers that are fired between the first and last triggers are executed in undefined order."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_settriggerorder
  [ @triggername = ]
  N
  'triggername'
  , [ @order = ]
  'order'
  , [ @stmttype = ]
  'stmttype'
  [ , [ @namespace = ]
  'DATABASE'
  |
  'SERVER'
  |
  NULL
  ]
  [ ; ]
---

## Description

triggers that are fired first or last. The triggers that are fired between the first and last triggers are executed in undefined order.

## Syntax

```sql
sp_settriggerorder
[ @triggername = ]
N
'triggername'
, [ @order = ]
'order'
, [ @stmttype = ]
'stmttype'
[ , [ @namespace = ]
'DATABASE'
|
'SERVER'
|
NULL
]
[ ; ]
```
