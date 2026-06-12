---
name: "sys.sp_help_jobsteplog"
title: "sp_help_jobsteplog"
category: "general"
description: "Returns metadata about a specific SQL Server Agent job step log. The job identification number for which to return job step log information. must be specified, but both can't be specified. must be specified, but both can't be specified. The identification number of the step in the job."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_help_jobsteplog
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
      [ ; ]
---

## Description

Returns metadata about a specific SQL Server Agent job step log. The job identification number for which to return job step log information. must be specified, but both can't be specified. must be specified, but both can't be specified. The identification number of the step in the job.

## Syntax

```sql
sp_help_jobsteplog
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
[ ; ]
```
