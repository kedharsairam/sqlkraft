---
name: "xquery-functions-on-string-values-string-length"
title: "XQuery - Functions on String Values - string-length"
category: "xquery"
description: "XQuery Language Reference: Functions on String Values - string-length"
syntax: "ROOT"
tags:
  - "xquery"
  - "functions-on-string-values-string-length"
pubDate: 2025-12-01
---

Article

•

04/03/2023

SQL Server

Returns the length of the string in characters.

$arg

Source string whose length is to be computed.

If the value of

$arg

is an empty sequence, an

value of 0 is returned.

The behavior of surrogate pairs in XQuery functions depends on the database compatibility

level. If the compatibility level is 110 or later, each surrogate pair is counted as a single

character. For earlier compatibility levels, they are counted as two characters. For more

information, see

ALTER DATABASE Compatibility Level (Transact-SQL)

and

Collation and

Unicode Support.

If the value contains a 4-byte Unicode character that is represented by two surrogate

characters, SQL Server will count the surrogate characters individually.

The

without a parameter can only be used inside a predicate. For example, the

following query returns the <

> element:

```sql
ROOT fn:string-length() as xs:integer fn:string-length($arg as xs:string?) as xs:integer
DECLARE @x xml;
SET @x='<ROOT>Hello</ROOT>';
SELECT @x.query('/ROOT[string-length()=5]');
```
