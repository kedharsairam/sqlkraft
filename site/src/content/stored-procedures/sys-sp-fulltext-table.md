---
name: "sys.sp_fulltext_table"
title: "sp_fulltext_table"
category: "general"
description: "Marks or unmarks a table for full-text indexing. A one-part or two-part table name. The table must exist in the current database. , with no default, and can be one of these This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_fulltext_table
      [ @tabname = ]
      N
      'tabname'
      , [ @action = ]
      'action'
      [ , [ @ftcat = ]
      N
      'ftcat'
      ]
      [ , [ @keyname = ]
      N
      'keyname'
      ]
      [ ; ]
---

## Description

Marks or unmarks a table for full-text indexing. A one-part or two-part table name. The table must exist in the current database. , with no default, and can be one of these This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_fulltext_table
[ @tabname = ]
N
'tabname'
, [ @action = ]
'action'
[ , [ @ftcat = ]
N
'ftcat'
]
[ , [ @keyname = ]
N
'keyname'
]
[ ; ]
```
