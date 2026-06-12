---
name: "sys.sp_adddynamicsnapshot_job"
title: "sp_adddynamicsnapshot_job"
category: "general"
description: "Creates an agent job that generates a filtered data snapshot for a publication with parameterized row filters. This stored procedure is executed at the Publisher on the publication database. This stored procedure is used by an administrator to manually create filtered data snapshot jobs for Subscribers. Create a Snapshot for a Merge Publication with Parameterized In"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_adddynamicsnapshot_job
              [ @publication = ]
              N
              'publication'
              [ , [ @suser_sname = ]
              N
              'suser_sname'
              ]
              [ , [ @host_name = ]
              N
              'host_name'
              ]
              [ , [ @dynamic_snapshot_jobname = ]
              N
              'dynamic_snapshot_jobname'
              OUTPUT
              ]
              [ , [ @dynamic_snapshot_jobid = ]
              'dynamic_snapshot_jobid'
              OUTPUT
              ]
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
              [ ; ]
---

## Description

Creates an agent job that generates a filtered data snapshot for a publication with parameterized row filters. This stored procedure is executed at the Publisher on the publication database. This stored procedure is used by an administrator to manually create filtered data snapshot jobs for Subscribers.

## Syntax

```sql
sp_adddynamicsnapshot_job
[ @publication = ]
N
'publication'
[ , [ @suser_sname = ]
N
'suser_sname'
]
[ , [ @host_name = ]
N
'host_name'
]
[ , [ @dynamic_snapshot_jobname = ]
N
'dynamic_snapshot_jobname'
OUTPUT
]
[ , [ @dynamic_snapshot_jobid = ]
'dynamic_snapshot_jobid'
OUTPUT
]
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
[ ; ]
```

## Permissions

Only members of the fixed server role or the fixed database role can execute. Create a Snapshot for a Merge Publication with Parameterized Filters Parameterized Filters - Parameterized Row Filters sp_dropdynamicsnapshot_job (Transact-SQL) sp_helpdynamicsnapshot_job (Transact-SQL)
