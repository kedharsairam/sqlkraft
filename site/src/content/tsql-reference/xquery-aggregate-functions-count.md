---
name: "xquery-aggregate-functions-count"
title: "XQuery - Aggregate Functions - count"
category: "xquery"
description: "XQuery Language Reference: Aggregate Functions - count"
syntax: "fn:count($arg as item()*) as xs:integer"
tags:
  - "xquery"
  - "aggregate-functions-count"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns the number of items that are contained in the sequence specified by

$arg

.

$arg

Items to count.

Returns 0 if

$arg

is an empty sequence.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

The following query counts the number of work center locations in the manufacturing process

of a product model (ProductModelID=7).

```sql
fn:count($arg as item()*) as xs:integer
SELECT Production.ProductModel.ProductModelID,
Production.ProductModel.Name,
Instructions.query('
```