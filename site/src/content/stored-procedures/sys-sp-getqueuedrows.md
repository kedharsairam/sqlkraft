---
name: "sys.sp_getqueuedrows"
title: "sp_getqueuedrows"
category: "general"
description: "Retrieves rows at the Subscriber that have updates pending in the queue. This stored procedure is executed at the Subscriber on the subscription database. , with no default. The table must be a part of a Allows the output to be filtered by the transaction ID. If specified, the transaction ID associated with the queued command is displayed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_getqueuedrows
              [ @tablename = ]
              N
              'tablename'
              [ , [ @owner = ]
              N
              'owner'
              ]
              [ , [ @tranid = ]
              N
              'tranid'
              ]
              [ ; ]
---

## Description

Retrieves rows at the Subscriber that have updates pending in the queue. This stored procedure is executed at the Subscriber on the subscription database. , with no default. The table must be a part of a Allows the output to be filtered by the transaction ID. If specified, the transaction ID associated with the queued command is displayed. If , all the commands in the queue are displayed.

## Syntax

```sql
sp_getqueuedrows
[ @tablename = ]
N
'tablename'
[ , [ @owner = ]
N
'owner'
]
[ , [ @tranid = ]
N
'tranid'
]
[ ; ]
```
