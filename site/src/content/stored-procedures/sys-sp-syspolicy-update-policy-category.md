---
name: "sys.sp_syspolicy_update_policy_category"
title: "sp_syspolicy_update_policy_category"
category: "general"
description: "Updates whether a policy category is set to mandate database subscriptions. If subscription is mandated, the policy category applies to all databases."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syspolicy_update_policy_category
  { [ @name = ]
  N
  'name'
  | [ @policy_category_id = ] policy_category_id }
  [ , [ @mandate_database_subscriptions = ] mandate_database_subscriptions ]
  [ ; ]
---

## Description

Updates whether a policy category is set to mandate database subscriptions. If subscription is mandated, the policy category applies to all databases.

## Syntax

```sql
sp_syspolicy_update_policy_category
{ [ @name = ]
N
'name'
| [ @policy_category_id = ] policy_category_id }
[ , [ @mandate_database_subscriptions = ] mandate_database_subscriptions ]
[ ; ]
```
