---
name: "sys.sp_syspolicy_rename_condition"
title: "sp_syspolicy_rename_condition"
category: "general"
description: "Renames an existing condition in Policy-Based Management."
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

Renames an existing condition in Policy-Based Management.

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
