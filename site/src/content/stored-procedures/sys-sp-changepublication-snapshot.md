---
name: "sys.sp_changepublication_snapshot"
title: "sp_changepublication_snapshot"
category: "general"
description: "Changes properties of the Snapshot Agent for the specified publication. This stored procedure is executed at the Publisher on the publication database. When you configure a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changepublication_snapshot
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
  [ ; ]
---

## Description

Changes properties of the Snapshot Agent for the specified publication. This stored procedure is executed at the Publisher on the publication database. When you configure a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor before executing this stored procedure.

## Syntax

```sql
sp_changepublication_snapshot
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
[ ; ]
```
