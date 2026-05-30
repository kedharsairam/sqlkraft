---
name: "sys.sp_repldropcolumn"
title: "sp_repldropcolumn"
category: "general"
description: "Drops a column from an existing table article that was published. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the table article that contains the column to drop. The name of the column in the table to be dropped. This stored procedure has been deprecated and is being supported mainly for backward- compatibility. It sho"
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

Drops a column from an existing table article that was published. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the table article that contains the column to drop. The name of the column in the table to be dropped. This stored procedure has been deprecated and is being supported mainly for backward- compatibility. It should only be used with SQL Server 2000 (8.x) Publishers and SQL Server

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
