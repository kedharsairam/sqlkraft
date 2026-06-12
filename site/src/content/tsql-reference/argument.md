---
name: "Argument"
title: "Argument"
category: "statements"
description: ") value as the number of minutes (signed). This statement"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

First Friday,

1-7 days of year

## returns the

(

) value as the number of minutes (signed). This statement

## returns a time zone offset of 310 minutes:

renders the tzoffset value as follows:

For datetimeoffset and datetime2, tzoffset returns the time offset in minutes, where the

offset for datetime2 is always 0 minutes.

For data types that can implicitly convert to

or

,

## returns the time offset in minutes. Exception: other date / time data types.

Parameters of all other types result in an error.

For a

smalldatetime

date

value,

## returns seconds as 00.

If the

date

argument data type doesn't have the specified

datepart

,

will return the

default for that

datepart

only when a literal is specified for

date.

For example, the default year-month-day for any

data type is 1900-01-01. This statement

has date part arguments for

datepart

, a time argument for

date

, and it returns.

### smalldatetime

`DATEPART`

`DATEPART`

`DATEPART`

`DATEPART`

`DATEPART`

```sql
1900, 1, 1, 1,
2
```

```sql
SELECT
DATEPART (tzoffset,
'2007-05-10 00:00:01.1234567 +05:10'
);
```

```sql
SELECT
DATEPART (
year
,
'12:10:30.123'
)
,
DATEPART (
month
,
'12:10:30.123'
)
```
