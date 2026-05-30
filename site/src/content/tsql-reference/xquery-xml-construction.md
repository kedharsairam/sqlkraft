---
name: "xquery-xml-construction"
title: "XQuery - XML Construction"
category: "xquery"
description: "XQuery Language Reference: XML Construction"
syntax: "<ProductModel>"
tags:
  - "xquery"
  - "xml-construction"
pubDate: 2025-12-01
---

09/29/2025

Applies to:

SQL Server

In XQuery, you can use the direct

and computed

constructors to construct XML structures within a query.

When you use direct constructors, you specify XML-like syntax when you construct the XML.

The following examples illustrate XML construction by the direct constructors.

In using XML notations, you can construct elements. The following example uses the direct element constructor expression and creates a

element. The constructed element has three child elements

A text node.

Two element nodes, and

.

The element has one text node child whose value is

.

The element has three element node children,

,

, and

. Each of these nodes has one text node child and have the values

,

,

, respectively.

SQL

７

Note

There's no difference between the direct

and computed

constructors.

```sql
<ProductModel>
<Summary>
<Features>
<Summary>
"Some description"
<Features>
<Color>
<Weight>
<Warranty>
Red
25
2 years parts and labor
DECLARE
@x
AS
XML
;
SET
@x =
''
;
SELECT
@x.query(
'<ProductModel ProductModelID="111">;
This is product model catalog description.
<Summary>Some description</Summary>
<Features>
```
