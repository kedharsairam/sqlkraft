---
name: "sys.sp_dropsubscriber"
title: "sp_dropsubscriber"
category: "general"
description: "Removes the Subscriber designation from a registered server. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the Subscriber to be dropped. Identified for informational purposes only. Not supported. Future compatibility is not This stored procedure has been deprecated. You're no longer required to explicitly register a Subs"
tags: ["stored-procedure"]
pubDate: 2026-05-29
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

Removes the Subscriber designation from a registered server. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the Subscriber to be dropped. Identified for informational purposes only. Not supported. Future compatibility is not This stored procedure has been deprecated. You're no longer required to explicitly register a Subscriber at the Publisher.

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
