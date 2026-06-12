---
name: "xquery-functions-on-string-values-substring"
title: "XQuery - Functions on String Values - substring"
category: "xquery"
description: "XQuery Language Reference: Functions on String Values - substring"
syntax: "$sourceString"
tags:
  - "xquery"
  - "functions-on-string-values-substring"
pubDate: 2025-12-01
---

Article

•

04/03/2023

SQL Server

Returns part of the value of

$sourceString

, starting at the position indicated by the value of

$startingLoc,

and continues for the number of characters indicated by the value of

$length.

$sourceString

Source string.

$startingLoc

Starting point in the source string from which the substring starts. If this value is negative or 0,

only those characters in positions greater than zero are returned. If it is greater than the length

of the

$sourceString

, the zero-length string is returned.

$length

[optional] Number of characters to retrieve. If not specified, it returns all the characters from

the location specified in

$startingLoc

up to the end of string.

The three-argument version of the function returns the characters in

whose

position

obeys:

```sql
$sourceString
$p fn:round($startingLoc) <= $p < fn:round($startingLoc) + fn:round($length) fn:substring($sourceString as xs:string?,
$startingLoc as xs:decimal?) as xs:string?
fn:substring($sourceString as xs:string?,
$startingLoc as xs:decimal?,
$length as xs:decimal?) as xs:string?
```
