---
name: "sys.sp_reinitmergepullsubscription"
title: "sp_reinitmergepullsubscription"
category: "general"
description: "Marks a merge pull subscription for reinitialization the next time the Merge Agent runs. This stored procedure is executed at the Subscriber in the subscription database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_reinitmergepullsubscription
              [ [ @publisher = ]
              N
              'publisher'
              ]
              [ , [ @publisher_db = ]
              N
              'publisher_db'
              ]
              [ , [ @publication = ]
              N
              'publication'
              ]
              [ , [ @upload_first = ]
              N
              'upload_first'
              ]
              [ ; ]
---

## Description

Marks a merge pull subscription for reinitialization the next time the Merge Agent runs. This stored procedure is executed at the Subscriber in the subscription database.

## Syntax

```sql
sp_reinitmergepullsubscription
[ [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @publication = ]
N
'publication'
]
[ , [ @upload_first = ]
N
'upload_first'
]
[ ; ]
```

## Permissions

SQL Only members of the fixed server role or the fixed database role can execute. Reinitialize a Subscription Reinitialize Subscriptions System stored procedures (Transact-SQL)
