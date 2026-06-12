---
name: "sys.sp_create_plan_guide_from_handle"
title: "sp_create_plan_guide_from_handle"
category: "general"
description: "Creates one or more plan guides from a query plan in the plan cache. You can use this stored procedure to ensure the query optimizer always uses a specific query plan for a specified query. For more information about plan guides, see , with no default. Plan guide names are scoped must comply with the rules for Identifies a batch in the plan cache."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_create_plan_guide_from_handle
  [ @name = ]
  N
  'name'
  , [ @plan_handle = ] plan_handle
  [ , [ @statement_start_offset = ] statement_start_offset ]
  [ ; ]
---

## Description

Creates one or more plan guides from a query plan in the plan cache. You can use this stored procedure to ensure the query optimizer always uses a specific query plan for a specified query. For more information about plan guides, see , with no default. Plan guide names are scoped must comply with the rules for Identifies a batch in the plan cache. Identifies the starting position of the statement within the batch of the specified

## Syntax

```sql
sp_create_plan_guide_from_handle
[ @name = ]
N
'name'
, [ @plan_handle = ] plan_handle
[ , [ @statement_start_offset = ] statement_start_offset ]
[ ; ]
```
