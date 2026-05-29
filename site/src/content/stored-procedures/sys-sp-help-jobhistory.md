---
name: 'sys.sp_help_jobhistory'
title: 'sp_help_jobhistory'
category: 'general'
description: 'Provides information about the jobs for servers in the multiserver administration domain. Transact-SQL syntax conventions The job identification number.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_jobhistory
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @step_id = ] step_id ]
  [ , [ @sql_message_id = ] sql_message_id ]
  [ , [ @sql_severity = ] sql_severity ]
  [ , [ @start_run_date = ] start_run_date ]
  [ , [ @end_run_date = ] end_run_date ]
  [ , [ @start_run_time = ] start_run_time ]
  [ , [ @end_run_time = ] end_run_time ]
  [ , [ @minimum_run_duration = ] minimum_run_duration ]
  [ , [ @run_status = ] run_status ]
  [ , [ @minimum_retries = ] minimum_retries ]
  [ , [ @oldest_first = ] oldest_first ]
  [ , [ @server = ]
  N
  'server'
  ]
  [ , [ @mode = ]
  'mode'
  ]
  [ ; ]
---

## Description

Provides information about the jobs for servers in the multiserver administration domain. Transact-SQL syntax conventions The job identification number.

## Syntax

```sql
sp_help_jobhistory
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @step_id = ] step_id ]
[ , [ @sql_message_id = ] sql_message_id ]
[ , [ @sql_severity = ] sql_severity ]
[ , [ @start_run_date = ] start_run_date ]
[ , [ @end_run_date = ] end_run_date ]
[ , [ @start_run_time = ] start_run_time ]
[ , [ @end_run_time = ] end_run_time ]
[ , [ @minimum_run_duration = ] minimum_run_duration ]
[ , [ @run_status = ] run_status ]
[ , [ @minimum_retries = ] minimum_retries ]
[ , [ @oldest_first = ] oldest_first ]
[ , [ @server = ]
N
'server'
]
[ , [ @mode = ]
'mode'
]
[ ; ]
```
