---
name: "Pattern match with the ESCAPE clause"
title: "Pattern match with the ESCAPE clause"
category: "queries"
description: "objects that don't match the"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

objects that don't match the

pattern.

You may not always find the same names with a pattern such as

. Instead of

19 names, you may find only 14, with all the names that start with

or have

as the second

letter eliminated from the results, and the dynamic management view names. This behavior is

because match strings with negative wildcard characters are evaluated in steps, one wildcard at

a time. If the match fails at any point in the evaluation, it's eliminated.

You can use the wildcard pattern matching characters as literal characters. To use a wildcard

character as a literal character, enclose the wildcard character in brackets. The following table

shows several examples of using the

keyword and the

wildcard characters.

,

,

,

, or

,

,

,

, or

and

,

, and

You can search for character strings that include one or more of the special wildcard characters.

For example, the discounts table in a customers database may store discount values that

include a percent sign (%). To search for the percent sign as a character instead of as a wildcard

character, the ESCAPE keyword and escape character must be provided. For example, a sample

database contains a column named comment that contains the text 30%. To search for any

rows that contain the string 30% anywhere in the comment column, specify a WHERE clause

such as

. If ESCAPE and the escape character aren't

specified, the Database Engine returns any rows with the string

.



Expand table

### char(0)

```sql
LIKE
```

```sql
LIKE '[^d][^m]%'
```

```sql
d
```

```sql
m
```

```sql
LIKE
```

```sql
[ ]
```

```sql
LIKE '5[%]'
5%
LIKE '[_]n'
_n
LIKE '[a-cdf]'
a
```

```sql
b
```

```sql
c
```

```sql
d
```

```sql
f
LIKE '[-acdf]'
-
```

```sql
a
```

```sql
c
```

```sql
d
```

```sql
f
LIKE '[ [ ]'
[
LIKE ']'
]
LIKE 'abc[_]d%'
abc_d
```

```sql
abc_de
LIKE 'abc[def]'
abcd
```

```sql
abce
```

```sql
abcf
```

```sql
WHERE comment LIKE '%30!%%' ESCAPE '!'
```

```sql
30!
```
