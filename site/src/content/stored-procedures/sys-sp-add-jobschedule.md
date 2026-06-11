---
name: "sys.sp_add_jobschedule"
title: "sp_add_jobschedule"
category: "general"
description: "Creates a schedule for a SQL Server Agent job."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_jobschedule
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  , [ @name = ]
  N
  'name'
  [ , [ @enabled = ] enabled ]
  [ , [ @freq_type = ] freq_type ]
  [ , [ @freq_interval = ] freq_interval ]
  [ , [ @freq_subday_type = ] freq_subday_type ]
  [ , [ @freq_subday_interval = ] freq_subday_interval ]
  [ , [ @freq_relative_interval = ] freq_relative_interval ]
  [ , [ @freq_recurrence_factor = ] freq_recurrence_factor ]
  [ , [ @active_start_date = ] active_start_date ]
  [ , [ @active_end_date = ] active_end_date ]
  [ , [ @active_start_time = ] active_start_time ]
  [ , [ @active_end_time = ] active_end_time ]
  [ , [ @schedule_id = ] schedule_id
  OUTPUT
  ]
  [ , [ @automatic_post = ] automatic_post ]
  [ , [ @schedule_uid = ]
  'schedule_uid'
  OUTPUT
  ]
  [ ; ]
---

## Description

Creates a schedule for a SQL Server Agent job. Transact-SQL syntax conventions , most, but not all SQL Server Agent features are

## Syntax

```sql
sp_add_jobschedule
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
, [ @name = ]
N
'name'
[ , [ @enabled = ] enabled ]
[ , [ @freq_type = ] freq_type ]
[ , [ @freq_interval = ] freq_interval ]
[ , [ @freq_subday_type = ] freq_subday_type ]
[ , [ @freq_subday_interval = ] freq_subday_interval ]
[ , [ @freq_relative_interval = ] freq_relative_interval ]
[ , [ @freq_recurrence_factor = ] freq_recurrence_factor ]
[ , [ @active_start_date = ] active_start_date ]
[ , [ @active_end_date = ] active_end_date ]
[ , [ @active_start_time = ] active_start_time ]
[ , [ @active_end_time = ] active_end_time ]
[ , [ @schedule_id = ] schedule_id
OUTPUT
]
[ , [ @automatic_post = ] automatic_post ]
[ , [ @schedule_uid = ]
'schedule_uid'
OUTPUT
]
[ ; ]
```
