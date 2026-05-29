---
name: 'Fractional time scale precision'
title: 'Fractional time scale precision'
category: 'data-types'
description: 'Accepts any expression, column, or user-defined variable that can resolve to any valid T-SQL'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

,

Accepts any expression, column, or user-defined variable that can resolve to any valid T-SQL

date or time type. Valid types are:

Don't confuse the

date

parameter with the

data type.

also accepts a string literal (of any string type) that can resolve to a

.

The returned data type for

is dynamic.


## returns a truncated date of the
same data type (and, if applicable, the same fractional time scale) as the input date. For

example, if

was given a

input date, it would return a

. If it was given a string literal that could resolve to a

,

would return a

.

７

Note

The

weekday

,

timezoneoffset

, and

nanosecond

T-SQL dateparts aren't supported for

.

### time

### datetime2

### datetimeoffset

```sql
minute
mi, n
second
ss
```

```sql
s
millisecond
ms
microsecond
mcs
```

```sql
DATETRUNC
```

```sql
DATETRUNC
```

```sql
DATETRUNC
```

```sql
DATETRUNC
```

```sql
DATETRUNC
```

```sql
DATETRUNC
```
