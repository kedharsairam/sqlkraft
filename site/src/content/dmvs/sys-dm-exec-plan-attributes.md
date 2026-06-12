---
name: "sys.dm_exec_plan_attributes"
title: "sys.dm_exec_plan_attributes"
category: "execution"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Returns one row per plan attribute for the plan specified by the plan handle. You can use this table-valued function to get details about a particular plan, such as the cache key values or the number of current simultaneous executions of the plan."
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_exec_plan_attributes ( plan_handle )"
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Returns one row per plan attribute for the plan specified by the plan handle. You can use this table-valued function to get details about a particular plan, such as the cache key values or the number of current simultaneous executions of the plan.

## Syntax

```sql
sys.dm_exec_plan_attributes ( plan_handle )
```
