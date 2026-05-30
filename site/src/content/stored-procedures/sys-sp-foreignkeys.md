---
name: "sys.sp_foreignkeys"
title: "sp_foreignkeys"
category: "general"
description: "Returns the foreign keys that reference primary keys on the table in the linked server. Transact-SQL syntax conventions The name of the linked server for which to return table information. The name of the table with a primary key. The name of the schema with a primary key. . In SQL Server, this parameter contains the owner name."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_foreignkeys
  [ @table_server = ]
  N
  'table_server'
  [ , [ @pktab_name = ]
  N
  'pktab_name'
  ]
  [ , [ @pktab_schema = ]
  N
  'pktab_schema'
  ]
  [ , [ @pktab_catalog = ]
  N
  'pktab_catalog'
  ]
  [ , [ @fktab_name = ]
  N
  'fktab_name'
  ]
  [ , [ @fktab_schema = ]
  N
  'fktab_schema'
  ]
  [ , [ @fktab_catalog = ]
  N
  'fktab_catalog'
  ]
  [ ; ]
---

## Description

Returns the foreign keys that reference primary keys on the table in the linked server. Transact-SQL syntax conventions The name of the linked server for which to return table information. The name of the table with a primary key. The name of the schema with a primary key. . In SQL Server, this parameter contains the owner name.

## Syntax

```sql
sp_foreignkeys
[ @table_server = ]
N
'table_server'
[ , [ @pktab_name = ]
N
'pktab_name'
]
[ , [ @pktab_schema = ]
N
'pktab_schema'
]
[ , [ @pktab_catalog = ]
N
'pktab_catalog'
]
[ , [ @fktab_name = ]
N
'fktab_name'
]
[ , [ @fktab_schema = ]
N
'fktab_schema'
]
[ , [ @fktab_catalog = ]
N
'fktab_catalog'
]
[ ; ]
```
