---
name: "sys.sp_help_fulltext_tables"
title: "sp_help_fulltext_tables"
category: "general"
description: "Returns a list of tables that are registered for full-text indexing."
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

Returns a list of tables that are registered for full-text indexing.

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
