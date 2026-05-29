---
name: "sys.sp_syspolicy_delete_policy_execution_history"
title: "sp_syspolicy_delete_policy_execution_history"
category: "general"
description: ", and to view execution history dates, you can use the following The following behavior applies if you specify To delete all policy execution history, specify To delete all policy execution history for a specific policy, specify a policy identifier for To delete policy execution history for all policies before a specific date, specify To archive policy execution history, you can open the Policy Hi"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_syspolicy_delete_policy_execution_history"
---

## Description

, and to view execution history dates, you can use the following The following behavior applies if you specify To delete all policy execution history, specify To delete all policy execution history for a specific policy, specify a policy identifier for To delete policy execution history for all policies before a specific date, specify To archive policy execution history, you can open the Policy History log, in Object Explorer, and

## Syntax

```sql
sp_syspolicy_delete_policy_execution_history
```

## Permissions

You must run in the context of the system database. To obtain values for @policy_id , and to view execution history dates, you can use the following query: SQL The following behavior applies if you specify for one or both values: To delete all policy execution history, specify for both @policy_id and for @oldest_date . To delete all policy execution history for a specific policy, specify a policy identifier for @policy_id , and specify as @oldest_date . To delete policy execution history for all policies before a specific date, specify for @policy_id , and specify a date for @oldest_date . To archive policy execution history, you can open the Policy History log, in Object Explorer, and export the execution history to a file. To access the Policy History log, expand , right-click , and then select . Requires membership in the fixed database role. ） Important Possible elevation of credentials: Users in the role can create server triggers and schedule policy executions that can affect the operation of the instance of the Database Engine. For example, users in the role can create a policy that can prevent most objects from being created in the Database Engine. Because of this possible elevation of credentials, the role

## Examples

### Example 1

```sql
7
```

### Example 2

```sql
EXECUTE
msdb.dbo.sp_syspolicy_delete_policy_execution_history
@policy_id = 7,
@oldest_date =
'2019-02-16 16:00:00.000'
;
GO
```
