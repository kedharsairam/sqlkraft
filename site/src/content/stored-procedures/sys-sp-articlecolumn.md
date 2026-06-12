---
name: "sys.sp_articlecolumn"
title: "sp_articlecolumn"
category: "general"
description: "Used to specify columns included in an article to vertically filter data in a published table. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_articlecolumn
      [ @publication = ]
      N
      'publication'
      , [ @article = ]
      N
      'article'
      [ , [ @column = ]
      N
      'column'
      ]
      [ , [ @operation = ]
      N
      'operation'
      ]
      [ , [ @refresh_synctran_procs = ] refresh_synctran_procs ]
      [ , [ @ignore_distributor = ] ignore_distributor ]
      [ , [ @change_active = ] change_active ]
      [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
      [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ , [ @internal = ] internal ]
      [ ; ]
---

## Description

Used to specify columns included in an article to vertically filter data in a published table. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_articlecolumn
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @column = ]
N
'column'
]
[ , [ @operation = ]
N
'operation'
]
[ , [ @refresh_synctran_procs = ] refresh_synctran_procs ]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @change_active = ] change_active ]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @internal = ] internal ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Define an Article Define and Modify a Column Filter Filter Published Data sp_addarticle (Transact-SQL) sp_articleview (Transact-SQL) sp_changearticle (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) sp_helparticlecolumns (Transact-SQL) Replication stored procedures (Transact-SQL)
