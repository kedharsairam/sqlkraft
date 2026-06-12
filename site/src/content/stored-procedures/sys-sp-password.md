---
name: "sys.sp_password"
title: "sp_password"
category: "general"
description: "Adds or changes a password for a SQL Server login. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_password
              [ [ @old = ]
              N
              'old'
              ]
              , [ @new = ]
              N
              'new'
              [ , [ @loginame = ]
              N
              'loginame'
              ]
              [ ; ]
---

## Description

Adds or changes a password for a SQL Server login. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_password
[ [ @old = ]
N
'old'
]
, [ @new = ]
N
'new'
[ , [ @loginame = ]
N
'loginame'
]
[ ; ]
```
