---
name: "xquery-logical-expressions"
title: "XQuery - Logical Expressions"
category: "xquery"
description: "XQuery Language Reference: Logical Expressions"
syntax: "expression1,``expression2"
tags:
  - "xquery"
  - "logical-expressions"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

XQuery supports the logical

and

operators.

The test expressions,

, in SQL Server can result in an empty

sequence, a sequence of one or more nodes, or a single Boolean value. Based on the result,

their effective Boolean value is determined in the following manner:

If the test expression results in an empty sequence, the result of the expression is False.

If the test expression results in a single Boolean value, this value is the result of the

expression.

If the test expression results in a sequence of one or more nodes, the result of the

expression is True.

Otherwise, a static error is raised.

The logical

and

operator is then applied to the resulting Boolean values of the

expressions with the standard logical semantics.

The following query retrieves from the product catalog the front-angle small pictures, the

<

> element, for a specific product model. Note that for each product description

document, the catalog can store one or more product pictures with different attributes, such as

size and angle.

```sql
expression1,``expression2
Picture expression1 and expression2 expression1 or expression2
SELECT CatalogDescription.query('
declare namespace
PD="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelDescription";
for $F in /PD:ProductDescription/PD:Picture[PD:Size="small"
and PD:Angle="front"]
return
$F
') as Result
```
