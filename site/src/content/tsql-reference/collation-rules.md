---
name: "Collation rules"
title: "Collation rules"
category: "statements"
description: "Indicates that the value of an expression is the result of an operation between two strings"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Indicates that the value of an expression is the result of an operation between two strings

that have conflicting collations of the implicit collation label. The expression result is

defined as not having a collation.

The collation label of a simple expression that references only one character string object is the

collation label of the referenced object.

The collation label of a complex expression that references two operand expressions with the

same collation label is the collation label of the operand expressions.

The collation label of the final result of a complex expression that references two operand

expressions with different collations is based on the following rules:

Explicit takes precedence over implicit. Implicit takes precedence over Coercible-default:

Explicit > Implicit > Coercible-default

Combining two Explicit expressions that have been assigned different collations generates

an error:

Explicit X + Explicit Y = Error

Combining two Implicit expressions that have different collations yields a result of No-

collation:

Implicit X + Implicit Y = No-collation

Combining an expression with No-collation with an expression of any label, except

Explicit collation (see the following rule), yields a result that has the No-collation label:

No-collation + anything = No-collation

Combining an expression with No-collation with an expression that has an Explicit

collation, yields an expression with an Explicit label:

No-collation + Explicit X = Explicit

The following table summarizes the rules.

Expand table

#### Operand coercion

#### label

#### Explicit X

#### Implicit X

#### Coercible-default

#### No-collation

Generates Error

Result is Explicit Y

Result is Explicit Y

Result is Explicit Y

Result is Explicit

X

Result is No-

collation

Result is Implicit Y

Result is No-

collation

Result is Explicit

X

Result is Implicit

X

Result is Coercible-

default

Result is No-

collation

Result is Explicit

X

Result is No-

collation

Result is No-collation

Result is No-

collation

The following additional rules also apply to collation precedence:

You can't have multiple

clauses on an expression that is already an explicit

expression. For example, the following

clause isn't valid because a

clause

is specified for an expression that is already an explicit expression:

Code page conversions for

data types aren't allowed. You can't cast a

expression

from one collation to another if they have the different code pages. The assignment

operator can't assign values when the collation of the right text operand has a different

code page than the left text operand.

Collation precedence is determined after data type conversion. The operand from which the

resulting collation is taken can be different from the operand that supplies the data type of the

final result. For example, consider the following batch:

７

Note

The

data type isn't supported in Fabric Warehouse, but most examples in this

article are applicable to both

using UTF-8 and

, and so remain applicable

## Examples of collation rules

## Collation conflict and error

The Unicode data type of the simple expression

has a higher data type precedence.

Therefore, the resulting expression has the Unicode data type assigned to. However,

the expression

has a collation label of Implicit, and

has a lower coercion label

of Coercible-default. Therefore, the collation that is used is the

collation of.

The following examples show how the collation rules work. To run the examples, create the

following test table.

The predicate in the following query has collation conflict and generates an error.

Here's the result set.

Output

to Fabric Warehouse unless otherwise noted.

## Explicit label vs. Implicit label

## No-collation labels

The predicate in the following query is evaluated in collation

because the right

expression has the Explicit label. This takes precedence over the Implicit label of the left

expression.

Here's the result set.

Output

The

expressions in the following queries have a No-collation label; therefore, they can't

appear in the select list or be operated on by collation-sensitive operators. However, the

expressions can be operated on by collation-insensitive operators.

Here's the result set.

Output

７

Note

Because of the difference between the behavior of

and

in a UTF-8

collation, this example doesn't apply in Fabric Warehouse.

```sql
No-
collation
```

```sql
Explicit Y
```

```sql
Implicit Y
```

```sql
Coercible-default
```

```sql
No-collation
```

`COLLATE`

`WHERE`

`COLLATE`

```sql
WHERE ColumnA = ( 'abc' COLLATE French_CI_AS) COLLATE French_CS_AS
```

```sql
CREATE
TABLE
TestTab (
PrimaryKey
INT
PRIMARY
KEY
,
CharCol
CHAR (10)
COLLATE
French_CI_AS
);
SELECT
*
FROM
TestTab
WHERE
CharCol
LIKE
N
'abc'
;
```

```sql
N'abc'
```

```sql
N'abc'
```

`CharCol`

```sql
N'abc'
```

`French_CI_AS`

`CharCol`

```sql
USE tempdb;
GO
CREATE
TABLE
TestTab (
id
INT
,
GreekCol
NVARCHAR (10)
COLLATE greek_ci_as,
LatinCol
NVARCHAR (10)
COLLATE latin1_general_cs_as
);
INSERT
TestTab
VALUES (1, N
'A'
, N
'a'
);
GO
```

```sql
SELECT
*
FROM
TestTab
WHERE
GreekCol = LatinCol;
Msg 448, Level 16, State 9, Line 2
Cannot resolve collation conflict between 'Latin1_General_CS_AS' and 'Greek_CI_AS'
```

`greek_ci_as`

`CASE`

```sql
in equal to operation.
```

```sql
SELECT
*
FROM
TestTab
WHERE
GreekCol = LatinCol
COLLATE greek_ci_as;
id GreekCol LatinCol
----------- -------------------- --------------------
1 A a
```

```sql
SELECT (
CASE
WHEN id
> 10
THEN
GreekCol
ELSE
LatinCol
END
)
FROM
TestTab;
```
