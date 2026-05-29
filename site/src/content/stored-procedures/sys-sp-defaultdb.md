---
name: 'sys.sp_defaultdb'
title: 'sp_defaultdb'
category: 'general'
description: 'Changes the default database for a SQL Server login. Transact-SQL syntax conventions Server login or a Windows user or group. If a login for the Windows user or group doesn''t exist in SQL Server, it''s automatically added. The name of the new default database. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applica'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_defaultdb
  [ @loginame = ]
  N
  'loginame'
  , [ @defdb = ]
  N
  'defdb'
  [ ; ]
---

## Description

Changes the default database for a SQL Server login. Transact-SQL syntax conventions Server login or a Windows user or group. If a login for the Windows user or group doesn't exist in SQL Server, it's automatically added. The name of the new default database. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_defaultdb
[ @loginame = ]
N
'loginame'
, [ @defdb = ]
N
'defdb'
[ ; ]
```
