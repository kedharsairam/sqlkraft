---
name: "xquery-functions-on-nodes-local-name"
title: "XQuery - Functions on Nodes - local-name"
category: "xquery"
description: "XQuery Language Reference: Functions on Nodes - local-name"
syntax: "xs:string"
tags: ["xquery","functions-on-nodes-local-name"]
pubDate: "2025-12-01"
---

Returns the local part of the name of

$arg

as an

that is either the zero-length string,

or has the lexical form of an. If the argument isn't provided, the default is the

context node.

Node name whose local-name part is retrieved.

In SQL Server,

without an argument can only be used in the context of a

context-dependent predicate. Specifically, it can only be used inside brackets (

).

If the argument is supplied and is the empty sequence, the function returns the zero-

length string.

If the target node has no name, because it's a document node, a comment, or a text

node, the function returns the zero-length string.

This article provides XQuery examples against XML instances that are stored in various

type columns in the AdventureWorks database.

```sql
xs:string xs:NCName fn:local-name()
[ ]
fn:local-name() as xs:string fn:local-name($arg as node()?) as xs:string
```
