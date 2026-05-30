---
name: "sys.sp_settriggerorder"
title: "sp_settriggerorder"
category: "general"
description: "SQL database in Microsoft Fabric triggers that are fired first or last. The triggers that are fired between the first and last triggers are executed in undefined order. Transact-SQL syntax conventions The name of the trigger and the schema to which it belongs, if applicable, whose order is to be , with no default, and is in the format . If the name doesn't correspond to a trigger or if the name tr"
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

SQL database in Microsoft Fabric triggers that are fired first or last. The triggers that are fired between the first and last triggers are executed in undefined order. Transact-SQL syntax conventions The name of the trigger and the schema to which it belongs, if applicable, whose order is to be , with no default, and is in the format . If the name doesn't correspond to a trigger or if the name trigger, the procedure returns an error. A schema can't be

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
