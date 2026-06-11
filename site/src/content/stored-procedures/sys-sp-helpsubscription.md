---
name: "sys.sp_helpsubscription"
title: "sp_helpsubscription"
category: "general"
description: "Lists subscription information associated with a particular publication, article, Subscriber, or set of subscriptions. This stored procedure is executed at a Publisher on the publication database. Transact-SQL syntax conventions The name of the associated publication. returns all subscription information for this server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpsubscription
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @article = ]
  N
  'article'
  ]
  [ , [ @subscriber = ]
  N
  'subscriber'
  ]
  [ , [ @destination_db = ]
  N
  'destination_db'
  ]
  [ , [ @found = ] found
  OUTPUT
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Lists subscription information associated with a particular publication, article, Subscriber, or set of subscriptions. This stored procedure is executed at a Publisher on the publication database. Transact-SQL syntax conventions The name of the associated publication. returns all subscription information for this server. , which returns all subscription information for the selected publications and Subscribers. If

## Syntax

```sql
sp_helpsubscription
[ [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
]
[ , [ @subscriber = ]
N
'subscriber'
]
[ , [ @destination_db = ]
N
'destination_db'
]
[ , [ @found = ] found
OUTPUT
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

is used in snapshot and transactional replication. Execute permissions default to the role. Users are only returned information for subscriptions that they created. Information on all subscriptions is returned to members of the fixed server role at the Publisher or members of the fixed database role on the publication database. sp_addsubscription (Transact-SQL) sp_changesubstatus (Transact-SQL) sp_dropsubscription (Transact-SQL) System stored procedures (Transact-SQL) Related content
