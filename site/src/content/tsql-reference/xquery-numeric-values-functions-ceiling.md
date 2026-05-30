---
name: "xquery-numeric-values-functions-ceiling"
title: "XQuery - Numeric Values Functions - ceiling"
category: "xquery"
description: "XQuery Language Reference: Numeric Values Functions - ceiling"
syntax: "fn:ceiling ( $arg as numeric?) as numeric?"
tags:
  - "xquery"
  - "numeric-values-functions-ceiling"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns the smallest number without a fractional part and that is not less than the value of its

argument. If the argument is an empty sequence, it returns the empty sequence.

$arg

Number to which the function is applied.

If the type of

$arg

is one of the three numeric base types,

,

, or

, the

return type is the same as the

$arg

type.

If the type of

$arg

is a type that is derived from one of the numeric types, the return type is the

base numeric type.

If the input to the fn:floor, fn:ceiling, or fn:round functions is

, it is implicitly

cast to

.

Any other type generates a static error.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

```sql
fn:ceiling ( $arg as numeric?) as numeric?
```
