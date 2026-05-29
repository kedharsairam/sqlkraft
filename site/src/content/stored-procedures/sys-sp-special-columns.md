---
name: 'sys.sp_special_columns'
title: 'sp_special_columns'
category: 'general'
description: 'SQL database in Microsoft Fabric Returns the optimal set of columns that uniquely identify a row in the table. Also returns columns automatically updated when any value in the row is updated by a transaction. Transact-SQL syntax conventions The name of the table used to return catalog information. default. Wildcard pattern matching isn''t supported. The table owner of the table used to return catal'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_special_columns
  [ @table_name = ]
  N
  'table_name'
  [ , [ @table_owner = ]
  N
  'table_owner'
  ]
  [ , [ @table_qualifier = ]
  N
  'table_qualifier'
  ]
  [ , [ @col_type = ]
  'col_type'
  ]
  [ , [ @scope = ]
  'scope'
  ]
  [ , [ @nullable = ]
  'nullable'
  ]
  [ , [ @
  ODBCV
  er = ]
  ODBCV
  er ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Returns the optimal set of columns that uniquely identify a row in the table. Also returns columns automatically updated when any value in the row is updated by a transaction. Transact-SQL syntax conventions The name of the table used to return catalog information. default. Wildcard pattern matching isn't supported. The table owner of the table used to return catalog information.

## Syntax

```sql
sp_special_columns
[ @table_name = ]
N
'table_name'
[ , [ @table_owner = ]
N
'table_owner'
]
[ , [ @table_qualifier = ]
N
'table_qualifier'
]
[ , [ @col_type = ]
'col_type'
]
[ , [ @scope = ]
'scope'
]
[ , [ @nullable = ]
'nullable'
]
[ , [ @
ODBCV
er = ]
ODBCV
er ]
[ ; ]
```

## Examples

### Example 1

```sql
sp_special_columns
```

### Example 2

```sql
SQLSpecialColumns
```

### Example 3

```sql
SCOPE
```

### Example 4

```sql
SELECT
```

### Example 5

```sql
HumanResources.Department
```

### Example 6

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sp_special_columns
@table_name =
'Department'
,
@table_owner =
'HumanResources'
;
```
