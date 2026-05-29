---
name: "xquery-functions-on-string-values-concat"
title: "XQuery - Functions on String Values - concat"
category: "xquery"
description: "XQuery Language Reference: Functions on String Values - concat"
syntax: |
  fn:concat ($string as xs:string?
  ,$string as xs:string?
  [, ...]) as xs:string
tags:
  - "xquery"
  - "functions-on-string-values-concat"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Accepts zero or more strings as arguments and returns a string created by concatenating the

values of each of these arguments.

$string

Optional string to concatenate.

The function requires at least two arguments. If an argument is an empty sequence, it is treated

as the zero-length string.

The behavior of surrogate pairs in XQuery functions depends on the database compatibility

level and, in some cases, on the default namespace URI for functions. For more information,

see the section "XQuery Functions Are Surrogate-Aware" in the topic

Breaking Changes to

Database Engine Features in SQL Server 2016

. Also see

ALTER DATABASE Compatibility Level

(Transact-SQL)

and

Collation and Unicode Support

.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks sample database.

```sql
fn:concat ($string as xs:string?
,$string as xs:string?
[, ...]) as xs:string
```