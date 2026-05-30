---
name: "sys.sp_approlepassword"
title: "sp_approlepassword"
category: "general"
description: "Changes the password of an application role in the current database. Transact-SQL syntax conventions The name of the application role. exist in the current database. The new password for the application role. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_approlepassword
  [ @rolename = ]
  N
  'rolename'
  , [ @newpwd = ]
  N
  'newpwd'
  [ ; ]
---

## Description

Changes the password of an application role in the current database. Transact-SQL syntax conventions The name of the application role. exist in the current database. The new password for the application role. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_approlepassword
[ @rolename = ]
N
'rolename'
, [ @newpwd = ]
N
'newpwd'
[ ; ]
```
