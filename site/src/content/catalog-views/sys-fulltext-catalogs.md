---
name: 'sys.fulltext_catalogs'
title: 'sys.fulltext_catalogs'
category: 'full-text'
description: 'Contains a row for each full-text catalog. ID of the full-text catalog. Is unique across the full-text catalogs Name of the catalog. Is unique within the database. Name of the catalog directory in the file system. The default full-text catalog. Accent-sensitivity setting of the catalog. False = Is not accent-sensitive. Filegroup where this catalog was created. File ID of the full-text file associa'
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

Contains a row for each full-text catalog. ID of the full-text catalog. Is unique across the full-text catalogs Name of the catalog. Is unique within the database. Name of the catalog directory in the file system. The default full-text catalog. Accent-sensitivity setting of the catalog. False = Is not accent-sensitive. Filegroup where this catalog was created. File ID of the full-text file associated with the catalog.

## Syntax

```sql
sp_help_fulltext_catalogs [ [ @fulltext_catalog_name = ]
N
'fulltext_catalog_name'
]
[ ; ]
```
