---
name: "sys.sp_syspolicy_rename_policy_category"
title: "sp_syspolicy_rename_policy_category"
category: "general"
description: "Renames an existing policy category in Policy-Based Management. Transact-SQL syntax conventions The name of the policy category that you want to rename. The identifier for the policy category that you want to rename. The new name for the policy category."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syspolicy_rename_policy_category
  { [ @name = ]
  N
  'name'
  | [ @policy_category_id = ] policy_category_id }
  , [ @new_name = ]
  N
  'new_name'
  [ ; ]
---

## Description

Renames an existing policy category in Policy-Based Management. Transact-SQL syntax conventions The name of the policy category that you want to rename. The identifier for the policy category that you want to rename. The new name for the policy category.

## Syntax

```sql
sp_syspolicy_rename_policy_category
{ [ @name = ]
N
'name'
| [ @policy_category_id = ] policy_category_id }
, [ @new_name = ]
N
'new_name'
[ ; ]
```
