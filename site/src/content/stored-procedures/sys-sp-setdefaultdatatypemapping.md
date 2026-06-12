---
name: "sys.sp_setdefaultdatatypemapping"
title: "sp_setdefaultdatatypemapping"
category: "general"
description: "Marks an existing data type mapping between SQL Server and a non-SQL Server database management system (DBMS) as the default. This stored procedure is executed at the Identifies an existing data type mapping. , then the remaining parameters aren't required."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_setdefaultdatatypemapping
  [ [ @mapping_id = ] mapping_id ]
  [ , [ @source_dbms = ]
  N
  'source_dbms'
  ]
  [ , [ @source_version = ]
  'source_version'
  ]
  [ , [ @source_type = ]
  N
  'source_type'
  ]
  [ , [ @source_length_min = ] source_length_min ]
  [ , [ @source_length_max = ] source_length_max ]
  [ , [ @source_precision_min = ] source_precision_min ]
  [ , [ @source_precision_max = ] source_precision_max ]
  [ , [ @source_scale_min = ] source_scale_min ]
  [ , [ @source_scale_max = ] source_scale_max ]
  [ , [ @source_nullable = ] source_nullable ]
  [ , [ @destination_dbms = ]
  N
  'destination_dbms'
  ]
  [ , [ @destination_version = ]
  'destination_version'
  ]
  [ , [ @destination_type = ]
  N
  'destination_type'
  ]
  [ , [ @destination_length = ] destination_length ]
  [ , [ @destination_precision = ] destination_precision ]
  [ , [ @destination_scale = ] destination_scale ]
  [ , [ @destination_nullable = ] destination_nullable ]
  [ ; ]
---

## Description

Marks an existing data type mapping between SQL Server and a non-SQL Server database management system (DBMS) as the default. This stored procedure is executed at the Identifies an existing data type mapping. , then the remaining parameters aren't required.

## Syntax

```sql
sp_setdefaultdatatypemapping
[ [ @mapping_id = ] mapping_id ]
[ , [ @source_dbms = ]
N
'source_dbms'
]
[ , [ @source_version = ]
'source_version'
]
[ , [ @source_type = ]
N
'source_type'
]
[ , [ @source_length_min = ] source_length_min ]
[ , [ @source_length_max = ] source_length_max ]
[ , [ @source_precision_min = ] source_precision_min ]
[ , [ @source_precision_max = ] source_precision_max ]
[ , [ @source_scale_min = ] source_scale_min ]
[ , [ @source_scale_max = ] source_scale_max ]
[ , [ @source_nullable = ] source_nullable ]
[ , [ @destination_dbms = ]
N
'destination_dbms'
]
[ , [ @destination_version = ]
'destination_version'
]
[ , [ @destination_type = ]
N
'destination_type'
]
[ , [ @destination_length = ] destination_length ]
[ , [ @destination_precision = ] destination_precision ]
[ , [ @destination_scale = ] destination_scale ]
[ , [ @destination_nullable = ] destination_nullable ]
[ ; ]
```

## Permissions

Only members of the fixed server role can execute. Specify Data Type Mappings for an Oracle Publisher sp_getdefaultdatatypemapping (Transact-SQL) sp_helpdatatypemap (Transact-SQL)
