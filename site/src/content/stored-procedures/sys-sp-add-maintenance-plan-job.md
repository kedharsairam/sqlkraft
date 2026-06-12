---
name: "sys.sp_add_maintenance_plan_job"
title: "sp_add_maintenance_plan_job"
category: "general"
description: "Associates a maintenance plan with an existing job. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Specifies the ID of the maintenance plan. Specifies the ID of the job to be associated with the maintenance plan. , and must be a valid I"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_maintenance_plan_job
  [ @plan_id = ]
  N
  'plan_id'
  , [ @job_id = ]
  N
  'job_id'
  [ ; ]
---

## Description

Associates a maintenance plan with an existing job. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Specifies the ID of the maintenance plan. Specifies the ID of the job to be associated with the maintenance plan. , and must be a valid ID. To create a job or jobs, execute

## Syntax

```sql
sp_add_maintenance_plan_job
[ @plan_id = ]
N
'plan_id'
, [ @job_id = ]
N
'job_id'
[ ; ]
```
