---
name: "xquery-data-accessor-functions-data"
title: "XQuery - Data Accessor Functions - data"
category: "xquery"
description: "XQuery Language Reference: Data Accessor Functions - data"
syntax: "xdt:untypedAtomic"
tags:
  - "xquery"
  - "data-accessor-functions-data"
pubDate: 2025-12-01
---

09/29/2025

Applies to:

SQL Server

Returns the typed value for each item specified by

$arg

.

syntaxsql

Sequence of items whose typed values are returned.

The following considerations apply to typed values:

The typed value of an atomic value is the atomic value.

The typed value of a text node is the string value of the text node.

The typed value of a comment is the string value of the comment.

The typed value of a processing instruction is the content of the processing-instruction,

without the processing instruction target name.

The typed value of a document node is its string value.

The following considerations apply to attribute and element nodes:

If an attribute node is typed with an XML schema type, its typed value is the typed value,

accordingly.

If the attribute node is untyped, its typed value is equal to its string value that is returned

as an instance of

.

```sql
xdt:untypedAtomic
fn:data ($arg as item()*) as xdt:untyped
A
tomic*
```
