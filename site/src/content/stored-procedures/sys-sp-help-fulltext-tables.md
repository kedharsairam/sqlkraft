---
name: 'sys.sp_help_fulltext_tables'
title: 'sp_help_fulltext_tables'
category: 'general'
description: 'Returns a list of tables that are registered for full-text indexing. Transact-SQL syntax conventions The name of the full-text catalog. , all full-text indexed tables associated with index information is retrieved for every full-text indexed table associated with this catalog. are specified, a row is returned if ; otherwise, an error is raised. This feature will be removed in a future version of S'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_fulltext_tables
  [ [ @fulltext_catalog_name = ]
  N
  'fulltext_catalog_name'
  ]
  [ , [ @table_name = ]
  N
  'table_name'
  ]
  [ ; ]
---

## Description

Returns a list of tables that are registered for full-text indexing. Transact-SQL syntax conventions The name of the full-text catalog. , all full-text indexed tables associated with index information is retrieved for every full-text indexed table associated with this catalog. are specified, a row is returned if ; otherwise, an error is raised. This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
sp_help_fulltext_tables
[ [ @fulltext_catalog_name = ]
N
'fulltext_catalog_name'
]
[ , [ @table_name = ]
N
'table_name'
]
[ ; ]
```
