---
name: "sys.sp_data_source_table_columns"
title: "sp_data_source_table_columns"
category: "general"
description: "Returns a list of columns in external data source table. Transact-SQL syntax conventions The name of the external data source to get the metadata from. The table location string that identifies the table. Identified for informational purposes only. Not supported. Future compatibility is not This procedure is introduced in"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_data_source_table_columns
  [ @data_source = ]
  N
  'data_source'
  , [ @table_location = ]
  N
  'table_location'
  [ , [ @column_name = ]
  N
  'column_name'
  ]
  [ , [ @search_options = ]
  N
  'search_options'
  ]
  [ ; ]
---

## Description

Returns a list of columns in external data source table. Transact-SQL syntax conventions The name of the external data source to get the metadata from. The table location string that identifies the table. Identified for informational purposes only. Not supported. Future compatibility is not This procedure is introduced in

## Syntax

```sql
sys.sp_data_source_table_columns
[ @data_source = ]
N
'data_source'
, [ @table_location = ]
N
'table_location'
[ , [ @column_name = ]
N
'column_name'
]
[ , [ @search_options = ]
N
'search_options'
]
[ ; ]
```

## Examples

### Example 1

```sql
sp_data_source_table_columns
```

### Example 2

```sql
sp_data_source_table_columns
```

### Example 3

```sql
server
```

### Example 4

```sql
schema
```

### Example 5

```sql
DECLARE
@data_source
AS
SYSNAME = N
'ExternalDataSourceName'
;
DECLARE
@table_location
AS
NVARCHAR
(400) = N
'[database].[schema].[table]'
;
EXECUTE
sp_data_source_table_columns
@data_source,
@table_location;
```
