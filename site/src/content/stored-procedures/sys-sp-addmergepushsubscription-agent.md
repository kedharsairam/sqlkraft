---
name: "sys.sp_addmergepushsubscription_agent"
title: "sp_addmergepushsubscription_agent"
category: "general"
description: "Adds a new agent job used to schedule synchronization of a push subscription to a merge publication. This stored procedure is executed at the Publisher on the publication database. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergepushsubscription_agent
  [ @publication = ]
  N
  'publication'
  [ , [ @subscriber = ]
  N
  'subscriber'
  ]
  [ , [ @subscriber_db = ]
  N
  'subscriber_db'
  ]
  [ , [ @subscriber_security_mode = ] subscriber_security_mode ]
  [ , [ @subscriber_login = ]
  N
  'subscriber_login'
  ]
  [ , [ @subscriber_password = ]
  N
  'subscriber_password'
  ]
  [ , [ @publisher_security_mode = ] publisher_security_mode ]
  [ , [ @publisher_login = ]
  N
  'publisher_login'
  ]
  [ , [ @publisher_password = ]
  N
  'publisher_password'
  ]
  [ , [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @frequency_type = ] frequency_type ]
  [ , [ @frequency_interval = ] frequency_interval ]
  [ , [ @frequency_relative_interval = ] frequency_relative_interval ]
---

## Description

Adds a new agent job used to schedule synchronization of a push subscription to a merge publication. This stored procedure is executed at the Publisher on the publication database. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor

## Syntax

```sql
sp_addmergepushsubscription_agent
[ @publication = ]
N
'publication'
[ , [ @subscriber = ]
N
'subscriber'
]
[ , [ @subscriber_db = ]
N
'subscriber_db'
]
[ , [ @subscriber_security_mode = ] subscriber_security_mode ]
[ , [ @subscriber_login = ]
N
'subscriber_login'
]
[ , [ @subscriber_password = ]
N
'subscriber_password'
]
[ , [ @publisher_security_mode = ] publisher_security_mode ]
[ , [ @publisher_login = ]
N
'publisher_login'
]
[ , [ @publisher_password = ]
N
'publisher_password'
]
[ , [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @frequency_type = ] frequency_type ]
[ , [ @frequency_interval = ] frequency_interval ]
[ , [ @frequency_relative_interval = ] frequency_relative_interval ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Create a push subscription Subscribe to Publications sp_addmergesubscription (Transact-SQL) sp_changemergesubscription (Transact-SQL) sp_dropmergesubscription (Transact-SQL) sp_helpmergesubscription (Transact-SQL)
