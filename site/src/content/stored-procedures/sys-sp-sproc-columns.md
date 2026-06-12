---
name: "sys.sp_sproc_columns"
title: "sp_sproc_columns"
category: "general"
description: "Returns column information for a single stored procedure or user-defined function in the The name of the procedure used to return catalog information. , which means all tables in the current database. Wildcard pattern matching is supported."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_sproc_columns
  [ [ @procedure_name = ]
  N
  'procedure_name'
  ]
  [ , [ @procedure_owner = ]
  N
  'procedure_owner'
  ]
  [ , [ @procedure_qualifier = ]
  N
  'procedure_qualifier'
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

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns column information for a single stored procedure or user-defined function in the The name of the procedure used to return catalog information. , which means all tables in the current database. Wildcard pattern matching is supported.

## Syntax

```sql
sp_sproc_columns
[ [ @procedure_name = ]
N
'procedure_name'
]
[ , [ @procedure_owner = ]
N
'procedure_owner'
]
[ , [ @procedure_qualifier = ]
N
'procedure_qualifier'
]
[ , [ @column_name = ]
N
'column_name'
]
[ , [ @
ODBCV er = ]
ODBCV er ]
[ , [ @f
U se
P attern = ] f
U se
P attern ]
[ ; ]
```
