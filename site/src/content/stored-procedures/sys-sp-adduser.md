---
name: "sys.sp_adduser"
title: "sp_adduser"
category: "general"
description: "Adds a new user to the current database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_adduser
              [ @loginame = ]
              N
              'loginame'
              [ , [ @name_in_db = ]
              N
              'name_in_db'
              ]
              [ , [ @grpname = ]
              N
              'grpname'
              ]
              [ ; ]
---

## Description

Adds a new user to the current database.

## Syntax

```sql
sp_adduser
[ @loginame = ]
N
'loginame'
[ , [ @name_in_db = ]
N
'name_in_db'
]
[ , [ @grpname = ]
N
'grpname'
]
[ ; ]
```
