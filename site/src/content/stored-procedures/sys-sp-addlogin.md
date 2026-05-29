---
name: 'sys.sp_addlogin'
title: 'sp_addlogin'
category: 'general'
description: 'Creates a new SQL Server login that allows a user to connect to an instance of SQL Server by using SQL Server authentication. Transact-SQL syntax conventions This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. When possible, use Windows authentication.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addlogin
  [ @loginame = ]
  N
  'loginame'
  [ , [ @passwd = ]
  N
  'passwd'
  ]
  [ , [ @defdb = ]
  N
  'defdb'
  ]
  [ , [ @deflanguage = ]
  N
  'deflanguage'
  ]
  [ , [ @sid = ] sid ]
  [ , [ @encryptopt = ]
  'encryptopt'
  ]
  [ ; ]
---

## Description

Creates a new SQL Server login that allows a user to connect to an instance of SQL Server by using SQL Server authentication. Transact-SQL syntax conventions This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. When possible, use Windows authentication.

## Syntax

```sql
sp_addlogin
[ @loginame = ]
N
'loginame'
[ , [ @passwd = ]
N
'passwd'
]
[ , [ @defdb = ]
N
'defdb'
]
[ , [ @deflanguage = ]
N
'deflanguage'
]
[ , [ @sid = ] sid ]
[ , [ @encryptopt = ]
'encryptopt'
]
[ ; ]
```
