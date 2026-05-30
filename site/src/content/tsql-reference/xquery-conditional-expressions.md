---
name: "xquery-conditional-expressions"
title: "XQuery - Conditional Expressions"
category: "xquery"
description: "XQuery Language Reference: Conditional Expressions"
syntax: "expression1"
tags:
  - "xquery"
  - "conditional-expressions"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

XQuery supports the following conditional

statement:

Depending on the effective Boolean value of

, either

or

is evaluated. For example:

If the test expression,

, results in an empty sequence, the result is False.

If the test expression,

, results in a simple Boolean value, this value is the

result of the expression.

If the test expression,

, results in a sequence of one or more nodes, the result

of the expression is True.

Otherwise, a static error is raised.

Also note the following:

The test expression must be enclosed between parentheses.

The

expression is required. If you do not need it, you can return " ( ) ", as illustrated in

the examples in this topic.

For example, the following query is specified against the

type variable. The

condition

tests the value of the SQL variable (@v) inside the XQuery expression by using the

sql:variable()

function

extension function. If the variable value is "FirstName", it returns the <

>

element. Otherwise, it returns the <

> element.

```sql
expression1 expression2 expression3 expression1 expression1 expression1
FirstName
LastName if (<expression1>) then
<expression2>
else
<expression3>
declare @x xml declare @v varchar(20) set @v='FirstName'
set @x='
<ROOT rootID="2">
```
