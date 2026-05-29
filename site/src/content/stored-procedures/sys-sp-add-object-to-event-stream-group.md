---
name: 'sys.sp_add_object_to_event_stream_group'
title: 'sys.sp_add_object_to_event_stream_group'
category: 'general'
description: 'Adds an object (that is, a table) to the stream group for the feature introduced in SQL Server 2025 (17.x) and Azure SQL Database. Transact-SQL syntax conventions Specifies the name of the event stream group you want to add the table to. , with no default, and can''t be Change event streaming is currently in Azure SQL Database (preview feature database scoped configuration not required). During pre'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_add_object_to_event_stream_group
  [ @stream_group_name = ]
  N
  'stream_group_name'
  , [ @object_name = ]
  N
  'schema_name_dot_object_name'
  [ , [ @include_all_columns = ] include_all_columns ]
  [ , [ @include_old_values = ] include_old_values ]
  [ , [ @include_old_lob_values = ] include_old_lob_values ]
  [ ; ]
---

## Description

Adds an object (that is, a table) to the stream group for the feature introduced in SQL Server 2025 (17.x) and Azure SQL Database. Transact-SQL syntax conventions Specifies the name of the event stream group you want to add the table to. , with no default, and can't be Change event streaming is currently in Azure SQL Database (preview feature database scoped configuration not required). During preview, this feature is subject to change. For current supportability, see

## Syntax

```sql
sys.sp_add_object_to_event_stream_group
[ @stream_group_name = ]
N
'stream_group_name'
, [ @object_name = ]
N
'schema_name_dot_object_name'
[ , [ @include_all_columns = ] include_all_columns ]
[ , [ @include_old_values = ] include_old_values ]
[ , [ @include_old_lob_values = ] include_old_lob_values ]
[ ; ]
```
