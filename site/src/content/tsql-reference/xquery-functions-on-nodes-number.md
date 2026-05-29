---
name: "xquery-functions-on-nodes-number"
title: "XQuery - Functions on Nodes - number"
category: "xquery"
description: "XQuery Language Reference: Functions on Nodes - number"
syntax: "ROOT"
tags:
  - "xquery"
  - "functions-on-nodes-number"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns the numeric value of the node that is indicated by

$arg

.

$arg

Node whose value will be returned as a number.

If

$arg

is not specified, the numeric value of the context node, converted to a double, is

returned. In SQL Server,

without an argument can only be used in the context of a

context-dependent predicate. Specifically, it can only be used inside brackets ([ ]). For example,

the following expression returns the <

> element.

If the value of the node is not a valid lexical representation of a numeric simple type, as defined

in

, the function returns an empty

sequence. NaN is not supported.

```sql
ROOT
fn:number() as xs:double?
fn:number($arg as node()?) as xs:double?
declare @x xml
set @x='<ROOT>111</ROOT>'
select @x.query('/ROOT[number()=111]')
```