---
name: 'sys.sp_delete_maintenance_plan_db'
title: 'sp_delete_maintenance_plan_db'
category: 'general'
description: 'Disassociates the specified maintenance plan from the specified database. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the maintenance plan ID. Specifies the database name to be deleted from the maintenance plan. This stored'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_maintenance_plan_db
  [ @plan_id = ]
  'plan_id'
  , [ @db_name = ]
  N
  'db_name'
  [ ; ]
---

## Description

Disassociates the specified maintenance plan from the specified database. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the maintenance plan ID. Specifies the database name to be deleted from the maintenance plan. This stored procedure is used with database maintenance plans. This feature has been

## Syntax

```sql
sp_delete_maintenance_plan_db
[ @plan_id = ]
'plan_id'
, [ @db_name = ]
N
'db_name'
[ ; ]
```
