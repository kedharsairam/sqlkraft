---
name: "sys.sp_defaultdb"
title: "sp_defaultdb"
category: "general"
description: "Changes the default database for a SQL Server login. Server login or a Windows user or group. If a login for the Windows user or group doesn't exist in SQL Server, it's automatically added."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
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

Changes the default database for a SQL Server login. Server login or a Windows user or group. If a login for the Windows user or group doesn't exist in SQL Server, it's automatically added.

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
