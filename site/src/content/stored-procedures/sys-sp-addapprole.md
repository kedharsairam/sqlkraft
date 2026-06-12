---
name: "sys.sp_addapprole"
title: "sp_addapprole"
category: "general"
description: "Adds an application role to the current database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addapprole
              [ @rolename = ]
              N
              'rolename'
              , [ @password = ]
              N
              'password'
              [ ; ]
---

## Description

Adds an application role to the current database.

## Syntax

```sql
sp_addapprole
[ @rolename = ]
N
'rolename'
, [ @password = ]
N
'password'
[ ; ]
```
