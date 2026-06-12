---
name: "sys.sp_addmergepullsubscription"
title: "sp_addmergepullsubscription"
category: "general"
description: "Adds a pull subscription to a merge publication. This stored procedure is executed at the Subscriber on the subscription database. , with a default of the local server name. The Publisher must be a valid server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergepullsubscription
              [ @publication = ]
              N
              'publication'
              [ , [ @publisher = ]
              N
              'publisher'
              ]
              [ , [ @publisher_db = ]
              N
              'publisher_db'
              ]
              [ , [ @subscriber_type = ]
              N
              'subscriber_type'
              ]
              [ , [ @subscription_priority = ] subscription_priority ]
              [ , [ @sync_type = ]
              N
              'sync_type'
              ]
              [ , [ @description = ]
              N
              'description'
              ]
              [ ; ]
---

## Description

Adds a pull subscription to a merge publication. This stored procedure is executed at the Subscriber on the subscription database. , with a default of the local server name. The Publisher must be a valid server.

## Syntax

```sql
sp_addmergepullsubscription
[ @publication = ]
N
'publication'
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @subscriber_type = ]
N
'subscriber_type'
]
[ , [ @subscription_priority = ] subscription_priority ]
[ , [ @sync_type = ]
N
'sync_type'
]
[ , [ @description = ]
N
'description'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Create a Pull Subscription Subscribe to Publications sp_addmergepullsubscription_agent (Transact-SQL) sp_changemergepullsubscription (Transact-SQL)
