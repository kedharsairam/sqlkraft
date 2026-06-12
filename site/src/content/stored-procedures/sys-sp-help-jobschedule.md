---
name: "sys.sp_help_jobschedule"
title: "sp_help_jobschedule"
category: "general"
description: "Returns information about the scheduling of jobs used by SQL Server Management Studio to The job identification number. must be specified, but both can't be specified. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_help_jobschedule
      [ [ @job_id = ]
      'job_id'
      ]
      [ , [ @job_name = ]
      N
      'job_name'
      ]
      [ , [ @schedule_name = ]
      N
      'schedule_name'
      ]
      [ , [ @schedule_id = ] schedule_id ]
      [ , [ @include_description = ] include_description ]
      [ ; ]
---

## Description

Returns information about the scheduling of jobs used by SQL Server Management Studio to The job identification number. must be specified, but both can't be specified. must be specified, but both can't be specified.

## Syntax

```sql
sp_help_jobschedule
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @schedule_id = ] schedule_id ]
[ , [ @include_description = ] include_description ]
[ ; ]
```
