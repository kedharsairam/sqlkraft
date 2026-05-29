---
name: 'sys.sp_getapplock'
title: 'sys.sp_getapplock'
category: 'general'
description: 'Summarize this article for me'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

An output parameter of type

, provided as indicated, to receive a string literal of

the parameter names and data types that are parameterized in

@templatetext

.


## returns an error when the following occur:
It doesn't parameterize any constant literal values in

@querytext

.

@querytext

is

, not a Unicode string, syntactically not valid, or can't be compiled.

If


## returns an error, it doesn't modify the values of the
@templatetext

and @parameters output parameters.

Requires membership in the

database role.

The following example returns the parameterized form of a query that contains two constant

literal values.

SQL

```sql
sp_get_query_template
```

```sql
NULL
```

```sql
sp_get_query_template
```

```sql
USE
AdventureWorks2022;
GO
DECLARE
@my_templatetext
AS
NVARCHAR
(
MAX
);
DECLARE
@my_parameters
AS
NVARCHAR
(
MAX
);
EXECUTE
sp_get_query_template N
'SELECT pi.ProductID, SUM(pi.Quantity) AS Total
FROM Production.ProductModel pm
INNER JOIN Production.ProductInventory pi
ON pm.ProductModelID = pi.ProductID
WHERE pi.ProductID = 2
GROUP BY pi.ProductID, pi.Quantity
HAVING SUM(pi.Quantity) > 400'
,
@my_templatetext
OUTPUT
,
@my_parameters
OUTPUT
;
SELECT
@my_templatetext;
SELECT
@my_parameters;
```
