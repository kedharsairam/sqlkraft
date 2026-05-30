---
name: "sys.sp_add_jobstep"
title: "sp_add_jobstep"
category: "general"
description: "Adds a step (operation) to a SQL Server Agent job. Transact-SQL syntax conventions , most, but not all SQL Server Agent job types are"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_jobstep
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @step_id = ] step_id ]
  , [ @step_name = ]
  N
  'step_name'
  [ , [ @subsystem = ]
  N
  'subsystem'
  ]
  [ , [ @command = ]
  N
  'command'
  ]
  [ , [ @additional_parameters = ]
  N
  'additional_parameters'
  ]
  [ , [ @cmdexec_success_code = ] cmdexec_success_code ]
  [ , [ @on_success_action = ] on_success_action ]
  [ , [ @on_success_step_id = ] on_success_step_id ]
  [ , [ @on_fail_action = ] on_fail_action ]
  [ , [ @on_fail_step_id = ] on_fail_step_id ]
  [ , [ @server = ]
  N
  'server'
  ]
  [ , [ @database_name = ]
  N
  'database_name'
  ]
  [ , [ @database_user_name = ]
  N
  'database_user_name'
  ]
  [ , [ @retry_attempts = ] retry_attempts ]
  [ , [ @retry_interval = ] retry_interval ]
  [ , [ @os_run_priority = ] os_run_priority ]
  [ , [ @output_file_name = ]
  N
  'output_file_name'
  ]
  [ , [ @flags = ] flags ]
  [ , [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ , [ @step_uid = ]
  'step_uid'
  OUTPUT
  ]
  [ ; ]
---

## Description

Adds a step (operation) to a SQL Server Agent job. Transact-SQL syntax conventions , most, but not all SQL Server Agent job types are

## Syntax

```sql
sp_add_jobstep
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @step_id = ] step_id ]
, [ @step_name = ]
N
'step_name'
[ , [ @subsystem = ]
N
'subsystem'
]
[ , [ @command = ]
N
'command'
]
[ , [ @additional_parameters = ]
N
'additional_parameters'
]
[ , [ @cmdexec_success_code = ] cmdexec_success_code ]
[ , [ @on_success_action = ] on_success_action ]
[ , [ @on_success_step_id = ] on_success_step_id ]
[ , [ @on_fail_action = ] on_fail_action ]
[ , [ @on_fail_step_id = ] on_fail_step_id ]
[ , [ @server = ]
N
'server'
]
[ , [ @database_name = ]
N
'database_name'
]
[ , [ @database_user_name = ]
N
'database_user_name'
]
[ , [ @retry_attempts = ] retry_attempts ]
[ , [ @retry_interval = ] retry_interval ]
[ , [ @os_run_priority = ] os_run_priority ]
[ , [ @output_file_name = ]
N
'output_file_name'
]
[ , [ @flags = ] flags ]
[ , [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ , [ @step_uid = ]
'step_uid'
OUTPUT
]
[ ; ]
```

## Examples

### Example 1

```sql
Weekly Sales Data Backup
```

### Example 2

```sql
USE msdb;
GO
EXECUTE sp_add_jobstep
@job_name = N
'Weekly Sales Data Backup'
,
@step_name = N
'Set database to read only'
,
@subsystem = N
'TSQL'
,
@command = N
'ALTER DATABASE SALES SET READ_ONLY'
,
@retry_attempts = 5,
@retry_interval = 5;
GO
```
