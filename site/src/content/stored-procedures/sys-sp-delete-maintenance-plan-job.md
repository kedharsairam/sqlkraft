---
name: 'sys.sp_delete_maintenance_plan_job'
title: 'sp_delete_maintenance_plan_job'
category: 'general'
description: 'Disassociates the specified maintenance plan from the specified job. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the ID of the maintenance plan. Specifies the ID of the job with which the maintenance plan is associated. Thi'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_maintenance_plan_job
  [ @plan_id = ]
  'plan_id'
  , [ @job_id = ]
  'job_id'
  [ ; ]
---

## Description

Disassociates the specified maintenance plan from the specified job. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the ID of the maintenance plan. Specifies the ID of the job with which the maintenance plan is associated. This stored procedure is used with database maintenance plans. This feature has been

## Syntax

```sql
sp_delete_maintenance_plan_job
[ @plan_id = ]
'plan_id'
, [ @job_id = ]
'job_id'
[ ; ]
```
