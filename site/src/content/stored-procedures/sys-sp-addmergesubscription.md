---
name: "sys.sp_addmergesubscription"
title: "sp_addmergesubscription"
category: "general"
description: "Creates a push or pull merge subscription. This stored procedure is executed at the Publisher Transact-SQL syntax conventions"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergesubscription
  [ @publication = ]
  N
  'publication'
  [ , [ @subscriber = ]
  N
  'subscriber'
  ]
  [ , [ @subscriber_db = ]
  N
  'subscriber_db'
  ]
  [ , [ @subscription_type = ]
  N
  'subscription_type'
  ]
  [ , [ @subscriber_type = ]
  N
  'subscriber_type'
  ]
  [ , [ @subscription_priority = ] subscription_priority ]
  [ , [ @sync_type = ]
  N
  'sync_type'
  ]
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
  [ , [ @optional_command_line = ]
  N
  'optional_command_line'
  ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @enabled_for_syncmgr = ]
  N
  'enabled_for_syncmgr'
  ]
  [ , [ @offloadagent = ] offloadagent ]
  [ , [ @offloadserver = ]
  N
  'offloadserver'
  ]
  [ , [ @use_interactive_resolver = ]
  N
  'use_interactive_resolver'
  ]
  [ , [ @merge_job_name = ]
  N
  'merge_job_name'
  ]
  [ , [ @hostname = ]
  N
  'hostname'
  ]
  [ ; ]
---

## Description

Creates a push or pull merge subscription. This stored procedure is executed at the Publisher Transact-SQL syntax conventions

## Syntax

```sql
sp_addmergesubscription
[ @publication = ]
N
'publication'
[ , [ @subscriber = ]
N
'subscriber'
]
[ , [ @subscriber_db = ]
N
'subscriber_db'
]
[ , [ @subscription_type = ]
N
'subscription_type'
]
[ , [ @subscriber_type = ]
N
'subscriber_type'
]
[ , [ @subscription_priority = ] subscription_priority ]
[ , [ @sync_type = ]
N
'sync_type'
]
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
[ , [ @optional_command_line = ]
N
'optional_command_line'
]
[ , [ @description = ]
N
'description'
]
[ , [ @enabled_for_syncmgr = ]
N
'enabled_for_syncmgr'
]
[ , [ @offloadagent = ] offloadagent ]
[ , [ @offloadserver = ]
N
'offloadserver'
]
[ , [ @use_interactive_resolver = ]
N
'use_interactive_resolver'
]
[ , [ @merge_job_name = ]
N
'merge_job_name'
]
[ , [ @hostname = ]
N
'hostname'
]
[ ; ]
```

## Permissions

SQL Only members of the fixed server role or fixed database role can execute . Create a push subscription Create a Pull Subscription Advanced Merge Replication Conflict - Interactive Resolution Related content
