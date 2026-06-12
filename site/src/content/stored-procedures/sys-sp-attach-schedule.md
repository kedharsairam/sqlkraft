---
name: "sys.sp_attach_schedule"
title: "sp_attach_schedule"
category: "general"
description: "The job identification number of the job to which the schedule is added. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_attach_schedule
      [ [ @job_id = ]
      'job_id'
      ]
      [ , [ @job_name = ]
      N
      'job_name'
      ]
      [ , [ @schedule_id = ] schedule_id ]
      [ , [ @schedule_name = ]
      N
      'schedule_name'
      ]
      [ , [ @automatic_post = ] automatic_post ]
      [ ; ]
---

## Description

## Syntax

```sql
sp_attach_schedule
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @schedule_id = ] schedule_id ]
[ , [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @automatic_post = ] automatic_post ]
[ ; ]
```
