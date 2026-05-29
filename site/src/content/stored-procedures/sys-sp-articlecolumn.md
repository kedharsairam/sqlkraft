---
name: 'sys.sp_articlecolumn'
title: 'sp_articlecolumn'
category: 'general'
description: 'Used to specify columns included in an article to vertically filter data in a published table. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication that contains this article. The name of the column to be added or dropped.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
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

Used to specify columns included in an article to vertically filter data in a published table. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication that contains this article. The name of the column to be added or dropped.

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

Only members of the fixed server role or fixed database role can execute . Define an Article Define and Modify a Column Filter Filter Published Data sp_addarticle (Transact-SQL) sp_articleview (Transact-SQL) sp_changearticle (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) sp_helparticlecolumns (Transact-SQL) Replication stored procedures (Transact-SQL) Related content Only members of the fixed server role or fixed database role can execute . Define an Article Define and Modify a Static Row Filter sp_addarticle (Transact-SQL) sp_articleview (Transact-SQL) sp_changearticle (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) Replication stored procedures (Transact-SQL) Related content Only members of the fixed server role or fixed database role can execute . Define an Article Define and Modify a Static Row Filter sp_addarticle (Transact-SQL) sp_articlefilter (Transact-SQL) sp_changearticle (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) Replication stored procedures (Transact-SQL) Related content By default, replication doesn't publish any columns in the source table when the column data type isn't supported by replication. If you need to publish such a column, you must execute sp_articlecolumn to add the column. When adding an article to a publication that supports peer-to-peer transactional replication, the following restrictions apply: Parameterized statements must be specified for all logbased articles. You must include in the @status value. Name and owner of the destination table must match the source table. The article can't be filtered horizontally or vertically. Automatic identity range management isn't supported. You must specify a value of manual for @identityrangemanagementoption . If a column exists in the table, you must include 0x08 in @schema_option to replicate the column as . A value of can't be specified for @ins_cmd , @upd_cmd , and @del_cmd . For more information, see Peer-to-Peer - Transactional Replication . When you publish objects, their definitions are copied to Subscribers. If you're publishing a database object that depends on one or more other objects, you must publish all referenced objects. For example, if you publish a view that depends on a table, you must publish the table also. If @vertical_partition is set to , defers the creation of the view until sp_articleview is called (after the last sp_articlecolumn is added). If the publication allows updating subscriptions and the published table doesn't have a column, adds a column to the table automatically. When replicating to a subscriber that isn't an instance of SQL Server (heterogeneous replication), only Transact-SQL statements are supported for , , and commands. When the log reader agent is running, adding an article to a peer-to-peer publication can cause a deadlock between the log reader agent and the process that adds the article. To avoid this issue, before adding an article to a peer-to-peer publication use the Replication Monitor to stop the log reader agent on the node where you're adding the article. Restart the log reader agent after adding the article.
