---
name: "sys.sp_syscollector_update_collection_item"
title: "sp_syscollector_update_collection_item"
category: "general"
description: "Used to modify the properties of a user-defined collection item or to rename a user-defined Transact-SQL syntax conventions The unique identifier that identifies the collection item. The name of the collection item. The new name for the collection item. used, can't be an empty string."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_update_collection_item
  [ [ @collection_item_id = ] collection_item_id ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ , [ @new_name = ]
  N
  'new_name'
  ]
  [ , [ @frequency = ] frequency ]
  [ , [ @parameters = ]
  N
  'parameters'
  ]
  [ ; ]
---

## Description

Used to modify the properties of a user-defined collection item or to rename a user-defined Transact-SQL syntax conventions The unique identifier that identifies the collection item. The name of the collection item. The new name for the collection item. used, can't be an empty string.

## Syntax

```sql
sp_syscollector_update_collection_item
[ [ @collection_item_id = ] collection_item_id ]
[ , [ @name = ]
N
'name'
]
[ , [ @new_name = ]
N
'new_name'
]
[ , [ @frequency = ] frequency ]
[ , [ @parameters = ]
N
'parameters'
]
[ ; ]
```
