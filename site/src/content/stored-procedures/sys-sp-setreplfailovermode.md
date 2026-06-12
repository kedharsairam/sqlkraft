---
name: "sys.sp_setreplfailovermode"
title: "sp_setreplfailovermode"
category: "general"
description: "Allows you to set the failover operation mode for subscriptions enabled for immediate updating, with queued updating as failover. This stored procedure is executed at the Subscriber on the subscription database. For more information about failover modes, see Updatable Subscriptions - For Transactional Replication , with no default. The publication must The name of t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_setreplfailovermode
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @failover_mode = ]
  N
  'failover_mode'
  [ , [ @override = ] override ]
  [ ; ]
---

## Description

Allows you to set the failover operation mode for subscriptions enabled for immediate updating, with queued updating as failover. This stored procedure is executed at the Subscriber on the subscription database. For more information about failover modes, see Updatable Subscriptions - For Transactional Replication , with no default. The publication must The name of the publication database.

## Syntax

```sql
sp_setreplfailovermode
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @failover_mode = ]
N
'failover_mode'
[ , [ @override = ] override ]
[ ; ]
```
