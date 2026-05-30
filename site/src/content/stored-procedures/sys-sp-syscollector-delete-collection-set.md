---
name: "sys.sp_syscollector_delete_collection_set"
title: "sp_syscollector_delete_collection_set"
category: "general"
description: "Deletes a user-defined collection set and all its collection items. Transact-SQL syntax conventions The unique identifier for the collection set. @collection_set_id , with a default of @collection_set_id must have a value if The name of the collection set. , with a default of @collection_set_id"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_delete_collection_set
  [ [ @collection_set_id = ] collection_set_id ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ ; ]
---

## Description

Deletes a user-defined collection set and all its collection items. Transact-SQL syntax conventions The unique identifier for the collection set. @collection_set_id , with a default of @collection_set_id must have a value if The name of the collection set. , with a default of @collection_set_id

## Syntax

```sql
sp_syscollector_delete_collection_set
[ [ @collection_set_id = ] collection_set_id ]
[ , [ @name = ]
N
'name'
]
[ ; ]
```

## Remarks

Applies to:

Deletes a user-defined collection set and all its collection items.

Transact-SQL syntax conventions

The unique identifier for the collection set.

@collection_set_id

, with a default of

@collection_set_id

must have a value if

The name of the collection set.

, with a default of

must have a

@collection_set_id

(success) or

## Examples

### Example 1

`sp_syscollector_delete_collection_set`

### Example 2

`msdb`

### Example 3

`NULL`

### Example 4

`syscollector_collection_set`

### Example 5

```sql
USE msdb;
GO
EXECUTE dbo.sp_syscollector_delete_collection_set @collection_set_id = 4;
```
