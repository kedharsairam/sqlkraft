---
name: "sys.sp_deletemergeconflictrow"
title: "sp_deletemergeconflictrow"
category: "general"
description: "Deletes rows from a conflict table or the table. This stored procedure is executed at the computer where the conflict table is stored, in any database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
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

Deletes rows from a conflict table or the table. This stored procedure is executed at the computer where the conflict table is stored, in any database.

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
