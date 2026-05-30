---
name: "sys.sp_syscollector_stop_collection_set"
title: "sp_syscollector_stop_collection_set"
category: "general"
description: "Transact-SQL syntax conventions The unique local identifier for the collection set. The name of the collection set. Specifies that the collection job for the collection set should be stopped if it's running. applies only to collection sets with collection mode set to cached. For sp_syscollector_create_collection_set"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_stop_collection_set
  [ [ @collection_set_id = ] collection_set_id ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ , [ @stop_collection_job = ] stop_collection_job ]
  [ ; ]
---

## Description

Transact-SQL syntax conventions The unique local identifier for the collection set. The name of the collection set. Specifies that the collection job for the collection set should be stopped if it's running. applies only to collection sets with collection mode set to cached. For sp_syscollector_create_collection_set

## Syntax

```sql
sp_syscollector_stop_collection_set
[ [ @collection_set_id = ] collection_set_id ]
[ , [ @name = ]
N
'name'
]
[ , [ @stop_collection_job = ] stop_collection_job ]
[ ; ]
```
