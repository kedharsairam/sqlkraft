---
name: "sys.sp_addsynctriggers"
title: "sp_addsynctriggers"
category: "general"
description: "Creates triggers at the Subscriber used with all types of updatable subscriptions (immediate, queued, and immediate updating with queued updating as failover). This stored procedure is executed at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addsynctriggers
  [ @sub_table = ]
  N
  'sub_table'
  , [ @sub_table_owner = ]
  N
  'sub_table_owner'
  , [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @ins_proc = ]
  N
  'ins_proc'
  , [ @upd_proc = ]
  N
  'upd_proc'
  , [ @del_proc = ]
  N
  'del_proc'
  , [ @cftproc = ]
  N
  'cftproc'
  , [ @proc_owner = ]
  N
  'proc_owner'
  [ , [ @identity_col = ]
  N
  'identity_col'
  ]
  [ , [ @ts_col = ]
  N
  'ts_col'
  ]
  [ , [ @filter_clause = ]
  N
  'filter_clause'
  ]
  , [ @primary_key_bitmap = ] primary_key_bitmap
  [ , [ @identity_support = ] identity_support ]
  [ , [ @independent_agent = ] independent_agent ]
  , [ @distributor = ]
  N
  'distributor'
  [ , [ @pubversion = ] pubversion ]
  [ , [ @dump_cmds = ] dump_cmds ]
  [ ; ]
---

## Description

Creates triggers at the Subscriber used with all types of updatable subscriptions (immediate, queued, and immediate updating with queued updating as failover). This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions procedure should be used instead of generates a script that contains the

## Syntax

```sql
sp_addsynctriggers
[ @sub_table = ]
N
'sub_table'
, [ @sub_table_owner = ]
N
'sub_table_owner'
, [ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @ins_proc = ]
N
'ins_proc'
, [ @upd_proc = ]
N
'upd_proc'
, [ @del_proc = ]
N
'del_proc'
, [ @cftproc = ]
N
'cftproc'
, [ @proc_owner = ]
N
'proc_owner'
[ , [ @identity_col = ]
N
'identity_col'
]
[ , [ @ts_col = ]
N
'ts_col'
]
[ , [ @filter_clause = ]
N
'filter_clause'
]
, [ @primary_key_bitmap = ] primary_key_bitmap
[ , [ @identity_support = ] identity_support ]
[ , [ @independent_agent = ] independent_agent ]
, [ @distributor = ]
N
'distributor'
[ , [ @pubversion = ] pubversion ]
[ , [ @dump_cmds = ] dump_cmds ]
[ ; ]
```

## Arguments

Applies to:

Creates triggers at the Subscriber used with all types of updatable subscriptions (immediate,

queued, and immediate updating with queued updating as failover). This stored procedure is

executed at the Subscriber on the subscription database.

Transact-SQL syntax conventions

procedure should be used instead of

generates a script that contains the

## Permissions

Only members of the fixed server role or fixed database role can execute . Updatable Subscriptions - For Transactional Replication sp_script_synctran_commands (Transact-SQL) System stored procedures (Transact-SQL) Related content
