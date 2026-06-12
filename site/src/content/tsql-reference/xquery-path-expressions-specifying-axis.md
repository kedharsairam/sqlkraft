---
name: "xquery-path-expressions-specifying-axis"
title: "XQuery - Path Expressions - Specifying Axis"
category: "xquery"
description: "XQuery Language Reference: Path Expressions - Specifying Axis"
syntax: "child::ProductDescription/child::Summary"
tags: ["xquery","path-expressions-specifying-axis"]
pubDate: "2025-12-01"
---

An axis step in a path expression includes the following components:

An axis

A

node test

Zero or more step qualifiers (optional)

For more information, see

Path Expressions (XQuery).

The XQuery implementation in SQL Server supports the following axis steps,

Description

Returns children of the context node.

Returns all descendants of the context node.

Returns the parent of the context node.

Returns attributes of the context node.

Returns the context node itself.

Returns the context node and all descendants of the context node.

All these axes, except the

axis, are forward axes. The

axis is a reverse axis,

because it searches backward in the document hierarchy. For example, the relative path

expression

has two steps, and each step specifies a

axis. The first step retrieves the <ProductDescription> element children of the context

node. For each <ProductDescription> element node, the second step retrieves the

<Summary> element node children.

The relative path expression,

, has three

steps. The first two steps each specify a

axis, and the third step specifies the

axis. When executed against the manufacturing instructions XML documents in the

table, the expression returns the

attribute of the

<Location> element node child of the <root> element.

Expand table

```sql
child::ProductDescription/child::Summary child child::root/child::Location/attribute::LocationID child attribute
LocationID
```
