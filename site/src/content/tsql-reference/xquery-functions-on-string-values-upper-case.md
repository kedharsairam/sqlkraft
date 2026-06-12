---
name: "xquery-functions-on-string-values-upper-case"
title: "XQuery - Functions on String Values - upper-case"
category: "xquery"
description: "XQuery Language Reference: Functions on String Values - upper-case"
syntax: "fn:upper-case($arg as xs:string?) as xs:string"
tags: ["xquery","functions-on-string-values-upper-case"]
pubDate: 2025-12-01
---

This function converts each character in

$arg

to its upper case equivalent. The Microsoft

Windows binary case conversion for Unicode code points specifies how characters are

converted to upper case. This standard is different than the mapping for Unicode standard

code point standard.

$arg

The string value to be converted to upper case.

If the value of

$arg

is empty, a zero length string is returned.

The following example changes the input string 'abcDEF!@4' to upper case.

Expand table

```sql
fn:upper-case($arg as xs:string?) as xs:string
DECLARE @x xml = N'abcDEF!@4';
SELECT @x.value('fn:upper-case(/text()[1])', 'nvarchar(10)');
```
