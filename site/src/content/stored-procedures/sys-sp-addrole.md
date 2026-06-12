---
name: "sys.sp_addrole"
title: "sp_addrole"
category: "general"
description: "Creates a new database role in the current database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addrole
              [ @rolename = ]
              N
              'rolename'
              [ , [ @ownername = ]
              N
              'ownername'
              ]
              [ ; ]
---

## Description

Creates a new database role in the current database.

## Syntax

```sql
sp_addrole
[ @rolename = ]
N
'rolename'
[ , [ @ownername = ]
N
'ownername'
]
[ ; ]
```
