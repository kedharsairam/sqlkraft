---
name: 'sys.sp_syscollector_delete_collection_item'
title: 'sp_syscollector_delete_collection_item'
category: 'general'
description: 'Deletes a collection item from a collection set. Transact-SQL syntax conventions The unique identifier for the collection item. @collection_item_id , with a default of @collection_item_id must have a value if The name of the collection item. , with a default of an empty string. must have a value if @collection_item_id'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_delete_collection_item
  [ [ @collection_item_id = ] collection_item_id ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ ; ]
---

## Description

Deletes a collection item from a collection set. Transact-SQL syntax conventions The unique identifier for the collection item. @collection_item_id , with a default of @collection_item_id must have a value if The name of the collection item. , with a default of an empty string. must have a value if @collection_item_id

## Syntax

```sql
sp_syscollector_delete_collection_item
[ [ @collection_item_id = ] collection_item_id ]
[ , [ @name = ]
N
'name'
]
[ ; ]
```

## Remarks

Applies to:

Deletes a collection item from a collection set.

Transact-SQL syntax conventions

The unique identifier for the collection item.

@collection_item_id

, with a default of

@collection_item_id

must have a value if

The name of the collection item.

, with a default of an empty string.

must have a value if

@collection_item_id

(success) or

## Examples

### Example 1

```sql
sp_syscollector_delete_collection_item
```

### Example 2

```sql
msdb
```

### Example 3

```sql
MyCollectionItem1
```

### Example 4

```sql
USE
msdb;
GO
EXECUTE
sp_syscollector_delete_collection_item @
name
=
'MyCollectionItem1'
;
```
