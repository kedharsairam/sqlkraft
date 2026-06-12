---
name: "sys.sp_helpmergepullsubscription"
title: "sp_helpmergepullsubscription"
category: "general"
description: "Returns information about pull subscriptions that exist at a Subscriber. This stored procedure is executed at the Subscriber on the subscription database. information about all merge publications and subscriptions in the current database is returned."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergepullsubscription
  [ [ @publication = ]
  N
  'publication'
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
  [ ; ]
---

## Description

Returns information about pull subscriptions that exist at a Subscriber. This stored procedure is executed at the Subscriber on the subscription database. information about all merge publications and subscriptions in the current database is returned.

## Syntax

```sql
sp_helpmergepullsubscription
[ [ @publication = ]
N
'publication'
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
[ ; ]
```

## Permissions

is used in merge replication. In the result set, the date returned in is formatted as. Only members of the fixed server role and the fixed database role can execute. sp_addmergepullsubscription (Transact-SQL) sp_changemergepullsubscription (Transact-SQL) sp_dropmergepullsubscription (Transact-SQL) Replication stored procedures (Transact-SQL)
