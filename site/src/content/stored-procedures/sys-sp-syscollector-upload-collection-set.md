---
name: "sys.sp_syscollector_upload_collection_set"
title: "sp_syscollector_upload_collection_set"
category: "general"
description: "Starts an upload of collection set data if the collection set is enabled. The unique local identifier for the collection set."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_upload_collection_set
              [ [ @collection_set_id = ] collection_set_id ]
              [ , [ @name = ]
              N
              'name'
              ]
              [ ; ]
---

## Description

Starts an upload of collection set data if the collection set is enabled. The unique local identifier for the collection set.

## Syntax

```sql
sp_syscollector_upload_collection_set
[ [ @collection_set_id = ] collection_set_id ]
[ , [ @name = ]
N
'name'
]
[ ; ]
```
