---
name: "sys.sp_delete_jobsteplog"
title: "sp_delete_jobsteplog"
category: "general"
description: "Removes all SQL Server Agent job step logs that are specified with the arguments. Use this stored procedure to maintain the The job identification number for the job that contains the job step log to be removed. must be specified, but both can't be specified. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_jobsteplog
              [ [ @job_id = ]
              'job_id'
              ]
              [ , [ @job_name = ]
              N
              'job_name'
              ]
              [ , [ @step_id = ] step_id ]
              [ , [ @step_name = ]
              N
              'step_name'
              ]
              [ , [ @older_than = ] older_than ]
              [ , [ @larger_than = ] larger_than ]
              [ ; ]
---

## Description

Removes all SQL Server Agent job step logs that are specified with the arguments. Use this stored procedure to maintain the The job identification number for the job that contains the job step log to be removed. must be specified, but both can't be specified. must be specified, but both can't be specified.

## Syntax

```sql
sp_delete_jobsteplog
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @step_id = ] step_id ]
[ , [ @step_name = ]
N
'step_name'
]
[ , [ @older_than = ] older_than ]
[ , [ @larger_than = ] larger_than ]
[ ; ]
```
