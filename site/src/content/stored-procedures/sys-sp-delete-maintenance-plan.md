---
name: "sys.sp_delete_maintenance_plan"
title: "sp_delete_maintenance_plan"
category: "general"
description: "Deletes the specified maintenance plan. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the ID of the maintenance plan to be deleted. must be run from the This stored procedure is used with database maintenance plans. This feat"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_delete_maintenance_plan"
---

## Description

Deletes the specified maintenance plan. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Transact-SQL syntax conventions Specifies the ID of the maintenance plan to be deleted. must be run from the This stored procedure is used with database maintenance plans. This feature has been replaced with maintenance plans that don't use this stored procedure. Use this procedure to maintain database maintenance plans on installations that were upgraded from a previous version of SQL Server.

## Syntax

```sql
sp_delete_maintenance_plan
```

## Remarks

Applies to:

Deletes the specified maintenance plan.

This feature will be removed in a future version of SQL Server. Avoid using this feature in new

development work, and plan to modify applications that currently use this feature.

Transact-SQL syntax conventions

Specifies the ID of the maintenance plan to be deleted.

be a valid ID.

(success) or

must be run from the

This stored procedure is used with database maintenance plans. This feature has been

replaced with maintenance plans that don't use this stored procedure. Use this procedure

to maintain database maintenance plans on installations that were upgraded from a

previous version of SQL Server.
