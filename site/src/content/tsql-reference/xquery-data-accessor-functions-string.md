---
name: "xquery-data-accessor-functions-string"
title: "XQuery - Data Accessor Functions - string"
category: "xquery"
description: "XQuery Language Reference: Data Accessor Functions - string"
syntax: "xs:string"
tags: ["xquery","data-accessor-functions-string"]
pubDate: 2025-12-01
---

Returns the value of

$arg

represented as a string.

A node or an atomic value.

If

$arg

is the empty sequence, the zero-length string is returned.

If

$arg

is a node, the function returns the string value of the node that is obtained by

using the string-value accessor. This is defined in the W3C XQuery 1.0 and XPath 2.0 Data

Model specification.

If

$arg

is an atomic value, the function returns the same string that is returned by the

expression cast as

,

$arg

, except when noted otherwise.

If the type of

$arg

is

, the URI is converted to a string without escaping special

characters.

In this implementation,

without an argument can only be used in the context

of a context-dependent predicate. Specifically, it can only be used inside brackets (

).

```sql
xs:string xs:anyURI fn:string()
[ ]
fn:string() as xs:string fn:string($arg as item()?) as xs:string
```
