---
name: "sys.sp_help_jobs_in_schedule"
title: "sp_help_jobs_in_schedule"
category: "general"
description: "Returns information about the jobs that a particular schedule is attached to. The identifier of the schedule to list information for."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_help_jobs_in_schedule
      [ [ @schedule_name = ]
      N
      'schedule_name'
      ]
      [ , [ @schedule_id = ] schedule_id ]
      [ ; ]
---

## Description

Returns information about the jobs that a particular schedule is attached to. The identifier of the schedule to list information for.

## Syntax

```sql
sp_help_jobs_in_schedule
[ [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @schedule_id = ] schedule_id ]
[ ; ]
```
