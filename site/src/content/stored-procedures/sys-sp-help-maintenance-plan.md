---
name: "sys.sp_help_maintenance_plan"
title: "sp_help_maintenance_plan"
category: "general"
description: "Returns information about the specified maintenance plan. If a plan isn't specified, this stored procedure returns information about all maintenance plans. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_maintenance_plan [ [ @plan_id = ]
  'plan_id'
  ]
  [ ; ]
---

## Description

Returns information about the specified maintenance plan. If a plan isn't specified, this stored procedure returns information about all maintenance plans. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Specifies the plan ID of the maintenance plan.

## Syntax

```sql
sp_help_maintenance_plan [ [ @plan_id = ]
'plan_id'
]
[ ; ]
```
