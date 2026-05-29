---
name: 'sys.sp_releaseapplock'
title: 'sp_releaseapplock'
category: 'general'
description: 'SQL database in Microsoft Fabric Releases a lock on an application resource. Transact-SQL syntax conventions A lock resource name specified by the client application. is binary-compared, thus is case-sensitive regardless of the collation settings of the current database. The application must ensure that the resource is unique. The specified name is hashed internally into a value that can be stored'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_releaseapplock
  [ [ @
  R
  esource = ]
  N
  'Resource'
  ]
  [ , [ @
  L
  ock
  O
  wner = ]
  'LockOwner'
  ]
  [ , [ @
  D
  b
  P
  rincipal = ]
  N
  'DbPrincipal'
  ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Releases a lock on an application resource. Transact-SQL syntax conventions A lock resource name specified by the client application. is binary-compared, thus is case-sensitive regardless of the collation settings of the current database. The application must ensure that the resource is unique. The specified name is hashed internally into a value that can be stored in the SQL Server lock manager.

## Syntax

```sql
sp_releaseapplock
[ [ @
R
esource = ]
N
'Resource'
]
[ , [ @
L
ock
O
wner = ]
'LockOwner'
]
[ , [ @
D
b
P
rincipal = ]
N
'DbPrincipal'
]
[ ; ]
```
