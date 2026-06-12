---
name: "datetime"
title: "Datetime"
category: "data-types"
description: ""
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Defines a date that is combined with a time of day with fractional seconds that is based on a

24-hour clock.

Avoid using

for new work. Instead, use the

,

,

, and

data types. These types align with the SQL Standard, and are more portable.

,

and

provide more seconds precision.

provides time zone

support for globally deployed applications.

Not applicable

1753-01-01 (January 1, 1753) through 9999-12-31 (December 31,

9999.

00:00:00 through 23:59:59.997

None

is four digits from

through

that represent a year.

is two digits, ranging from

to

, that represent a month in

the specified year.

is two digits, ranging from

to

depending on the month,

which represent a day of the specified month.

is two digits, ranging from

to

, that represent the hour.

is two digits, ranging from

to

, that represent the

minute.

## Description

#### User-defined fractional second

#### precision

#### preservation

`DATETIME`

```sql
DECLARE @MyDatetime DATETIME;
CREATE TABLE Table1 (Column1 DATETIME);
```

`yyyy`

```sql
1753
```

```sql
9999
```

`MM`

```sql
01
```

```sql
12
```

`dd`

```sql
01
```

```sql
31
```

`HH`

```sql
00
```

```sql
23
```

`mm`

```sql
00
```

```sql
59
```
