---
name: "xquery-sequencetype-expressions"
title: "XQuery - SequenceType Expressions"
category: "xquery"
description: "XQuery Language Reference: SequenceType Expressions"
syntax: "instance of"
tags:
  - "xquery"
  - "sequencetype-expressions"
pubDate: 2025-12-01
---

Article

•

11/19/2024

Applies to:

SQL Server

In XQuery, a value is always a sequence. The type of the value is referred to as a sequence type.

The sequence type can be used in an

XQuery expression. The SequenceType syntax

described in the XQuery specification is used when you need to refer to a type in an XQuery

expression.

The atomic type name can also be used in the

XQuery expression. In SQL Server, the

and

XQuery expressions on SequenceTypes are partially supported.

The

operator can be used to determine the dynamic, or run-time, type of the value

of the specified expression. For example:

Note that the

operator, the

, specifies the cardinality,

number of items in the resulting sequence. If this is not specified, the cardinality is assumed to

be 1. In SQL Server, only the question mark (

occurrence indicator is supported. The

occurrence indicator indicates that

can return zero or one item. If the

occurrence

indicator is specified,

returns True when the

type matches the

specified

, regardless of whether

returns a singleton or an empty

sequence.

If the

occurrence indicator is not specified,

returns True only when the

type matches the

specified and

returns a singleton.

Note

The plus symbol (

) and the asterisk (

) occurrence indicators are not supported in SQL

Server.

The following examples illustrate the use of the

XQuery operator.

```sql
instance of
Occurrence indicator
Expression instance of
Expression
SequenceType
Expression sequence of
Expression
Type
Expression
Expression instance of SequenceType[Occurrence indicator]
```
