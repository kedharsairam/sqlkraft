---
name: "Comparison of supported GROUP BY features"
title: "Comparison of supported GROUP BY features"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

For a

clause that uses

,

, or

, the maximum number of

expressions is 32. The maximum number of groups is 4,096 (2

). The following examples fail

because the

clause has more than 4,096 groups.

The following example generates 4,097 (2

- 1. grouping sets and then fails.

The following example generates 4,097 (2

- 1. groups and then fails. Both

and

the

grouping set produce a grand total row and duplicate grouping sets aren't

eliminated.

This example uses the backward compatible syntax. It generates 8,192 (2

) grouping sets

and then fails.

For backward compatible

clauses that don't contain

or

, the

column sizes, the aggregated columns, and the aggregate values involved in the query

limit the number of

items. This limit originates from the limit of 8,060 bytes on

the intermediate worktable that holds intermediate query results. You can use a maximum

of 12 grouping expressions when you specify

or.

The following table describes the

features that different products support.

Integration Services

aggregates

Not supported for

or.

Supported for

,

,

,

, or

12

12

12

13

Expand table

1

#### Feature

```sql
GROUP BY
```

`ROLLUP`

`CUBE`

```sql
GROUPING SETS
```

```sql
GROUP BY
```

```sql
CUBE ()
```

```sql
()
```

```sql
GROUP BY
```

`CUBE`

`ROLLUP`

```sql
GROUP
BY
```

```sql
GROUP BY
```

`CUBE`

`ROLLUP`

```sql
GROUP BY
```

`DISTINCT`

```sql
WITH CUBE
```

```sql
WITH
ROLLUP
```

```sql
WITH CUBE
```

```sql
WITH
ROLLUP
```

```sql
GROUPING SETS
```

`CUBE`

```sql
GROUP BY GROUPING SETS( CUBE(a1,., a12), b)
```

```sql
GROUP BY GROUPING SETS( CUBE(a1,., a12), ())
```

```sql
GROUP BY CUBE (a1,., a13)
GROUP BY a1,., a13
WITH
CUBE
```
