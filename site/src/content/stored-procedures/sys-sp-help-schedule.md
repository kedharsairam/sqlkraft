---
name: "sys.sp_help_schedule"
title: "sp_help_schedule"
category: "general"
description: "Lists information about schedules. The identifier of the schedule to list."
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

Lists information about schedules. The identifier of the schedule to list.

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
