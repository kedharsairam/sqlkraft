---
name: "xquery-effective-boolean-value"
title: "XQuery - Effective Boolean Value"
category: "xquery"
description: "XQuery Language Reference: Effective Boolean Value"
syntax: "/a[1]"
tags: ["xquery","effective-boolean-value"]
pubDate: 2025-12-01
---

These are the effective Boolean values:

False if the operand is an empty sequence or a Boolean false.

Otherwise, the value is true.

The effective Boolean value can be computed for expressions that return a single Boolean

value, a node sequence, or an empty sequence. Note that the Boolean value is computed

implicitly when the following types of expressions are processed:

Logical expressions

The

not function

The WHERE clause of a FLWOR expression

Conditional expressions

QuantifiedeExpressions

Following is an example of an effective Boolean value. When the

expression is processed, the

effective Boolean value of the condition is determined. Because

returns an empty

sequence, the effective Boolean value is false. The result is returned as XML with one text node

(false).

In the following example, the effective Boolean value is true, because the expression returns a

nonempty sequence.

```sql
/a[1]
value is false
DECLARE @x XML
SET @x = '<b/>'
SELECT @x.query('if (/a[1]) then "true" else "false"') go
DECLARE @x XML
SET @x = '<a/>'
```
