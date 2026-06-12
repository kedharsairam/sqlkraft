---
name: "sys.sp_stored_procedures"
title: "sp_stored_procedures"
category: "general"
description: "Returns a list of stored procedures in the current environment."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_stored_procedures
  [ [ @sp_name = ]
  N
  'sp_name'
  ]
  [ , [ @sp_owner = ]
  N
  'sp_owner'
  ]
  [ , [ @sp_qualifier = ]
  N
  'sp_qualifier'
  ]
  [ , [ @f
  U
  se
  P
  attern = ] f
  U
  se
  P
  attern ]
  [ ; ]
---

## Description

Returns a list of stored procedures in the current environment.

## Syntax

```sql
sp_stored_procedures
[ [ @sp_name = ]
N
'sp_name'
]
[ , [ @sp_owner = ]
N
'sp_owner'
]
[ , [ @sp_qualifier = ]
N
'sp_qualifier'
]
[ , [ @f
U se
P attern = ] f
U se
P attern ]
[ ; ]
```
