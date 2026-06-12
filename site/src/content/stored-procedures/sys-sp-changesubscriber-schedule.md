---
name: "sys.sp_changesubscriber_schedule"
title: "sp_changesubscriber_schedule"
category: "general"
description: "Changes the Distribution Agent or Merge Agent schedule for a subscriber. This stored procedure is executed at the Publisher on any database. , with no default."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_changesubscriber_schedule
      [ @subscriber = ]
      N
      'subscriber'
      , [ @agent_type = ] agent_type
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

Changes the Distribution Agent or Merge Agent schedule for a subscriber. This stored procedure is executed at the Publisher on any database. , with no default.

## Syntax

```sql
sp_changesubscriber_schedule
[ @subscriber = ]
N
'subscriber'
, [ @agent_type = ] agent_type
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
