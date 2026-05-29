---
name: 'sys.sp_grantdbaccess'
title: 'sp_grantdbaccess'
category: 'general'
description: 'Adds a database user to the current database. Transact-SQL syntax conventions The name of the Windows group, Windows login, or SQL Server login, to be mapped to the , with no default. Names of Windows groups and Windows logins must be qualified with a Windows domain name in the form . The login can''t already be mapped to a user in the The name for the new database user. is an OUTPUT parameter of t'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_grantdbaccess
  [ @loginame = ]
  N
  'loginame'
  [ , [ @name_in_db = ]
  N
  'name_in_db'
  OUTPUT
  ]
  [ ; ]
---

## Description

Adds a database user to the current database. Transact-SQL syntax conventions The name of the Windows group, Windows login, or SQL Server login, to be mapped to the , with no default. Names of Windows groups and Windows logins must be qualified with a Windows domain name in the form . The login can't already be mapped to a user in the The name for the new database user. is an OUTPUT parameter of type

## Syntax

```sql
sp_grantdbaccess
[ @loginame = ]
N
'loginame'
[ , [ @name_in_db = ]
N
'name_in_db'
OUTPUT
]
[ ; ]
```
