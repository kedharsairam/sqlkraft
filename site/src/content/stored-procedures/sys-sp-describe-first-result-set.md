---
name: "sys.sp_describe_first_result_set"
title: "sp_describe_first_result_set"
category: "general"
description: "Position of this column in ORDER BY list Returns NULL if the column does not appear in the ORDER BY list or if the ORDER BY list cannot be uniquely Length of the ORDER BY list. Returns NULL if there is no ORDER BY list or if the ORDER BY list cannot be uniquely determined. Note that this value will be the same for all rows returned by sp_describe_first_result_set. If the ordinal_in_order_by_list i"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_describe_first_result_set [ @tsql = ]
              N
              'tsql'
              [ , [ @params = ]
              N
              '@parameter_name data_type [ , ... n ]'
              ]
              [ , [ @browse_information_mode = ]
              <tinyint>
              ]
              [ ; ]
---

## Description

Position of this column in ORDER BY list Returns NULL if the column does not appear in the ORDER BY list or if the ORDER BY list cannot be uniquely Length of the ORDER BY list. Returns NULL if there is no ORDER BY list or if the ORDER BY list cannot be uniquely determined. Note that this value will be the same for all rows returned by sp_describe_first_result_set. If the ordinal_in_order_by_list is not NULL, the column reports the direction of the ORDER BY clause for this column. Otherwise it Contains the error number returned by the function. Contains NULL if no error occurred in the column. Contains the severity returned by the function. Contains NULL if no error occurred in the column. Contains the state message returned by the function. If no error occurred. the column will contain NULL.

## Syntax

```sql
sp_describe_first_result_set [ @tsql = ]
N
'tsql'
[ , [ @params = ]
N
'@parameter_name data_type [ ,. n ]'
]
[ , [ @browse_information_mode = ]
<tinyint>
]
[ ; ]
```

## Permissions

## Remarks

Position of this column in ORDER BY list Returns

NULL if the column does not appear in the ORDER BY

list or if the ORDER BY list cannot be uniquely

determined.

Length of the ORDER BY list. Returns NULL if there is

no ORDER BY list or if the ORDER BY list cannot be

uniquely determined. Note that this value will be the

same for all rows returned by

sp_describe_first_result_set.

If the ordinal_in_order_by_list is not NULL, the

column reports the direction

of the ORDER BY clause for this column. Otherwise it

reports NULL.

Contains the error number returned by the function.

Contains NULL if no error occurred in the column.

Contains the severity returned by the function.

Contains NULL if no error occurred in the column.

Contains the state message returned by the function.

If no error occurred. the column will contain NULL.

Contains the message returned by the function. If no

error occurred, the column will contain NULL.

Contains an integer representing the error being

returned. Maps to error_type_desc. See the list under

Contains a short uppercase string representing the

error being returned. Maps to error_type. See the list

under remarks.

This function uses the same algorithm as. For more information,

sp_describe_first_result_set (Transact-SQL)

The following table lists the error types and their descriptions

## Examples

### Example 1

```sql
0
```

### Example 2

```sql
EXECUTE sp_describe_first_result_set @tsql = N
'SELECT object_id, name, type_desc FROM sys.indexes'
;
EXECUTE sp_describe_first_result_set @tsql = N
'
SELECT object_id, name, type_desc
FROM sys.indexes
WHERE object_id = @id1'
, @params = N
'@id1 int'
;
```

### Example 3

```sql
CREATE
TABLE dbo.t (
a
INT
PRIMARY
KEY
,
b1
INT
);
GO
CREATE
VIEW dbo.v
AS
SELECT b1
AS b2
FROM dbo.t;
GO
EXECUTE sp_describe_first_result_set N
'SELECT b2 AS b3 FROM dbo.v'
,
NULL
, 0;
```
