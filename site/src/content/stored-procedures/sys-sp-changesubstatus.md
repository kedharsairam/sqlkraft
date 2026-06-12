---
name: "sys.sp_changesubstatus"
title: "sp_changesubstatus"
category: "general"
description: "Changes the status of an existing Subscriber. This stored procedure is executed at the Publisher"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_changesubstatus
      [ [ @publication = ]
      N
      'publication'
      ]
      [ , [ @article = ]
      N
      'article'
      ]
      [ , [ @subscriber = ]
      N
      'subscriber'
      ]
      , [ @status = ]
      N
      'status'
      [ , [ @previous_status = ]
      N
      'previous_status'
      ]
      [ , [ @destination_db = ]
      N
      'destination_db'
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
      [ , [ @distribution_jobid = ] distribution_jobid
      OUTPUT
      ]
      [ , [ @from_auto_sync = ] from_auto_sync ]
      [ , [ @ignore_distributor = ] ignore_distributor ]
      [ , [ @offloadagent = ] offloadagent ]
      [ , [ @offloadserver = ]
      N
      'offloadserver'
      ]
      [ , [ @dts_package_name = ]
      N
      'dts_package_name'
      ]
      [ , [ @dts_package_password = ]
      N
      'dts_package_password'
      ]
      [ , [ @dts_package_location = ] dts_package_location ]
      [ , [ @skipobjectactivation = ] skipobjectactivation ]
      [ , [ @distribution_job_name = ]
      N
      'distribution_job_name'
      ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ , [ @ignore_distributor_failure = ] ignore_distributor_failure ]
      [ ; ]
---

## Description

Changes the status of an existing Subscriber. This stored procedure is executed at the Publisher ## Syntax

```sql
sp_changesubstatus
[ [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
]
[ , [ @subscriber = ]
N
'subscriber'
]
, [ @status = ]
N
'status'
[ , [ @previous_status = ]
N
'previous_status'
]
[ , [ @destination_db = ]
N
'destination_db'
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
[ , [ @distribution_jobid = ] distribution_jobid
OUTPUT
]
[ , [ @from_auto_sync = ] from_auto_sync ]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @offloadagent = ] offloadagent ]
[ , [ @offloadserver = ]
N
'offloadserver'
]
[ , [ @dts_package_name = ]
N
'dts_package_name'
]
[ , [ @dts_package_password = ]
N
'dts_package_password'
]
[ , [ @dts_package_location = ] dts_package_location ]
[ , [ @skipobjectactivation = ] skipobjectactivation ]
[ , [ @distribution_job_name = ]
N
'distribution_job_name'
]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @ignore_distributor_failure = ] ignore_distributor_failure ]
[ ; ]
```

## Arguments

Changes the status of an existing Subscriber. This stored procedure is executed at the Publisher

on the publication database.

## Permissions

changes the status of the Subscriber in the table with the changed status. If required, it updates the article status in the table to indicate active or inactive. If required, it sets the replication flag on or off in the table for the replicated table. Only members of the fixed server role, fixed database role, or the creator of the subscription can execute. sp_addsubscription (Transact-SQL) sp_dropsubscription (Transact-SQL) sp_helpdistributor (Transact-SQL) sp_helpsubscription (Transact-SQL) System stored procedures (Transact-SQL)
