---
name: "sys.sp_help_schedule"
title: "sp_help_schedule"
category: "general"
description: "Lists information about schedules. Transact-SQL syntax conventions The identifier of the schedule to list. The name of the schedule to list. Specifies whether to show only schedules that a job is attached to. , all schedules are shown. When , the result set contains only schedules that are attached to a"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_schedule
  [ [ @schedule_id = ] schedule_id ]
  [ , [ @schedule_name = ]
  N
  'schedule_name'
  ]
  [ , [ @attached_schedules_only = ] attached_schedules_only ]
  [ , [ @include_description = ] include_description ]
  [ ; ]
---

## Description

Lists information about schedules. Transact-SQL syntax conventions The identifier of the schedule to list. The name of the schedule to list. Specifies whether to show only schedules that a job is attached to. , all schedules are shown. When , the result set contains only schedules that are attached to a

## Syntax

```sql
sp_help_schedule
[ [ @schedule_id = ] schedule_id ]
[ , [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @attached_schedules_only = ] attached_schedules_only ]
[ , [ @include_description = ] include_description ]
[ ; ]
```
