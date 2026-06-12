---
name: "sys.sp_addqueued_artinfo"
title: "sp_addqueued_artinfo"
category: "general"
description: "table at the Subscriber that is used to track article subscription information (queued, updating, and immediate updating with queued updating as failover). This stored procedure is executed at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addqueued_artinfo
  [ @artid = ] artid
  , [ @article = ]
  N
  'article'
  , [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @dest_table = ]
  N
  'dest_table'
  , [ @owner = ]
  N
  'owner'
  , [ @cft_table = ]
  N
  'cft_table'
  [ , [ @columns = ] columns ]
  [ ; ]
---

## Description

table at the Subscriber that is used to track article subscription information (queued, updating, and immediate updating with queued updating as failover). This stored procedure is executed at the Subscriber on the subscription database.

## Syntax

```sql
sp_addqueued_artinfo
[ @artid = ] artid
, [ @article = ]
N
'article'
, [ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @dest_table = ]
N
'dest_table'
, [ @owner = ]
N
'owner'
, [ @cft_table = ]
N
'cft_table'
[ , [ @columns = ] columns ]
[ ; ]
```

## Permissions

is used by the Distribution Agent as part of subscription initialization. This stored procedure isn't commonly run by users, but might be useful if you need to manually set up a subscription. Use sp_script_synctran_commands instead of. Only members of the fixed server role or fixed database role can execute. Updatable Subscriptions - For Transactional Replication sp_script_synctran_commands (Transact-SQL) MSsubscription_articles (Transact-SQL) System stored procedures (Transact-SQL)
