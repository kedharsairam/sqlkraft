---
name: "sys.sp_table_privileges_ex"
title: "sp_table_privileges_ex"
category: "general"
description: "Returns privilege information about the specified table from the specified linked server. Transact-SQL syntax conventions The name of the linked server for which to return information. The name of the table for which to provide table privilege information. The table schema. This in some DBMS environments is the table owner."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_table_privileges_ex
  [ @table_server = ]
  N
  'table_server'
  [ , [ @table_name = ]
  N
  'table_name'
  ]
  [ , [ @table_schema = ]
  N
  'table_schema'
  ]
  [ , [ @table_catalog = ]
  N
  'table_catalog'
  ]
  [ , [ @f
  U
  se
  P
  attern = ] f
  U
  se
  P
  attern ]
  [ ; ]
---

## Description

Returns privilege information about the specified table from the specified linked server. Transact-SQL syntax conventions The name of the linked server for which to return information. The name of the table for which to provide table privilege information. The table schema. This in some DBMS environments is the table owner.

## Syntax

```sql
sp_table_privileges_ex
[ @table_server = ]
N
'table_server'
[ , [ @table_name = ]
N
'table_name'
]
[ , [ @table_schema = ]
N
'table_schema'
]
[ , [ @table_catalog = ]
N
'table_catalog'
]
[ , [ @f
U se
P attern = ] f
U se
P attern ]
[ ; ]
```
