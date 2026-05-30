---
name: "sys.sp_columns"
title: "sp_columns"
category: "general"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns column information for the specified objects that can be queried in the current Transact-SQL syntax conventions The name of the object that is used to return catalog information. view, or other object that's columns such as table-valued functions. , with no default. Wildcard pattern matching is supported. The object owner of "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_columns
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
  [ , [ @
  ODBCV
  er = ]
  ODBCV
  er ]
  [ ; ]
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns column information for the specified objects that can be queried in the current Transact-SQL syntax conventions The name of the object that is used to return catalog information. view, or other object that's columns such as table-valued functions. , with no default. Wildcard pattern matching is supported. The object owner of the object that is used to return catalog information.

## Syntax

```sql
sp_columns
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
[ , [ @
ODBCV
er = ]
ODBCV
er ]
[ ; ]
```
