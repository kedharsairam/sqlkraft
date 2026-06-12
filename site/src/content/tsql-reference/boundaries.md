---
name: "boundaries"
title: "Boundaries"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

The difference between the

startdate and

enddate

, expressed in the boundary set by datepart.

For example,

## returns

, hinting that

2036 must be a leap year. This case means that if we start at startdate

, and then count

days, we reach the enddate

of.

For a return value out of range for

(-2,147,483,648 to +2,147,483,647),

## returns an

error. For

, the maximum difference between startdate

and enddate

is 24 days, 20 hours, 31 minutes, and 23.647 seconds. For

, the maximum difference is 68 years, 19 days, 3 hours, 14 minutes, and 7 seconds.

If startdate

and enddate

are both assigned only a time value, and the datepart

isn't a time datepart

,

## returns.

uses the time zone offset component of startdate

or enddate

to calculate the return value.

Because

smalldatetime

is accurate only to the minute, seconds and milliseconds are always set to

in the return value when startdate

or enddate

have a value.

If only a time value is assigned to a date data type variable, sets the value of the missing date part to the default value:. If only a date value is assigned to a variable of a time or date data type,

sets the value of the missing time part to the default value:. If either startdate

or enddate

have only a time part and the other only a date part,

sets the missing time and date parts to the default values.

If startdate

and enddate

have different date data types, and one has more time parts or fractional seconds precision than the other, sets the missing parts of the other to.

The following statements have the same startdate

and the same enddate

values. Those dates are adjacent and they differ in time by a hundred nanoseconds (.0000001 second). The

difference between the startdate

and enddate

in each statement crosses one calendar or time boundary of its

datepart. Each statement returns.

datetime2

datetime

smalldatetime

int

```sql
SELECT DATEDIFF(day, '2036-03-01', '2036-02-28');
```

```sql
-2
```

```sql
2036-03-01
```

```sql
-2
```

```sql
2036-02-28
```

`DATEDIFF`

`millisecond`

`second`

`DATEDIFF`

```sql
0
```

`DATEDIFF`

```sql
0
```

`DATEDIFF`

```sql
1900-01-01
```

`DATEDIFF`

```sql
00:00:00
```

`DATEDIFF`

`DATEDIFF`

```sql
0
```

```sql
1
```
