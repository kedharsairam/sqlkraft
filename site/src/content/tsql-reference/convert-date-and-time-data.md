---
name: "Convert date and time data"
title: "Convert date and time data"
category: "data-types"
description: ""
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---

is two digits, ranging from 01 to 31 depending on the month, which

represents a day of the specified month.

is two digits, ranging from 00 to 23, which represents the hour.

is two digits, ranging from 00 to 59, that represents the minute.

is two digits, ranging from 00 to 59, that represents the second. Values that

are 29.998 seconds or less are rounded down to the nearest minute. Values of

29.999 seconds or more are rounded up to the nearest minute.

19 positions maximum

4 bytes, fixed

One minute

Gregorian

(Doesn't include the complete range of years.)

No

No

No

isn't ANSI or ISO 8601 compliant.

When you convert to date and time data types, SQL Server rejects all values it can't recognize

as dates or times. For information about using the

and

functions with date and

time data, see

CAST and CONVERT.

### smalldatetime

### smalldatetime

### time(

### n

### )

### smalldatetime

### time(4)

## Convert smalldatetime to other date and time types

This section describes what occurs when a

data type is converted to other date

and time data types.

For a conversion to

, the year, month, and day are copied. The following code shows the

results of converting a

value to a

value.

Here's the result set.

Output

When the conversion is to

, the hours, minutes, and seconds are copied. The fractional

seconds are set to. The following code shows the results of converting a

value to a

value.

Here's the result set.

Output

### smalldatetime

### smalldatetime

### datetimeoffset(

### n

### )

### smalldatetime

### datetimeoffset(

### n

### )

### smalldatetime

### datetimeoffset(4)

### datetime2(n)

### smalldatetime

### datetime2(n)

### smalldatetime

### datetime2(4)

When the conversion is to

, the

value is copied to the

value.

The fractional seconds are set to. The following code shows the results of converting a

value to a

value.

Here's the result set.

Output

For a conversion to

, the

value is copied to the

value. The fractional seconds are set to

, and the time zone offset is set to. The following code shows the results of converting a

value to a

value.

Here's the result set.

Output

For the conversion to

, the

value is copied to the

value. The fractional seconds are set to. The following code shows the results of converting a

value to a

value.

### smalldatetime

#### Input

#### Output

`dd`

`HH`

`mm`

`ss`

```sql
1900-01-01 00:00:00
```

`CAST`

`CONVERT`

```sql
0
```

```sql
DECLARE
@smalldatetime
AS
SMALLDATETIME =
'1955-12-13 12:43:10'
;
DECLARE
@
date
AS
DATE
= @smalldatetime;
SELECT
@smalldatetime
AS
'@smalldatetime'
,
@
date
AS
'date'
;
@smalldatetime date
--------------------- ----------
1955-12-13 12:43:00 1955-12-13
DECLARE
@smalldatetime
AS
SMALLDATETIME =
'1955-12-13 12:43:10'
;
DECLARE
@
time
AS
TIME (4) = @smalldatetime;
SELECT
@smalldatetime
AS
'@smalldatetime'
,
@
time
AS
'time'
;
@smalldatetime time
----------------------- -------------
1955-12-13 12:43:00 12:43:00.0000
```

```sql
0
```

```sql
0
```

```sql
+00:0
```

```sql
0
```

```sql
DECLARE
@smalldatetime
AS
SMALLDATETIME =
'1955-12-13 12:43:10'
;
DECLARE
@datetime
AS
DATETIME = @smalldatetime;
SELECT
@smalldatetime
AS
'@smalldatetime'
,
@datetime
AS
'datetime'
;
@smalldatetime datetime
----------------------- -----------------------
1955-12-13 12:43:00 1955-12-13 12:43:00.000
DECLARE
@smalldatetime
AS
SMALLDATETIME =
'1955-12-13 12:43:10'
;
DECLARE
@datetimeoffset
AS
DATETIMEOFFSET (4) = @smalldatetime;
SELECT
@smalldatetime
AS
'@smalldatetime'
,
@datetimeoffset
AS
'datetimeoffset(4)'
;
@smalldatetime datetimeoffset(4)
--------------------- ------------------------------
1955-12-13 12:43:00 1955-12-13 12:43:00.0000 +00:0
```
