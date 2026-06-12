---
name: "sys.sp_dbmmonitorchangealert"
title: "sp_dbmmonitorchangealert"
category: "general"
description: "Adds or changes warning threshold for a specified mirroring performance metric. Specifies the database for which to add or change the specified warning threshold. An integer value that identifies the warning to be added or changed."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_dbmmonitorchangealert
      [ @database_name = ]
      N
      'database_name'
      , [ @alert_id = ] alert_id
      , [ @threshold = ] threshold
      [ , [ @enabled = ] enabled ]
      [ ; ]
---

## Description

Adds or changes warning threshold for a specified mirroring performance metric. Specifies the database for which to add or change the specified warning threshold. An integer value that identifies the warning to be added or changed. be one of the following values: Specifies the number of minutes worth of transactions that can accumulate in the send queue before a warning is generated on the principal server instance.

## Syntax

```sql
sp_dbmmonitorchangealert
[ @database_name = ]
N
'database_name'
, [ @alert_id = ] alert_id
, [ @threshold = ] threshold
[ , [ @enabled = ] enabled ]
[ ; ]
```
