---
name: 'sys.dm_exec_describe_first_result_set_for_object'
title: 'sys.dm_exec_describe_first_result_set_for_object'
category: 'execution'
description: 'SQL database in Microsoft Fabric This dynamic management function takes an @object_id as a parameter and describes the first result metadata for the module with that ID. The @object_id specified can be the ID of a Transact-SQL stored procedure or a Transact-SQL trigger. If it is the ID of any other object (such as a view, table, function, or CLR procedure), an error will be specified in the error '
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: |
  sys.dm_exec_describe_first_result_set_for_object
  ( @object_id , @include_browse_information )
---

## Description

SQL database in Microsoft Fabric This dynamic management function takes an @object_id as a parameter and describes the first result metadata for the module with that ID. The @object_id specified can be the ID of a Transact-SQL stored procedure or a Transact-SQL trigger. If it is the ID of any other object (such as a view, table, function, or CLR procedure), an error will be specified in the error columns of

## Syntax

```sql
sys.dm_exec_describe_first_result_set_for_object
( @object_id , @include_browse_information )
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Returns only metadata to the client. Can be used to test the format of the response without actually running the query. Transact-SQL syntax conventions syntaxsql When is , a rowset is returned with the column names, but without any data rows. has no effect when the Transact-SQL batch is parsed. The effect occurs during execution run time. The default value is . Requires membership in the public role. ７ Note Do not use this feature. This feature has been replaced by the following items:
