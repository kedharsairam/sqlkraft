---
name: "xquery-functions-on-string-values-contains"
title: "XQuery - Functions on String Values - contains"
category: "xquery"
description: "XQuery Language Reference: Functions on String Values - contains"
syntax: "fn:contains ($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean?"
tags:
  - "xquery"
  - "functions-on-string-values-contains"
pubDate: 2025-12-01
---

Article

•

04/15/2024

SQL Server

Returns a value of type xs:boolean indicating whether the value of

$arg1

contains a string value

specified by

$arg2.

$arg1

String value to test.

$arg2

Substring to look for.

If the value of

$arg2

is a zero-length string, the function returns. If the value of

$arg1

is a

zero-length string and the value of

$arg2

is not a zero-length string, the function returns.

If the value of

$arg1

or

$arg2

is the empty sequence, the argument is treated as the zero-

length string.

The contains() function uses XQuery's default Unicode code point collation for the string

comparison.

The substring value specified for

$arg2

has to be less than or equal to 4000 characters. If the

value specified is greater than 4000 characters, a dynamic error condition occurs and the

contains() function returns an empty sequence instead of a Boolean value of

or. SQL

Server does not raise dynamic errors on XQuery expressions.

In order to get case-insensitive comparisons, the

upper-case

or lower-case functions can be

used.

```sql
fn:contains ($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean?
```
