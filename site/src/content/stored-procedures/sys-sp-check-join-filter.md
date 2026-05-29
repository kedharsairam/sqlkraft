---
name: "sys.sp_check_join_filter"
title: "sp_check_join_filter"
category: "general"
description: "Verifies a join filter between two tables to determine if the join filter clause is valid. This stored procedure also returns information about the supplied join filter, including if it can be used with precomputed partitions for the given table. This stored procedure is executed at the Publisher on the publication. For more information, see Parameterized Filters - Optimize for Transact-SQL syntax"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_check_join_filter
  [ @filtered_table = ]
  N
  'filtered_table'
  , [ @join_table = ]
  N
  'join_table'
  , [ @join_filterclause = ]
  N
  'join_filterclause'
  [ ; ]
---

## Description

Verifies a join filter between two tables to determine if the join filter clause is valid. This stored procedure also returns information about the supplied join filter, including if it can be used with precomputed partitions for the given table. This stored procedure is executed at the Publisher on the publication. For more information, see Parameterized Filters - Optimize for Transact-SQL syntax conventions

## Syntax

```sql
sp_check_join_filter
[ @filtered_table = ]
N
'filtered_table'
, [ @join_table = ]
N
'join_table'
, [ @join_filterclause = ]
N
'join_filterclause'
[ ; ]
```
