---
name: "Date and time functions"
title: "Date and time functions"
category: "data-types"
description: "The following tables list the Transact-SQL date and time functions. For more information about determinism, see"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

## Functions that return system date and time values

### Higher-precision system date and time functions

### Lower-precision system date and time functions

The following tables list the Transact-SQL date and time functions. For more information about determinism, see

Deterministic and Nondeterministic Functions

.

Transact-SQL derives all system date and time values from the operating system of the computer on which the

instance of SQL Server runs.

Since SQL Server 2008 (10.0.x), the Database Engine derives the date and time values through use of the

Windows API. The accuracy depends on the computer hardware and version of

Windows on which the instance of SQL Server runs. This API has a precision fixed at 100 nanoseconds. Use the

Windows API to determine the accuracy.

Function

## Syntax

Return value

Return data

type

Determinism

SYSDATETIME

The

function returns a

datetime2(7)

value containing the date

and time of the computer on which the

instance of SQL Server runs. The

returned value doesn't include the time

zone offset.

datetime2(7)

Nondeterministic

SYSDATETIMEOFFSET

The

function returns

a

datetimeoffset(7)

value containing

the date and time of the computer on

which the instance of SQL Server runs.

The returned value includes the time

zone offset.

datetimeoffset(7)

Nondeterministic

SYSUTCDATETIME

The

function returns a

datetime2(7)

value containing the date

and time of the computer on which the

instance of SQL Server is running.

## returns the date and

time values as UTC time (Coordinated

Universal Time).

datetime2(7)

Nondeterministic

ﾉ

Expand table

ﾉ

Expand table

## Functions that return date and time parts

Function

## Syntax

Return value

Return

data type

Determinism

CURRENT_TIMESTAMP

The

function returns a

datetime

value containing the date and time

of the computer on which the instance of SQL

Server runs. The returned value doesn't

include the time zone offset.

datetime

Nondeterministic

GETDATE

The

function returns a

datetime

value

containing the date and time of the computer

on which the instance of SQL Server runs. The

returned value doesn't include the time zone

offset.

datetime

Nondeterministic

GETUTCDATE

The

function returns a

datetime

value containing the date and time of the

computer on which the instance of SQL Server

runs. The

function returns the

date and time values as UTC time

(Coordinated Universal Time).

datetime

Nondeterministic

CURRENT_DATE

The

function returns a

date

value containing only the date of the

computer on which the instance of the

Database Engine runs. The returned value

doesn't include the time and the time zone

offset.

date

Nondeterministic

Function

## Syntax

Return value

Return data

type

Determinism

DATE_BUCKET

The

function returns a value

corresponding to the start of each date-time

bucket from the timestamp defined by the

origin

parameter, or the default origin value of

if the origin

parameter isn't specified.

The return type

depends on the

argument

supplied for

date

.

Nondeterministic

DATENAME

The

function returns a character string

representing the specified

datepart

of the

specified date.

nvarchar

Nondeterministic

DATEPART

The

function returns an integer

representing the specified

datepart

of the

specified

date

.

int

Nondeterministic

DATETRUNC

The

function returns an input

date

truncated to a specified

datepart

.

The return type

depends on the

argument

supplied for

date

.

Nondeterministic

ﾉ

Expand table

## Functions that return date and time values from their parts

Function

## Syntax

Return value

Return data

type

Determinism

DAY

The

function returns an integer

representing the day part of the specified

date

.

int

Deterministic

MONTH

The

function returns an integer

representing the month part of a specified

date

.

int

Deterministic

YEAR

The

function returns an integer

representing the year part of a specified

date

.

int

Deterministic

Function

## Syntax

Return value

Return data type

Determinism

DATEFROMPARTS

The

function returns a

date

value for the specified

year, month, and day.

date

Deterministic

DATETIME2FROMPARTS

The

function returns a

datetime2

value for the

specified date and time,

with the specified

precision.

datetime2(

precision

)

Deterministic

DATETIMEFROMPARTS

The

function returns a

datetime

value for the

specified date and time.

datetime

Deterministic

DATETIMEOFFSETFROMPARTS

The

function returns a

datetimeoffset

value for

the specified date and

time, with the specified

offsets and precision.

datetimeoffset(

precision

)

Deterministic

SMALLDATETIMEFROMPARTS

The

function returns a

smalldatetime

value for

the specified date and

time.

smalldatetime

Deterministic

TIMEFROMPARTS

The

function returns a

time

value for the specified

time(

precision

)

Deterministic

ﾉ

Expand table

## Functions that return date and time difference values

## Functions that modify date and time values

#### datetimeoffset

#### AT TIME ZONE

Function

## Syntax

Return value

Return data type

Determinism

time, with the specified

precision.

Function

## Syntax

Return value

Return

data type

Determinism

DATEDIFF

The

function returns the number of

date or time

datepart

boundaries, crossed

between two specified dates.

int

Deterministic

DATEDIFF_BIG

The

function returns the number of

date or time

datepart

boundaries, crossed

between two specified dates.

bigint

Deterministic

Function

## Syntax

Return value

Return data type

Determinism

DATEADD

The

function returns a

new

datetime

value by adding an

interval to the specified

datepart

of the specified

date

.

The data type of the

date

argument

Deterministic

EOMONTH

The

function returns the

last day of the month containing

the specified date, with an

optional offset.

Return type is the type

of the

start_date

argument, or

alternately, the

date

data type.

Deterministic

SWITCHOFFSET

The

function returns

changes the time zone offset of a

datetimeoffset

value, and

preserves the UTC value.

datetimeoffset

with the

fractional precision of

the

DATETIMEOFFSET

argument

Deterministic

TODATETIMEOFFSET

The

function

transforms a

datetime2

value into

a datetimeoffset value.

interprets the

datetime2

value in local time, for

the specified

time_zone

.

datetimeoffset

with the

fractional precision of

the

datetime

argument

Deterministic

ﾉ

Expand table

ﾉ

Expand table



Tip

For more information and recommendations about manipulating time zone information in SQL Server with

the

data type, see

.

## Functions that set or return session format functions

## Functions that validate date and time values

```sql
GetSystemTimeAsFileTime()
```

```sql
GetSystemTimeAdjustment()
```

```sql
SYSDATETIME()
```

```sql
SYSDATETIME
```

```sql
SYSDATETIMEOFFSET
()
```

```sql
SYSDATETIMEOFFSET
```

```sql
SYSUTCDATETIME
()
```

```sql
SYSUTCDATETIME
```

```sql
SYSUTCDATETIME
```

```sql
CURRENT_TIMESTAMP
```

```sql
CURRENT_TIMESTAMP
```

```sql
GETDATE()
```

```sql
GETDATE
```

```sql
GETUTCDATE()
```

```sql
GETUTCDATE
```

```sql
GETUTCDATE
```

```sql
CURRENT_DATE
```

```sql
CURRENT_DATE
```

```sql
DATE_BUCKET (
<datepart>,
<number>, <date>,
<origin>)
```

```sql
DATE_BUCKET
```

```sql
1900-01-01 00:00:00.000
```

```sql
DATENAME (
<datepart>,
<date> )
```

```sql
DATENAME
```

```sql
DATEPART (
<datepart>,
<date> )
```

```sql
DATEPART
```

```sql
DATETRUNC (
<datepart>,
<date> )
```

```sql
DATETRUNC
```

```sql
DAY ( <date> )
```

```sql
DAY
```

```sql
MONTH ( <date> )
```

```sql
MONTH
```

```sql
YEAR ( <date> )
```

```sql
YEAR
```

```sql
DATEFROMPARTS ( <year>,
<month>, <day> )
```

```sql
DATEFROMPARTS
```

```sql
DATETIME2FROMPARTS (
<year>, <month>, <day>,
<hour>, <minute>,
<seconds>, <fractions>,
<precision> )
```

```sql
DATETIME2FROMPARTS
```

```sql
DATETIMEFROMPARTS (
<year>, <month>, <day>,
<hour>, <minute>,
<seconds>,
<milliseconds> )
```

```sql
DATETIMEFROMPARTS
```

```sql
DATETIMEOFFSETFROMPARTS
( <year>, <month>,
<day>, <hour>,
<minute>, <seconds>,
<fractions>,
<hour_offset>,
<minute_offset>,
<precision> )
```

```sql
DATETIMEOFFSETFROMPARTS
```

```sql
SMALLDATETIMEFROMPARTS
( <year>, <month>,
<day>, <hour>, <minute>
)
```

```sql
SMALLDATETIMEFROMPARTS
```

```sql
TIMEFROMPARTS ( <hour>,
<minute>, <seconds>,
<fractions>,
<precision> )
```

```sql
TIMEFROMPARTS
```

```sql
DATEDIFF ( <datepart>,
<startdate>, <enddate> )
```

```sql
DATEDIFF
```

```sql
DATEDIFF_BIG (
<datepart>, <startdate>,
<enddate> )
```

```sql
DATEDIFF_BIG
```

```sql
DATEADD (<datepart>,
<number>, <date> )
```

```sql
DATEADD
```

```sql
EOMONTH (
<start_date> [ ,
<month_to_add> ] )
```

```sql
EOMONTH
```

```sql
SWITCHOFFSET
(<DATETIMEOFFSET>,
<time_zone> )
```

```sql
SWITCHOFFSET
```

```sql
TODATETIMEOFFSET
(<expression>,
<time_zone> )
```

```sql
TODATETIMEOFFSET
```

```sql
TODATETIMEOFFSET
```
