---
name: "xquery-functions-related-to-qnames-namespace-uri-from-qname"
title: "XQuery - Functions Related to QNames - namespace-uri-from-QName"
category: "xquery"
description: "XQuery Language Reference: Functions Related to QNames - namespace-uri-from-QName"
syntax: "namespace-uri-from-QName($arg as xs:QName?) as xs:string?"
tags: ["xquery","functions-related-to-qnames-namespace-uri-from-qname"]
pubDate: 2025-12-01
---

Returns a string representing the namespace uri of the QName specified by

$arg. The result is

the empty sequence if

$arg

is the empty sequence.

$arg

Is the QName whose namespace URI is returned.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

For a working sample, see

local-name-from-QName (XQuery).

These are the limitations:

The

function returns instances of xs:string instead of

xs:anyURI.

Functions Related to QNames (XQuery)

```sql
namespace-uri-from-QName($arg as xs:QName?) as xs:string?
```
