---
title: "Nonfoldable expressions"
topic: "io-fundamentals"
description: "compilation so that the resulting execution plan is more efficient. This is referred to as constant"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

compilation so that the resulting execution plan is more efficient. This is referred to as constant

folding. A constant is a Transact-SQL literal, such as

,

,

,

, or

. For example, take this query:

Here, 30 \* 12 is a constant expression. SQL Server can evaluate this during compilation and

rewrite the query internally as:

SQL Server uses constant folding with the following types of expressions:

Arithmetic expressions, such as

and

, that contain only constants.

Logical expressions, such as

and

, that contain only constants.

Built-in functions that are considered foldable by SQL Server, including

and

. Generally, an intrinsic function is foldable if it is a function of its inputs only and

not other contextual information, such as SET options, language settings, database

options, and encryption keys. Nondeterministic functions aren't foldable. Deterministic

built-in functions are foldable, with some exceptions.

Deterministic methods of CLR user-defined types and deterministic scalar-valued CLR

user-defined functions (starting with SQL Server 2012 (11.x)). For more information, see

Constant Folding for CLR User-Defined Functions and Methods

.

All other expression types aren't foldable. In particular, the following types of expressions

aren't foldable:

７

Note

An exception is made for large object types. If the output type of the folding process is a

large object type (text,ntext, image, nvarchar(max), varchar(max), varbinary(max), or XML),

then SQL Server does not fold the expression.

```sql
3
```

```sql
'ABC'
```

```sql
'2005-12-31'
```

```sql
1.0e3
```

```sql
0x12345678
```

```sql
1 + 1
```

```sql
5 / 3 * 2
```

```sql
1 = 1
```

```sql
1 > 2 AND 3 > 4
```

`CAST`

`CONVERT`

```sql
SELECT
*
FROM
Orders
WHERE
OrderDate <
DATEADD (
day
, 30 * 12,
'2020-01-01'
);
SELECT
*
FROM
Orders
WHERE
OrderDate <
DATEADD (
day
, 360,
'2020-01-01'
);
```
