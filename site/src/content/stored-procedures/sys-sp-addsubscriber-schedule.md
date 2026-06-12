---
name: "sys.sp_addsubscriber_schedule"
title: "sp_addsubscriber_schedule"
category: "general"
description: "Adds a schedule for the Distribution Agent and Merge Agent. This stored procedure is executed at the Publisher on any database. unique in the database, must not already exist, and can't be , and can be one of these values."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addsubscriber_schedule
  [ @subscriber = ]
  N
  'subscriber'
  [ , [ @agent_type = ] agent_type ]
  [ , [ @frequency_type = ] frequency_type ]
  [ , [ @frequency_interval = ] frequency_interval ]
  [ , [ @frequency_relative_interval = ] frequency_relative_interval ]
  [ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
  [ , [ @frequency_subday = ] frequency_subday ]
  [ , [ @frequency_subday_interval = ] frequency_subday_interval ]
  [ , [ @active_start_time_of_day = ] active_start_time_of_day ]
  [ , [ @active_end_time_of_day = ] active_end_time_of_day ]
  [ , [ @active_start_date = ] active_start_date ]
  [ , [ @active_end_date = ] active_end_date ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Adds a schedule for the Distribution Agent and Merge Agent. This stored procedure is executed at the Publisher on any database. unique in the database, must not already exist, and can't be , and can be one of these values.

## Syntax

```sql
sp_addsubscriber_schedule
[ @subscriber = ]
N
'subscriber'
[ , [ @agent_type = ] agent_type ]
[ , [ @frequency_type = ] frequency_type ]
[ , [ @frequency_interval = ] frequency_interval ]
[ , [ @frequency_relative_interval = ] frequency_relative_interval ]
[ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
[ , [ @frequency_subday = ] frequency_subday ]
[ , [ @frequency_subday_interval = ] frequency_subday_interval ]
[ , [ @active_start_time_of_day = ] active_start_time_of_day ]
[ , [ @active_end_time_of_day = ] active_end_time_of_day ]
[ , [ @active_start_date = ] active_start_date ]
[ , [ @active_end_date = ] active_end_date ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
