---
name: "sys.sp_update_jobschedule"
title: "sp_update_jobschedule"
category: "general"
description: "Changes the schedule settings for the specified job in the SQL Server Agent service. is provided for backward compatibility only. Job schedules can now be managed independently of jobs. To update a schedule, use permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_update_jobschedule"
---

## Description

Changes the schedule settings for the specified job in the SQL Server Agent service. is provided for backward compatibility only. Job schedules can now be managed independently of jobs. To update a schedule, use permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade.

## Syntax

`sp_update_jobschedule`

## Permissions

06/23/2025 Changes the schedule settings for the specified job in the SQL Server Agent service. is provided for backward compatibility only. Job schedules can now be managed independently of jobs. To update a schedule, use sp_update_schedule. You can grant permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade. Other users must be granted one of the following SQL Server Agent fixed database roles in the database: SQLAgentUserRole SQLAgentReaderRole SQLAgentOperatorRole For details about the permissions of these roles, see SQL Server Agent Fixed Database Roles. Only members of can use this stored procedure to update job schedules that are owned by other users. SQL Server Agent stored procedures (Transact-SQL) sp_update_schedule (Transact-SQL)
