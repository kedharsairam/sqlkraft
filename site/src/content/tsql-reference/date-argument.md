---
name: 'date Argument'
title: 'date Argument'
category: 'data-types'
description: 'The return value depends on the language environment set by using'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

The return value depends on the language environment set by using

SET LANGUAGE

, and by

the

Configure the default language Server Configuration Option

of the login. The return value

depends on

SET DATEFORMAT

if

date

is a string literal of some formats. SET DATEFORMAT

does not change the return value when the date is a column expression of a date or time data

type.

When the

date

parameter has a

data type argument, the return value depends on the

setting specified by

SET DATEFIRST

.

If the

datepart

argument is

(

) and the

date

argument has no time zone offset,


## returns 0.
When

date

is

smalldatetime

,


## returns seconds as 00.
If the data type of the

date

argument does not have the specified

datepart

,

will return

the default for that

datepart

only if the

date

argument has a literal .

For example, the default year-month-day for any

data type is 1900-01-01. This statement

has date part arguments for

datepart

, a time argument for

date

, and


## returns
.

SQL

If

date

is specified as a variable or table column, and the data type for that variable or column

does not have the specified

datepart

,

will return error 9810. In this example, variable

@t

has a

data type. The example fails because the date part year is invalid for the

data type:

### datetime2

### datetime

### smalldatetime

#### datepart

#### Return value

#### year, yyyy, yy

#### quarter, qq, q

#### month, mm, m

#### dayofyear, dy, y

#### day, dd, d

#### week, wk, ww

#### weekday, dw

```sql
DATEADD
```

```sql
DATENAME
```

```sql
DATENAME
```

```sql
DATENAME
```

```sql
1900,
January, 1, 1, Monday
```

```sql
DATENAME
```

```sql
SELECT
DATENAME
(
year
,
'12:10:30.123'
)
,
DATENAME
(
month
,
'12:10:30.123'
)
,
DATENAME
(
day
,
'12:10:30.123'
)
,
DATENAME
(
dayofyear
,
'12:10:30.123'
)
,
DATENAME
(
weekday
,
'12:10:30.123'
);
```
