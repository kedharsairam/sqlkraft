---
name: "sys.sp_dbmmonitorhelpalert"
title: "sp_dbmmonitorhelpalert"
category: "general"
description: "Returns information about warning thresholds on one or all of several key database mirroring An integer value that identifies the warning to be returned. If this argument is omitted, all the warnings are returned, but not the retention period. To return a specific warning, specify one of the following values: Specifies the number of minutes worth of transactions t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitorhelpalert
              [ @database_name = ]
              N
              'database_name'
              [ , [ @alert_id = ] alert_id ]
              [ ; ]
---

## Description

Returns information about warning thresholds on one or all of several key database mirroring An integer value that identifies the warning to be returned. If this argument is omitted, all the warnings are returned, but not the retention period.

## Syntax

```sql
sp_dbmmonitorhelpalert
[ @database_name = ]
N
'database_name'
[ , [ @alert_id = ] alert_id ]
[ ; ]
```
