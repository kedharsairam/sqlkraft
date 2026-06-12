---
name: "sys.sp_dropsubscriber"
title: "sp_dropsubscriber"
category: "general"
description: "Removes the Subscriber designation from a registered server. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_dropsubscriber
      [ @subscriber = ]
      N
      'subscriber'
      [ , [ @reserved = ]
      N
      'reserved'
      ]
      [ , [ @ignore_distributor = ] ignore_distributor ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ ; ]
---

## Description

Removes the Subscriber designation from a registered server. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_dropsubscriber
[ @subscriber = ]
N
'subscriber'
[ , [ @reserved = ]
N
'reserved'
]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
