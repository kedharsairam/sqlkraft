---
name: 'sys.sp_stored_procedures'
title: 'sp_stored_procedures'
category: 'general'
description: 'Returns a list of stored procedures in the current environment. Transact-SQL syntax conventions The name of the procedure used to return catalog information. . Wildcard pattern matching is supported. The name of the schema to which the procedure belongs. . Wildcard pattern matching is supported. If default procedure visibility rules of the underlying database management system (DBMS) In SQL Server'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_stored_procedures
  [ [ @sp_name = ]
  N
  'sp_name'
  ]
  [ , [ @sp_owner = ]
  N
  'sp_owner'
  ]
  [ , [ @sp_qualifier = ]
  N
  'sp_qualifier'
  ]
  [ , [ @f
  U
  se
  P
  attern = ] f
  U
  se
  P
  attern ]
  [ ; ]
---

## Description

Returns a list of stored procedures in the current environment. Transact-SQL syntax conventions The name of the procedure used to return catalog information. . Wildcard pattern matching is supported. The name of the schema to which the procedure belongs. . Wildcard pattern matching is supported. If default procedure visibility rules of the underlying database management system (DBMS) In SQL Server, if the current schema contains a procedure with the specified name, that

## Syntax

```sql
sp_stored_procedures
[ [ @sp_name = ]
N
'sp_name'
]
[ , [ @sp_owner = ]
N
'sp_owner'
]
[ , [ @sp_qualifier = ]
N
'sp_qualifier'
]
[ , [ @f
U
se
P
attern = ] f
U
se
P
attern ]
[ ; ]
```
