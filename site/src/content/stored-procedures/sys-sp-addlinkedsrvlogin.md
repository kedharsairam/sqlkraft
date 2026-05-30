---
name: "sys.sp_addlinkedsrvlogin"
title: "sp_addlinkedsrvlogin"
category: "general"
description: "Creates or updates a mapping between a login on the local instance of SQL Server and a security account on a remote server. Transact-SQL syntax conventions The name of a linked server that the login mapping applies to. Determines whether to connect to by impersonating local logins or explicitly submitting a login and password. specifies that logins use their own credentials to connect to arguments"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addlinkedsrvlogin
  [ @rmtsrvname = ]
  N
  'rmtsrvname'
  [ , [ @useself = ]
  'useself'
  ]
  [ , [ @locallogin = ]
  N
  'locallogin'
  ]
  [ , [ @rmtuser = ]
  N
  'rmtuser'
  ]
  [ , [ @rmtpassword = ]
  N
  'rmtpassword'
  ]
  [ ; ]
---

## Description

Creates or updates a mapping between a login on the local instance of SQL Server and a security account on a remote server. Transact-SQL syntax conventions The name of a linked server that the login mapping applies to. Determines whether to connect to by impersonating local logins or explicitly submitting a login and password. specifies that logins use their own credentials to connect to arguments are used to connect to

## Syntax

```sql
sp_addlinkedsrvlogin
[ @rmtsrvname = ]
N
'rmtsrvname'
[ , [ @useself = ]
'useself'
]
[ , [ @locallogin = ]
N
'locallogin'
]
[ , [ @rmtuser = ]
N
'rmtuser'
]
[ , [ @rmtpassword = ]
N
'rmtpassword'
]
[ ; ]
```

## Examples

### Example 1

`sp_addlinkedserver`

### Example 2

`sp_addlinkedsrvlogin`

### Example 3

`true`

### Example 4

`sp_addlinkedsrvlogin`

### Example 5

`sp_droplinkedsrvlogin`

### Example 6

`sp_addlinkedsrvlogin`

### Example 7

`sp_addlinkedsrvlogin`

### Example 8

`sp_addlinkedsrvlogin`
