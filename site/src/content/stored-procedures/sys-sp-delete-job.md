---
name: "sys.sp_delete_job"
title: "sp_delete_job"
category: "general"
description: "Deletes a job from the SQL Server Agent service. Transact-SQL syntax conventions The identification number of the job to be deleted. must be specified; both can't be specified. The name of the job to be deleted. must be specified; both can't be specified. Identified for informational purposes only. Not supported. Future compatibility is not"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_job
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @originating_server = ]
  N
  'originating_server'
  ]
  [ , [ @delete_history = ] delete_history ]
  [ , [ @delete_unused_schedule = ] delete_unused_schedule ]
  [ ; ]
---

## Description

Deletes a job from the SQL Server Agent service. Transact-SQL syntax conventions The identification number of the job to be deleted. must be specified; both can't be specified. The name of the job to be deleted. must be specified; both can't be specified. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_delete_job
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @originating_server = ]
N
'originating_server'
]
[ , [ @delete_history = ] delete_history ]
[ , [ @delete_unused_schedule = ] delete_unused_schedule ]
[ ; ]
```

## Examples

### Example 1

`sp_delete_job`

### Example 2

`EXECUTE`

### Example 3

`msdb`

### Example 4

`sp_delete_job`

### Example 5

`NightlyBackups`

### Example 6

```sql
USE msdb;
GO
EXECUTE sp_delete_job @job_name = N
'NightlyBackups'
;
GO
```

### Example 7

```sql
USE msdb;
GO
EXECUTE dbo.sp_help_job
@job_name = N
'NightlyBackups'
,
@job_aspect = N
'ALL'
;
GO
```
