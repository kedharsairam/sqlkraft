---
name: 'sys.sp_cursor_list'
title: 'sp_cursor_list'
category: 'general'
description: 'Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric A data type for variables or stored procedure OUTPUT parameters that contain a reference to a The operations that can reference variables and parameters having a @local_variable @local_variable The OPEN, FETCH, CLOSE, and DEALLOCATE cursor statements. Stored procedure output parameters. The CURSOR_STATUS function. syste'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_cursor_list
  [ @cursor_return = ] cursor_return
  OUTPUT
  , [ @cursor_scope = ] cursor_scope
  [ ; ]
---

## Description

Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric A data type for variables or stored procedure OUTPUT parameters that contain a reference to a The operations that can reference variables and parameters having a @local_variable @local_variable The OPEN, FETCH, CLOSE, and DEALLOCATE cursor statements. Stored procedure output parameters. The CURSOR_STATUS function. system stored procedures. output column of returns the name of the cursor variable. Any variables created with the data type are nullable. data type cannot be used for a column in a CREATE TABLE statement. CAST and CONVERT (Transact-SQL) CURSOR_STATUS (Transact-SQL) Data Type Conversion (Database Engine) Data Types (Transact-SQL) DECLARE CURSOR (Transact-SQL) DECLARE @local_variable (Transact-SQL) SET @local_variable (Transact-SQL)

## Syntax

```sql
sp_cursor_list
[ @cursor_return = ] cursor_return
OUTPUT
, [ @cursor_scope = ] cursor_scope
[ ; ]
```

## Remarks

Applies to:

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

Last updated on 11/18/2025

## Examples

### Example 1

```sql
sp_cursor_list
```

### Example 2

```sql
sp_cursor_list
```

### Example 3

```sql
SQLSetCursorName
```

### Example 4

```sql
sp_describe_cursor_columns
```

### Example 5

```sql
sp_describe_cursor_tables
```

### Example 6

```sql
sp_describe_cursor
```

### Example 7

```sql
sp_cursor_list
```

### Example 8

```sql
sp_cursor_list
```

### Example 9

```sql
USE
AdventureWorks2022;
GO
-- Declare and open a keyset-driven cursor.
DECLARE
abc
CURSOR
KEYSET
FOR
SELECT
LastName
FROM
Person.Person
WHERE
LastName
LIKE
'S%'
;
OPEN abc;
-- Declare a cursor variable to hold the cursor output variable
-- from sp_cursor_list.
DECLARE
@Report
AS
CURSOR
;
-- Execute sp_cursor_list into the cursor variable.
EXECUTE
master.dbo.sp_cursor_list
@cursor_return = @Report
OUTPUT
,
@cursor_scope = 2;
```

### Example 10

```sql
-- Fetch all the rows from the sp_cursor_list output cursor.
FETCH NEXT FROM @Report;
WHILE (@@FETCH_STATUS <> -1)
BEGIN
FETCH
NEXT
FROM
@Report;
END
-- Close and deallocate the cursor from sp_cursor_list.
CLOSE
@Report;
DEALLOCATE
@Report;
GO
-- Close and deallocate the original cursor.
CLOSE abc;
DEALLOCATE
abc;
GO
```
