---
name: "sys.sp_columns_ex"
title: "sp_columns_ex"
category: "general"
description: "Returns the column information, one row per column, for the specified linked server tables. returns column information for only the specific column if The name of the linked server for which to return column information."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_columns_ex
              [ @table_server = ]
              N
              'table_server'
              [ , [ @table_name = ]
              N
              'table_name'
              ]
              [ , [ @table_schema = ]
              N
              'table_schema'
              ]
              [ , [ @table_catalog = ]
              N
              'table_catalog'
              ]
              [ , [ @column_name = ]
              N
              'column_name'
              ]
              [ , [ @
              ODBCV
              er = ]
              ODBCV
              er ]
              [ ; ]
---

## Description

Returns the column information, one row per column, for the specified linked server tables. returns column information for only the specific column if The name of the linked server for which to return column information.

## Syntax

```sql
sp_columns_ex
[ @table_server = ]
N
'table_server'
[ , [ @table_name = ]
N
'table_name'
]
[ , [ @table_schema = ]
N
'table_schema'
]
[ , [ @table_catalog = ]
N
'table_catalog'
]
[ , [ @column_name = ]
N
'column_name'
]
[ , [ @
ODBCV er = ]
ODBCV er ]
[ ; ]
```

## Examples

### Example 1

`SS_DATA_TYPE`

### Example 2

`sp_columns_ex`

### Example 3

`COLUMNS`

### Example 4

`IDBSchemaRowset`

### Example 5

`sp_columns_ex`

### Example 6

`COLUMNS`

### Example 7

`IDBSchemaRowset`

### Example 8

`sp_columns_ex`

### Example 9

`SELECT`

### Example 10

`JobTitle`

_(. and 4 more examples)_
