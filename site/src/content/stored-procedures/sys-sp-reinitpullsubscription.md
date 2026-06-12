---
name: "sys.sp_reinitpullsubscription"
title: "sp_reinitpullsubscription"
category: "general"
description: "Marks a transactional pull or anonymous subscription for reinitialization the next time the Distribution Agent runs. This stored procedure is executed at the Subscriber on the pull The name of the Publisher database. subscriptions for reinitialization."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_reinitpullsubscription
      [ @publisher = ]
      N
      'publisher'
      [ , [ @publisher_db = ]
      N
      'publisher_db'
      ]
      [ , [ @publication = ]
      N
      'publication'
      ]
      [ ; ]
---

## Description

Marks a transactional pull or anonymous subscription for reinitialization the next time the Distribution Agent runs. This stored procedure is executed at the Subscriber on the pull The name of the Publisher database. subscriptions for reinitialization.

## Syntax

```sql
sp_reinitpullsubscription
[ @publisher = ]
N
'publisher'
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @publication = ]
N
'publication'
]
[ ; ]
```

## Permissions

is used in transactional replication. isn't supported for peer-to-peer transactional replication. can be called from the Subscriber to reinitialize the subscription, during the next run of the Distribution Agent. Subscriptions to publications created with a value of for @immediate_sync can't be reinitialized from the Subscriber. You can reinitialize a pull subscription by either executing at the Subscriber or at the Publisher. SQL Only members of the fixed server role or the fixed database role can execute.
