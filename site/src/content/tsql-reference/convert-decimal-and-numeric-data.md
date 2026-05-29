---
name: 'Convert decimal and numeric data'
title: 'Convert decimal and numeric data'
category: 'data-types'
description: 'data types, SQL Server considers each combination of precision and'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

10-19

9

20-28

13

29-38

17

For

and

data types, SQL Server considers each combination of precision and

scale as a different data type. For example,

and

are considered

different data types.

In Transact-SQL statements, a constant with a decimal point is automatically converted into a

data value, using the minimum precision and scale necessary. For example, the

constant

is converted into a

value, with a precision of

, and a scale of

.

and

or

Possible loss of

precision

,

,

,

,

,

, or

and

Possible overflow

By default, SQL Server uses rounding when converting a number to a

or

value

with a lower precision and scale. Conversely, if the

option is

, SQL Server

raises an error when overflow occurs. Loss of only precision and scale isn't sufficient to raise an

error.

Before SQL Server 2016 (13.x), conversion of

values to

or

is restricted to

values of precision 17 digits only. Any

value less than

(when set using either the

scientific notation of

or the decimal notation of

) rounds down to

. This restriction doesn't appear in SQL Server 2016 (13.x) and later versions.

７

Note

Informatica (connected through the SQL Server PDW Informatica Connector) only

supports 16 significant digits, regardless of the precision and scale specified.

ﾉ

Expand table

```sql
12.345
```

```sql
5
```

```sql
3
```

```sql
SET ARITHABORT
```

```sql
ON
```

```sql
5E-18
```

```sql
5E-18
```

```sql
0.000000000000000005
```

```sql
0
```
