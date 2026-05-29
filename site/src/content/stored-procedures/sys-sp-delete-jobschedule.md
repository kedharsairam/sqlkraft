---
name: 'sys.sp_delete_jobschedule'
title: 'sp_delete_jobschedule'
category: 'general'
description: 'Deletes a schedule for a job in the SQL Server Agent service. is provided for backward compatibility only. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Job schedules can now be managed independently of jobs. To remove a schedule from a job, doesn''t support schedules'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_delete_jobschedule'
---

## Description

Deletes a schedule for a job in the SQL Server Agent service. is provided for backward compatibility only. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Job schedules can now be managed independently of jobs. To remove a schedule from a job, doesn't support schedules that are attached to multiple jobs. If an

## Syntax

```sql
sp_delete_jobschedule
```

## Permissions

06/23/2025 Applies to: SQL Server Azure SQL Managed Instance Deletes a schedule for a job in the SQL Server Agent service. is provided for backward compatibility only. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Job schedules can now be managed independently of jobs. To remove a schedule from a job, use . To delete a schedule, use . doesn't support schedules that are attached to multiple jobs. If an existing script calls to remove a schedule that is attached to more than one job, the procedure returns an error. You can grant permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade. Other users must be granted one of the following SQL Server Agent fixed database roles in the database: SQLAgentUserRole SQLAgentReaderRole SQLAgentOperatorRole For details about the permissions of these roles, see SQL Server Agent Fixed Database Roles . Members of the role can delete any job schedule. Users who aren't members of the role can only delete job schedules that they own. sp_delete_schedule (Transact-SQL) Related content
