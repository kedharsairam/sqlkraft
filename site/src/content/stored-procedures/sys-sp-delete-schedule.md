---
name: "sys.sp_delete_schedule"
title: "sp_delete_schedule"
category: "general"
description: "Transact-SQL syntax conventions The schedule identification number of the schedule to delete. must be specified, but both can't be specified. The name of the schedule to delete. must be specified, but both can't be specified. Specifies whether the procedure should fail if the schedule is attached to a job. , the stored procedure fails if the schedule is attached to a job."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_schedule
  [ [ @schedule_id = ] schedule_id ]
  [ , [ @schedule_name = ]
  N
  'schedule_name'
  ]
  [ , [ @force_delete = ] force_delete ]
  [ , [ @automatic_post = ] automatic_post ]
  [ ; ]
---

## Description

Transact-SQL syntax conventions The schedule identification number of the schedule to delete. must be specified, but both can't be specified. The name of the schedule to delete. must be specified, but both can't be specified. Specifies whether the procedure should fail if the schedule is attached to a job. , the stored procedure fails if the schedule is attached to a job.

## Syntax

```sql
sp_delete_schedule
[ [ @schedule_id = ] schedule_id ]
[ , [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @force_delete = ] force_delete ]
[ , [ @automatic_post = ] automatic_post ]
[ ; ]
```
