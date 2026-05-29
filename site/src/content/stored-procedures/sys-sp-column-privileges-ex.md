---
name: 'sys.sp_column_privileges_ex'
title: 'sp_column_privileges_ex'
category: 'general'
description: 'Returns column privileges for the specified table on the specified linked server. Transact-SQL syntax conventions The name of the linked server for which to return information. The name of the table that contains the specified column.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_column_privileges_ex
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
  [ , [ @column_name = ]
  N
  'column_name'
  ]
  [ ; ]
---

## Description

Returns column privileges for the specified table on the specified linked server. Transact-SQL syntax conventions The name of the linked server for which to return information. The name of the table that contains the specified column.

## Syntax

```sql
sp_column_privileges_ex
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
[ , [ @column_name = ]
N
'column_name'
]
[ ; ]
```
