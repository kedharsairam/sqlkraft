---
name: "sys.sp_syspolicy_repair_policy_automation"
title: "sp_syspolicy_repair_policy_automation"
category: "general"
description: 'Repairs policy automation in Policy-Based Management. For example, you can use this stored procedure to repair triggers and jobs that are associated with policies that are configured to use "On schedule" or "On change" evaluation modes. Transact-SQL syntax conventions This stored procedure has no parameters.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_syspolicy_repair_policy_automation"
---

## Description

Repairs policy automation in Policy-Based Management. For example, you can use this stored procedure to repair triggers and jobs that are associated with policies that are configured to use "On schedule" or "On change" evaluation modes. Transact-SQL syntax conventions This stored procedure has no parameters.

## Syntax

```sql
sp_syspolicy_repair_policy_automation
```

## Permissions

06/23/2025 Applies to: SQL Server Repairs policy automation in Policy-Based Management. For example, you can use this stored procedure to repair triggers and jobs that are associated with policies that are configured to use "On schedule" or "On change" evaluation modes. Transact-SQL syntax conventions syntaxsql This stored procedure has no parameters. (success) or (failure). You must run in the context of the system database. Requires membership in the fixed database role. ） Important

## Examples

### Example 1

```sql
EXECUTE
msdb.dbo.sp_syspolicy_repair_policy_automation;
GO
```
