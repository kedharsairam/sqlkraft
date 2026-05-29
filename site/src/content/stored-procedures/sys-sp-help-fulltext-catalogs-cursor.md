---
name: 'sys.sp_help_fulltext_catalogs_cursor'
title: 'sp_help_fulltext_catalogs_cursor'
category: 'general'
description: 'Uses a cursor to return the ID, name, root directory, status, and number of full-text indexed tables for the specified full-text catalog. Transact-SQL syntax conventions is an OUTPUT parameter of type . The cursor is a read-only, scrollable, The name of the full-text catalog. this parameter is omitted or is , information about all full-text catalogs associated with the This feature will be removed'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_fulltext_catalogs_cursor
  [ @cursor_return = ] cursor_return
  OUTPUT
  [ , [ @fulltext_catalog_name = ]
  N
  'fulltext_catalog_name'
  ]
  [ ; ]
---

## Description

Uses a cursor to return the ID, name, root directory, status, and number of full-text indexed tables for the specified full-text catalog. Transact-SQL syntax conventions is an OUTPUT parameter of type . The cursor is a read-only, scrollable, The name of the full-text catalog. this parameter is omitted or is , information about all full-text catalogs associated with the This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
sp_help_fulltext_catalogs_cursor
[ @cursor_return = ] cursor_return
OUTPUT
[ , [ @fulltext_catalog_name = ]
N
'fulltext_catalog_name'
]
[ ; ]
```
