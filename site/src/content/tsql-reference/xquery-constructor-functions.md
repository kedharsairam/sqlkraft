---
name: "xquery-constructor-functions"
title: "XQuery - Constructor Functions"
category: "xquery"
description: "XQuery Language Reference: Constructor Functions"
syntax: |
  TYP($atomicvalue as xdt:anyAtomicType?
  ) as TYP?
tags:
  - "xquery"
  - "constructor-functions"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

From a specified input, the constructor functions create instances of any of the XSD built-in or

user-defined atomic types.

$strval

String that will be converted.

TYP

Any built-in XSD type.

Constructors are supported for base and derived atomic XSD types. However, the subtypes of

, which includes

, and

,

, and

are not supported. User-defined atomic types

that are available in the associated schema collections are also available, provided they are

directly or indirectly derived from the following types.

These are the supported base types:

xs:string

xs:boolean

```sql
TYP($atomicvalue as xdt:anyAtomicType?
) as TYP?
```