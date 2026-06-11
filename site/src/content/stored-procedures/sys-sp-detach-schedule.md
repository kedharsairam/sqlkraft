---
name: "sys.sp_detach_schedule"
title: "sp_detach_schedule"
category: "general"
description: "Removes an association between a schedule and a job. Transact-SQL syntax conventions The job identification number of the job to remove the schedule from. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_detach_schedule
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @schedule_id = ] schedule_id ]
  [ , [ @schedule_name = ]
  N
  'schedule_name'
  ]
  [ , [ @delete_unused_schedule = ] delete_unused_schedule ]
  [ , [ @automatic_post = ] automatic_post ]
  [ ; ]
---

## Description

Removes an association between a schedule and a job. Transact-SQL syntax conventions The job identification number of the job to remove the schedule from. must be specified, but both can't be specified. The name of the job to remove the schedule from. must be specified, but both can't be specified.

## Syntax

```sql
sp_detach_schedule
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @schedule_id = ] schedule_id ]
[ , [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @delete_unused_schedule = ] delete_unused_schedule ]
[ , [ @automatic_post = ] automatic_post ]
[ ; ]
```

## Permissions

06/23/2025 Applies to: SQL Server Azure SQL Managed Instance Deletes a schedule for a job in the SQL Server Agent service. is provided for backward compatibility only. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Job schedules can now be managed independently of jobs. To remove a schedule from a job, use . To delete a schedule, use . doesn't support schedules that are attached to multiple jobs. If an existing script calls to remove a schedule that is attached to more than one job, the procedure returns an error. You can grant permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade. Other users must be granted one of the following SQL Server Agent fixed database roles in the database: SQLAgentUserRole SQLAgentReaderRole SQLAgentOperatorRole For details about the permissions of these roles, see SQL Server Agent Fixed Database Roles . Members of the role can delete any job schedule. Users who aren't members of the role can only delete job schedules that they own. sp_delete_schedule (Transact-SQL) Related content sp_attach_schedule (Transact-SQL) sp_delete_schedule (Transact-SQL) sp_detach_schedule (Transact-SQL)
