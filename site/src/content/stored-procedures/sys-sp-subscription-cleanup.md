---
name: "sys.sp_subscription_cleanup"
title: "sp_subscription_cleanup"
category: "general"
description: "Removes metadata when a subscription is dropped at a Subscriber. For a synchronizing transaction subscription, it also includes immediate-updating triggers. This stored procedure is executed at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_subscription_cleanup
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
      [ , [ @reserved = ]
      N
      'reserved'
      ]
      [ , [ @from_backup = ] from_backup ]
      [ ; ]
---

## Description

Removes metadata when a subscription is dropped at a Subscriber. For a synchronizing transaction subscription, it also includes immediate-updating triggers. This stored procedure is executed at the Subscriber on the subscription database.

## Syntax

```sql
sp_subscription_cleanup
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
[ , [ @reserved = ]
N
'reserved'
]
[ , [ @from_backup = ] from_backup ]
[ ; ]
```
