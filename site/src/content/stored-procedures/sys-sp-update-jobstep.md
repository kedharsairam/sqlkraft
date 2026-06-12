---
name: "sys.sp_update_jobstep"
title: "sp_update_jobstep"
category: "general"
description: "Changes the setting for a step in a job that is used to perform automated activities in the SQL The identification number of the job to which the step belongs."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_update_jobstep
      [ [ @job_id = ]
      'job_id'
      ]
      [ , [ @job_name = ]
      N
      'job_name'
      ]
      , [ @step_id = ] step_id
      [ , [ @step_name = ]
      N
      'step_name'
      ]
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
      [ ; ]
---

## Description

Changes the setting for a step in a job that is used to perform automated activities in the SQL The identification number of the job to which the step belongs.

## Syntax

```sql
sp_update_jobstep
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
, [ @step_id = ] step_id
[ , [ @step_name = ]
N
'step_name'
]
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
[ ; ]
```

## Examples

### Example 1

`sp_update_jobstep`

### Example 2

`EXECUTE`

### Example 3

`msdb`

### Example 4

```sql
Weekly
Sales Data Backup
```

### Example 5

```sql
10
```

### Example 6

```sql
USE msdb;
GO
EXECUTE dbo.sp_update_jobstep
@job_name = N
'Weekly Sales Data Backup'
,
@step_id = 1,
@retry_attempts = 10;
GO
```
