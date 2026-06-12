---
name: "sys.sp_helpdatatypemap"
title: "sp_helpdatatypemap"
category: "general"
description: "Returns information on the defined data type mappings between SQL Server and non-SQL Server database management systems (DBMS). This stored procedure is executed at the The name of the DBMS from which the data types are mapped."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
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

Returns information on the defined data type mappings between SQL Server and non-SQL Server database management systems (DBMS). This stored procedure is executed at the The name of the DBMS from which the data types are mapped.

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
