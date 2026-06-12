---
name: "sys.sp_syspolicy_subscribe_to_policy_category"
title: "sp_syspolicy_subscribe_to_policy_category"
category: "general"
description: "Adds a policy category subscription for the specified database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "msdb.dbo.syspolicy_policy_categories"
---

## Description

Adds a policy category subscription for the specified database.

## Syntax

`msdb.dbo.syspolicy_policy_categories`

## Permissions

06/23/2025 syntaxsql The name of the policy category that you want the database to subscribe to. @policy_category is , and is required. To obtain values for @policy_category , query the system view. (success) or (failure). You must run in the context of the database where you want to add a policy category subscription.

## Examples

### Example 1

`Finance`

### Example 2

```sql
USE
<database_name>;
GO
EXECUTE sys.sp_syspolicy_subscribe_to_policy_category
@policy_category = N
'Finance'
;
GO
```
