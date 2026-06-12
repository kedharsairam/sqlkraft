---
name: "xquery-path-expressions"
title: "XQuery - Path Expressions"
category: "xquery"
description: "XQuery Language Reference: Path Expressions"
syntax: "child::Features"
tags: ["xquery","path-expressions"]
pubDate: 2025-12-01
---

XQuery path expressions locate nodes, such as element, attribute, and text nodes, in a

document. The result of a path expression always occurs in document order without duplicate

nodes in the result sequence. In specifying a path, you can use either unabbreviated or

abbreviated syntax. The following information focuses on the unabbreviated syntax.

Abbreviated syntax is described later in this topic.

A path expression can be relative or absolute. Following is a description of both of these:

A relative path expression is made up of one or more steps separated by one or two slash

marks (/ or //). For example,

is a relative path expression, where

refers only to child nodes of the context node. This is the node that is currently being

processed. The expression retrieves the <Features> element node children of the context

node.

An absolute path expression starts with one or two slash marks (/ or //), followed by an

optional, relative path. For example, the initial slash mark in the expression,

, indicates that it is an absolute path expression. Because a

slash mark at the start of an expression returns the document root node of the context

node, the expression returns all the <ProductDescription> element node children of the

document root.

If an absolute path starts with a single slash mark, it may or may not be followed by a

relative path. If you specify only a single slash mark, the expression returns the root node

of the context node. For an XML data type, this is its document node.

A typical path expression is made up of steps. For example, the absolute path expression,

,contains two steps separated by a slash mark.

The first step retrieves the <ProductDescription> element node children of the document

root.

７

Note

Because the sample queries in this topic are specified against the

type columns,

and

, in the

table, you should familiarize

yourself with the contents and structure of the XML documents stored in these columns.

```sql
child::Features
Child
/child::ProductDescription
/child::ProductDescription/child::Summary
```
