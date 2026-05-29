---
name: "Expression results"
title: "Expression results"
category: "statements"
description: "Unary operators can be applied only to expressions that evaluate to any one of the data types"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL

Unary operators can be applied only to expressions that evaluate to any one of the data types

of the numeric data type category. Is an operator that has only one numeric operand:

indicates a positive number

indicates a negative number

indicates the one's complement operator

An operator that defines the way two expressions are combined to yield a single result.

binary_operator

can be an arithmetic operator, the assignment operator (

), a bitwise operator,

a comparison operator, a logical operator, the string concatenation operator (

), or a unary

operator. For more information about operators, see

Operators

.

Any Transact-SQL ranking function. For more information, see

Ranking Functions

.

Any Transact-SQL aggregate function with the OVER clause. For more information, see

SELECT -

OVER clause

.

For a simple expression made up of a single constant, variable, scalar function, or column

name: the data type, collation, precision, scale, and value of the expression is the data type,

collation, precision, scale, and value of the referenced element.

When two expressions are combined by using comparison or logical operators, the resulting

data type is Boolean and the value is either:

,

, or

. For more information

about Boolean data types, see

Comparison Operators

.

```sql
+
```

```sql
-
```

```sql
~
```

```sql
=
```

```sql
+
```

```sql
TRUE
```

```sql
FALSE
```

```sql
UNKNOWN
```

```sql
SELECT
MAX
(UnitPrice)
FROM
Products;
```
