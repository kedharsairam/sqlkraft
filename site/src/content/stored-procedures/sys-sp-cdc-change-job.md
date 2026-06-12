---
name: "sys.sp_cdc_change_job"
title: "sys.sp_cdc_change_job"
category: "general"
description: "Modifies the configuration of a change data capture cleanup or capture job in the current database. To view the current configuration of a job, query the Maximum number of transactions to process in each scan cycle. , which indicates no change for this parameter. If specified, the value must be a is valid only for capture jobs."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_change_job [ [ @job_type = ]
  N
  'job_type'
  ]
  [ , [ @maxtrans = ] max_trans ]
  [ , [ @maxscans = ] max_scans ]
  [ , [ @continuous = ] continuous ]
  [ , [ @pollinginterval = ] polling_interval ]
  [ , [ @retention ] = retention ]
  [ @threshold = ]
  'delete threshold'
  [ ; ]
---

## Description

Modifies the configuration of a change data capture cleanup or capture job in the current database. To view the current configuration of a job, query the Maximum number of transactions to process in each scan cycle. , which indicates no change for this parameter. If specified, the value must be a is valid only for capture jobs.

## Syntax

```sql
sys.sp_cdc_change_job [ [ @job_type = ]
N
'job_type'
]
[ , [ @maxtrans = ] max_trans ]
[ , [ @maxscans = ] max_scans ]
[ , [ @continuous = ] continuous ]
[ , [ @pollinginterval = ] polling_interval ]
[ , [ @retention ] = retention ]
[ @threshold = ]
'delete threshold'
[ ; ]
```
