---
name: 'sys.sp_helpmergesubscription'
title: 'sp_helpmergesubscription'
category: 'general'
description: 'Returns information about a subscription to a merge publication, both push and pull. This stored procedure is executed at the Publisher on the publication database or at a republishing Subscriber on the subscription database. Transact-SQL syntax conventions must already exist and conform to the rules for merge publications and subscriptions in the current database is returned. information about al'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergesubscription
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
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  [ , [ @subscription_type = ]
  N
  'subscription_type'
  ]
  [ , [ @found = ] found
  OUTPUT
  ]
  [ ; ]
---

## Description

Returns information about a subscription to a merge publication, both push and pull. This stored procedure is executed at the Publisher on the publication database or at a republishing Subscriber on the subscription database. Transact-SQL syntax conventions must already exist and conform to the rules for merge publications and subscriptions in the current database is returned. information about all subscriptions to the given publication is returned.

## Syntax

```sql
sp_helpmergesubscription
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
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @subscription_type = ]
N
'subscription_type'
]
[ , [ @found = ] found
OUTPUT
]
[ ; ]
```
