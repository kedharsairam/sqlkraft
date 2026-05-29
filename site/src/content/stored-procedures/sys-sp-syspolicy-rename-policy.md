---
name: "sys.sp_syspolicy_rename_policy"
title: "sp_syspolicy_rename_policy"
category: "general"
description: "Renames an existing policy in Policy-Based Management. Transact-SQL syntax conventions The name of the policy that you want to rename. The identifier for the policy that you want to rename."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syspolicy_rename_policy
  { [ @name = ]
  N
  'name'
  | [ @policy_id = ] policy_id }
  , [ @new_name = ]
  N
  'new_name'
  [ ; ]
---

## Description

Renames an existing policy in Policy-Based Management. Transact-SQL syntax conventions The name of the policy that you want to rename. The identifier for the policy that you want to rename.

## Syntax

```sql
sp_syspolicy_rename_policy
{ [ @name = ]
N
'name'
| [ @policy_id = ] policy_id }
, [ @new_name = ]
N
'new_name'
[ ; ]
```

## Examples

### Example 1

```sql
sp_syspolicy_rename_policy
```

### Example 2

```sql
msdb
```

### Example 3

```sql
NULL
```

### Example 4

```sql
msdb.dbo.syspolicy_policies
```

### Example 5

```sql
Test Policy 1
```

### Example 6

```sql
Test Policy 2
```

### Example 7

```sql
EXECUTE
msdb.dbo.sp_syspolicy_rename_policy
@
name
= N
'Test Policy 1'
,
@new_name = N
'Test Policy 2'
;
GO
```
