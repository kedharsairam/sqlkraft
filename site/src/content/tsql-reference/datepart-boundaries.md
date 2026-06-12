---
name: "datepart boundaries"
title: "Datepart boundaries"
category: "data-types"
description: ""
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Signed

## Returns the

difference between the

startdate

and

enddate

, expressed in the boundary set

by

datepart.

For a return value out of range for

(-9,223,372,036,854,775,808 to

9,223,372,036,854,775,807),

## returns an error. Unlike , which returns an

and

therefore may overflow a

or higher,

can only overflow if using

precision where the difference between

enddate

and

startdate

is more than 292

years, 3 months, 10 days, 23 hours, 47 minutes, and 16.8547758 seconds.

If

startdate

and

enddate

are both assigned only a time value, and the

datepart

isn't a time

datepart

,

## returns 0.

does use a time zone offset component of

startdate

or

enddate

to calculate the

return value.

For a

value used for

startdate

or

enddate

,

always sets seconds and

milliseconds to 0 in the return value because

smalldatetime

only has accuracy to the minute.

If only a time value is assigned to a date data type variable,

sets the value of the

missing date part to the default value:. If only a date value is assigned to a variable

of a time or date data type,

sets the value of the missing time part to the default

value:. If either

startdate

or

enddate

have only a time part and the other only a date

part,

sets the missing time and date parts to the default values.

If

startdate

and

enddate

have different date data types, and one has more time parts or

fractional seconds precision than the other,

sets the missing parts of the other to

0.

The following statements have the same

startdate

and the same

enddate

values. Those dates

are adjacent and they differ in time by one hundred nanoseconds (.0000001 second). The

difference between the

startdate

and

enddate

in each statement crosses one calendar or time

boundary of its

datepart. Each statement returns 1. If

startdate

and

enddate

have different year

values but they have the same calendar week values,

will return 0 for

datepart.

### smalldatetime

### nanosecond

`DATEDIFF_BIG`

`DATEDIFF_BIG`

`DATEDIFF_BIG`

`DATEDIFF_BIG`

`DATEDIFF_BIG`

`DATEDIFF_BIG`

```sql
1900-01-01
```

`DATEDIFF_BIG`

```sql
00:00:00
```

`DATEDIFF_BIG`

`DATEDIFF_BIG`

`DATEDIFF_BIG`
