---
name: "sys.sp_syspolicy_add_policy_category"
title: "sp_syspolicy_add_policy_category"
category: "general"
description: "Adds a policy category that can be used with Policy-Based Management. Policy categories enable you to organize policies, and to set policy scope. Transact-SQL syntax conventions The name of the policy category. Determines whether database subscription is mandated for the policy category. @mandate_database_subscriptions The identifier for the policy category."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syspolicy_add_policy_category
  [ @name = ]
  N
  'name'
  [ , [ @mandate_database_subscriptions = ] mandate_database_subscriptions ]
  , [ @policy_category_id = ] policy_category_id
  OUTPUT
  [ ; ]
---

## Description

Adds a policy category that can be used with Policy-Based Management. Policy categories enable you to organize policies, and to set policy scope. Transact-SQL syntax conventions The name of the policy category. Determines whether database subscription is mandated for the policy category. @mandate_database_subscriptions The identifier for the policy category.

## Syntax

```sql
sp_syspolicy_add_policy_category
[ @name = ]
N
'name'
[ , [ @mandate_database_subscriptions = ] mandate_database_subscriptions ]
, [ @policy_category_id = ] policy_category_id
OUTPUT
[ ; ]
```
