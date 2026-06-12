---
name: "sys.dm_exec_describe_first_result_set_for_object"
title: "sys.dm_exec_describe_first_result_set_for_object"
category: "execution"
description: "This dynamic management function takes an @object_id as a parameter and describes the first result metadata for the module with that ID. The @object_id specified can be the ID of a Transact-SQL stored procedure or a Transact-SQL trigger."
tags: ["execution","dmv"]
pubDate: 2026-05-29
syntax: |
  sys.dm_exec_describe_first_result_set_for_object
                ( @object_id , @include_browse_information )
---

## Description

This dynamic management function takes an @object_id as a parameter and describes the first result metadata for the module with that ID. The @object_id specified can be the ID of a Transact-SQL stored procedure or a Transact-SQL trigger.

## Syntax

```sql
sys.dm_exec_describe_first_result_set_for_object ( @object_id , @include_browse_information )
```

## Permissions
