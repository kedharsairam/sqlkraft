---
name: "sys.sp_statistics"
title: "sp_statistics"
category: "general"
description: "Analytics Platform System (PDW) Returns a list of all indexes and statistics on a specified table or indexed view. Transact-SQL syntax conventions Specifies the table used to return catalog information. default. Wildcard pattern matching isn't supported. The name of the table owner of the table used to return catalog information. . Wildcard pattern matching isn't supported. If specified, the defau"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_statistics
  [ @table_name = ]
  N
  'table_name'
  [ , [ @table_owner = ]
  N
  'table_owner'
  ]
  [ , [ @table_qualifier = ]
  N
  'table_qualifier'
  ]
  [ , [ @index_name = ]
  N
  'index_name'
  ]
  [ , [ @is_unique = ]
  'is_unique'
  ]
  [ , [ @accuracy = ]
  'accuracy'
  ]
  [ ; ]
---

## Description

Analytics Platform System (PDW) Returns a list of all indexes and statistics on a specified table or indexed view. Transact-SQL syntax conventions Specifies the table used to return catalog information. default. Wildcard pattern matching isn't supported. The name of the table owner of the table used to return catalog information. . Wildcard pattern matching isn't supported. If specified, the default table visibility rules of the underlying database management system

## Syntax

```sql
sp_statistics
[ @table_name = ]
N
'table_name'
[ , [ @table_owner = ]
N
'table_owner'
]
[ , [ @table_qualifier = ]
N
'table_qualifier'
]
[ , [ @index_name = ]
N
'index_name'
]
[ , [ @is_unique = ]
'is_unique'
]
[ , [ @accuracy = ]
'accuracy'
]
[ ; ]
```
