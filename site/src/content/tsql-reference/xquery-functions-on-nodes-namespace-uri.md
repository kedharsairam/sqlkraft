---
name: "xquery-functions-on-nodes-namespace-uri"
title: "XQuery - Functions on Nodes - namespace-uri"
category: "xquery"
description: "XQuery Language Reference: Functions on Nodes - namespace-uri"
syntax: "namespace-uri(/ROOT[1])"
tags:
  - "xquery"
  - "functions-on-nodes-namespace-uri"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Returns the namespace URI of the QName specified in

$arg

as a xs:string.

$arg

Node name whose namespace URI part will be retrieved.

If the argument is omitted, the default is the context node.

In SQL Server,

without an argument can only be used in the context

of a context-dependent predicate. Specifically, it can only be used inside brackets ([ ]).

If

$arg

is the empty sequence, the zero-length string is returned.

If

$arg

is an element or attribute node whose expanded-QName is not in a namespace,

the function returns the zero-length string

This topic provides XQuery examples against XML instances stored in various

type columns

in the AdventureWorks database.

The following query is specified against an untyped XML instance. The query expression,

, retrieves the namespace URI part of the specified node.

```sql
namespace-uri(/ROOT[1]) fn:namespace-uri() as xs:string fn:namespace-uri($arg as node()?) as xs:string
```
