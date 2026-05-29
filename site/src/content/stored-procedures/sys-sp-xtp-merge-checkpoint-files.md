---
name: 'sys.sp_xtp_merge_checkpoint_files'
title: 'sys.sp_xtp_merge_checkpoint_files'
category: 'general'
description: 'Merges all data and delta files in the transaction range specified. Creating and Managing Storage for Memory-Optimized Objects Transact-SQL syntax conventions The name of the database on which to invoke the merge. database doesn''t have in-memory tables, this procedure returns with user error. If the database is offline, it returns an error. lower bound of transactions for a data file as shown in s'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_xtp_merge_checkpoint_files
  [ @database_name = ] database_name
  , [ @transaction_lower_bound = ] lower_bound_tid
  , [ @transaction_upper_bound = ] upper_bound_tid
  [ ; ]
---

## Description

Merges all data and delta files in the transaction range specified. Creating and Managing Storage for Memory-Optimized Objects Transact-SQL syntax conventions The name of the database on which to invoke the merge. database doesn't have in-memory tables, this procedure returns with user error. If the database is offline, it returns an error. lower bound of transactions for a data file as shown in sys.dm_db_xtp_checkpoint_files

## Syntax

```sql
sys.sp_xtp_merge_checkpoint_files
[ @database_name = ] database_name
, [ @transaction_lower_bound = ] lower_bound_tid
, [ @transaction_upper_bound = ] upper_bound_tid
[ ; ]
```
