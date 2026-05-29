---
title: "Nullability & three-value logic comparisons"
topic: "clr-integration"
description: |
  Article
  
  •
  
  12/30/2024
  
  Applies to:
  
  SQL Server
  
  If you're familiar with the SQL Server data types, you find similar semantics and precision in the
  
  namespace in the .NET Framework. There are some dif
tags:
  - "clr-integration"
  - "nullability-three-value-logic-comparisons"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

If you're familiar with the SQL Server data types, you find similar semantics and precision in the

namespace in the .NET Framework. There are some differences, however,

and this article covers the most important of these differences.

A primary difference between native common language runtime (CLR) data types and SQL

Server data types is that the former don't allow for

values, while the latter provide full

semantics.

Comparisons are affected by

values. When you compare two values

and

, if either

or

is

, then some logical comparisons evaluate to an

value rather than true or

false.

The

namespace introduces a

type to represent this three-

value logic. Comparisons between any

return a

value type. The

value is represented by the null value of the

type. The properties

,

,

and

are provided to check the value of a

type.

All arithmetic operators (

,

,

,

,

), bitwise operators (

,

, and

), and most functions

return

if any of the operands or arguments of

are null. The

property

always returns a

or

value.

Decimal data types in the .NET Framework CLR have different maximum values than numeric

and decimal data types in SQL Server. In addition, in the .NET Framework CLR decimal data

types assume the maximum precision. In the CLR for SQL Server, however,

provides

SqlBoolean data type

```sql
System.Data.SqlTypes
NULL
NULL
NULL
x
y
x
y
NULL
UNKNOWN
System.Data.SqlTypes
SqlBoolean
SqlTypes
SqlBoolean
UNKNOWN
SqlBoolean
IsTrue
IsFalse
IsNull
SqlBoolean
+
-
*
/
%
~
&
|
NULL
SqlTypes
IsNull
true
false
SqlDecimal
```