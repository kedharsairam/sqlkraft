---
name: "sys.sp_deletemergeconflictrow"
title: "sp_deletemergeconflictrow"
category: "general"
description: "Deletes rows from a conflict table or the table. This stored procedure is executed at the computer where the conflict table is stored, in any database. Transact-SQL syntax conventions The name of the conflict table. , the conflict is assumed to be a delete conflict and the The row identifier for the delete conflict."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_deletemergeconflictrow
  [ [ @conflict_table = ]
  N
  'conflict_table'
  ]
  [ , [ @source_object = ]
  N
  'source_object'
  ]
  , [ @rowguid = ]
  'rowguid'
  , [ @origin_datasource = ]
  'origin_datasource'
  [ , [ @drop_table_if_empty = ]
  'drop_table_if_empty'
  ]
  [ ; ]
---

## Description

Deletes rows from a conflict table or the table. This stored procedure is executed at the computer where the conflict table is stored, in any database. Transact-SQL syntax conventions The name of the conflict table. , the conflict is assumed to be a delete conflict and the The row identifier for the delete conflict.

## Syntax

```sql
sp_deletemergeconflictrow
[ [ @conflict_table = ]
N
'conflict_table'
]
[ , [ @source_object = ]
N
'source_object'
]
, [ @rowguid = ]
'rowguid'
, [ @origin_datasource = ]
'origin_datasource'
[ , [ @drop_table_if_empty = ]
'drop_table_if_empty'
]
[ ; ]
```
