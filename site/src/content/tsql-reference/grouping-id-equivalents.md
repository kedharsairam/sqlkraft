---
name: "GROUPING_ID() equivalents"
title: "GROUPING_ID() equivalents"
category: "statements"
description: "interprets that string as a base-2 number and returns the"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

of ones and zeros.

interprets that string as a base-2 number and returns the

equivalent integer.

For example, consider the following statement:

SQL

This table shows the

input and output values.

Each

argument must be an element of the

list.

## returns an

integer bitmap whose lowest

n

bits might be

lit

. A lit bit indicates the corresponding argument

isn't a grouping column for the given output row. The lowest-order bit corresponds to

argument

n

, and the

n

-1

lowest-order bit corresponds to argument 1.

For a single grouping query,

is equivalent to

, and both return

.



Expand table

th

## Statement A

## Statement B

```sql
GROUPING_ID
```

```sql
GROUPING_ID()
```

```sql
a
100
4
b
010
2
c
001
1
ab
110
6
ac
101
5
bc
011
3
abc
111
7
```

```sql
GROUPING_ID
```

```sql
GROUP BY
```

```sql
GROUPING_ID()
```

```sql
GROUPING (<column_expression>)
```

```sql
GROUPING_ID
(<column_expression>)
```

```sql
0
```

```sql
SELECT
a, b, c,
SUM
(d),
GROUPING_ID
(a, b, c)
FROM
T
GROUP
BY
<group_by_list>
```
