---
name: "sys.sp_syspolicy_unsubscribe_from_policy_category"
title: "sp_syspolicy_unsubscribe_from_policy_category"
category: "general"
description: "The following example deletes a subscription to the policy category for the specified Policy-Based Management stored procedures (Transact-SQL) sp_syspolicy_subscribe_to_policy_category (Transact-SQL)"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  USE
      <database_name>;
      GO
      EXECUTE
      sys.sp_syspolicy_unsubscribe_from_policy_category
      @policy_category = N
      'Finance'
      ;
      GO
---

## Description

The following example deletes a subscription to the policy category for the specified Policy-Based Management stored procedures (Transact-SQL) sp_syspolicy_subscribe_to_policy_category (Transact-SQL)

## Syntax

```sql
USE
<database_name>;
GO
EXECUTE sys.sp_syspolicy_unsubscribe_from_policy_category
@policy_category = N
'Finance'
;
GO
```

## Examples

### Example 1

`Finance`

### Example 2

```sql
USE
<database_name>;
GO
EXECUTE sys.sp_syspolicy_unsubscribe_from_policy_category
@policy_category = N
'Finance'
;
GO
```
