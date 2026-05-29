---
name: 'Specify negative and positive numbers'
title: 'Specify negative and positive numbers'
category: 'operators'
description: 'SQL Server doesn''t enforce any kind of grouping rules such as inserting a comma ('
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

SQL Server doesn't enforce any kind of grouping rules such as inserting a comma (

) every

three digits in strings that represent money.

The following are examples of

constants:

text

constants are a string representing a GUID. They can be specified in either a

character or binary string format.

The following examples both specify the same GUID:

text

To indicate whether a number is positive or negative, apply the

or

unary operators to a

numeric constant. This creates a numeric expression that represents the signed numeric value.

Numeric constants use positive when the

or

unary operators aren't applied.

Signed

expressions:

text

Signed

expressions:

７

Note

Commas are ignored anywhere in a string literal that is cast to the

data type.

### float

### money

```sql
,
```

```sql
+
```

```sql
-
```

```sql
+
```

```sql
-
```

```sql
$12
$542023.14
$-23
```

```sql
'6F9619FF-8B86-D011-B42D-00C04FC964FF'
0xff19966f868b11d0b42d00c04fc964ff
```

```sql
+145345234
-2147483648
```
