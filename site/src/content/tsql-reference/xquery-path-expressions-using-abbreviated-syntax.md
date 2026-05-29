---
name: "xquery-path-expressions-using-abbreviated-syntax"
title: "XQuery - Path Expressions - Using Abbreviated Syntax"
category: "xquery"
description: "XQuery Language Reference: Path Expressions - Using Abbreviated Syntax"
syntax: "child"
tags:
  - "xquery"
  - "path-expressions-using-abbreviated-syntax"
pubDate: 2025-12-01
---

09/26/2025

Applies to:

SQL Server

All the examples in

Path Expressions (XQuery)

use unabbreviated syntax for path expressions.

The unabbreviated syntax for an axis step in a path expression includes the axis name and

node test, separated by double colon, and followed by zero or more step qualifiers.

For example:

SQL

XQuery supports the following abbreviations for use in path expressions:

The

axis is the default axis. Therefore, the

axis can be omitted from a step

in an expression. For example,

can be written

as

.

An

axis can be abbreviated as @. For example,

can be written as

.

A

can be abbreviated as //. For example,

can be written as

.

The previous query retrieves all telephone numbers stored in the AdditionalContactInfo

column in the Contact table. The schema for AdditionalContactInfo is defined in a way

that a <telephoneNumber> element can appear anywhere in the document. Therefore, to

retrieve all the telephone numbers, you must search every node in the document. The

search starts at the root of the document and continues through all the descendant

nodes.

The following query retrieves all the telephone numbers for a specific customer contact:

SQL

```sql
child
child::
/child::ProductDescription/child::Summary
/ProductDescription/Summary
attribute
/child::ProductDescription[attribute::ProductModelID=10]
/ProductDescription[@ProductModelID=10]
/descendant-or-self::node()/
/descendant-or-
self::node()/child::act:telephoneNumber
//act:telephoneNumber
child::ProductDescription[attribute::ProductModelID=19]
SELECT
AdditionalContactInfo.query(
'
declare namespace
act="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
```