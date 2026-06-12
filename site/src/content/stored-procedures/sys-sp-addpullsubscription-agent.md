---
name: "sys.sp_addpullsubscription_agent"
title: "sp_addpullsubscription_agent"
category: "general"
description: "Adds a new scheduled agent job used to synchronize a pull subscription to a transactional publication. This stored procedure is executed at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_addpullsubscription_agent
      [ @publisher = ]
      N
      'publisher'
      [ , [ @publisher_db = ]
      N
      'publisher_db'
      ]
      , [ @publication = ]
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
      [ , [ @distributor = ]
      N
      'distributor'
      ]
      [ , [ @distribution_db = ]
      N
      'distribution_db'
      ]
      [ , [ @distributor_security_mode = ] distributor_security_mode ]
      [ , [ @distributor_login = ]
      N
      'distributor_login'
      ]
      [ , [ @distributor_password = ]
      N
      'distributor_password'
      ]
      [ , [ @optional_command_line = ]
      N
      'optional_command_line'
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
      [ , [ @distribution_jobid = ] distribution_jobid
      OUTPUT
      ]
      [ , [ @encrypted_distributor_password = ] encrypted_distributor_password ]
      [ , [ @enabled_for_syncmgr = ]
      N
      'enabled_for_syncmgr'
      ]
      [ , [ @ftp_address = ]
      N
      'ftp_address'
      ]
      [ , [ @ftp_port = ] ftp_port ]
      [ , [ @ftp_login = ]
      N
      'ftp_login'
      ]
      [ , [ @ftp_password = ]
      N
      'ftp_password'
      ]
      [ , [ @alt_snapshot_folder = ]
      N
      'alt_snapshot_folder'
      ]
---

## Description

Adds a new scheduled agent job used to synchronize a pull subscription to a transactional publication. This stored procedure is executed at the Subscriber on the subscription database. ## Syntax

```sql
sp_addpullsubscription_agent
[ @publisher = ]
N
'publisher'
[ , [ @publisher_db = ]
N
'publisher_db'
]
, [ @publication = ]
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
[ , [ @distributor = ]
N
'distributor'
]
[ , [ @distribution_db = ]
N
'distribution_db'
]
[ , [ @distributor_security_mode = ] distributor_security_mode ]
[ , [ @distributor_login = ]
N
'distributor_login'
]
[ , [ @distributor_password = ]
N
'distributor_password'
]
[ , [ @optional_command_line = ]
N
'optional_command_line'
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
[ , [ @distribution_jobid = ] distribution_jobid
OUTPUT
]
[ , [ @encrypted_distributor_password = ] encrypted_distributor_password ]
[ , [ @enabled_for_syncmgr = ]
N
'enabled_for_syncmgr'
]
[ , [ @ftp_address = ]
N
'ftp_address'
]
[ , [ @ftp_port = ] ftp_port ]
[ , [ @ftp_login = ]
N
'ftp_login'
]
[ , [ @ftp_password = ]
N
'ftp_password'
]
[ , [ @alt_snapshot_folder = ]
N
'alt_snapshot_folder'
]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Create a Pull Subscription Subscribe to Publications sp_addpullsubscription (Transact-SQL) sp_change_subscription_properties (Transact-SQL) sp_droppullsubscription (Transact-SQL) sp_helppullsubscription (Transact-SQL) sp_helpsubscription_properties (Transact-SQL)
