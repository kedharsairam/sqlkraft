---
name: 'sys.sp_syspolicy_rename_condition'
title: 'sp_syspolicy_rename_condition'
category: 'general'
description: 'Renames an existing condition in Policy-Based Management. Transact-SQL syntax conventions The name of the condition that you want to rename. The identifier for the condition that you want to rename. The new name of the condition.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syspolicy_rename_condition
  { [ @name = ]
  N
  'name'
  | [ @condition_id = ] condition_id }
  , [ @new_name = ]
  N
  'new_name'
  [ ; ]
---

## Description

Renames an existing condition in Policy-Based Management. Transact-SQL syntax conventions The name of the condition that you want to rename. The identifier for the condition that you want to rename. The new name of the condition.

## Syntax

```sql
sp_syspolicy_rename_condition
{ [ @name = ]
N
'name'
| [ @condition_id = ] condition_id }
, [ @new_name = ]
N
'new_name'
[ ; ]
```
