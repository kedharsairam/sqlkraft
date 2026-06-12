---
name: "xquery-functions-on-sequences-distinct-values"
title: "XQuery - Functions on Sequences - distinct-values"
category: "xquery"
description: "XQuery Language Reference: Functions on Sequences - distinct-values"
syntax: "fn:distinct-values($arg as xdt:anyAtomicType*) as xdt:anyAtomicType*"
tags:
  - "xquery"
  - "functions-on-sequences-distinct-values"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Removes duplicate values from the sequence specified by

$arg. If

$arg

is an empty sequence,

the function returns the empty sequence.

$arg

Sequence of atomic values.

All types of the atomized values that are passed to

have to be subtypes of the

same base type. Base types that are accepted are the types that support the

operation.

These types include the three built-in numeric base types, the date/time base types, xs:string,

xs:boolean, and xdt:untypedAtomic. Values of type xdt:untypedAtomic are cast to xs:string. If

there is a mixture of these types, or if other values of other types are passed, a static error is

raised.

The result of

receives the base type of the passed in types, such as xs:string in

the case of xdt:untypedAtomic, with the original cardinality. If the input is statically empty,

empty is implied and a static error is raised.

Values of type xs:string are compared to the XQuery default Unicode Codepoint Collation.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

```sql
fn:distinct-values($arg as xdt:anyAtomicType*) as xdt:anyAtomicType*
```
