---
name: 'sys.sp_dropsrvrolemember'
title: 'sp_dropsrvrolemember'
category: 'general'
description: 'Removes a SQL Server login, a Windows user, or Windows group, from a fixed server role. Transact-SQL syntax conventions The name of a login to remove from the fixed server role. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.'
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

Removes a SQL Server login, a Windows user, or Windows group, from a fixed server role. Transact-SQL syntax conventions The name of a login to remove from the fixed server role. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

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
