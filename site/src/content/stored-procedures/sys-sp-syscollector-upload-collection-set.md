---
name: "sys.sp_syscollector_upload_collection_set"
title: "sp_syscollector_upload_collection_set"
category: "general"
description: "Starts an upload of collection set data if the collection set is enabled. Transact-SQL syntax conventions The unique local identifier for the collection set. The name of the collection set. This stored procedure can only be used for collection sets that are configured for cached mode data collection and upload."
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

Starts an upload of collection set data if the collection set is enabled. Transact-SQL syntax conventions The unique local identifier for the collection set. The name of the collection set. This stored procedure can only be used for collection sets that are configured for cached mode data collection and upload.

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
