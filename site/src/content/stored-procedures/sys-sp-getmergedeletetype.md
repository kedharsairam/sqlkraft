---
name: "sys.sp_getmergedeletetype"
title: "sp_getmergedeletetype"
category: "general"
description: "Returns the type of merge delete. This stored procedure is executed at the Publisher on the publication database or at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_getmergedeletetype
      [ @source_object = ]
      N
      'source_object'
      , [ @rowguid = ]
      'rowguid'
      , [ @delete_type = ] delete_type
      OUTPUT
      [ ; ]
---

## Description

Returns the type of merge delete. This stored procedure is executed at the Publisher on the publication database or at the Subscriber on the subscription database.

## Syntax

```sql
sp_getmergedeletetype
[ @source_object = ]
N
'source_object'
, [ @rowguid = ]
'rowguid'
, [ @delete_type = ] delete_type
OUTPUT
[ ; ]
```
