---
name: "sys.sp_primarykeys"
title: "sp_primarykeys"
category: "general"
description: "Returns the primary key columns, one row per key column, for the specified remote table."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_primarykeys
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
      [ ; ]
---

## Description

Returns the primary key columns, one row per key column, for the specified remote table.

## Syntax

```sql
sp_primarykeys
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
[ ; ]
```
