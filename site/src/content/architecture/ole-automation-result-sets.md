---
title: "OLE automation result sets"
topic: "spatial-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  If an OLE Automation property or method returns data in an array with one or two dimensions,

  the array is returned to the client as a result set:

  A o
tags:
  - "spatial-data"
  - "ole-automation-result-sets"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

If an OLE Automation property or method returns data in an array with one or two dimensions,

the array is returned to the client as a result set:

A one-dimensional array is returned to the client as a single-row result set with as many

columns as there are elements in the array. For example, an array(10) is returned as a

single row of 10 columns.

A two-dimensional array is returned to the client as a result set with as many columns as

there are elements in the first dimension of the array and with as many rows as there are

elements in the second dimension of the array. For example, an array(2,3) is returned as 2

columns in 3 rows.

When a property return value or method return value is an array,

or

returns a result set to the client. (Method output parameters cannot be arrays.)

These procedures scan all the data values in the array to determine the appropriate SQL Server

data types and data lengths to use for each column in the result set. For a particular column,

these procedures use the data type and length required to represent all data values in that

column.

When all data values in a column share the same data type, that data type is used for the whole

column. When data values in a column are different data types, the data type of the whole

column is chosen based on the following table. To use the following table, find one data type

along the left row axis and a second data type along the top column axis. The intersection of

the row and column describes the data type of the result set column.

ﾉ

Expand table

```sql
sp_OAGetProperty sp_OAMethod
```
