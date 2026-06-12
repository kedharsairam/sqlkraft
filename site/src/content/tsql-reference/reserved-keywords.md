---
name: "Reserved keywords"
title: "Reserved keywords"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

This behavior is applicable only when

the compatibility level is set to 90.

Variable assignment is allowed in a

statement containing a top-level

operator, but returns

unexpected results. Learn more in

example E.

Variable assignment isn't allowed in a statement

containing a top-level

operator. Error 10734

is returned. Find a suggested rewrite in

example E.

Low

The ODBC function {fn CONVERT()}

uses the default date format of the

language. For some languages, the

default format is YDM, which can

result in conversion errors when

CONVERT() is combined with other

functions, such as

,

that expect a YMD format.

The ODBC function

uses style 121

(a language-independent YMD format) when

converting to the ODBC data types

,

,

, SQLDATE,

, and.

Low

Datetime intrinsics such as

don't require string input values to be

valid datetime literals. For example,

compiles successfully.

Datetime intrinsics such as

require string

input values to be valid datetime literals. Error 241

is returned when an invalid datetime literal is used.

Low

Trailing spaces specified in the first

input parameter to the

function are trimmed when the

parameter is of type. For

example, in the statement

, the value

is

incorrectly evaluated as.

Trailing spaces are always preserved. For

applications that rely on the previous behavior of

the function, use the

function when

specifying the first input parameter for the

function. For example, the following syntax will

reproduce the SQL Server 2005 behavior:.

Low

The compatibility setting also determines the keywords that are reserved by the Database

Engine. The following table shows the reserved keywords that are introduced by each of the

compatibility levels.

Expand table

#### Compatibility level

#### setting

#### Reserved keywords

### []

### ""

`UNION`

`UNION`

```sql
{fn CURDATE()}
```

```sql
{fn CONVERT()}
```

`SQL_TIMESTAMP`

`SQL_DATE`

`SQL_TIME`

`SQL_TYPE_TIME`

`SQL_TYPE_TIMESTAMP`

`DATEPART`

```sql
SELECT DATEPART (year, '2007/05-
30')
```

`DATEPART`

`REPLACE`

```sql
SELECT '<'
+ REPLACE(CONVERT(char(6), 'ABC '),
' ', 'L') + '>'
```

```sql
'ABC '
```

```sql
'ABC'
```

`RTRIM`

```sql
SELECT
'<' + REPLACE(RTRIM(CONVERT(char(6), 'ABC ')),
' ', 'L') + '>'
```
