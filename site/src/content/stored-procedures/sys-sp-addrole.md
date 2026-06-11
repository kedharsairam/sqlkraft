---
name: "sys.sp_addrole"
title: "sp_addrole"
category: "general"
description: "Creates a new database role in the current database. Transact-SQL syntax conventions The name of the new database role. be a valid identifier and must not already exist in the current database. The owner of the new database role."
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

Creates a new database role in the current database. Transact-SQL syntax conventions The name of the new database role. be a valid identifier and must not already exist in the current database. The owner of the new database role. , with a default of the current must be a database user or database role in the current is included for compatibility with earlier versions of SQL Server and might not be supported in a future release. Use

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
