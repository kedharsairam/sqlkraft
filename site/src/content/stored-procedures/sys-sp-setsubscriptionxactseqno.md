---
name: "sys.sp_setsubscriptionxactseqno"
title: "sp_setsubscriptionxactseqno"
category: "general"
description: "Used during troubleshooting to specify the last delivered transaction using the log sequence number (LSN), allowing the Distribution Agent to begin delivering at the next transaction. After it restarts, the Distribution Agent returns transactions greater than this watermark (LSN) from the Distribution database cache (msrepl_commands)."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_setsubscriptionxactseqno
              [ @publisher = ]
              N
              'publisher'
              , [ @publisher_db = ]
              N
              'publisher_db'
              , [ @publication = ]
              N
              'publication'
              , [ @xact_seqno = ] xact_seqno
              [ ; ]
---

## Description

Used during troubleshooting to specify the last delivered transaction using the log sequence number (LSN), allowing the Distribution Agent to begin delivering at the next transaction. After it restarts, the Distribution Agent returns transactions greater than this watermark (LSN) from the Distribution database cache (msrepl_commands). This stored procedure is executed at the Subscriber on the subscription database. Not supported for non-SQL Server Subscribers.

## Syntax

```sql
sp_setsubscriptionxactseqno
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @xact_seqno = ] xact_seqno
[ ; ]
```

## Permissions

Specify a value of for @xact_seqno to deliver all pending commands in the distribution database to the Subscriber. might fail if the Distribution Agent uses multi-subscription streams. When this error occurs, you must run the Distribution Agent with a single subscription stream. For more information, see Replication Distribution Agent. Only members of the fixed server role or fixed database role can execute.
