---
name: "sys.sp_tables_ex"
title: "sp_tables_ex"
category: "general"
description: "Returns table information about the tables from the specified linked server. Transact-SQL syntax conventions The name of the linked server for which to return table information. The name of the table for which to return data type information."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_tables_ex
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
  [ , [ @table_type = ]
  N
  'table_type'
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

Returns table information about the tables from the specified linked server. Transact-SQL syntax conventions The name of the linked server for which to return table information. The name of the table for which to return data type information.

## Syntax

```sql
sp_tables_ex
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
[ , [ @table_type = ]
N
'table_type'
]
[ , [ @f
U se
P attern = ] f
U se
P attern ]
[ ; ]
```
