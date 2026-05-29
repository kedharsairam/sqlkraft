---
title: "Scalar-valued"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  A scalar-valued function (SVF) returns a single value, such as a string, integer, or bit value. You

  can create scalar-valued user-defined functions in
tags:
  - "clr-integration"
  - "scalar-valued"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

A scalar-valued function (SVF) returns a single value, such as a string, integer, or bit value. You

can create scalar-valued user-defined functions in managed code using any .NET Framework

programming language. These functions are accessible to Transact-SQL or other managed

code. For information about the advantages of common language runtime (CLR) integration

and choosing between managed code and Transact-SQL, see

CLR integration overview

.

.NET Framework SVFs are implemented as methods on a class in a .NET Framework assembly.

The input parameters and the type returned from an SVF can be any of the scalar data types

supported by SQL Server, except

,

,

,

,

,

,

,

, or

. SVFs must ensure a match between the SQL Server data type and the return

data type of the implementation method. For more information about type conversions, see

Map CLR parameter data

.

When you implement a .NET Framework SVF in a .NET Framework language, you can specify

the

custom attribute to include additional information about the function. The

attribute indicates whether or not the function accesses or modifies data, if it's

deterministic, and if the function involves floating point operations.

Scalar-valued user-defined functions might be deterministic or non-deterministic. A

deterministic function always returns the same result when it's called with a specific set of input

parameters. A non-deterministic function might return different results when it's called with a

specific set of input parameters.

７

Note

Don't mark a function as deterministic if the function doesn't always produces the same

output values, given the same input values and the same database state. Marking a

function as deterministic, when the function isn't truly deterministic can result in corrupted

indexed views and computed columns. You mark a function as deterministic by setting the

property to true.

```sql
SqlFunction
SqlFunction
IsDeterministic
```
