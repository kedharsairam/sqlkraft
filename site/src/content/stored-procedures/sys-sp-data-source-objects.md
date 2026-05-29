---
name: 'sys.sp_data_source_objects'
title: 'sp_data_source_objects'
category: 'general'
description: 'Returns list of table objects that are available to be virtualized. Transact-SQL syntax conventions The name of the external data source to get the metadata from. The root of the name of the object or objects to search for. This call only returns external objects that begin with the value set for If an ODBC data source connects to a relational database management system (RDBMS) that can''t contain '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_data_source_objects
  [ @data_source = ]
  N
  'data_source'
  [ , [ @object_root_name = ]
  N
  'object_root_name'
  ]
  [ , [ @max_search_depth = ] max_search_depth ]
  [ , [ @search_options = ]
  N
  'search_options'
  ]
  [ ; ]
---

## Description

Returns list of table objects that are available to be virtualized. Transact-SQL syntax conventions The name of the external data source to get the metadata from. The root of the name of the object or objects to search for. This call only returns external objects that begin with the value set for If an ODBC data source connects to a relational database management system (RDBMS) that can't contain a partial database name. In these

## Syntax

```sql
sys.sp_data_source_objects
[ @data_source = ]
N
'data_source'
[ , [ @object_root_name = ]
N
'object_root_name'
]
[ , [ @max_search_depth = ] max_search_depth ]
[ , [ @search_options = ]
N
'search_options'
]
[ ; ]
```

## Examples

### Example 1

```sql
DATABASE
"database"
database
NULL
SCHEMA
"database"."dbo"
dbo
NULL
TABLE
"database"."dbo"."customer"
customer
[database].[dbo].[customer]
TABLE
"database"."dbo"."item"
item
[database].[dbo].[item]
TABLE
"database"."dbo"."nation"
nation
[database].[dbo].[nation]
```

### Example 2

```sql
DECLARE
@data_source
AS
SYSNAME = N
'ExternalDataSourceName'
;
DECLARE
@object_root_name
AS
NVARCHAR
(
MAX
) =
NULL
;
DECLARE
@max_search_depth
AS
INT
= 3;
EXECUTE
sp_data_source_objects
@data_source,
@object_root_name,
@max_search_depth;
```

### Example 3

```sql
DECLARE
@data_source
AS
SYSNAME = N
'ExternalDataSourceName'
;
DECLARE
@object_root_name
AS
NVARCHAR
(
MAX
) =
NULL
;
EXECUTE
sp_data_source_objects
@data_source,
@object_root_name;
```
