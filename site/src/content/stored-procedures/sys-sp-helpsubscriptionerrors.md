---
name: 'sys.sp_helpsubscriptionerrors'
title: 'sp_helpsubscriptionerrors'
category: 'general'
description: 'Returns all transactional replication errors for a given subscription. This stored procedure is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication database.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpsubscriptionerrors
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @subscriber = ]
  N
  'subscriber'
  , [ @subscriber_db = ]
  N
  'subscriber_db'
  [ ; ]
---

## Description

Returns all transactional replication errors for a given subscription. This stored procedure is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication database.

## Syntax

```sql
sp_helpsubscriptionerrors
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @subscriber = ]
N
'subscriber'
, [ @subscriber_db = ]
N
'subscriber_db'
[ ; ]
```
