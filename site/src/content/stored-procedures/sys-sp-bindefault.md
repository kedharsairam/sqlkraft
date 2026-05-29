---
name: 'sys.sp_bindefault'
title: 'sp_bindefault'
category: 'general'
description: 'SQL database in Microsoft Fabric Binds a default to a column or to an alias data type. Transact-SQL syntax conventions The name of the default created by The name of table and column, or the alias data type, to which the default is to be bound. is a one-part name, it resolves as an alias data type. If it''s a two- or three-part name, it first resolves as a table and column; and if this resolution f'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_bindefault
  [ @defname = ]
  N
  'defname'
  , [ @objname = ]
  N
  'objname'
  [ , [ @futureonly = ]
  'futureonly'
  ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Binds a default to a column or to an alias data type. Transact-SQL syntax conventions The name of the default created by The name of table and column, or the alias data type, to which the default is to be bound. is a one-part name, it resolves as an alias data type. If it's a two- or three-part name, it first resolves as a table and column; and if this resolution fails, it resolves as an alias

## Syntax

```sql
sp_bindefault
[ @defname = ]
N
'defname'
, [ @objname = ]
N
'objname'
[ , [ @futureonly = ]
'futureonly'
]
[ ; ]
```
