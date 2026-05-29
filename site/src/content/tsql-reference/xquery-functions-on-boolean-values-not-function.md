---
name: "xquery-functions-on-boolean-values-not-function"
title: "XQuery - Functions on Boolean Values - not Function"
category: "xquery"
description: "XQuery Language Reference: Functions on Boolean Values - not Function"
syntax: "Specifications"
tags:
  - "xquery"
  - "functions-on-boolean-values-not-function"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns TRUE if the effective Boolean value of

$arg

is false, and returns FALSE if the effective

Boolean value of

$arg

is true.

$arg

A sequence of items for which there is an effective Boolean value.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

The following query constructs XML that contains product model IDs for product models

whose catalog descriptions do not include the <

> element.

```sql
Specifications
fn:not($arg as item()*) as xs:boolean
WITH XMLNAMESPACES ('https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelDescription' AS pd)
SELECT ProductModelID, CatalogDescription.query('
<Product
ProductModelID="{ sql:column("ProductModelID") }"
/>
') as Result
FROM Production.ProductModel
```
