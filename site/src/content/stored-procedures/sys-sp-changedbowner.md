---
name: "sys.sp_changedbowner"
title: "sp_changedbowner"
category: "general"
description: "Changes the owner of the current database. Transact-SQL syntax conventions The login ID of the new owner of the current database. must be an already existing SQL Server login or Windows user. become the owner of the current database if it already has access to the database through an existing user security account within the database. To avoid this scenario, drop the user within This parameter is "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changedbowner
  [ @loginame = ]
  N
  'loginame'
  [ , [ @map = ]
  'map'
  ]
  [ ; ]
---

## Description

Changes the owner of the current database. Transact-SQL syntax conventions The login ID of the new owner of the current database. must be an already existing SQL Server login or Windows user. become the owner of the current database if it already has access to the database through an existing user security account within the database. To avoid this scenario, drop the user within This parameter is deprecated and is maintained for backward compatibility of scripts.

## Syntax

```sql
sp_changedbowner
[ @loginame = ]
N
'loginame'
[ , [ @map = ]
'map'
]
[ ; ]
```
