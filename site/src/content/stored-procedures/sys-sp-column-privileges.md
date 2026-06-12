---
name: "sys.sp_column_privileges"
title: "sp_column_privileges"
category: "general"
description: "Returns column privilege information for a single table in the current environment. The table used to return catalog information. Wildcard pattern matching isn't supported. The owner of the table used to return catalog information. Wildcard pattern matching isn't supported. If default table visibility rules of the underlying databa"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_column_privileges
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
  [ , [ @column_name = ]
  N
  'column_name'
  ]
  [ ; ]
---

## Description

Returns column privilege information for a single table in the current environment. The table used to return catalog information. Wildcard pattern matching isn't supported. The owner of the table used to return catalog information. Wildcard pattern matching isn't supported. If default table visibility rules of the underlying database management system (DBMS) apply.

## Syntax

```sql
sp_column_privileges
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
[ , [ @column_name = ]
N
'column_name'
]
[ ; ]
```
