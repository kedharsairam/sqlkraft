---
name: "Compare COALESCE and ISNULL"
title: "Compare COALESCE and ISNULL"
category: "language-elements"
description: ""
tags: ["tsql","language-elements"]
pubDate: 2026-05-29
---

If all arguments are

,

## returns. At least one of the null values must be a

typed.

The

expression is a syntactic shortcut for the

expression. That is, the code

is rewritten by the query optimizer as the following

expression:

As such, the input values (

expression1

,

expression2

,

expressionN

, and so on) are evaluated

multiple times. A value expression that contains a subquery is considered nondeterministic and

the subquery is evaluated twice. This result is in compliance with the SQL standard. In either

case, different results can be returned between the first evaluation and upcoming evaluations.

For example, when the code

is executed, the subquery is evaluated

twice. As a result, you can get different results depending on the isolation level of the query.

For example, the code can return

under the

isolation level in a multi-user

environment. To ensure stable results are returned, use the

isolation level,

or replace

with the

function. As an alternative, you can rewrite the query to

push the subquery into a subselect as shown in the following example:

The

function and the

expression have a similar purpose but can behave

differently.

1. Because

is a function, it's evaluated only once. As described previously, the input

values for the

expression can be evaluated multiple times.

2. Data type determination of the resulting expression is different.

uses the data

type of the first parameter, and

follows the

expression rules to return the

data type of value with the highest precedence.

3. The NULLability of the result expression is different for

and. The

return value is always considered not nullable (assuming the return value is a non-

nullable one). By contrast,

with non-null parameters is considered to be. So

the expressions

and

, although equal, have different

nullability values. These values make a difference if you're using these expressions in

computed columns, creating key constraints, or making the return value of a scalar user-

defined function (UDF) deterministic, so that it can be indexed as shown in the following

example:

4. Validations for

and

are also different. For example, a

value for

is converted to

though for

, you must provide a data type.

5.

takes only two parameters. By contrast

takes a variable number of

parameters.

`NULL`

`COALESCE`

`NULL`

`NULL`

`COALESCE`

`CASE`

```sql
COALESCE(<expression1>,.n)
```

`CASE`

```sql
COALESCE((subquery), 1)
```

`NULL`

```sql
READ COMMITTED
```

```sql
SNAPSHOT ISOLATION
```

`COALESCE`

`ISNULL`

`ISNULL`

`COALESCE`

```sql
CASE
WHEN (expression1 IS NOT NULL) THEN expression1
WHEN (expression2 IS NOT NULL) THEN expression2.
ELSE expressionN
END
SELECT
CASE
WHEN x
IS
NOT
NULL
THEN x
ELSE
1
END
FROM (
SELECT (
SELECT
Nullable
FROM
Demo
WHERE
SomeCol = 1)
AS x)
AS
T;
```

`ISNULL`

`COALESCE`

`ISNULL`

`COALESCE`

`CASE`

`ISNULL`

`COALESCE`

`ISNULL`

`COALESCE`

`NULL`

```sql
ISNULL(NULL, 1)
```

```sql
COALESCE(NULL, 1)
```

`ISNULL`

`COALESCE`

`NULL`

`ISNULL`

`COALESCE`

`ISNULL`

`COALESCE`

```sql
USE tempdb;
GO
-- This statement fails because the PRIMARY KEY cannot accept NULL values
-- and the nullability of the COALESCE expression for col2
-- evaluates to NULL.
CREATE
TABLE
#Demo (
col1
INT
NULL
,
col2
AS
COALESCE (col1, 0) PRIMARY
KEY
,
col3
AS
ISNULL (col1, 0)
);
-- This statement succeeds because the nullability of the
-- ISNULL function evaluates AS NOT NULL.
CREATE
TABLE
#Demo (
col1
INT
NULL
,
col2
AS
COALESCE (col1, 0),
col3
AS
ISNULL (col1, 0) PRIMARY
KEY
);
```
