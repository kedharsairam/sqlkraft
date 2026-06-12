---
name: "sys.sp_reinitmergesubscription"
title: "sp_reinitmergesubscription"
category: "general"
description: "Marks a merge subscription for reinitialization the next time the Merge Agent runs. This stored procedure is executed at the Publisher in the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_reinitmergesubscription
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
              [ , [ @upload_first = ]
              N
              'upload_first'
              ]
              [ ; ]
---

## Description

Marks a merge subscription for reinitialization the next time the Merge Agent runs. This stored procedure is executed at the Publisher in the publication database.

## Syntax

```sql
sp_reinitmergesubscription
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
[ , [ @upload_first = ]
N
'upload_first'
]
[ ; ]
```

## Permissions

SQL Only members of the fixed server role or the fixed database role can execute. Reinitialize Subscriptions System stored procedures (Transact-SQL)
