---
name: 'sys.sp_help_fulltext_catalogs'
title: 'sp_help_fulltext_catalogs'
category: 'general'
description: 'Returns the ID, name, root directory, status, and number of full-text indexed tables for the Transact-SQL syntax conventions The name of the full-text catalog. this parameter is omitted or has the value , information about all full-text catalogs associated with the current database is returned. This feature will be removed in a future version of SQL Server. Avoid using this feature in new developm'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_fulltext_catalogs [ [ @fulltext_catalog_name = ]
  N
  'fulltext_catalog_name'
  ]
  [ ; ]
---

## Description

Returns the ID, name, root directory, status, and number of full-text indexed tables for the Transact-SQL syntax conventions The name of the full-text catalog. this parameter is omitted or has the value , information about all full-text catalogs associated with the current database is returned. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_help_fulltext_catalogs [ [ @fulltext_catalog_name = ]
N
'fulltext_catalog_name'
]
[ ; ]
```
