---
name: "year, month, and day datepart Arguments"
title: "Year, month, and day datepart Arguments"
category: "operators"
description: "return value depends on the"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

For a

(

,

) or

(

) datepart

, the return value depends on the value set by SET DATEFIRST

.

January 1 of any year defines the starting number for the datepart

. For example:

DATEPART (

, 'Jan 1, xxx x') = 1 where xxxx is any year.

This table shows the return value for the and datepart for '2007-04-21 ' for each

SET DATEFIRST argument. January 1, 2007 falls on a Monday. April 21, 2007 falls on a Saturday.

For U.S. English, serves as the default. After setting DATEFIRST, use this suggested SQL statement for the datepart table values:
1

16

6

2

17

5

3

17

4

4

17

3

5

17

2

6

17

1

7

16

7

The values that are returned for DATEPART (

, date

), DATEPART (

, date

), and

DATEPART (

, date

) are the same as those returned by the functions

YEAR

, MONTH

, and DAY

, respectively.

First day of week

First week of year contains

Weeks assigned two times

Used by/in

```sql
DATEPART
```

```sql
SET DATEFIRST 7 -- ( Sunday )
```

```sql
SELECT DATEPART(week, '2007-04-21 '), DATEPART(weekday, '2007-04-21 ')
```
