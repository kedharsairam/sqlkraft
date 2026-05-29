---
name: 'sys.sp_addapprole'
title: 'sp_addapprole'
category: 'general'
description: 'Adds an application role to the current database. Transact-SQL syntax conventions The name of the new application role. must be a valid identifier and can''t already exist in the current database. Application role names can contain from 1 up to 128 characters, including letters, symbols, and numbers. Role names can''t contain a backslash ( The password required to activate the application role. This'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addapprole
  [ @rolename = ]
  N
  'rolename'
  , [ @password = ]
  N
  'password'
  [ ; ]
---

## Description

Adds an application role to the current database. Transact-SQL syntax conventions The name of the new application role. must be a valid identifier and can't already exist in the current database. Application role names can contain from 1 up to 128 characters, including letters, symbols, and numbers. Role names can't contain a backslash ( The password required to activate the application role. This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
sp_addapprole
[ @rolename = ]
N
'rolename'
, [ @password = ]
N
'password'
[ ; ]
```
