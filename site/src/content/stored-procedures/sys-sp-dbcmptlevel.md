---
name: 'sys.sp_dbcmptlevel'
title: 'sp_dbcmptlevel'
category: 'general'
description: 'Sets certain database behaviors to be compatible with the specified version of SQL Server. Transact-SQL syntax conventions The name of the database for which the compatibility level is to be changed. Database names must conform to the rules for identifiers. The version of SQL Server with which the database is to be made compatible. is an OUTPUT parameter of type , and must be one of the following '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbcmptlevel
  [ [ @dbname = ]
  N
  'dbname'
  ]
  [ , [ @new_cmptlevel = ] new_cmptlevel
  OUTPUT
  ]
  [ ; ]
---

## Description

Sets certain database behaviors to be compatible with the specified version of SQL Server. Transact-SQL syntax conventions The name of the database for which the compatibility level is to be changed. Database names must conform to the rules for identifiers. The version of SQL Server with which the database is to be made compatible. is an OUTPUT parameter of type , and must be one of the following values:

## Syntax

```sql
sp_dbcmptlevel
[ [ @dbname = ]
N
'dbname'
]
[ , [ @new_cmptlevel = ] new_cmptlevel
OUTPUT
]
[ ; ]
```
