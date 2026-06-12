---
name: "sys.sp_indexes"
title: "sp_indexes"
category: "general"
description: "Returns index information for the specified remote table."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_indexes
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
      [ , [ @index_name = ]
      N
      'index_name'
      ]
      [ , [ @is_unique = ] is_unique ]
      [ ; ]
---

## Description

Returns index information for the specified remote table.

## Syntax

```sql
sp_indexes
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
[ , [ @index_name = ]
N
'index_name'
]
[ , [ @is_unique = ] is_unique ]
[ ; ]
```
