---
name: "sys.sp_dropmergepullsubscription"
title: "sp_dropmergepullsubscription"
category: "general"
description: "Drops a merge pull subscription. This stored procedure is executed at the Subscriber on the Transact-SQL syntax conventions to remove subscriptions to all publications."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmergepullsubscription
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
  [ , [ @reserved = ] reserved ]
  [ ; ]
---

## Description

Drops a merge pull subscription. This stored procedure is executed at the Subscriber on the Transact-SQL syntax conventions to remove subscriptions to all publications. The name of the Publisher database.

## Syntax

```sql
sp_dropmergepullsubscription
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
[ , [ @reserved = ] reserved ]
[ ; ]
```
