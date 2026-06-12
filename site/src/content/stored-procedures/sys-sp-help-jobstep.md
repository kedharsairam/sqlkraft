---
name: "sys.sp_help_jobstep"
title: "sp_help_jobstep"
category: "general"
description: "Returns information for the steps in a job used by SQL Server Agent service to perform The job identification number for which to return job information. must be specified, but both can't be specified. must be specified, but both can't be specified. The identification number of the step in the job."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_jobstep
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
  [ , [ @suffix = ] suffix ]
  [ ; ]
---

## Description

Returns information for the steps in a job used by SQL Server Agent service to perform The job identification number for which to return job information. must be specified, but both can't be specified. must be specified, but both can't be specified. The identification number of the step in the job.

## Syntax

```sql
sp_help_jobstep
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
[ , [ @suffix = ] suffix ]
[ ; ]
```
