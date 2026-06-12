---
name: "sys.sp_addpushsubscription_agent"
title: "sp_addpushsubscription_agent"
category: "general"
description: "Adds a new scheduled agent job used to synchronize a push subscription to a transactional publication. This stored procedure is executed at the Publisher on the publication database. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addpushsubscription_agent
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
  [ , [ @subscriber_security_mode = ] subscriber_security_mode ]
  [ , [ @subscriber_login = ]
  N
  'subscriber_login'
  ]
  [ , [ @subscriber_password = ]
  N
  'subscriber_password'
  ]
  [ , [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
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
  [ , [ @dts_package_name = ]
  N
  'dts_package_name'
  ]
  [ , [ @dts_package_password = ]
  N
  'dts_package_password'
  ]
---

## Description

Adds a new scheduled agent job used to synchronize a push subscription to a transactional publication. This stored procedure is executed at the Publisher on the publication database. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor

## Syntax

```sql
sp_addpushsubscription_agent
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
[ , [ @subscriber_security_mode = ] subscriber_security_mode ]
[ , [ @subscriber_login = ]
N
'subscriber_login'
]
[ , [ @subscriber_password = ]
N
'subscriber_password'
]
[ , [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @job_name = ]
N
'job_name'
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
[ , [ @dts_package_name = ]
N
'dts_package_name'
]
[ , [ @dts_package_password = ]
N
'dts_package_password'
]
```

## Permissions

SQL Only members of the fixed server role or fixed database role can execute. Create a push subscription Create a Subscription for a Non-SQL Server Subscriber Subscribe to Publications Replication stored procedures (Transact-SQL) sp_addsubscription (Transact-SQL) sp_changesubscription (Transact-SQL) sp_dropsubscription (Transact-SQL) sp_helpsubscription (Transact-SQL)
