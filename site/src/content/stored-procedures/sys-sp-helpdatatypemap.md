---
name: 'sys.sp_helpdatatypemap'
title: 'sp_helpdatatypemap'
category: 'general'
description: 'Returns information on the defined data type mappings between SQL Server and non-SQL Server database management systems (DBMS). This stored procedure is executed at the Transact-SQL syntax conventions The name of the DBMS from which the data types are mapped. can be one of the following values. The source is a SQL Server database. The source is an Oracle database.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpdatatypemap
  [ @source_dbms = ]
  N
  'source_dbms'
  [ , [ @source_version = ]
  'source_version'
  ]
  [ , [ @source_type = ]
  N
  'source_type'
  ]
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
  [ , [ @defaults_only = ] defaults_only ]
  [ ; ]
---

## Description

Returns information on the defined data type mappings between SQL Server and non-SQL Server database management systems (DBMS). This stored procedure is executed at the Transact-SQL syntax conventions The name of the DBMS from which the data types are mapped. can be one of the following values. The source is a SQL Server database. The source is an Oracle database.

## Syntax

```sql
sp_helpdatatypemap
[ @source_dbms = ]
N
'source_dbms'
[ , [ @source_version = ]
'source_version'
]
[ , [ @source_type = ]
N
'source_type'
]
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
[ , [ @defaults_only = ] defaults_only ]
[ ; ]
```
