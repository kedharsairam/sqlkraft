---
name: "sys.sp_repldropcolumn"
title: "sp_repldropcolumn"
category: "general"
description: "Drops a column from an existing table article that was published. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_repldropcolumn
              [ @source_object = ]
              N
              'source_object'
              , [ @column = ]
              N
              'column'
              [ , [ @from_agent = ] from_agent ]
              [ , [ @schema_change_script = ]
              N
              'schema_change_script'
              ]
              [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
              [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
              [ ; ]
---

## Description

Drops a column from an existing table article that was published. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_repldropcolumn
[ @source_object = ]
N
'source_object'
, [ @column = ]
N
'column'
[ , [ @from_agent = ] from_agent ]
[ , [ @schema_change_script = ]
N
'schema_change_script'
]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ ; ]
```
