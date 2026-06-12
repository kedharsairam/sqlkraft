---
name: "Converting Date and Time Data"
title: "Converting Date and Time Data"
category: "data-types"
description: "When you convert to date and time data types, SQL Server rejects all values it cannot recognize"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

## Converting time(n) Data Type to Other Date and Time Types

SQL Server

SQLCLIENT

hh:mm:ss[.nnnnnnn]

SQL_WVARCHAR

or

SQL_VARCHAR

DBTYPE_WSTRor

DBTYPE_STR

Java.sql.String

String or

SqString

YYYY-MM-DD

SQL_WVARCHAR

or

SQL_VARCHAR

DBTYPE_WSTRor

DBTYPE_STR

Java.sql.String

String or

SqString

YYYY-MM-DD

hh:mm:ss[.nnnnnnn]

SQL_WVARCHAR

or

SQL_VARCHAR

DBTYPE_WSTRor

DBTYPE_STR

Java.sql.String

String or

SqString

YYYY-MM-DD

hh:mm:ss[.nnnnnnn]

[+|-]hh:mm

SQL_WVARCHAR

or

SQL_VARCHAR

DBTYPE_WSTRor

DBTYPE_STR

Java.sql.String

String or

SqString

When you convert to date and time data types, SQL Server rejects all values it cannot recognize

as dates or times. For information about using the CAST and CONVERT functions with date and

time data, see

CAST and CONVERT (Transact-SQL)

This section describes what occurs when a

data type is converted to other date and time

data types.

When the conversion is to

, the hour, minute, and seconds are copied. When the

destination precision is less than the source precision, the fractional seconds is rounded up to

fit the destination precision. The following example shows the results of converting a

value to a

value.

Here's the result set.

### time(n)

### smalldatetime

Output

If the conversion is to

, the conversion fails, and error message 206 is raised: "Operand

type clash: date is incompatible with time".

When the conversion is to

, hour, minute, and second values are copied; and the date

component is set to '1900-01-01'. When the fractional seconds precision of the

value is

greater than three digits, the

result will be truncated. The following code shows the

results of converting a

value to a

value.

Here's the result set.

Output

When the conversion is to

, the date is set to '1900-01-01', and the hour and

minute values are rounded up. The seconds and fractional seconds are set to 0. The following

code shows the results of converting a

value to a

value.

Show rounding up of the minute value:

Here's the result set.

Output

### datetimeoffset(n)

### time(n)

### datetimeoffset(n)

### datetime2(n)

### datetime2(n)

### time(n)

Show rounding up of the hour value:

Here's the result set.

Output

If the conversion is to

, the date is set to '1900-01-01', and the time is copied.

The time zone offset is set to +00:00. When the fractional seconds precision of the

value is greater than the precision of the

value, the value is rounded up to

fit. The following example shows the results of converting a

value to a

type.

Here's the result set.

Output

When converting to

, the date is set to '1900-01-01', the time component is

copied, and the time zone offset is set to 00:00. When the fractional seconds precision of the

value is greater than the

value, the value will be rounded up to fit. The

following example shows the results of converting a

value to a

value.

#### Input string

#### literal

#### Conversion Rule

## Converting String Literals to time(n)

Here's the result set.

Output

Conversions from string literals to date and time types are permitted if all parts of the strings

are in valid formats. Otherwise, a runtime error is raised. Implicit conversions or explicit

conversions that do not specify a style, from date and time types to string literals will be in the

default format of the current session. The following table shows the rules for converting a

string literal to the

data type.

ODBC DATE

ODBC string literals are mapped to the

data type. Any assignment operation

from ODBC DATETIME literals into

types will cause an implicit conversion between

and this type as defined by the conversion rules.

ODBC TIME

See ODBC DATE rule above.

ODBC

DATETIME

See ODBC DATE rule above.

DATE only

Default values are supplied.

TIME only

Trivial

TIMEZONE only

Default values are supplied.

DATE + TIME

The TIME part of the input string is used.

DATE +

TIMEZONE

Not allowed.

Expand table

#### Input string

#### literal

#### Conversion Rule

#### Data type

#### Output

#### smalldatetime

### time(7)

`time(4)`

`time(3)`

```sql
DECLARE
@timeFrom
TIME (4) =
'12:34:54.1237'
;
DECLARE
@timeTo
TIME (3) = @timeFrom;
SELECT
@timeTo
AS
'time(3)'
, @timeFrom
AS
'time(4)'
;
```

`time(4)`

`datetime`

`time(4)`

`smalldatetime`

```sql
time(3) time(4)
------------ -------------
12:34:54.124 12:34:54.1237
DECLARE
@
time
TIME (4) =
'12:15:04.1237'
;
DECLARE
@datetime DATETIME = @
time
;
SELECT
@
time
AS
'@time'
, @datetime
AS
'@datetime'
;
@time @datetime
------------- -----------------------
12:15:04.1237 1900-01-01 12:15:04.123
DECLARE
@
time
TIME (4) =
'12:15:59.9999'
;
DECLARE
@smalldatetime SMALLDATETIME = @
time
;
SELECT
@
time
AS
'@time'
, @smalldatetime
AS
'@smalldatetime'
;
```

`time(4)`

`datetimeoffset(3)`

`time(4)`

`datetime2(2)`

```sql
@time @smalldatetime
---------------- -----------------------
12:15:59.9999 1900-01-01 12:16:00--
DECLARE
@
time
TIME (4) =
'12:59:59.9999'
;
DECLARE
@smalldatetime SMALLDATETIME = @
time
;
SELECT
@
time
AS
'@time'
, @smalldatetime
AS
'@smalldatetime'
;
@time @smalldatetime
---------------- -----------------------
12:59:59.9999 1900-01-01 13:00:00
DECLARE
@
time
TIME (4) =
'12:15:04.1237'
;
DECLARE
@datetimeoffset DATETIMEOFFSET(3) = @
time
;
SELECT
@
time
AS
'@time'
, @datetimeoffset
AS
'@datetimeoffset'
;
@time @datetimeoffset
------------- ------------------------------
12:15:04.1237 1900-01-01 12:15:04.124 +00:00
```

```sql
DECLARE
@
time
TIME (4) =
'12:15:04.1237'
;
DECLARE
@datetime2 DATETIME2(3) = @
time
;
SELECT
@datetime2
AS
'@datetime2'
, @
time
AS
'@time'
;
@datetime2 @time
----------------------- -------------
1900-01-01 12:15:04.124 12:15:04.1237
```
