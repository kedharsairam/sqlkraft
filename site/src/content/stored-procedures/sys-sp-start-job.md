---
name: "sys.sp_start_job"
title: "sp_start_job"
category: "general"
description: "Instructs SQL Server Agent to execute a job immediately. Transact-SQL syntax conventions must be specified, but both can't be specified. The identification number of the job to start. must be specified, but both can't be specified. Identified for informational purposes only. Not supported. Future compatibility is not"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_start_job
  [ [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @job_id = ]
  'job_id'
  ]
  [ , [ @error_flag = ] error_flag ]
  [ , [ @server_name = ]
  N
  'server_name'
  ]
  [ , [ @step_name = ]
  N
  'step_name'
  ]
  [ , [ @output_flag = ] output_flag ]
  [ ; ]
---

## Description

Instructs SQL Server Agent to execute a job immediately. Transact-SQL syntax conventions must be specified, but both can't be specified. The identification number of the job to start. must be specified, but both can't be specified. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_start_job
[ [ @job_name = ]
N
'job_name'
]
[ , [ @job_id = ]
'job_id'
]
[ , [ @error_flag = ] error_flag ]
[ , [ @server_name = ]
N
'server_name'
]
[ , [ @step_name = ]
N
'step_name'
]
[ , [ @output_flag = ] output_flag ]
[ ; ]
```

## Examples

### Example 1

```sql
Weekly Sales Data Backup
```

### Example 2

```sql
USE
msdb;
GO
EXECUTE
dbo.sp_start_job N
'Weekly Sales Data Backup'
;
GO
```
