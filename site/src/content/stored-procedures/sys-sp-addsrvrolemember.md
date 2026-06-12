---
name: "sys.sp_addsrvrolemember"
title: "sp_addsrvrolemember"
category: "general"
description: "Adds a login, or security principal, as a member of a fixed server role."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addsrvrolemember
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

Adds a login, or security principal, as a member of a fixed server role.

## Syntax

```sql
sp_addsrvrolemember
[ @loginame = ]
N
'loginame'
[ , [ @rolename = ]
N
'rolename'
]
[ ; ]
```
