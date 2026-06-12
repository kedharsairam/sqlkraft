---
name: "sys.sp_dropmergesubscription"
title: "sp_dropmergesubscription"
category: "general"
description: "Drops a subscription to a merge publication and its associated Merge Agent. This stored procedure is executed at the Publisher on the publication database. already exist and conform to the rules for The name of the subscription database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmergesubscription
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @subscriber = ]
  N
  'subscriber'
  ]
  [ , [ @subscriber_db = ]
  N
  'subscriber_db'
  ]
  [ , [ @subscription_type = ]
  N
  'subscription_type'
  ]
  [ , [ @ignore_distributor = ] ignore_distributor ]
  [ , [ @reserved = ] reserved ]
  [ ; ]
---

## Description

Drops a subscription to a merge publication and its associated Merge Agent. This stored procedure is executed at the Publisher on the publication database. already exist and conform to the rules for The name of the subscription database.

## Syntax

```sql
sp_dropmergesubscription
[ [ @publication = ]
N
'publication'
]
[ , [ @subscriber = ]
N
'subscriber'
]
[ , [ @subscriber_db = ]
N
'subscriber_db'
]
[ , [ @subscription_type = ]
N
'subscription_type'
]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @reserved = ] reserved ]
[ ; ]
```

## Permissions

Only members of the fixed server role or the fixed database role can execute. Delete a Push Subscription Delete a Pull Subscription sp_addmergesubscription (Transact-SQL) sp_changemergesubscription (Transact-SQL) sp_helpmergesubscription (Transact-SQL)
