---
name: "xquery-aggregate-functions-min"
title: "XQuery - Aggregate Functions - min"
category: "xquery"
description: ""
syntax: "fn:min($arg as xdt:anyAtomicType*) as xdt:anyAtomicType?"
tags:
  - "xquery"
  - "aggregate-functions-min"
pubDate: 2025-12-01
---

Article

•

04/03/2023

SQL Server

Returns from a sequence of atomic values,

$arg

, the one item whose value is less than that of

all the others.

$arg

Sequence of items from which to return the minimum value.

All types of the atomized values that are passed to

have to be subtypes of the same base

type. Base types that are accepted are the types that support the

operation. These types

include the three built-in numeric base types, the date/time base types, xs:string, xs:boolean,

and xdt:untypedAtomic. Values of type xdt:untypedAtomic are cast to xs:double. If there is a

mixture of these types, or if other values of other types are passed, a static error is raised.

The result of

receives the base type of the passed in types, such as xs:double in the case

of xdt:untypedAtomic. If the input is statically empty, empty is implied and a static error is

returned.

The

function returns the one value in the sequence that is smaller than any other in the

input sequence. For xs:string values, the default Unicode Codepoint Collation is being used. If

an xdt:untypedAtomic value cannot be cast to xs:double, the value is ignored in the input

sequence,

$arg. If the input is a dynamically calculated empty sequence, the empty sequence is

returned.

```sql
fn:min($arg as xdt:anyAtomicType*) as xdt:anyAtomicType?
```
