---
name: "sys.sp_syscollector_start_collection_set"
title: "sp_syscollector_start_collection_set"
category: "general"
description: "Starts a collection set if the collector is already enabled and the collection set isn't running. If the collector isn't enabled, enable the collector by running sp_syscollector_enable_collector then use this stored procedure to start a collection set. Transact-SQL syntax conventions The unique local identifier for the collection set. @collection_set_id , with a default of @collection_set_id must "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_start_collection_set
  [ [ @collection_set_id = ] collection_set_id ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ ; ]
---

## Description

Starts a collection set if the collector is already enabled and the collection set isn't running. If the collector isn't enabled, enable the collector by running sp_syscollector_enable_collector then use this stored procedure to start a collection set. Transact-SQL syntax conventions The unique local identifier for the collection set. @collection_set_id , with a default of @collection_set_id must have a value if The name of the collection set. , with a default of @collection_set_id

## Syntax

```sql
sp_syscollector_start_collection_set
[ [ @collection_set_id = ] collection_set_id ]
[ , [ @name = ]
N
'name'
]
[ ; ]
```

## Remarks

Applies to:

Starts a collection set if the collector is already enabled and the collection set isn't running. If

the collector isn't enabled, enable the collector by running

sp_syscollector_enable_collector

then use this stored procedure to start a collection set.

Transact-SQL syntax conventions

The unique local identifier for the collection set.

@collection_set_id

, with a default of

@collection_set_id

must have a value if

The name of the collection set.

, with a default of

must have a

@collection_set_id

(success) or
