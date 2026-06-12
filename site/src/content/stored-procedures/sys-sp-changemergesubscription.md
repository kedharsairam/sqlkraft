---
name: "sys.sp_changemergesubscription"
title: "sp_changemergesubscription"
category: "general"
description: "Changes selected properties of a merge push subscription. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_changemergesubscription
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
      [ , [ @property = ]
      N
      'property'
      ]
      [ , [ @value = ]
      N
      'value'
      ]
      [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
      [ ; ]
---

## Description

Changes selected properties of a merge push subscription. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_changemergesubscription
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
[ , [ @property = ]
N
'property'
]
[ , [ @value = ]
N
'value'
]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. sp_addmergesubscription (Transact-SQL) sp_dropmergesubscription (Transact-SQL) sp_helpmergesubscription (Transact-SQL) System stored procedures (Transact-SQL)
