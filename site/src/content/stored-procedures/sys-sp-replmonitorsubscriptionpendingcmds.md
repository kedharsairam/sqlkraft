---
name: "sys.sp_replmonitorsubscriptionpendingcmds"
title: "sp_replmonitorsubscriptionpendingcmds"
category: "general"
description: "Returns information on the number of pending commands for a subscription to a transactional publication and a rough estimate of how much time it takes to process them. This stored procedure returns one row for each returned subscription. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replmonitorsubscriptionpendingcmds [ @publisher = ]
  'publisher'
  , [ @publisher_db = ]
  'publisher_db'
  , [ @publication = ]
  'publication'
  , [ @subscriber = ]
  'subscriber'
  , [ @subscriber_db = ]
  'subscriber_db'
  , [ @subscription_type = ] subscription_type
  , [ @subdb_version = ] subdb_version
---

## Description

Returns information on the number of pending commands for a subscription to a transactional publication and a rough estimate of how much time it takes to process them. This stored procedure returns one row for each returned subscription. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the published database.

## Syntax

```sql
sp_replmonitorsubscriptionpendingcmds [ @publisher = ]
'publisher'
, [ @publisher_db = ]
'publisher_db'
, [ @publication = ]
'publication'
, [ @subscriber = ]
'subscriber'
, [ @subscriber_db = ]
'subscriber_db'
, [ @subscription_type = ] subscription_type
, [ @subdb_version = ] subdb_version
```

## Permissions

is used with transactional replication. Prior to SQL Server 2019 (15.x) CU17, wasn't supported with peer-to-peer replication, and returned an incorrect number of pending commands when used to query peer-to-peer replication topology. In SQL Server 2019 (15.x) CU 17, support was added to make compatible with peer-to-peer publications. However, even with SQL Server 2019 (15.x) CU17 or later, could report an incorrect number of pending commands when used with peer-to-peer replication if the table contains a stale entry of an incorrect version of the subscription database. To correct the problem, either delete all the stale entries from or pass the correct of the subscription database when using the argument for the stored procedure. See KB5017009 for details on how to determine . Only members of the fixed server role at the Distributor or members of the fixed database role in the distribution database can execute . Members of the publication access list for a publication that uses the distribution database can execute to return pending commands for that publication. Programmatically monitor replication Related content
