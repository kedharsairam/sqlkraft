---
name: "sys.sp_syscollector_stop_collection_set"
title: "sp_syscollector_stop_collection_set"
category: "general"
description: "The unique local identifier for the collection set."
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
