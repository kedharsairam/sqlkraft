---
name: "sys.sp_addsubscriber"
title: "sp_addsubscriber"
category: "general"
description: "Adds a new Subscriber to a Publisher, enabling it to receive publications. This stored procedure is executed at the Publisher on the publication database for snapshot and transactional publications; and for merge publications using a remote Distributor, this stored procedure is This stored procedure has been deprecated. You're no longer required to explicitly regist"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addsubscriber
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
  [ , [ @encrypted_password = ] encrypted_password ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Adds a new Subscriber to a Publisher, enabling it to receive publications. This stored procedure is executed at the Publisher on the publication database for snapshot and transactional publications; and for merge publications using a remote Distributor, this stored procedure is This stored procedure has been deprecated. You're no longer required to explicitly register

## Syntax

```sql
sp_addsubscriber
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
[ , [ @encrypted_password = ] encrypted_password ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
