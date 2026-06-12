---
name: "sys.sp_cdc_scan"
title: "sys.sp_cdc_scan"
category: "general"
description: "Executes the change data capture log scan operation. Maximum number of transactions to process in each scan cycle. Maximum number of scan cycles to execute in order to extract all rows from the log."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sys.sp_cdc_scan [ [ @maxtrans = ] max_trans ]
      [ , [ @maxscans = ] max_scans ]
      [ , [ @continuous = ] continuous ]
      [ , [ @pollinginterval = ] polling_interval ]
      [ ; ]
---

## Description

Executes the change data capture log scan operation. Maximum number of transactions to process in each scan cycle. Maximum number of scan cycles to execute in order to extract all rows from the log. Indicates whether the stored procedure should end after executing a single scan cycle ( run continuously, pausing for the time specified by Number of seconds between log scan cycles.

## Syntax

```sql
sys.sp_cdc_scan [ [ @maxtrans = ] max_trans ]
[ , [ @maxscans = ] max_scans ]
[ , [ @continuous = ] continuous ]
[ , [ @pollinginterval = ] polling_interval ]
[ ; ]
```
