---
name: "sys.sp_getdefaultdatatypemapping"
title: "sp_getdefaultdatatypemapping"
category: "general"
description: "Returns information on the default mapping for the specified data type between SQL Server and a non-SQL Server database management system (DBMS). This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the DBMS from which the data types are mapped."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_getdefaultdatatypemapping [ @source_dbms = ]
  'source_dbms'
  [ , [ @source_version = ]
  'source_version'
  ]
  , [ @source_type = ]
  'source_type'
  [ , [ @source_length = ] source_length ]
  [ , [ @source_precision = ] source_precision ]
  [ , [ @source_scale = ] source_scale ]
  [ , [ @source_nullable = ] source_nullable ]
  , [ @destination_dbms = ]
  'destination_dbms'
  [ , [ @destination_version = ]
  'destination_version'
  ]
  [ , [ @destination_type = ]
  'destination_type'
  OUTPUT
  ]
  [ , [ @destination_length = ] destination_length
  OUTPUT
  ]
  [ , [ @destination_precision = ] destination_precision
  OUTPUT
  ]
  [ , [ @destination_scale = ] destination_scale
  OUTPUT
  ]
  [ , [ @destination_nullable = ] source_nullable
  OUTPUT
  ]
  [ , [ @dataloss = ] dataloss
  OUTPUT
  ]
  [ ; ]
---

## Description

Returns information on the default mapping for the specified data type between SQL Server and a non-SQL Server database management system (DBMS). This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the DBMS from which the data types are mapped. can be one of the following values:

## Syntax

```sql
sp_getdefaultdatatypemapping [ @source_dbms = ]
'source_dbms'
[ , [ @source_version = ]
'source_version'
]
, [ @source_type = ]
'source_type'
[ , [ @source_length = ] source_length ]
[ , [ @source_precision = ] source_precision ]
[ , [ @source_scale = ] source_scale ]
[ , [ @source_nullable = ] source_nullable ]
, [ @destination_dbms = ]
'destination_dbms'
[ , [ @destination_version = ]
'destination_version'
]
[ , [ @destination_type = ]
'destination_type'
OUTPUT
]
[ , [ @destination_length = ] destination_length
OUTPUT
]
[ , [ @destination_precision = ] destination_precision
OUTPUT
]
[ , [ @destination_scale = ] destination_scale
OUTPUT
]
[ , [ @destination_nullable = ] source_nullable
OUTPUT
]
[ , [ @dataloss = ] dataloss
OUTPUT
]
[ ; ]
```
