---
name: "xquery-context-functions-position"
title: "XQuery - Context Functions - position"
category: "xquery"
description: "XQuery Language Reference: Context Functions - position"
syntax: "AdventureWorks2022"
tags:
  - "xquery"
  - "context-functions-position"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Returns an integer value that indicates the position of the context item within the sequence of

items currently being processed.

In SQL Server,

can only be used in the context of a context-dependent predicate.

Specifically, it can only be used inside brackets ([ ]).Comparing against this function does not

reduce the cardinality during static type inference.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the

database.

The following query retrieves the first two features, the first two child elements of the

<

> element, from the product model catalog description. If there are more features, it

adds a <

> element to the result.

```sql
AdventureWorks2022
Features there-is-more/
fn:position() as xs:integer
SELECT CatalogDescription.query('
declare namespace pd="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelDescription";
<Product>
{ /pd:ProductDescription/@ProductModelID }
```
