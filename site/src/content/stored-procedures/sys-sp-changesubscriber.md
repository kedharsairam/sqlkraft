---
name: "sys.sp_changesubscriber"
title: "sp_changesubscriber"
category: "general"
description: "Changes the options for a Subscriber. Any distribution task for the Subscribers to this Publisher is updated. This stored procedure writes to the database. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_changesubscriber
      [ @subscriber = ]
      N
      'subscriber'
      [ , [ @type = ] type ]
      [ , [ @login = ]
      N
      'login'
      ]
      [ , [ @password = ]
      N
      'password'
      ]
      [ , [ @commit_batch_size = ] commit_batch_size ]
      [ , [ @status_batch_size = ] status_batch_size ]
      [ , [ @flush_frequency = ] flush_frequency ]
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
      [ , [ @description = ]
      N
      'description'
      ]
      [ , [ @security_mode = ] security_mode ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ ; ]
---

## Description

Changes the options for a Subscriber. Any distribution task for the Subscribers to this Publisher is updated. This stored procedure writes to the database. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_changesubscriber
[ @subscriber = ]
N
'subscriber'
[ , [ @type = ] type ]
[ , [ @login = ]
N
'login'
]
[ , [ @password = ]
N
'password'
]
[ , [ @commit_batch_size = ] commit_batch_size ]
[ , [ @status_batch_size = ] status_batch_size ]
[ , [ @flush_frequency = ] flush_frequency ]
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
[ , [ @description = ]
N
'description'
]
[ , [ @security_mode = ] security_mode ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
