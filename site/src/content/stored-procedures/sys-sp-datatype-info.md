---
name: "sys.sp_datatype_info"
title: "sp_datatype_info"
category: "general"
description: "Returns information about the data types supported by the current environment. The code number for the specified data type. list of all data types, omit this parameter. The version of ODBC that is used."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_datatype_info
  [ [ @data_type = ] data_type ]
  [ , [ @
  ODBCV
  er = ]
  ODBCV
  er ]
  [ ; ]
---

## Description

Returns information about the data types supported by the current environment. The code number for the specified data type. list of all data types, omit this parameter. The version of ODBC that is used.

## Syntax

```sql
sp_datatype_info
[ [ @data_type = ] data_type ]
[ , [ @
ODBCV er = ]
ODBCV er ]
[ ; ]
```

## Examples

### Example 1

`sp_datatype_info`

### Example 2

`SQLGetTypeInfo`

### Example 3

`DATA_TYPE`

### Example 4

```sql
-9
```

### Example 5

```sql
USE master
;
GO
EXECUTE sp_datatype_info -9;
GO
```
