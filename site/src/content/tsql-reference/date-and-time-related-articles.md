---
name: "Date and time-related articles"
title: "Date and time-related articles"
category: "data-types"
description: ""
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---

Function

## Syntax

Return value

Return data type

Determinism

@@DATEFIRST

The function returns the current value, for the session, of.

tinyint

Nondeterministic

SET DATEFIRST

or

The statement sets the first day of the week to a number from 1 through 7.

Not

applicable

Not applicable

SET

DATEFORMAT

or

The statement sets the order of the date parts (month/day/year) for entering

datetime

or

smalldatetime

data.

Not

applicable

Not applicable

@@LANGUAGE

The function returns the name of the language in current used.

isn't a date or time function. However, the language setting can affect the output of date functions.

Not

applicable

Not applicable

SET LANGUAGE

or

Sets the language environment for the session and system messages.

isn't a date or time function, but the language setting affects the output of date functions.

Not

applicable

Not applicable

sp_helplanguage

]

The function returns information about date formats of all supported languages. The language setting affects the output of date functions.

Not

applicable

Not applicable

Function

## Syntax

Return value

Return data type

Determinism

ISDATE

The function determines whether a datetime or smalldatetime input expression has a valid date or time value.

int

The function is deterministic only used with the function, when the style parameter is specified, and when style isn't equal to 0, 100, 9, or 109.

## Description

FORMAT

The function returns a value formatted with the specified format and optional culture.

Use the FORMAT function for locale-aware formatting of date/time and number values as strings.

CAST and CONVERT

The and functions convert of date and time values to and from string literals and other date and time formats.

Write International

Transact-SQL Statements

Provides guidelines for portability of databases and database applications that use Transact-

SQL statements from one language to another, or that support multiple languages.

ODBC Scalar Functions

Provides information about ODBC scalar functions available for use in Transact-SQL statements.

Includes ODBC date and time functions.

Functions

Data types (Transact-SQL)

```sql
@@DATEFIRST
```

```sql
@@DATEFIRST
```

```sql
SET
DATEFIRST
```

```sql
SET DATEFIRST {
*number* }
```

```sql
SET
DATEFIRST {
*@number_var* }
```

```sql
SET DATEFIRST
```

```sql
SET DATEFORMAT {
*format* }
```

```sql
SET
DATEFORMAT {
*@format_var* }
```

```sql
SET DATEFORMAT
```

```sql
@@LANGUAGE
```

```sql
@@LANGUAGE
```

```sql
@@LANGUAGE
```

```sql
SET LANGUAGE { [ N ]
'*language*' }
```

```sql
SET
LANGUAGE {
*@language_var* }
```

```sql
SET
LANGUAGE
```

```sql
sp_helplanguage [ [
*@language* = ]
'*language*'
```

`sp_helplanguage`

```sql
ISDATE (
<expression> )
```

`ISDATE`

`ISDATE`

`CONVERT`

`CONVERT`

`FORMAT`

`CAST`

`CONVERT`
