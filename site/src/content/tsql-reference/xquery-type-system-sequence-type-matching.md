---
name: "xquery-type-system-sequence-type-matching"
title: "XQuery - Type System - Sequence Type Matching"
category: "xquery"
description: "XQuery Language Reference: Type System - Sequence Type Matching"
syntax: "instance of"
tags:
  - "xquery"
  - "type-system-sequence-type-matching"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

An XQuery expression value is always a sequence of zero or more items. An item can be either

an atomic value or a node. The sequence type refers to the ability to match the sequence type

returned by a query expression with a specific type. For example:

If the expression value is atomic, you may want to know if it is an integer, decimal, or

string type.

If the expression value is an XML node, you may want to know if it is a comment node, a

processing instruction node, or a text node.

You may want to know if the expression returns an XML element or an attribute node of a

specific name and type.

You can use the

Boolean operator in sequence type matching. For more

information about the

expression, see

SequenceType Expressions (XQuery)

.

If an expression returns a sequence of atomic values, you may have to find the type of the

value in the sequence. The following examples illustrate how sequence type syntax can be used

to evaluate the atomic value type returned by an expression.

The

sequence type can be used in a sequence type expression to determine whether

the sequence returned by the specified expression is an empty sequence.

In the following example, the XML schema allows the <

> element to be nilled:

```sql
instance of instance of root
CREATE XML SCHEMA COLLECTION SC AS N'
<schema xmlns="http://www.w3.org/2001/XMLSchema">
<element name="root" nillable="true" type="byte"/>
</schema>'
GO
```
