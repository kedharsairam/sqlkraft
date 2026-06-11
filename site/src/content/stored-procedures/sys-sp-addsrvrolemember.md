---
name: "sys.sp_addsrvrolemember"
title: "sp_addsrvrolemember"
category: "general"
description: "Adds a login, or security principal, as a member of a fixed server role. Transact-SQL syntax conventions The name of the security principal being added to the fixed server role."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addsrvrolemember
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

Adds a login, or security principal, as a member of a fixed server role. Transact-SQL syntax conventions The name of the security principal being added to the fixed server role. can be a SQL Server login or a Windows account. If the Windows account isn't already granted access to SQL Server, access is automatically granted. The name of the fixed server role to which the security principal is being added.

## Syntax

```sql
sp_addsrvrolemember
[ @loginame = ]
N
'loginame'
[ , [ @rolename = ]
N
'rolename'
]
[ ; ]
```
