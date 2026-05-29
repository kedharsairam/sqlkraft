---
name: 'sys.sp_marksubscriptionvalidation'
title: 'sp_marksubscriptionvalidation'
category: 'general'
description: 'Marks the current open transaction to be a subscription-level validation transaction for the specified subscriber. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions The name of the destination database.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_marksubscriptionvalidation
  [ @publication = ]
  N
  'publication'
  , [ @subscriber = ]
  N
  'subscriber'
  , [ @destination_db = ]
  N
  'destination_db'
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Marks the current open transaction to be a subscription-level validation transaction for the specified subscriber. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions The name of the destination database.

## Syntax

```sql
sp_marksubscriptionvalidation
[ @publication = ]
N
'publication'
, [ @subscriber = ]
N
'subscriber'
, [ @destination_db = ]
N
'destination_db'
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
