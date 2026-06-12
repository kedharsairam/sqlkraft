---
name: "sys.sp_dbmmonitordropalert"
title: "sp_dbmmonitordropalert"
category: "general"
description: "Drops the warning for a specified performance metric, by setting the threshold to Specifies the database for which to drop the specified warning threshold. An integer value that identifies the warning to be dropped. Specifies the number of minutes worth of transactions that can accumulate in the send queue before a warning is generated on the principal server instan"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitordropalert
  [ @database_name = ]
  N
  'database_name'
  [ , [ @alert_id = ] alert_id ]
  [ ; ]
---

## Description

Drops the warning for a specified performance metric, by setting the threshold to Specifies the database for which to drop the specified warning threshold. An integer value that identifies the warning to be dropped. Specifies the number of minutes worth of transactions that can accumulate in the send queue before a warning is generated on the principal server instance.

## Syntax

```sql
sp_dbmmonitordropalert
[ @database_name = ]
N
'database_name'
[ , [ @alert_id = ] alert_id ]
[ ; ]
```
