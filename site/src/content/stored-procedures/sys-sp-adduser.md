---
name: "sys.sp_adduser"
title: "sp_adduser"
category: "general"
description: "Adds a new user to the current database. Transact-SQL syntax conventions The name of the SQL Server login or Windows account. must be an existing SQL Server login or Windows account. The name for the new database user. isn't specified, the name of the new database user defaults to gives the new user a name in the database different from the server- This feature will be removed in a future version"
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

Adds a new user to the current database. Transact-SQL syntax conventions The name of the SQL Server login or Windows account. must be an existing SQL Server login or Windows account. The name for the new database user. isn't specified, the name of the new database user defaults to gives the new user a name in the database different from the server- This feature will be removed in a future version of SQL Server. Avoid using this feature in

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
