---
title: "Invoking functions"
topic: "clr-integration"
description: |
  Applies to:

  SQL Server

  In Transact-SQL

  statements, you can invoke common language runtime (CLR) user-

  defined aggregates, subject to all the rules that apply to system aggregate functions.

  The fo
tags:
  - "clr-integration"
  - "invoking-functions"
pubDate: 2025-12-01
---

Applies to:

SQL Server

In Transact-SQL

statements, you can invoke common language runtime (CLR) user-

defined aggregates, subject to all the rules that apply to system aggregate functions.

The following additional rules apply:

The current user must have

permission on the user-defined aggregate.

User-defined aggregates must be invoked by using a two-part name in the form of

<schema_name>.<udagg_name>.

The argument type of the user-defined aggregate must match or be implicitly convertible

to the

input_type

of the aggregate, as defined in the

statement.

The return type of the user-defined aggregate must match the

return_type

in the

statement.

The following code is an example of a user-defined aggregate function that concatenates a set

of string values taken from a column in a table:

C#

```sql
SELECT
EXECUTE
CREATE AGGREGATE
CREATE
AGGREGATE
using
System;
using
System.Data;
using
Microsoft.SqlServer.Server;
using
System.Data.SqlTypes;
using
System.IO;
using
System.Text;
[
Serializable
]
[
SqlUserDefinedAggregate(
Format.UserDefined, //use clr serialization to serialize the intermediate
result
```
