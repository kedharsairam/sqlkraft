---
name: 'sys.sp_syspolicy_update_policy_category'
title: 'sp_syspolicy_update_policy_category'
category: 'general'
description: 'Updates whether a policy category is set to mandate database subscriptions. If subscription is mandated, the policy category applies to all databases. Transact-SQL syntax conventions The name of the policy category. The identifier for the policy category. Determines whether database subscription is mandated for the policy category. @mandate_database_subscriptions'
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

Updates whether a policy category is set to mandate database subscriptions. If subscription is mandated, the policy category applies to all databases. Transact-SQL syntax conventions The name of the policy category. The identifier for the policy category. Determines whether database subscription is mandated for the policy category. @mandate_database_subscriptions

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
