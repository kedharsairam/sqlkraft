---
name: 'sys.sp_copy_data_in_batches'
title: 'sp_copy_data_in_batches'
category: 'general'
description: 'Copies data from the source table to the target table after verifying that their schema is identical in terms of number of columns, column names and their data types. columns are ignored since they''re system generated and this allows copying data from a regular table to a ledger table and vice versa. Indexes between the tables can be different but the target table can only be a heap or have a clus'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_copy_data_in_batches
  [ @source_table_name = ]
  N
  'source_table_name'
  , [ @target_table_name = ]
  N
  'target_table_name'
---

## Description

Copies data from the source table to the target table after verifying that their schema is identical in terms of number of columns, column names and their data types. columns are ignored since they're system generated and this allows copying data from a regular table to a ledger table and vice versa. Indexes between the tables can be different but the target table can only be a heap or have a clustered

## Syntax

```sql
sp_copy_data_in_batches
[ @source_table_name = ]
N
'source_table_name'
, [ @target_table_name = ]
N
'target_table_name'
```
