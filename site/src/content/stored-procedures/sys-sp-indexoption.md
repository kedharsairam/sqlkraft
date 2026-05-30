---
name: "sys.sp_indexoption"
title: "sp_indexoption"
category: "general"
description: "Sets locking option values for user-defined clustered and nonclustered indexes or tables with The SQL Server Database Engine automatically makes choices of page-, row-, or table-level locking. You don't have to set these options manually. users who know with certainty that a particular type of lock is always appropriate. Transact-SQL syntax conventions The qualified or nonqualified name of a user-"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_indexoption
  [ @
  I
  ndex
  N
  ame
  P
  attern = ]
  N
  'IndexNamePattern'
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

Sets locking option values for user-defined clustered and nonclustered indexes or tables with The SQL Server Database Engine automatically makes choices of page-, row-, or table-level locking. You don't have to set these options manually. users who know with certainty that a particular type of lock is always appropriate. Transact-SQL syntax conventions The qualified or nonqualified name of a user-defined table or index.

## Syntax

```sql
sp_indexoption
[ @
I
ndex
N
ame
P
attern = ]
N
'IndexNamePattern'
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
