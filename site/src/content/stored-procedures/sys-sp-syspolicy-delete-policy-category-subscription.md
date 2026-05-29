---
name: "sys.sp_syspolicy_delete_policy_category_subscription"
title: "sp_syspolicy_delete_policy_category_subscription"
category: "general"
description: "@policy_category_subscription_id , you can use the following query: The following example deletes a policy category subscription with an ID of 1. Policy-Based Management stored procedures (Transact-SQL) sp_syspolicy_update_policy_category_subscription (Transact-SQL)"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  SELECT
  a.policy_category_subscription_id,
  a.target_object,
  b.name
  AS
  category_name
  FROM
  msdb.dbo.syspolicy_policy_category_subscriptions
  AS
  a
  INNER
  JOIN
  msdb.dbo.syspolicy_policy_categories
  AS
  b
  ON
  a.policy_category_id = b.policy_category_id;
---

## Description

@policy_category_subscription_id , you can use the following query: The following example deletes a policy category subscription with an ID of 1. Policy-Based Management stored procedures (Transact-SQL) sp_syspolicy_update_policy_category_subscription (Transact-SQL)

## Syntax

```sql
SELECT
a.policy_category_subscription_id,
a.target_object,
b.name
AS
category_name
FROM
msdb.dbo.syspolicy_policy_category_subscriptions
AS
a
INNER
JOIN
msdb.dbo.syspolicy_policy_categories
AS
b
ON
a.policy_category_id = b.policy_category_id;
```

## Examples

### Example 1

```sql
SELECT
a.policy_category_subscription_id,
a.target_object,
b.name
AS
category_name
FROM
msdb.dbo.syspolicy_policy_category_subscriptions
AS
a
INNER
JOIN
msdb.dbo.syspolicy_policy_categories
AS
b
ON
a.policy_category_id = b.policy_category_id;
```

### Example 2

```sql
EXECUTE
msdb.dbo.sp_syspolicy_delete_policy_category_subscription
@policy_category_subscription_id = 1;
GO
```
