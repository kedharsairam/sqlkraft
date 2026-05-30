---
name: "Supported string literal formats for datetime"
title: "Supported string literal formats for datetime"
category: "data-types"
description: "is two digits, ranging from"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

## Numeric format

is two digits, ranging from

to

, that represent the

second.

is zero to three digits, ranging from

to

, that represent

the fractional seconds.

19 positions minimum to 23 maximum

8 bytes

Rounded to increments of

,

, or

seconds

Gregorian (includes the complete range of years)

No

No

No

The following tables list the supported string literal formats for

. Except for ODBC,

string literals are in single quotation marks (

), for example,

. If the

environment isn't

, the string literals should be in Unicode format

.

You can specify date data with a numeric month specified. For example,

represents the

twentieth day of May 1997. When you use numeric date format, specify the month, day, and

year in a string that uses slash marks (

), hyphens (

), or periods (

) as separators. This string

must appear in the following form:

When the language is set to

, the default order for the date is

(month, day,

year). You can change the date order by using the

SET DATEFORMAT

statement.

#### Date format

#### Order

#### Time format

## Alphabetical format

The setting for

determines how date values are interpreted. If the order

doesn't match the setting, the values aren't interpreted as dates. Out-of-order dates might be

misinterpreted as out of range or with wrong values. For example,

can be interpreted

as one of six dates, depending on the

setting. A four-part year is interpreted as the

year.

You can specify date data with a month specified as the full month name. For example,

,

or the month abbreviation of

, specified in the current language. Commas are optional and

capitalization is ignored.

Here are some guidelines for using alphabetical date formats:



Expand table



Expand table

### two digit year cutoff

#### Alphabetical

### datetime

## ISO 8601 format

Enclose the date and time data in single quotation marks (

). For languages other than

English, use

.

Characters that are enclosed in brackets are optional.

If you specify only the last two digits of the year, values less than the last two digits of the

value of the

two digit year cutoff

configuration option are in the same century as the

cutoff year. Values greater than or equal to the value of this option are in the century that

comes before the cutoff year. For example, if

is

(default),

is

interpreted as

and

is interpreted as

. To avoid ambiguity, use four-digit

years.

If the day is missing, the first day of the month is supplied.

The

session setting isn't applied when you specify the month in

alphabetical form.

To use the ISO 8601 format, you must specify each element in the format, including the

, the

colons (

), and the period (

) that are shown in the format.

The brackets indicate that the fraction of second component is optional. The time component

is specified in the 24-hour format. The

indicates the start of the time part of the



Expand table

#### ISO 8601

#### Unseparated

## Unseparated format

## ODBC format

value.

The advantage in using the ISO 8601 format is that it's an international standard with

unambiguous specification. Also, this format isn't affected by the

or

SET

LANGUAGE

setting.

## Examples:

This format is similar to the ISO 8601 format, except it contains no date separators.

The ODBC API defines escape sequences to represent date and time values, which ODBC calls

timestamp data. This ODBC timestamp format is also supported by the OLE DB language

definition (DBGUID-SQL) supported by the Microsoft OLE DB provider for SQL Server.

Applications that use the ADO, OLE DB, and ODBC-based APIs can use this ODBC timestamp

format to represent dates and times.

ODBC timestamp escape sequences are of the format:

:

specifies the type of the escape sequence. Timestamps have three

specifiers:

= date only

= time only



Expand table



Expand table

#### ODBC

### datetime

#### User-specified value

#### System stored value

```sql
ss
```

```sql
00
```

```sql
59
```

```sql
n*
```

```sql
0
```

```sql
999
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
1900-01-01 00:00:00
```

```sql
'
```

```sql
'string_literaL'
```

```sql
us_english
```

```sql
N'string_literaL'
```

```sql
5/20/97
```

```sql
/
```

```sql
-
```

```sql
.
```

```sql
<number separator number separator number [time] [time]>
```

```sql
us_english
```

```sql
mdy
```

```sql
SET DATEFORMAT
```

```sql
12/10/08
```

```sql
DATEFORMAT
```

```sql
[0]4/15/[19]96
mdy
[0]4-15-[19]96
mdy
[0]4.15.[19]96
mdy
[0]4/[19]96/15
myd
15/[0]4/[19]96
dmy
15/[19]96/[0]4
dym
[19]96/15/[0]4
ydm
[19]96/[0]4/15
ymd
```

```sql
14:30
14:30[:20:997]
14:30[:20.9]
4am
4 PM
```

```sql
April
```

```sql
Apr
```

```sql
'
```

```sql
N''
```

```sql
2050
```

```sql
25
```

```sql
2025
```

```sql
50
```

```sql
1950
```

```sql
SET DATEFORMAT
```

```sql
Apr[il] [15][,] 1996
Apr[il] 15[,] [19]96
Apr[il] 1996 [15]
[15] Apr[il][,] 1996
15 Apr[il][,][19]96
15 [19]96 apr[il]
[15] 1996 apr[il]
1996 APR[IL] [15]
1996 [15] APR[IL]
```

```sql
T
```

```sql
:
```

```sql
.
```

```sql
T
```

```sql
SET DATEFORMAT
```

```sql
2004-05-23T14:25:10
2004-05-23T14:25:10.487
```

```sql
yyyy-MM-ddTHH:mm:ss[.mmm]
yyyyMMdd[ HH:mm:ss[.mmm]]
```

```sql
yyyyMMdd HH:mm:ss[.mmm]
```

```sql
{ <literal_type> '<constant_value>' }
```

```sql
<literal_type>
```

```sql
<literal_type>
```

```sql
d
```

```sql
t
```
