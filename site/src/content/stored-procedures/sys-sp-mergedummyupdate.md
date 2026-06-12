---
name: "sys.sp_mergedummyupdate"
title: "sp_mergedummyupdate"
category: "general"
description: "Does a dummy update on the given row, so that it sends again during the next merge. This stored procedure can be executed at the Publisher, on the publication database, or at the Subscriber, on the subscription database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_mergedummyupdate
      [ @source_object = ]
      N
      'source_object'
      , [ @rowguid = ]
      'rowguid'
      [ ; ]
---

## Description

Does a dummy update on the given row, so that it sends again during the next merge. This stored procedure can be executed at the Publisher, on the publication database, or at the Subscriber, on the subscription database.

## Syntax

```sql
sp_mergedummyupdate
[ @source_object = ]
N
'source_object'
, [ @rowguid = ]
'rowguid'
[ ; ]
```

## Permissions

is useful if you write your own alternative to the Replication Conflict Viewer ( ). Only members of the fixed database role can execute. System stored procedures (Transact-SQL)
## Remarks

Does a dummy update on the given row, so that it sends again during the next merge. This

stored procedure can be executed at the Publisher, on the publication database, or at the

Subscriber, on the subscription database.

The name of the source object.

@source_object

, with no default.

The row identifier.

, with no default.

(success) or

is used in merge replication.
