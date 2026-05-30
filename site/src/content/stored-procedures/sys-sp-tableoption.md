---
name: "sys.sp_tableoption"
title: "sp_tableoption"
category: "general"
description: "SQL database in Microsoft Fabric Sets option values for user-defined tables. can be used to control the in-row or large user-defined type columns. Transact-SQL syntax conventions The qualified or nonqualified name of a user-defined database table. , with no default. If a fully qualified table name, including a database name, is provided, the database name must be the name of the current database. "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_tableoption
  [ @
  T
  able
  N
  ame
  P
  attern = ]
  N
  'TableNamePattern'
  , [ @
  O
  ption
  N
  ame = ]
  'OptionName'
  , [ @
  O
  ption
  V
  alue = ]
  'OptionValue'
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Sets option values for user-defined tables. can be used to control the in-row or large user-defined type columns. Transact-SQL syntax conventions The qualified or nonqualified name of a user-defined database table. , with no default. If a fully qualified table name, including a database name, is provided, the database name must be the name of the current database. Table options for

## Syntax

```sql
sp_tableoption
[ @
T
able
N
ame
P
attern = ]
N
'TableNamePattern'
, [ @
O
ption
N
ame = ]
'OptionName'
, [ @
O
ption
V
alue = ]
'OptionValue'
[ ; ]
```
