---
name: "sys.sp_describe_cursor"
title: "sp_describe_cursor"
category: "general"
description: "A data type for variables or stored procedure OUTPUT parameters that contain a reference to a The operations that can reference variables and parameters having a @local_variable @local_variable The OPEN, FETCH, CLOSE, and DEALLOCATE cursor statements. Stored procedure output parameters. The CURSOR_STATUS function. syste"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_describe_cursor
  [ @cursor_return = ] cursor_return
  OUTPUT
  , [ @cursor_source = ] {
  N
  'local'
  |
  N
  'global'
  |
  N
  '*cursor_source*'
  }
  , [ @cursor_identity = ]
  N
  'cursor_identity'
  [ ; ]
---

## Description

A data type for variables or stored procedure OUTPUT parameters that contain a reference to a The operations that can reference variables and parameters having a @local_variable @local_variable The OPEN, FETCH, CLOSE, and DEALLOCATE cursor statements. Stored procedure output parameters. The CURSOR_STATUS function. system stored procedures. output column of returns the name of the cursor variable. Any variables created with the data type are nullable. data type cannot be used for a column in a CREATE TABLE statement. CAST and CONVERT (Transact-SQL) CURSOR_STATUS (Transact-SQL) Data Type Conversion (Database Engine) Data Types (Transact-SQL) DECLARE CURSOR (Transact-SQL) DECLARE @local_variable (Transact-SQL) SET @local_variable (Transact-SQL)

## Syntax

```sql
sp_describe_cursor
[ @cursor_return = ] cursor_return
OUTPUT
, [ @cursor_source = ] {
N
'local'
|
N
'global'
|
N
'*cursor_source*'
}
, [ @cursor_identity = ]
N
'cursor_identity'
[ ; ]
```

## Remarks

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

A data type for variables or stored procedure OUTPUT parameters that contain a reference to a

The operations that can reference variables and parameters having a

data type are:

The DECLARE

@local_variable

@local_variable

statements.

The OPEN, FETCH, CLOSE, and DEALLOCATE cursor statements.

Stored procedure output parameters.

The CURSOR_STATUS function.

system stored procedures.

output column of

returns the name of

the cursor variable.

Any variables created with the

data type are nullable.

data type cannot be used for a column in a CREATE TABLE statement.

CAST and CONVERT (Transact-SQL)

CURSOR_STATUS (Transact-SQL)

Data Type Conversion (Database Engine)

Data Types (Transact-SQL)

DECLARE CURSOR (Transact-SQL)

DECLARE @local_variable (Transact-SQL)

SET @local_variable (Transact-SQL)
