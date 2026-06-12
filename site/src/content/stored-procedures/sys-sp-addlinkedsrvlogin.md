---
name: "sys.sp_addlinkedsrvlogin"
title: "sp_addlinkedsrvlogin"
category: "general"
description: "Creates or updates a mapping between a login on the local instance of SQL Server and a security account on a remote server."
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

Creates or updates a mapping between a login on the local instance of SQL Server and a security account on a remote server.

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
