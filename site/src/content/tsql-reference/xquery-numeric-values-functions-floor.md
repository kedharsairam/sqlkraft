---
name: "xquery-numeric-values-functions-floor"
title: "XQuery - Numeric Values Functions - floor"
category: "xquery"
description: ""
syntax: "fn:floor ($arg as numeric?) as numeric?"
tags: ["xquery","numeric-values-functions-floor"]
pubDate: "2025-12-01"
---

Returns the largest number with no fraction part that is not greater than the value of its

argument. If the argument is an empty sequence, it returns the empty sequence.

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

If input to the fn:floor, fn:ceiling, or fn:round functions is

, untyped data, it

is implicitly cast to. Any other type generates a static error.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks sample database.

You can use the working sample in the

ceiling function (XQuery)

for the

XQuery

function. All you have to do is replace the

function in the query with the

function.

```sql
fn:floor ($arg as numeric?) as numeric?
```
