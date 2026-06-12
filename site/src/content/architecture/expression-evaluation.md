---
title: "Expression evaluation"
topic: "io-fundamentals"
description: "Nonconstant expressions such as an expression whose result depends on the value of a"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Nonconstant expressions such as an expression whose result depends on the value of a

column.

Expressions whose results depend on a local variable or parameter, such as @x.

Nondeterministic functions.

User-defined Transact-SQL functions.

Expressions whose results depend on language settings.

Expressions whose results depend on SET options.

Expressions whose results depend on server configuration options.

Before SQL Server 2012 (11.x), deterministic scalar-valued CLR user-defined functions and

methods of CLR user-defined types were not foldable.

Consider the following query:

If the

database option isn't set to

for this query, then the expression

is evaluated and replaced by its result,

, before the query is

compiled. Benefits of this constant folding include the following:

The expression doesn't have to be evaluated repeatedly at run time.

The value of the expression after it is evaluated is used by the Query Optimizer to

estimate the size of the result set of the portion of the query.

On the other hand, if

is a scalar user-defined function, the expression

isn't

folded, because SQL Server doesn't fold expressions that involve user-defined functions, even if

they are deterministic. For more information on parameterization, see

Forced Parameterization

later in this article.

In addition, some expressions that aren't constant folded but whose arguments are known at

compile time, whether the arguments are parameters or constants, are evaluated by the result-

set size (cardinality) estimator that is part of the optimizer during optimization.

1

1

`PARAMETERIZATION`

`FORCED`

```sql
117.00 + 1000.00
```

```sql
1117.00
```

```sql
TotalDue > 117.00 +
1000.00
```

`dbo.f`

`dbo.f(100)`

```sql
SELECT
*
FROM
Sales.SalesOrderHeader
AS s
INNER
JOIN
Sales.SalesOrderDetail
AS d
ON s.SalesOrderID = d.SalesOrderID
WHERE
TotalDue > 117.00 + 1000.00;
```
