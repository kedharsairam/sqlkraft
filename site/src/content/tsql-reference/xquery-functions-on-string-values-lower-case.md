---
name: "xquery-functions-on-string-values-lower-case"
title: "XQuery - Functions on String Values - lower-case"
category: "xquery"
description: "XQuery Language Reference: Functions on String Values - lower-case"
syntax: "fn:lower-case($arg as xs:string?) as xs:string"
tags:
  - "xquery"
  - "functions-on-string-values-lower-case"
pubDate: 2025-12-01
---

Article

•

08/10/2023

Applies to:

SQL Server

The lower-case function converts each character in

$arg

to its lower case equivalent. The

Microsoft Windows binary case conversion for Unicode code points specifies how characters

are converted to lower case. This standard is not identical to the mapping for Unicode code

point standard.

$arg

The string value to be converted to lower case.

If the value of

$arg

is empty, a zero length string is returned.

The following example changes the input string 'abcDEF!@4' to lower case.

Expand table

```sql
fn:lower-case($arg as xs:string?) as xs:string
DECLARE @x xml = N'abcDEF!@4';
SELECT @x.value('fn:lower-case(/text()[1])', 'nvarchar(10)');
```
