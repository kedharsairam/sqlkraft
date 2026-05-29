---
name: 'Time zone offset'
title: 'Time zone offset'
category: 'data-types'
description: 'doesn''t allow addition for a'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

doesn't allow addition for a

datepart

of

or

for

date

data types

,

, and

.

Milliseconds have a scale of 3 (

), microseconds have a scale of 6 (

), and

nanoseconds have a scale of 9 (

). The

,

, and

data

types have a maximum scale of 7 (

). For a

datepart

of

,

number

must be

100 before the fractional seconds of

date

increase. A

number

between 1 and 49 rounds down

to 0, and a number from 50 to 99 rounds up to 100.

These statements add a

datepart

of

,

, or

.

SQL

Here's the result set.

Output

```sql
GROUP BY
HAVING
ORDER BY
SELECT <list>
WHERE
DATEADD
```

```sql
microsecond
```

```sql
nanosecond
```

```sql
.123
```

```sql
.123456
```

```sql
.123456789
```

```sql
.1234567
```

```sql
nanosecond
```

```sql
millisecond
```

```sql
microsecond
```

```sql
nanosecond
```

```sql
DECLARE
@datetime2
AS
DATETIME2 =
'2024-01-01 13:10:10.1111111'
;
SELECT
'1 millisecond'
,
DATEADD
(millisecond, 1, @datetime2)
UNION
ALL
SELECT
'2 milliseconds'
,
DATEADD
(millisecond, 2, @datetime2)
UNION
ALL
SELECT
'1 microsecond'
,
DATEADD
(
microsecond
, 1, @datetime2)
UNION
ALL
SELECT
'2 microseconds'
,
DATEADD
(
microsecond
, 2, @datetime2)
UNION
ALL
SELECT
'49 nanoseconds'
,
DATEADD
(nanosecond, 49, @datetime2)
UNION
ALL
SELECT
'50 nanoseconds'
,
DATEADD
(nanosecond, 50, @datetime2)
UNION
ALL
SELECT
'150 nanoseconds'
,
DATEADD
(nanosecond, 150, @datetime2);
1 millisecond     2024-01-01 13:10:10.1121111
2 milliseconds    2024-01-01 13:10:10.1131111
1 microsecond     2024-01-01 13:10:10.1111121
2 microseconds    2024-01-01 13:10:10.1111131
49 nanoseconds    2024-01-01 13:10:10.1111111
50 nanoseconds    2024-01-01 13:10:10.1111112
150 nanoseconds   2024-01-01 13:10:10.1111113
```
