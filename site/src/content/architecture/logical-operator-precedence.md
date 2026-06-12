---
title: "Logical operator precedence"
topic: "transaction-log"
description: "When it was first introduced, batch mode execution was closely integrated with, and optimized"
tags: ["transaction-log","architecture"]
pubDate: 2026-05-29
---

When it was first introduced, batch mode execution was closely integrated with, and optimized

around, the columnstore storage format. However, starting with SQL Server 2019 (15.x) and in

, batch mode execution no longer requires columnstore indexes. For more

information, see

Batch mode on rowstore.

Batch mode processing operates on compressed data when possible, and eliminates the

exchange operator

used by row mode execution. The result is better parallelism and faster

performance.

When a query is executed in batch mode, and accesses data in columnstore indexes, the

execution tree operators and child operators read multiple rows together in column segments.

reads only the columns required for the result, as referenced by a SELECT

statement, JOIN predicate, or filter predicate. For more information on columnstore indexes,

see

Columnstore Index Architecture.

Processing a single Transact-SQL statement is the most basic way that SQL Server executes

Transact-SQL statements. The steps used to process a single

statement that references

only local base tables (no views or remote tables) illustrates the basic process.

When more than one logical operator is used in a statement,

is evaluated first, then

,

and finally. Arithmetic, and bitwise, operators are handled before logical operators. For

more information, see

Operator Precedence.

In the following example, the color condition pertains to product model 21, and not to product

model 20, because

has precedence over.

７

Note

Batch mode execution is very efficient Data Warehousing scenarios, where large amounts

of data are read and aggregated.

SQL statement processing

`SELECT`

`NOT`

`AND`

`OR`

`AND`

`OR`

```sql
SELECT
ProductID, ProductModelID
FROM
Production.Product
WHERE
ProductModelID = 20
OR
ProductModelID = 21
AND
Color =
'Red'
;
GO
```
