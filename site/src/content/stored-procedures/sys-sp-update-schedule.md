---
name: "sys.sp_update_schedule"
title: "sp_update_schedule"
category: "general"
description: "Changes the settings for a SQL Server Agent schedule. The identifier of the schedule to modify."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_schedule
  [ [ @schedule_id = ] schedule_id ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ , [ @new_name = ]
  N
  'new_name'
  ]
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
  N
  'owner_login_name'
  ]
  [ , [ @automatic_post = ] automatic_post ]
  [ ; ]
---

## Description

Changes the settings for a SQL Server Agent schedule. The identifier of the schedule to modify.

## Syntax

```sql
sp_update_schedule
[ [ @schedule_id = ] schedule_id ]
[ , [ @name = ]
N
'name'
]
[ , [ @new_name = ]
N
'new_name'
]
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
N
'owner_login_name'
]
[ , [ @automatic_post = ] automatic_post ]
[ ; ]
```
