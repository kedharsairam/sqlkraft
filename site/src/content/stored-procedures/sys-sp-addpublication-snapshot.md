---
name: "sys.sp_addpublication_snapshot"
title: "sp_addpublication_snapshot"
category: "general"
description: "Creates the Snapshot Agent for the specified publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor before executing t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
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

Creates the Snapshot Agent for the specified publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor before executing this stored procedure. For more information, see

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

Only members of the fixed server role or fixed database role can execute . Create a publication Create and Apply the Initial Snapshot sp_addpublication (Transact-SQL) sp_changepublication_snapshot (Transact-SQL) sp_startpublication_snapshot (Transact-SQL) Replication stored procedures (Transact-SQL) Related content Create a publication sp_addpublication (Transact-SQL) sp_changelogreader_agent (Transact-SQL) Replication stored procedures (Transact-SQL) Related content Description sp_addpublication_snapshot Creates the Snapshot Agent job for a publication. sp_addqreader_agent Creates the Queue Reader Agent job for a Distributor that supports queued updating subscriptions. sp_changedistpublisher Changes the properties of a Publisher registered at the Distributor. sp_changedistributiondb Modifies properties of the distribution database, including retention periods. sp_changedistributor_password Changes the password used for the connection between the Publisher and a remote Distributor. sp_changedistributor_property Modifies Distributor properties such as the heartbeat interval for agent status checks. sp_changepublication Modifies properties of a Snapshot or Transactional publication. sp_changepublication_snapshot Changes the security credentials or scheduling properties of the Snapshot Agent. sp_changelogreader_agent Changes the security properties of the Log Reader Agent. sp_changeqreader_agent Changes the security properties for the Queue Reader Agent. sp_changereplicationserverpasswords Changes stored passwords for the Windows account or SQL Server login used by replication agents when connecting to servers in a replication topology. sp_dropdistpublisher Removes a Publisher from the Distributor. sp_dropdistributiondb Drops a distribution database and its associated replication jobs. sp_dropdistributor Drops the Distributor by removing the distribution configuration. sp_droppublication Drops a publication and all articles associated with it. sp_get_distributor Returns the Distributor installed on a server. sp_get_redirected_publisher Returns the redirected Publisher for an availability group publisher database. sp_grant_publication_access Adds a login to the publication access list. sp_helpdistpublisher Returns properties of Publishers registered at a Distributor. sp_helpdistributiondb Returns properties of a specified distribution database.
