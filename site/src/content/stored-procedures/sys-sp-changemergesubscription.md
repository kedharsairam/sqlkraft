---
name: 'sys.sp_changemergesubscription'
title: 'sp_changemergesubscription'
category: 'general'
description: 'Changes selected properties of a merge push subscription. This stored procedure is executed at the Publisher on the publication database. The name of the publication to change. publication must already exist and must conform to the rules for identifiers. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encry'
tags: ["stored-procedure"]
pubDate: 2026-05-29
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

Changes selected properties of a merge push subscription. This stored procedure is executed at the Publisher on the publication database. The name of the publication to change. publication must already exist and must conform to the rules for identifiers. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor

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

Only members of the fixed server role or fixed database role can execute . sp_addmergesubscription (Transact-SQL) sp_dropmergesubscription (Transact-SQL) sp_helpmergesubscription (Transact-SQL) System stored procedures (Transact-SQL) Related content Subscribe to Publications sp_changemergesubscription (Transact-SQL) sp_dropmergesubscription (Transact-SQL) sp_helpmergesubscription (Transact-SQL) sp_changemergesubscription (Transact-SQL) sp_dropmergesubscription (Transact-SQL) System stored procedures (Transact-SQL)
