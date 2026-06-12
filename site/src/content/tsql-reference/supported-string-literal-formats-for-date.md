---
name: "Supported string literal formats for date"
title: "Supported string literal formats for date"
category: "data-types"
description: ""
tags: ["tsql","data-types"]
pubDate: "2026-05-29"
---

## String literal formats for month-day-year

Default value

This value is used for the appended date part for implicit conversion from

to

or.

Calendar

Gregorian

User-defined fractional

second precision

No

Time zone offset aware

and preservation

No

Daylight saving aware

No

The following lists show the valid string literal formats for the

data type.

,

, and

represent month, day, and year in a string with slash marks (

), hyphens

(

), or periods (

) as separators.

Only four-digit or two-digit years are supported. Use four-digit years whenever possible. To

specify an integer from

to

that represents the cutoff year for interpreting two-digit

years as four-digit years, use the

two digit year cutoff

server configuration option.

For Informatica,

is limited to the range

to.

A two-digit year that is less than or equal to the last two digits of the cutoff year is in the same

century as the cutoff year. A two-digit year greater than the last two digits of the cutoff year is

in the century that comes before the cutoff year. For example, if the two-digit year cutoff is the

default

, the two-digit year

is interpreted as

and the two-digit year

is

interpreted as.

The current language setting determines the default date format. You can change the date

format by using the

SET LANGUAGE

and

SET DATEFORMAT

statements.

The

format isn't supported for.

## String literal formats for month-year-day

## String literal formats for day-month-year

## String literal formats for day-year-month

## String literal formats for year-month-day

## Alphabetical list of formats

## ISO 8601 list of formats

## Unseparated list of formats

## ODBC date format

represents the full month name, or the month abbreviation, given in the current language.

Commas are optional and capitalization is ignored.

To avoid ambiguity, use four-digit years.

If the day is missing, the first day of the month is supplied.

Same as the SQL standard. This format is the only format defined as an international standard.

The

data can be specified with four, six, or eight digits. A six-digit or eight-digit string is

always interpreted as. The month and day must always be two digits. A four-digit string is

interpreted as the year.

## W3C XML date format

```sql
1900-01-01
```

```sql
[m]m
```

`dd`

```sql
[yy]yy
```

```sql
/
```

```sql
-
```

```sql.
```

```sql
0001
```

```sql
9999
```

`yyyy`

```sql
1582
```

```sql
9999
```

```sql
2049
```

```sql
49
```

```sql
2049
```

```sql
50
```

```sql
1950
```

`ydm`

```sql
[m]m/dd/[yy]yy
[m]m-dd-[yy]yy
```

```sql
[m]m/[yy]yy/dd
[m]m-[yy]yy-dd
[m]m.[yy]yy.dd
```

```sql
dd/[m]m/[yy]yy dd-[m]m-[yy]yy dd.[m]m.[yy]yy
```

```sql
dd/[yy]yy/[m]m dd-[yy]yy-[m]m dd.[yy]yy.[m]m
```

```sql
SET
DATEFORMAT mdy;
```

```sql
SET
DATEFORMAT myd;
```

```sql
SET
DATEFORMAT dmy;
```

```sql
SET
DATEFORMAT dym;
```

```sql
SET
DATEFORMAT ymd;
```

```sql
[yy]yy/[m]m/dd
[yy]yy-[m]m-dd
[yy]yy-[m]m-dd
[dd] mon[,] yyyy dd mon[,][yy]yy dd [yy]yy mon
[dd] yyyy mon mon [dd][,] yyyy mon dd[,] [yy]
mon yyyy [dd]
yyyy mon [dd]
yyyy [dd] mon mon
```

```sql
yyyy-MM-dd yyyyMMdd
```

```sql
[yy]yyMMdd yyyy[MMdd]
```

`ymd`
