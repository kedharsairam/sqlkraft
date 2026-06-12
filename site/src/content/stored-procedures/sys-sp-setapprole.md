---
name: "sys.sp_setapprole"
title: "sp_setapprole"
category: "general"
description: "Activates the permissions associated with an application role in the current database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_setapprole
      [ @rolename = ]
      N
      'rolename'
      , [ @password = ]
      N
      'password'
      [ , [ @encrypt = ]
      'encrypt'
      ]
      [ , [ @f
      C
      reate
      C
      ookie = ] f
      C
      reate
      C
      ookie ]
      [ , [ @cookie = ] cookie
      OUTPUT
      ]
      [ ; ]
---

## Description

Activates the permissions associated with an application role in the current database.

## Syntax

```sql
sp_setapprole
[ @rolename = ]
N
'rolename'
, [ @password = ]
N
'password'
[ , [ @encrypt = ]
'encrypt'
]
[ , [ @f
C reate
C ookie = ] f
C reate
C ookie ]
[ , [ @cookie = ] cookie
OUTPUT
]
[ ; ]
```
