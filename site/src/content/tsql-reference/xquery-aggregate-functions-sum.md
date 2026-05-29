---
name: "xquery-aggregate-functions-sum"
title: "XQuery - Aggregate Functions - sum"
category: "xquery"
description: "XQuery Language Reference: Aggregate Functions - sum"
syntax: "AdventureWorks2022"
tags:
  - "xquery"
  - "aggregate-functions-sum"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns the sum of a sequence of numbers.

$arg

Sequence of atomic values whose sum is to be computed.

All types of the atomized values that are passed to

have to be subtypes of the same

base type. Base types that are accepted are the three built-in numeric base types or

xdt:untypedAtomic. Values of type xdt:untypedAtomic are cast to xs:double. If there is a

mixture of these types, or if other values of other types are passed, a static error is raised.

The result of

receives the base type of the passed in types such as xs:double in the case

of xdt:untypedAtomic, even if the input is optionally the empty sequence. If the input is

statically empty, the result is 0 with the static and dynamic type of xs:integer.

The

function returns the sum of the numeric values. If an xdt:untypedAtomic value

cannot be cast to xs:double, the value is ignored in the input sequence,

$arg

. If the input is a

dynamically calculated empty sequence, the value 0 of the used base type is returned.

The function returns a runtime error when an overflow or out of range exception occurs.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the

database.

```sql
AdventureWorks2022
fn:sum($arg as xdt:anyAtomicType*) as xdt:anyAtomicType
```