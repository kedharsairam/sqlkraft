---
name: "sys.sp_oamethod"
title: "sp_OAMethod"
category: "general"
description: "Calls a method of an OLE object. The object token of an OLE object that was previously created by using The method name of the OLE object to call. The return value of the method of the OLE object. If specified, it must be a local variable of the Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered o"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_
  OAM
  ethod objecttoken , methodname
  [ , returnvalue
  OUTPUT
  ]
  [ , [ @parametername = ] parameter [
  OUTPUT
  ] [ ...n ] ]
  [ ; ]
---

## Description

Calls a method of an OLE object. The object token of an OLE object that was previously created by using The method name of the OLE object to call. The return value of the method of the OLE object. If specified, it must be a local variable of the Arguments for extended stored procedures must be entered in the specific order as section.

## Syntax

```sql
sp_
OAM ethod objecttoken , methodname
[ , returnvalue
OUTPUT
]
[ , [ @parametername = ] parameter [
OUTPUT
] [.n ] ]
[ ; ]
```

## Permissions

columns. A two-dimensional array is returned to the client as a result set with as many columns as there are elements in the first dimension of the array and with as many rows as there are elements in the second dimension of the array. In other words, the array is returned as (columns, rows). When a property return value or method return value is an array, or returns a result set to the client. (Method output parameters can't be arrays.) These procedures scan all the data values in the array to determine the appropriate SQL Server data types and data lengths to use for each column in the result set. For a particular column, these procedures use the data type and length required to represent all data values in that column. When all data values in a column share the same data type, that data type is used for the whole column. When data values in a column are of different data types, the data type of the whole column is chosen based on the following chart. You can also use to get a property value. Requires membership in the fixed server role or execute permission directly on this stored procedure. The Ole Automation Procedures server configuration option must be enabled to use any system procedure related to OLE Automation. ﾉ Expand table
