---
name: "xquery-path-expressions-specifying-node-test"
title: "XQuery - Path Expressions - Specifying Node Test"
category: "xquery"
description: "XQuery Language Reference: Path Expressions - Specifying Node Test"
syntax: "/child::ProductDescription"
tags:
  - "xquery"
  - "path-expressions-specifying-node-test"
pubDate: 2025-12-01
---

Article

•

12/17/2024

Applies to:

SQL Server

An axis step in a path expression includes the following components:

An axis

A node test

Zero or more step qualifiers (optional)

For more information, see

Path Expressions (XQuery)

.

A node test is a condition and is the second component of the axis step in a path expression.

All the nodes selected by a step must satisfy this condition. For the path expression,

, the node test is

. This step retrieves only

those element node children whose name is ProductDescription.

A node test condition can include the following:

A node name. Only nodes of the principal node kind with the specified name are

returned.

A node type. Only nodes of the specified type are returned.

When specifying a node name as a node test in a path expression step, you must understand

the concept of principal node kind. Every axis, child, parent, or attribute, has a principal node

kind. For example:

An attribute axis can contain only attributes. Therefore, the attribute node is the principal

node kind of the attribute axis.

For other axes, if the nodes selected by the axis can contain element nodes, element is

the principal node kind for that axis.

７

Note

Node names that are specified in XQuery path expressions are not subject to the same

collation-sensitive rules as Transact-SQL queries are and are always case-sensitive.

```sql
/child::ProductDescription
ProductDescription
```
