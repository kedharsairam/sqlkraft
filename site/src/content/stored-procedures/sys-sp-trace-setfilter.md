---
name: 'sys.sp_trace_setfilter'
title: 'sp_trace_setfilter'
category: 'general'
description: 'can be executed only on existing traces that are ). SQL Server returns an error if this stored procedure is executed on a trace that doesn''t exist or whose Transact-SQL syntax conventions This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Arguments for extended stored pro'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_trace_setfilter
  [ @traceid = ] traceid
  , [ @columnid = ] columnid
  , [ @logical_operator = ] logical_operator
  , [ @comparison_operator = ] comparison_operator
  , [ @value = ] value
  [ ; ]
---

## Description

can be executed only on existing traces that are ). SQL Server returns an error if this stored procedure is executed on a trace that doesn't exist or whose Transact-SQL syntax conventions This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Arguments for extended stored procedures must be entered in the specific order as

## Syntax

```sql
sp_trace_setfilter
[ @traceid = ] traceid
, [ @columnid = ] columnid
, [ @logical_operator = ] logical_operator
, [ @comparison_operator = ] comparison_operator
, [ @value = ] value
[ ; ]
```

## Examples

### Example 1

```sql
sp_trace_setfilter
```

### Example 2

```sql
sp_trace_setfilter
```

### Example 3

```sql
xp_trace_set*filter
```

### Example 4

```sql
sp_trace_setfilter
```

### Example 5

```sql
sp_trace_*
```

### Example 6

```sql
1
```

### Example 7

```sql
N'SQLT%'
```

### Example 8

```sql
N'MS%'
```

### Example 9

```sql
AppName
```

### Example 10

```sql
10
```


*(... and 18 more examples)*
