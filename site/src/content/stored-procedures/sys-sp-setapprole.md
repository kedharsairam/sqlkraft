---
name: "sys.sp_setapprole"
title: "sp_setapprole"
category: "general"
description: "Activates the permissions associated with an application role in the current database. Transact-SQL syntax conventions The name of the application role defined in the current database. must exist in the current database. The password required to activate the application role."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_setapprole
  [ @rolename = ]
  N
  'rolename'
  , [ @password = ]
  N
  'password'
  [ , [ @encrypt = ]
  'encrypt'
  ]
  [ , [ @f
  C
  reate
  C
  ookie = ] f
  C
  reate
  C
  ookie ]
  [ , [ @cookie = ] cookie
  OUTPUT
  ]
  [ ; ]
---

## Description

Activates the permissions associated with an application role in the current database. Transact-SQL syntax conventions The name of the application role defined in the current database. must exist in the current database. The password required to activate the application role. can be obfuscated by using the ODBC function, the password must be converted to a Unicode string by placing The encrypt option isn't supported on connections that use

## Syntax

```sql
sp_setapprole
[ @rolename = ]
N
'rolename'
, [ @password = ]
N
'password'
[ , [ @encrypt = ]
'encrypt'
]
[ , [ @f
C reate
C ookie = ] f
C reate
C ookie ]
[ , [ @cookie = ] cookie
OUTPUT
]
[ ; ]
```
