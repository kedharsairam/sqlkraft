---
name: 'sys.sp_fulltext_catalog'
title: 'sp_fulltext_catalog'
category: 'general'
description: 'Creates and drops a full-text catalog, and starts and stops the indexing action for a catalog. Multiple full-text catalogs can be created for each database. Transact-SQL syntax conventions The name of the full-text catalog. Catalog names must be unique for each database. , and can be one of these values. This feature will be removed in a future version of SQL Server. Avoid using this feature in ne'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_fulltext_catalog
  [ @ftcat = ]
  N
  'ftcat'
  , [ @action = ]
  'action'
  [ , [ @path = ]
  N
  'path'
  ]
  [ ; ]
---

## Description

Creates and drops a full-text catalog, and starts and stops the indexing action for a catalog. Multiple full-text catalogs can be created for each database. Transact-SQL syntax conventions The name of the full-text catalog. Catalog names must be unique for each database. , and can be one of these values. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_fulltext_catalog
[ @ftcat = ]
N
'ftcat'
, [ @action = ]
'action'
[ , [ @path = ]
N
'path'
]
[ ; ]
```
