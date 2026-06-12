---
title: "Examples of compile-time expression evaluation"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Specifically, the following built-in functions and special operators are evaluated at compile time

if all their inputs are known:

,

,

,

,

,

, and. The following operators are also evaluated at compile time if all their inputs are

known:

Arithmetic operators: +, -, \*, /, unary -

Logical Operators:

,

,

Comparison operators: <, >, <=, >=, <>,

,

,

No other functions or operators are evaluated by the Query Optimizer during cardinality

estimation.

Consider this stored procedure:

During optimization of the

statement in the procedure, the Query Optimizer tries to

evaluate the expected cardinality of the result set for the condition. The

expression

isn't constant-folded, because

is a parameter. However, at optimization

time, the value of the parameter is known. This allows the Query Optimizer to accurately

estimate the size of the result set, which helps it select a good query plan.

Now consider an example similar to the previous one, except that a local variable

replaces

in the query and the expression is evaluated in a SET statement instead of in the query.

`UPPER`

`LOWER`

`RTRIM`

```sql
DATEPART( YY only )
```

`GETDATE`

`CAST`

`CONVERT`

`AND`

`OR`

`NOT`

`LIKE`

```sql
IS NULL
```

```sql
IS NOT NULL
```

`SELECT`

```sql
OrderDate > @d+1
```

```sql
@d+1
```

```sql
@d
```

```sql
@d2
```

```sql
@d+1
```

```sql
USE
AdventureWorks2022;
GO
CREATE
PROCEDURE
MyProc( @d datetime )
AS
SELECT
COUNT (*)
FROM
Sales.SalesOrderHeader
WHERE
OrderDate > @d+1;
USE
AdventureWorks2022;
GO
CREATE
PROCEDURE
MyProc2( @d datetime )
AS
BEGIN
DECLARE
@d2 datetime
SET
@d2 = @d+1
SELECT
COUNT (*)
FROM
Sales.SalesOrderHeader
```
