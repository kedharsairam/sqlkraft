---
name: "sys.sp_help_fulltext_columns"
title: "sp_help_fulltext_columns"
category: "general"
description: "Returns the columns designated for full-text indexing. The one- or two-part table name for which full-text index information is requested. is omitted, full-text index column information is retrieved for every full-text The name of the column for which full-text index metadata is requested. information is returned for every full-text indexed column for This feature w"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_fulltext_columns
  [ [ @table_name = ]
  N
  'table_name'
  ]
  [ , [ @column_name = ]
  N
  'column_name'
  ]
  [ ; ]
---

## Description

Returns the columns designated for full-text indexing. The one- or two-part table name for which full-text index information is requested. is omitted, full-text index column information is retrieved for every full-text The name of the column for which full-text index metadata is requested. information is returned for every full-text indexed column for This feature will be removed in a future version of SQL Server.

## Syntax

```sql
sp_help_fulltext_columns
[ [ @table_name = ]
N
'table_name'
]
[ , [ @column_name = ]
N
'column_name'
]
[ ; ]
```
