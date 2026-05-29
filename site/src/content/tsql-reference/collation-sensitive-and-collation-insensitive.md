---
name: 'Collation sensitive and collation insensitive'
title: 'Collation sensitive and collation insensitive'
category: 'operators'
description: 'Here''s the result set.'
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

## Operators and collation

SQL

Here's the result set.

Output

SQL

Here's the result set.

Output

Operators and functions are either collation sensitive or insensitive.

Collation sensitive: This means that specifying a No-collation operand is a compile-time

error. The expression result can't be No-collation.

Collation insensitive: This means that the operands and result can be No-collation.

The comparison operators, and the

,

,

,

, and

operators, are collation

sensitive. The string used by the operators is assigned the collation label of the operand that

has the higher precedence. The

statement is also collation sensitive, and all string

operands and the final result is assigned the collation of the operand with the highest

### char

### varchar

### text

## Functions and collation

precedence. The collation precedence of the

operand and result are evaluated column

by column.

The assignment operator is collation insensitive and the right expression is cast to the left

collation.

The string concatenation operator is collation sensitive, the two string operands and the result

are assigned the collation label of the operand with the highest collation precedence. The

and

statements are collation insensitive, and all string operands and the final

results are assigned the collation label of the operand with the highest precedence. The

collation precedence of the

operands and result are evaluated column by column.

The

,

, and

functions are collation sensitive for

,

, and

data types. If the input and output of the

and

functions are character strings, the

output string has the collation label of the input string. If the input isn't a character string, the

output string is Coercible-default and assigned the collation of the current database for the

connection, or the database that contains the user-defined function, stored procedure, or

trigger in which the

or

is referenced.

For the built-in functions that return a string but don't take a string input, the result string is

Coercible-default. The result string is assigned either the collation of the current database, or

the collation of the database that contains the user-defined function, stored procedure, or

trigger in which the function is referenced.

The following functions are collation-sensitive and their output strings have the collation label

of the input string:

COLLATE (Transact-SQL)

Data type conversion (Database Engine)

Operators (Transact-SQL)

Expressions (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
MAX
```

```sql
MIN
```

```sql
BETWEEN
```

```sql
LIKE
```

```sql
IN
```

```sql
UNION
```

```sql
Msg 451, Level 16, State 1, Line 1
Cannot resolve collation conflict for column 1 in SELECT statement.
SELECT
PATINDEX
((
CASE
WHEN
id
> 10
THEN
GreekCol
ELSE
LatinCol
END
),
'a'
)
FROM
TestTab;
Msg 446, Level 16, State 9, Server LEIH2, Line 1
Cannot resolve collation conflict for patindex operation.
SELECT
(
CASE
WHEN
id
> 10
THEN
GreekCol
ELSE
LatinCol
END
)
COLLATE
Latin1_General_CI_AS
FROM
TestTab;
--------------------
a
```

```sql
UNION
```

```sql
UNION ALL
```

```sql
CASE
```

```sql
UNION ALL
```

```sql
CAST
```

```sql
CONVERT
```

```sql
COLLATE
```

```sql
CAST
```

```sql
CONVERT
```

```sql
CAST
```

```sql
CONVERT
```

```sql
CHARINDEX
DIFFERENCE
ISNUMERIC
LEFT
LEN
LOWER
PATINDEX
REPLACE
REVERSE
RIGHT
SOUNDEX
STUFF
```

```sql
SUBSTRING
UPPER
```
