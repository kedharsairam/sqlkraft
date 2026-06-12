---
name: "Supported string literal formats for datetimeoffset"
title: "Supported string literal formats for datetimeoffset"
category: "data-types"
description: "26 positions minimum (yyyy-MM-dd HH:mm:ss {+|-}hh:mm) to 34"
tags: ["tsql","data-types"]
pubDate: "2026-05-29"
---

26 positions minimum (yyyy-MM-dd HH:mm:ss {+|-}hh:mm) to 34 maximum (yyyy-MM-dd HH:mm:ss.nnnnnnn {+|-}hh:mm)

See the following table.

10 bytes, fixed is the default with the default of 100-ns fractional second precision.

100 nanoseconds

Gregorian

Yes

Yes

No

(34, 7)

10

7

(26, 0)

8

0 to 2

(28, 1)

8

0 to 2

(29, 2)

8

0 to 2

(30, 3)

9

3 to 4

(31, 4)

9

3 to 4

(32, 5)

10

5 to 7

(33, 6)

10

5 to 7

(34, 7)

10

5 to 7

The following table lists the supported ISO 8601 string literal formats for. For information about alphabetical, numeric, unseparated, and time formats for the date and time

datetimeoffset

ISO 8601 yyyy-MM- ddTHH:mm:ss[.nnnnnnn]

[{+|-}hh:mm]

datetimeoffset

datetime

yyyy-MM- ddTHH:mm:ss[.nnnnnnn]Z

datetime

date

time

Data type

Output

parts of

, see

date

and

time.

## Description

These two formats aren't affected by the and session locale settings. Spaces aren't allowed between the and the parts.

(UTC)

This format by ISO definition indicates the portion should be expressed in Coordinated Universal Time (UTC). For example, should be represented as.

The following example compares the results of casting a string to each and data type.

Here's the result set.

time

datetime

datetime

datetimeoffset

datetime

datetime

datetimeoffset

```sql
1900-01-01 00:00:00 00:00
```

```sql
SET LANGUAGE
```

```sql
SET
DATEFORMAT
```

```sql
1999-12-
12 12:30:30.12345 -07:00
```

```sql
1999-12-12
19:30:30.12345Z
```

```sql
time

2007-05-08 smalldatetime
2007-05-08 12:35:00 datetime
2007-05-08 12:35:29.123 datetime2
2007-05-08 12:35:29.1234567 datetimeoffset
2007-05-08 12:35:29.1234567 +12:15 datetimeoffset ISO8601
2007-05-08 12:35:29.1234567 +12:15
```

```sql
SELECT
CAST (
'2007-05-08 12:35:29. 1234567 +12:15'
AS
TIME (7))
AS
'time'
,
CAST (
'2007-05-08 12:35:29. 1234567 +12:15'
AS
DATE
)
AS
'date'
,
CAST (
'2007-05-08 12:35:29.123'
AS
SMALLDATETIME)
AS
'smalldatetime'
,
CAST (
'2007-05-08 12:35:29.123'
AS
DATETIME)
AS
'datetime'
,
CAST (
'2007-05-08 12:35:29.1234567+12:15'
AS
DATETIME2 (7))
AS
'datetime2'
,
CAST (
'2007-05-08 12:35:29.1234567 +12:15'
AS
DATETIMEOFFSET (7))
AS
'datetimeoffset'
,
CAST (
'2007-05-08 12:35:29.1234567+12:15'
AS
DATETIMEOFFSET (7))
AS
'datetimeoffset ISO8601'
;
```
