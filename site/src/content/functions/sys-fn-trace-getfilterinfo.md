---
name: 'sys.fn_trace_getfilterinfo'
title: 'sys.fn_trace_getfilterinfo'
category: 'system'
description: 'Returns information about the filters applied to a specified trace. Transact-SQL syntax conventions Returns the following information. For more information about the columns, see sp_trace_setfilter (Transact-SQL) The ID of the column on which the filter is applied. Specifies whether the AND or OR operator is applied. Specifies the type of comparison made: This feature will be removed in a future v'
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: 'fn_trace_getfilterinfo ( trace_id )'
---

## Description

Returns information about the filters applied to a specified trace. Transact-SQL syntax conventions Returns the following information. For more information about the columns, see sp_trace_setfilter (Transact-SQL) The ID of the column on which the filter is applied. Specifies whether the AND or OR operator is applied. Specifies the type of comparison made: This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
fn_trace_getfilterinfo ( trace_id )
```

## Examples

### Example 1

```sql
SELECT * FROM fn_trace_getfilterinfo(2) ;
GO
```
