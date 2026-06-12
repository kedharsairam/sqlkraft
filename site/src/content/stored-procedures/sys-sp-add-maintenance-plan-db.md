---
name: "sys.sp_add_maintenance_plan_db"
title: "sp_add_maintenance_plan_db"
category: "general"
description: "Associates a database with a maintenance plan. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Specifies the plan ID of the maintenance plan. This stored procedure is used with database maintenance plans. This feature has been replaced w"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_maintenance_plan_db
              [ @plan_id = ]
              'plan_id'
              , [ @db_name = ]
              'database_name'
              [ ; ]
---

## Description

Associates a database with a maintenance plan. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Specifies the plan ID of the maintenance plan. This stored procedure is used with database maintenance plans. This feature has been replaced with maintenance plans which don't use this stored procedure.

## Syntax

```sql
sp_add_maintenance_plan_db
[ @plan_id = ]
'plan_id'
, [ @db_name = ]
'database_name'
[ ; ]
```
