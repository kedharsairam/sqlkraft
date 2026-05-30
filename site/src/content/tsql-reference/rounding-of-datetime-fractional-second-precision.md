---
name: "Rounding of datetime fractional second precision"
title: "Rounding of datetime fractional second precision"
category: "data-types"
description: "= timestamp (time + date)"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

= timestamp (time + date)

is the value of the escape sequence.

must follow

these formats for each

:

:

:

:

values are rounded to increments of

,

, or

seconds, as shown in the

following example.

SQL

Here's the result set.



Expand table



Expand table

#### User-specified value

#### System stored value

### datetime

### datetime

### date

```sql
ts
```

```sql
<constant_value>
```

```sql
<constant_value>
```

```sql
<literal_type>
```

```sql
d
```

```sql
yyyy-MM-dd
t
```

```sql
hh:mm:ss[.fff]
ts
```

```sql
yyyy-MM-dd HH:mm:ss[.fff]
```

```sql
{ ts '1998-05-02 01:23:56.123' }
{ d '1990-10-02' }
{ t '13:33:41' }
```

```sql
.000
```

```sql
.003
```

```sql
.007
```

```sql
01/01/2024 23:59:59.999
2024-01-02 00:00:00.000
```

```sql
SELECT
'01/01/2024 23:59:59.999'
AS
[
User
-specified
value
],
CAST
(
'01/01/2024 23:59:59.999'
AS
DATETIME)
AS
[
System
stored
value
]
UNION
SELECT
'01/01/2024 23:59:59.998'
,
CAST
(
'01/01/2024 23:59:59.998'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.997'
,
CAST
(
'01/01/2024 23:59:59.997'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.996'
,
CAST
(
'01/01/2024 23:59:59.996'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.995'
,
CAST
(
'01/01/2024 23:59:59.995'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.994'
,
CAST
(
'01/01/2024 23:59:59.994'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.993'
,
CAST
(
'01/01/2024 23:59:59.993'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.992'
,
CAST
(
'01/01/2024 23:59:59.992'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.991'
,
CAST
(
'01/01/2024 23:59:59.991'
AS
DATETIME)
UNION
SELECT
'01/01/2024 23:59:59.990'
,
CAST
(
'01/01/2024 23:59:59.990'
AS
DATETIME);
```
