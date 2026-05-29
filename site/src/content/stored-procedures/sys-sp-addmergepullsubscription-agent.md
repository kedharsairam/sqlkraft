---
name: "sys.sp_addmergepullsubscription_agent"
title: "sp_addmergepullsubscription_agent"
category: "general"
description: "Adds a new agent job used to schedule synchronization of a pull subscription to a merge publication. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergepullsubscription_agent
  [ [ @name = ]
  N
  'name'
  ]
  , [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  [ , [ @publisher_security_mode = ] publisher_security_mode ]
  [ , [ @publisher_login = ]
  N
  'publisher_login'
  ]
  [ , [ @publisher_password = ]
  N
  'publisher_password'
  ]
  [ , [ @publisher_encrypted_password = ] publisher_encrypted_password ]
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
  [ , [ @distributor_security_mode = ] distributor_security_mode ]
  [ , [ @distributor_login = ]
  N
  'distributor_login'
  ]
  [ , [ @distributor_password = ]
  N
  'distributor_password'
  ]
  [ , [ @encrypted_password = ] encrypted_password ]
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
  [ , [ @merge_jobid = ] merge_jobid
  OUTPUT
  ]
  [ , [ @enabled_for_syncmgr = ]
  N
  'enabled_for_syncmgr'
  ]
  [ , [ @ftp_address = ]
  N
  'ftp_address'
  ]
---

## Description

Adds a new agent job used to schedule synchronization of a pull subscription to a merge publication. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions

## Syntax

```sql
sp_addmergepullsubscription_agent
[ [ @name = ]
N
'name'
]
, [ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
[ , [ @publisher_security_mode = ] publisher_security_mode ]
[ , [ @publisher_login = ]
N
'publisher_login'
]
[ , [ @publisher_password = ]
N
'publisher_password'
]
[ , [ @publisher_encrypted_password = ] publisher_encrypted_password ]
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
[ , [ @distributor_security_mode = ] distributor_security_mode ]
[ , [ @distributor_login = ]
N
'distributor_login'
]
[ , [ @distributor_password = ]
N
'distributor_password'
]
[ , [ @encrypted_password = ] encrypted_password ]
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
[ , [ @merge_jobid = ] merge_jobid
OUTPUT
]
[ , [ @enabled_for_syncmgr = ]
N
'enabled_for_syncmgr'
]
[ , [ @ftp_address = ]
N
'ftp_address'
]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Create a Pull Subscription Subscribe to Publications sp_addmergepullsubscription (Transact-SQL) sp_changemergepullsubscription (Transact-SQL) sp_dropmergepullsubscription (Transact-SQL) sp_helpmergepullsubscription (Transact-SQL) sp_helpsubscription_properties (Transact-SQL) Related content
