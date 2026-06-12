---
name: "sys.sp_fulltext_catalog"
title: "sp_fulltext_catalog"
category: "general"
description: "Creates and drops a full-text catalog, and starts and stops the indexing action for a catalog. Multiple full-text catalogs can be created for each database."
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

Creates and drops a full-text catalog, and starts and stops the indexing action for a catalog. Multiple full-text catalogs can be created for each database.

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
