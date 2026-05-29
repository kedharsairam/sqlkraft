---
name: "sys.sp_changedynamicsnapshot_job"
title: "sp_changedynamicsnapshot_job"
category: "general"
description: "Modifies the agent job that generates the snapshot for a subscription to a publication with a parameterized row filter. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changedynamicsnapshot_job
  [ @publication = ]
  N
  'publication'
  [ , [ @dynamic_snapshot_jobname = ]
  N
  'dynamic_snapshot_jobname'
  ]
  [ , [ @dynamic_snapshot_jobid = ]
  'dynamic_snapshot_jobid'
  ]
  [ , [ @frequency_type = ] frequency_type ]
  [ , [ @frequency_interval = ] frequency_interval ]
  [ , [ @frequency_subday = ] frequency_subday ]
  [ , [ @frequency_subday_interval = ] frequency_subday_interval ]
  [ , [ @frequency_relative_interval = ] frequency_relative_interval ]
  [ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
  [ , [ @active_start_date = ] active_start_date ]
  [ , [ @active_end_date = ] active_end_date ]
  [ , [ @active_start_time_of_day = ] active_start_time_of_day ]
  [ , [ @active_end_time_of_day = ] active_end_time_of_day ]
  [ , [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ ; ]
---

## Description

Modifies the agent job that generates the snapshot for a subscription to a publication with a parameterized row filter. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions

## Syntax

```sql
sp_changedynamicsnapshot_job
[ @publication = ]
N
'publication'
[ , [ @dynamic_snapshot_jobname = ]
N
'dynamic_snapshot_jobname'
]
[ , [ @dynamic_snapshot_jobid = ]
'dynamic_snapshot_jobid'
]
[ , [ @frequency_type = ] frequency_type ]
[ , [ @frequency_interval = ] frequency_interval ]
[ , [ @frequency_subday = ] frequency_subday ]
[ , [ @frequency_subday_interval = ] frequency_subday_interval ]
[ , [ @frequency_relative_interval = ] frequency_relative_interval ]
[ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
[ , [ @active_start_date = ] active_start_date ]
[ , [ @active_end_date = ] active_end_date ]
[ , [ @active_start_time_of_day = ] active_start_time_of_day ]
[ , [ @active_end_time_of_day = ] active_end_time_of_day ]
[ , [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ ; ]
```
