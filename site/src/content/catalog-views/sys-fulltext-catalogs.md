---
name: "sys.fulltext_catalogs"
title: "sys.fulltext_catalogs"
category: "full-text"
description: "Contains a row for each full-text catalog."
tags: ["full-text", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  sp_help_fulltext_catalogs [ [ @fulltext_catalog_name = ]
  N
  'fulltext_catalog_name'
  ]
  [ ; ]
---

## Description

Contains a row for each full-text catalog.

## Syntax

```sql
sp_help_fulltext_catalogs [ [ @fulltext_catalog_name = ]
N
'fulltext_catalog_name'
]
[ ; ]
```
