---
name: 'sys.sp_add_maintenance_plan'
title: 'sp_add_maintenance_plan'
category: 'general'
description: 'Adds a maintenance plan and returns the plan ID. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the name of the maintenance plan to be added. Specifies the ID of the maintenance plan. This stored procedure is used with databas'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_maintenance_plan
  [ @plan_name = ]
  'plan_name'
  , [ @plan_id = ]
  'plan_id'
  OUTPUT
  [ ; ]
---

## Description

Adds a maintenance plan and returns the plan ID. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the name of the maintenance plan to be added. Specifies the ID of the maintenance plan. This stored procedure is used with database maintenance plans. This feature has been

## Syntax

```sql
sp_add_maintenance_plan
[ @plan_name = ]
'plan_name'
, [ @plan_id = ]
'plan_id'
OUTPUT
[ ; ]
```

## Examples

### Example 1

```sql
EXECUTE
```

### Example 2

```sql
sp_add_maintenance_plan
```

### Example 3

```sql
EXECUTE
sp_delete_maintenance_plan
'FAD6F2AB-3571-11D3-9D4A-00C04FB925FC'
;
```
