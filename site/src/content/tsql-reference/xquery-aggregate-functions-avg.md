---
name: "xquery-aggregate-functions-avg"
title: "XQuery - Aggregate Functions - avg"
category: "xquery"
description: ""
syntax: "fn:avg($arg as xdt:anyAtomicType*) as xdt:anyAtomicType?"
tags:
  - "xquery"
  - "aggregate-functions-avg"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Returns the average of a sequence of numbers.

$arg

The sequence of atomic values whose average is computed.

All the types of the atomized values that are passed to

have to be a subtype of exactly

one of the three built-in numeric base types or xdt:untypedAtomic. They cannot be a mixture.

Values of type xdt:untypedAtomic are treated as xs:double. The result of

receives the

base type of the passed in types, such as xs:double in the case of xdt:untypedAtomic.

If the input is statically empty, empty is implied and a static error is raised.

The

function returns the average of the numbers computed. For example:

$arg

$arg

If

$arg

is an empty sequence, the empty sequence is returned.

If an xdt:untypedAtomic value cannot be cast to xs:double, the value is disregarded in the input

sequence,

$arg

.

In all other cases, the function returns a static error.

```sql
fn:avg($arg as xdt:anyAtomicType*) as xdt:anyAtomicType?
```
