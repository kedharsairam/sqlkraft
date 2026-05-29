---
name: 'sys.sp_add_schedule'
title: 'sp_add_schedule'
category: 'general'
description: 'Creates a schedule that can be used by any number of jobs. Transact-SQL syntax conventions Indicates the current status of the schedule. , the schedule isn''t enabled. When the schedule isn''t enabled, no jobs run on this schedule.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_schedule
  [ @schedule_name = ]
  'schedule_name'
  [ , [ @enabled = ] enabled ]
  [ , [ @freq_type = ] freq_type ]
  [ , [ @freq_interval = ] freq_interval ]
  [ , [ @freq_subday_type = ] freq_subday_type ]
  [ , [ @freq_subday_interval = ] freq_subday_interval ]
  [ , [ @freq_relative_interval = ] freq_relative_interval ]
  [ , [ @freq_recurrence_factor = ] freq_recurrence_factor ]
  [ , [ @active_start_date = ] active_start_date ]
  [ , [ @active_end_date = ] active_end_date ]
  [ , [ @active_start_time = ] active_start_time ]
  [ , [ @active_end_time = ] active_end_time ]
  [ , [ @owner_login_name = ]
  'owner_login_name'
  ]
  [ , [ @schedule_uid = ] schedule_uid
  OUTPUT
  ]
  [ , [ @schedule_id = ] schedule_id
  OUTPUT
  ]
  [ , [ @originating_server = ] server_name ] /* internal */
  [ ; ]
---

## Description

Creates a schedule that can be used by any number of jobs. Transact-SQL syntax conventions Indicates the current status of the schedule. , the schedule isn't enabled. When the schedule isn't enabled, no jobs run on this schedule.

## Syntax

```sql
sp_add_schedule
[ @schedule_name = ]
'schedule_name'
[ , [ @enabled = ] enabled ]
[ , [ @freq_type = ] freq_type ]
[ , [ @freq_interval = ] freq_interval ]
[ , [ @freq_subday_type = ] freq_subday_type ]
[ , [ @freq_subday_interval = ] freq_subday_interval ]
[ , [ @freq_relative_interval = ] freq_relative_interval ]
[ , [ @freq_recurrence_factor = ] freq_recurrence_factor ]
[ , [ @active_start_date = ] active_start_date ]
[ , [ @active_end_date = ] active_end_date ]
[ , [ @active_start_time = ] active_start_time ]
[ , [ @active_end_time = ] active_end_time ]
[ , [ @owner_login_name = ]
'owner_login_name'
]
[ , [ @schedule_uid = ] schedule_uid
OUTPUT
]
[ , [ @schedule_id = ] schedule_id
OUTPUT
]
[ , [ @originating_server = ] server_name ] /* internal */
[ ; ]
```
