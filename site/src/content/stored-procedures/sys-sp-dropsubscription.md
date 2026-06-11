---
name: "sys.sp_dropsubscription"
title: "sp_dropsubscription"
category: "general"
description: "Drops subscriptions to a particular article, publication, or set of subscriptions on the Publisher. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the associated publication. , all subscriptions for all publications for the specified Subscriber are canceled."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropsubscription
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @article = ]
  N
  'article'
  ]
  , [ @subscriber = ]
  N
  'subscriber'
  [ , [ @destination_db = ]
  N
  'destination_db'
  ]
  [ , [ @ignore_distributor = ] ignore_distributor ]
  [ , [ @reserved = ]
  N
  'reserved'
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Drops subscriptions to a particular article, publication, or set of subscriptions on the Publisher. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the associated publication. , all subscriptions for all publications for the specified Subscriber are canceled. articles for each specified publication and Subscriber are dropped. Use

## Syntax

```sql
sp_dropsubscription
[ [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
]
, [ @subscriber = ]
N
'subscriber'
[ , [ @destination_db = ]
N
'destination_db'
]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @reserved = ]
N
'reserved'
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

Only members of the fixed server role, the fixed database role, or the user that created the subscription can execute . Delete a Push Subscription sp_addsubscription (Transact-SQL) sp_changesubstatus (Transact-SQL) sp_helpsubscription (Transact-SQL) Related content
