---
name: 'sys.sp_syscollector_delete_execution_log_tree'
title: 'sp_syscollector_delete_execution_log_tree'
category: 'general'
description: 'Deletes all the log entries for the run of a single collection set. It also deletes the log entries from the SSIS tables for that run. Transact-SQL syntax conventions The unique identifier for the collection set log. The identifier for the collection set.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_delete_execution_log_tree
  [ @log_id = ] log_id
  [ , [ @from_collection_set = ] from_collection_set ]
  [ ; ]
---

## Description

Deletes all the log entries for the run of a single collection set. It also deletes the log entries from the SSIS tables for that run. Transact-SQL syntax conventions The unique identifier for the collection set log. The identifier for the collection set.

## Syntax

```sql
sp_syscollector_delete_execution_log_tree
[ @log_id = ] log_id
[ , [ @from_collection_set = ] from_collection_set ]
[ ; ]
```

## Permissions

06/23/2025 Applies to: SQL Server Deletes all the log entries for the run of a single collection set. It also deletes the log entries from the SSIS tables for that run. Transact-SQL syntax conventions syntaxsql The unique identifier for the collection set log. @log_id is , with no default. The identifier for the collection set. @from_collection_set is , with a default of an empty string. (success) or (failure).
