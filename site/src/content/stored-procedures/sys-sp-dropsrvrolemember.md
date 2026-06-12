---
name: "sys.sp_dropsrvrolemember"
title: "sp_dropsrvrolemember"
category: "general"
description: "Removes a SQL Server login, a Windows user, or Windows group, from a fixed server role."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropsrvrolemember
  [ @loginame = ]
  N
  'loginame'
  [ , [ @rolename = ]
  N
  'rolename'
  ]
  [ ; ]
---

## Description

Removes a SQL Server login, a Windows user, or Windows group, from a fixed server role.

## Syntax

```sql
sp_dropsrvrolemember
[ @loginame = ]
N
'loginame'
[ , [ @rolename = ]
N
'rolename'
]
[ ; ]
```
