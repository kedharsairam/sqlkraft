---
name: "sys.sp_create_plan_guide"
title: "sp_create_plan_guide"
category: "general"
description: "Creates a plan guide for associating query hints or actual query plans with queries in a database. For more information about plan guides, see Transact-SQL syntax conventions , with no default, and a maximum length of 124 characters. Plan guide names are scoped to the current database. and can't start with the number sign ( A Transact-SQL statement against which to create a plan guide. . When the "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_create_plan_guide
  [ @name = ]
  N
  'name'
  [ , [ @stmt = ]
  N
  'stmt'
  ]
  , [ @type = ] {
  N
  'OBJECT'
  |
  N
  'SQL'
  |
  N
  'TEMPLATE'
  }
  [ , [ @module_or_batch = ] {
  N
  ' [ schema_name. ] object_name'
  |
  N
  'batch_text'
  } ]
  [ , [ @params = ]
  N
  '@parameter_name data_type [ , ... n ]'
  ]
  [ , [ @hints = ] {
  N
  'OPTION ( query_hint [ , ...n ] )'
  |
  N
  'XML_showplan'
  } ]
  [ ; ]
---

## Description

Creates a plan guide for associating query hints or actual query plans with queries in a database. For more information about plan guides, see Transact-SQL syntax conventions , with no default, and a maximum length of 124 characters. Plan guide names are scoped to the current database. and can't start with the number sign ( A Transact-SQL statement against which to create a plan guide. . When the SQL Server query optimizer recognizes a query that matches

## Syntax

```sql
sp_create_plan_guide
[ @name = ]
N
'name'
[ , [ @stmt = ]
N
'stmt'
]
, [ @type = ] {
N
'OBJECT'
|
N
'SQL'
|
N
'TEMPLATE'
}
[ , [ @module_or_batch = ] {
N
' [ schema_name. ] object_name'
|
N
'batch_text'
} ]
[ , [ @params = ]
N
'@parameter_name data_type [ , ... n ]'
]
[ , [ @hints = ] {
N
'OPTION ( query_hint [ , ...n ] )'
|
N
'XML_showplan'
} ]
[ ; ]
```
