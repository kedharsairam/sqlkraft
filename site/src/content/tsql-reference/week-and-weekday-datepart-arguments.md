---
name: "Week and weekday datepart arguments"
title: "Week and weekday datepart arguments"
category: "operators"
description: ""
tags: ["tsql","operators"]
pubDate: 2026-05-29
---

The return value depends on the language environment set by using

SET LANGUAGE

, and by the

Configure the default language Server Configuration Option of the login. The return value depends on SET DATEFORMAT

if

date

is a string literal of some formats. SET DATEFORMAT doesn't change the return value when the date is a column expression of a date or time data type.

This table lists all datepart

## arguments, with corresponding return values, for the statement. The date argument has a data type. The last two positions of the datepart

return value are always and this value has a scale of 9:

2007

4

10

303

30

44

3

12

15

32

123

123456

123456700

310

44 week wk ww

weekday dw week wk

week weekday

SET DATEFIRST

argument week returned weekday

returned year month day

```sql
SELECT DATEPART(datepart,'2007-10-30 12:15:32.1234567 +05:10')
```

```sql
00
```
