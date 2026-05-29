---
name: "sys.sp_check_subset_filter"
title: "sp_check_subset_filter"
category: "general"
description: "Checks a filter clause against any table to determine if the filter clause is valid for the table. This stored procedure returns information about the supplied filter, including if the filter qualifies for use with precomputed partitions. This stored procedure is executed at the Publisher on the database containing the publication. Transact-SQL syntax conventions The filter clause being tested. Sp"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_check_subset_filter
  [ @filtered_table = ]
  N
  'filtered_table'
  , [ @subset_filterclause = ]
  N
  'subset_filterclause'
  [ , [ @has_dynamic_filters = ] has_dynamic_filters
  OUTPUT
  ]
  [ , [ @dynamic_filters_function_list = ]
  N
  'dynamic_filters_function_list'
  OUTPUT
  ]
  [ ; ]
---

## Description

Checks a filter clause against any table to determine if the filter clause is valid for the table. This stored procedure returns information about the supplied filter, including if the filter qualifies for use with precomputed partitions. This stored procedure is executed at the Publisher on the database containing the publication. Transact-SQL syntax conventions The filter clause being tested. Specifies whether the filter clause is a parameterized row filter.

## Syntax

```sql
sp_check_subset_filter
[ @filtered_table = ]
N
'filtered_table'
, [ @subset_filterclause = ]
N
'subset_filterclause'
[ , [ @has_dynamic_filters = ] has_dynamic_filters
OUTPUT
]
[ , [ @dynamic_filters_function_list = ]
N
'dynamic_filters_function_list'
OUTPUT
]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Parameterized Filters - Optimize for Precomputed Partitions Related content
