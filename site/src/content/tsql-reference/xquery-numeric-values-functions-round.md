---
name: "xquery-numeric-values-functions-round"
title: "XQuery - Numeric Values Functions - round"
category: "xquery"
description: ""
syntax: "fn:round ( $arg as numeric?) as numeric?"
tags:
  - "xquery"
  - "numeric-values-functions-round"
pubDate: 2025-12-01
---

Article

•

04/03/2023

SQL Server

Returns the number not having a fractional part that is closest to the argument. If there is more

than one number like that, the one that is closest to positive infinity is returned. For example:

If the argument is 2.5,

returns 3.

If the argument is 2.4999,

returns 2.

If the argument is -2.5,

returns -2.

If the argument is an empty sequence,

returns the empty sequence.

$arg

Number to which the function is applied.

If the type of

$arg

is one of the three numeric base types,

,

, or

, the

return type is same as the

$arg

type. If the type of

$arg

is a type that is derived from one of the

numeric types, the return type is the base numeric type.

If input to the

,

, or

functions is

, untyped data, it

is implicitly cast to.

Any other type generates a static error.

```sql
fn:round ( $arg as numeric?) as numeric?
```
