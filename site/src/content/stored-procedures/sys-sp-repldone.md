---
name: "sys.sp_repldone"
title: "sp_repldone"
category: "general"
description: "Updates the record that identifies the last distributed transaction of the server. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The log sequence number (LSN) of the first record for the last distributed transaction of the manually, you can invalidate the order and consistency of delivered transactions. You should only use for troub"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_repldone [ @xactid = ] xactid
  , [ @xact_seqno = ] xact_seqno
  [ , [ @numtrans = ] numtrans ]
  [ , [ @time = ] time ]
  [ , [ @reset = ] reset ]
  [ ; ]
---

## Description

Updates the record that identifies the last distributed transaction of the server. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The log sequence number (LSN) of the first record for the last distributed transaction of the manually, you can invalidate the order and consistency of delivered transactions. You should only use for troubleshooting replication as

## Syntax

```sql
sp_repldone [ @xactid = ] xactid
, [ @xact_seqno = ] xact_seqno
[ , [ @numtrans = ] numtrans ]
[ , [ @time = ] time ]
[ , [ @reset = ] reset ]
[ ; ]
```
