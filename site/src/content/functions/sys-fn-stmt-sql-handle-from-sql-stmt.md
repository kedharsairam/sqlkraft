---
name: 'sys.fn_stmt_sql_handle_from_sql_stmt'
title: 'sys.fn_stmt_sql_handle_from_sql_stmt'
category: 'system'
description: 'SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric for a Transact-SQL statement under the given parameterization type (simple or forced). You can refer to queries stored in the Query Store by using their Transact-SQL syntax conventions The text of the query in the Query Store that you want the handle of. The parameter type of the query.'
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: |
  sys.fn_stmt_sql_handle_from_sql_stmt
  (
  N
  'query_sql_text'
  , [ query_param_type ]
  )
  [ ; ]
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric for a Transact-SQL statement under the given parameterization type (simple or forced). You can refer to queries stored in the Query Store by using their Transact-SQL syntax conventions The text of the query in the Query Store that you want the handle of. The parameter type of the query.

## Syntax

```sql
sys.fn_stmt_sql_handle_from_sql_stmt
(
N
'query_sql_text'
, [ query_param_type ]
)
[ ; ]
```

## Examples

### Example 1

```sql
sys.fn_stmt_sql_handle_from_sql_stmt
```

### Example 2

```sql
statement_sql_handle
```

### Example 3

```sql
query_sql_text
```

### Example 4

```sql
query_parameterization_type
```

### Example 5

```sql
0
```

### Example 6

```sql
1
```

### Example 7

```sql
EXECUTE
```

### Example 8

```sql
DELETE
```

### Example 9

```sql
sys.fn_stmt_sql_handle_from_sql_stmt
```

### Example 10

```sql
SELECT
*
FROM
sys.databases;
```


*(... and 1 more examples)*
