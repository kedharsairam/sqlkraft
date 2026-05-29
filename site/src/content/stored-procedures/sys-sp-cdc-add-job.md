---
name: 'sys.sp_cdc_add_job'
title: 'sys.sp_cdc_add_job'
category: 'general'
description: 'Creates a change data capture cleanup or capture job in the current database. Transact-SQL syntax conventions Flag indicating whether the job should be started immediately after it''s added. Maximum number of transactions to process in each scan cycle. . If specified, the value must be a positive integer. is valid only for capture jobs.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_add_job [ @job_type = ]
  N
  'job_type'
  [ , [ @start_job = ] start_job ]
  [ , [ @maxtrans = ] max_trans ]
  [ , [ @maxscans = ] max_scans ]
  [ , [ @continuous = ] continuous ]
  [ , [ @pollinginterval = ] polling_interval ]
  [ , [ @retention ] = retention ]
  [ , [ @threshold ] =
  'delete_threshold'
  ]
  [ ; ]
---

## Description

Creates a change data capture cleanup or capture job in the current database. Transact-SQL syntax conventions Flag indicating whether the job should be started immediately after it's added. Maximum number of transactions to process in each scan cycle. . If specified, the value must be a positive integer. is valid only for capture jobs.

## Syntax

```sql
sys.sp_cdc_add_job [ @job_type = ]
N
'job_type'
[ , [ @start_job = ] start_job ]
[ , [ @maxtrans = ] max_trans ]
[ , [ @maxscans = ] max_scans ]
[ , [ @continuous = ] continuous ]
[ , [ @pollinginterval = ] polling_interval ]
[ , [ @retention ] = retention ]
[ , [ @threshold ] =
'delete_threshold'
]
[ ; ]
```
