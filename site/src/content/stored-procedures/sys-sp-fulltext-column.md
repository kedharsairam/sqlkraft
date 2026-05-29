---
name: 'sys.sp_fulltext_column'
title: 'sp_fulltext_column'
category: 'general'
description: 'Specifies whether or not a particular column of a table participates in full-text indexing. Transact-SQL syntax conventions A one-part or two-part table name. The table must exist in the current database. The table . The column must be either a character, , and can''t be a computed column. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development wo'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_fulltext_column
  [ @tabname = ]
  N
  'tabname'
  , [ @colname = ]
  N
  'colname'
  , [ @action = ]
  'action'
  [ , [ @language = ] language ]
  [ , [ @type_colname = ]
  N
  'type_colname'
  ]
  [ ; ]
---

## Description

Specifies whether or not a particular column of a table participates in full-text indexing. Transact-SQL syntax conventions A one-part or two-part table name. The table must exist in the current database. The table . The column must be either a character, , and can't be a computed column. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_fulltext_column
[ @tabname = ]
N
'tabname'
, [ @colname = ]
N
'colname'
, [ @action = ]
'action'
[ , [ @language = ] language ]
[ , [ @type_colname = ]
N
'type_colname'
]
[ ; ]
```
