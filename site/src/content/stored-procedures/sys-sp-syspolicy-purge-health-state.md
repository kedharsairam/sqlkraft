---
name: "sys.sp_syspolicy_purge_health_state"
title: "sp_syspolicy_purge_health_state"
category: "general"
description: 'Deletes the policy health states in Policy-Based Management. Policy health states are visual indicators within Object Explorer (a scroll symbol with a red "X") that help you to determine which nodes have failed a policy evaluation. Transact-SQL syntax conventions Represents the node in Object Explorer where you want to clear the health state. @target_tree_root_with_id , with a default of You can s'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "msdb.dbo.syspolicy_system_health_state"
---

## Description

Deletes the policy health states in Policy-Based Management. Policy health states are visual indicators within Object Explorer (a scroll symbol with a red "X") that help you to determine which nodes have failed a policy evaluation. Transact-SQL syntax conventions Represents the node in Object Explorer where you want to clear the health state. @target_tree_root_with_id , with a default of You can specify values from the target_query_expression_with_id column of the in the context of the system database.

## Syntax

`msdb.dbo.syspolicy_system_health_state`

## Remarks

Applies to:

Deletes the policy health states in Policy-Based Management. Policy health states are visual

indicators within Object Explorer (a scroll symbol with a red "X") that help you to determine

which nodes have failed a policy evaluation.

Transact-SQL syntax conventions

Represents the node in Object Explorer where you want to clear the health state.

@target_tree_root_with_id

, with a default of

You can specify values from the target_query_expression_with_id column of the

system view.

(success) or

You must run

in the context of the

system database.

## Examples

### Example 1

```sql
EXECUTE msdb.dbo.sp_syspolicy_purge_health_state
@target_tree_root_with_id =
'Server/Database[@ID=7]'
;
GO
```
