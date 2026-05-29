---
name: "sys.sp_mschange_snapshot_agent_properties"
title: "sp_MSchange_snapshot_agent_properties"
category: "general"
description: "Changes the properties of a Snapshot Agent job that runs at a SQL Server 2005 (9.x) or later version Distributor. This stored procedure is used to change properties when the Publisher runs on an instance of SQL Server 2000 (8.x). This stored procedure is executed at the Distributor on Transact-SQL syntax conventions"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_
  MS
  change_snapshot_agent_properties
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @frequency_type = ] frequency_type
  , [ @frequency_interval = ] frequency_interval
  , [ @frequency_subday = ] frequency_subday
  , [ @frequency_subday_interval = ] frequency_subday_interval
  , [ @frequency_relative_interval = ] frequency_relative_interval
  , [ @frequency_recurrence_factor = ] frequency_recurrence_factor
  , [ @active_start_date = ] active_start_date
  , [ @active_end_date = ] active_end_date
  , [ @active_start_time_of_day = ] active_start_time_of_day
  , [ @active_end_time_of_day = ] active_end_time_of_day
  , [ @snapshot_job_name = ]
  N
  'snapshot_job_name'
  , [ @publisher_security_mode = ] publisher_security_mode
  , [ @publisher_login = ]
  N
  'publisher_login'
  , [ @publisher_password = ]
  N
  'publisher_password'
  , [ @job_login = ]
  N
  'job_login'
  , [ @job_password = ]
  N
  'job_password'
  , [ @publisher_type = ]
  N
  'publisher_type'
  [ ; ]
---

## Description

Changes the properties of a Snapshot Agent job that runs at a SQL Server 2005 (9.x) or later version Distributor. This stored procedure is used to change properties when the Publisher runs on an instance of SQL Server 2000 (8.x). This stored procedure is executed at the Distributor on Transact-SQL syntax conventions

## Syntax

```sql
sp_
MS
change_snapshot_agent_properties
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @frequency_type = ] frequency_type
, [ @frequency_interval = ] frequency_interval
, [ @frequency_subday = ] frequency_subday
, [ @frequency_subday_interval = ] frequency_subday_interval
, [ @frequency_relative_interval = ] frequency_relative_interval
, [ @frequency_recurrence_factor = ] frequency_recurrence_factor
, [ @active_start_date = ] active_start_date
, [ @active_end_date = ] active_end_date
, [ @active_start_time_of_day = ] active_start_time_of_day
, [ @active_end_time_of_day = ] active_end_time_of_day
, [ @snapshot_job_name = ]
N
'snapshot_job_name'
, [ @publisher_security_mode = ] publisher_security_mode
, [ @publisher_login = ]
N
'publisher_login'
, [ @publisher_password = ]
N
'publisher_password'
, [ @job_login = ]
N
'job_login'
, [ @job_password = ]
N
'job_password'
, [ @publisher_type = ]
N
'publisher_type'
[ ; ]
```

## Permissions

You must specify all parameters when executing . Execute sp_helppublication_snapshot to return the current properties of the Snapshot Agent job. You can use sp_changepublication_snapshot on the Publisher to change properties of a Snapshot Agent job. Only members of the fixed server role at the Distributor can execute . sp_addpublication_snapshot (Transact-SQL) Related content
