---
name: 'Boolean Data Type'
title: 'Boolean Data Type'
category: 'data-types'
description: 'Azure SQL Managed Instance'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Comparison operators test whether two expressions are the same. Comparison operators can

be used on all expressions except expressions of the

,

, or

data types. The

following table lists the Transact-SQL comparison operators.

= (Equals)

Equal to

> (Greater Than)

Greater than

< (Less Than)

Less than

>= (Greater Than or Equal To)

Greater than or equal to

<= (Less Than or Equal To)

Less than or equal to

<> (Not Equal To)

Not equal to

!= (Not Equal To)

Not equal to (not ISO standard)

!< (Not Less Than)

Not less than (not ISO standard)

!> (Not Greater Than)

Not greater than (not ISO standard)

The result of a comparison operator has the

data type. This has three values: TRUE,

FALSE, and UNKNOWN. Expressions that return a

data type are known as Boolean

expressions.

Unlike other SQL Server data types, a

data type cannot be specified as the data type

of a table column or variable, and cannot be returned in a result set.

When SET ANSI_NULLS is ON, an operator that has one or two NULL expressions returns

UNKNOWN. When SET ANSI_NULLS is OFF, the same rules apply, except for the equals (=) and

not equals (<>) operators. When SET ANSI_NULLS is OFF, these operators treat NULL as a

known value, equivalent to any other NULL, and only return TRUE or FALSE (never UNKNOWN).

ﾉ

Expand table

### Boolean

Expressions with

data types are used in the WHERE clause to filter the rows that

qualify for the search conditions and in control-of-flow language statements such as IF and

WHILE, for example:


## syntaxsql
Expressions (Transact-SQL)

Operators (Transact-SQL)

Last updated on 11/18/2025

See Also

```sql
-- Uses AdventureWorks
DECLARE
@
M
y
P
roduct
INT
;
SET
@
M
y
P
roduct = 750;
IF
(@
M
y
P
roduct
<>
0)
SELECT
P
roduct
ID
,
N
ame,
P
roduct
N
umber
FROM
P
roduction.
P
roduct
WHERE
P
roduct
ID
= @
M
y
P
roduct;
```
