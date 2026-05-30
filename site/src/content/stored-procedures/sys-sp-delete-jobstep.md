---
name: "sys.sp_delete_jobstep"
title: "sp_delete_jobstep"
category: "general"
description: "Removes a job step from a job in the SQL Server Agent service. Transact-SQL syntax conventions The identification number of the job from which the step will be removed. must be specified; both can't be specified. The name of the job from which the step will be removed. must be specified; both can't be specified. The identification number of the step being removed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_jobstep
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  , [ @step_id = ] step_id
  [ ; ]
---

## Description

Removes a job step from a job in the SQL Server Agent service. Transact-SQL syntax conventions The identification number of the job from which the step will be removed. must be specified; both can't be specified. The name of the job from which the step will be removed. must be specified; both can't be specified. The identification number of the step being removed.

## Syntax

```sql
sp_delete_jobstep
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
, [ @step_id = ] step_id
[ ; ]
```
