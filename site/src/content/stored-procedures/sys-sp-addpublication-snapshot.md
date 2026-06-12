---
name: "sys.sp_addpublication_snapshot"
title: "sp_addpublication_snapshot"
category: "general"
description: "Creates the Snapshot Agent for the specified publication. This stored procedure is executed at the Publisher on the publication database. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor before executing t"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_addpublication_snapshot
      [ @publication = ]
      N
      'publication'
      [ , [ @frequency_type = ] frequency_type ]
      [ , [ @frequency_interval = ] frequency_interval ]
      [ , [ @frequency_subday = ] frequency_subday ]
      [ , [ @frequency_subday_interval = ] frequency_subday_interval ]
      [ , [ @frequency_relative_interval = ] frequency_relative_interval ]
      [ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
      [ , [ @active_start_date = ] active_start_date ]
      [ , [ @active_end_date = ] active_end_date ]
      [ , [ @active_start_time_of_day = ] active_start_time_of_day ]
      [ , [ @active_end_time_of_day = ] active_end_time_of_day ]
      [ , [ @snapshot_job_name = ]
      N
      'snapshot_job_name'
      ]
      [ , [ @publisher_security_mode = ] publisher_security_mode ]
      [ , [ @publisher_login = ]
      N
      'publisher_login'
      ]
      [ , [ @publisher_password = ]
      N
      'publisher_password'
      ]
      [ , [ @job_login = ]
      N
      'job_login'
      ]
      [ , [ @job_password = ]
      N
      'job_password'
      ]
      [ , [ @publisher = ]
      N
      'publisher'
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
      [ ; ]
---

## Description

Creates the Snapshot Agent for the specified publication. This stored procedure is executed at the Publisher on the publication database. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor before executing this stored procedure.

## Syntax

```sql
sp_addpublication_snapshot
[ @publication = ]
N
'publication'
[ , [ @frequency_type = ] frequency_type ]
[ , [ @frequency_interval = ] frequency_interval ]
[ , [ @frequency_subday = ] frequency_subday ]
[ , [ @frequency_subday_interval = ] frequency_subday_interval ]
[ , [ @frequency_relative_interval = ] frequency_relative_interval ]
[ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
[ , [ @active_start_date = ] active_start_date ]
[ , [ @active_end_date = ] active_end_date ]
[ , [ @active_start_time_of_day = ] active_start_time_of_day ]
[ , [ @active_end_time_of_day = ] active_end_time_of_day ]
[ , [ @snapshot_job_name = ]
N
'snapshot_job_name'
]
[ , [ @publisher_security_mode = ] publisher_security_mode ]
[ , [ @publisher_login = ]
N
'publisher_login'
]
[ , [ @publisher_password = ]
N
'publisher_password'
]
[ , [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @publisher = ]
N
'publisher'
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
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Create a publication Create and Apply the Initial Snapshot sp_addpublication (Transact-SQL) sp_changepublication_snapshot (Transact-SQL) sp_startpublication_snapshot (Transact-SQL) Replication stored procedures (Transact-SQL)
