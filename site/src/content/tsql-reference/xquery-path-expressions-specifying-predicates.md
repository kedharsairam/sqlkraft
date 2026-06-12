---
name: "xquery-path-expressions-specifying-predicates"
title: "XQuery - Path Expressions - Specifying Predicates"
category: "xquery"
description: "XQuery Language Reference: Path Expressions - Specifying Predicates"
syntax: |
  declare @x xml
  set @x = '
  <People>
  <Person>
  <Name>John</Name>
  <Age>24</Age>
  </Person>
  <Person>
  <Name>Goofy</Name>
  <Age>54</Age>
  </Person>
  <Person>
  <Name>Daffy</Name>
  <Age>30</Age>
  </Person>
  </People>
  '
tags:
  - "xquery"
  - "path-expressions-specifying-predicates"
pubDate: 2025-12-01
---

Article

•

10/17/2024

SQL Server

As described in the topic,

Path Expressions in XQuery

, an axis step in a path expression includes

the following components:

An axis.

A node test. For more information, see

Specifying Node Test in a Path Expression Step.

Zero or more predicates. This is optional.

The optional predicate is the third part of the axis step in a path expression.

A predicate is used to filter a node sequence by applying a specified test. The predicate

expression is enclosed in a square bracket and is bound to the last node in a path expression.

For example, assume that a SQL parameter value (x) of the

data type is declared, as shown

in the following:

In this case, the following are valid expressions that use a predicate value of [1] at each of three

different node levels:

```sql
declare @x xml set @x = '
<People>
<Person>
<Name>John</Name>
<Age>24</Age>
</Person>
<Person>
<Name>Goofy</Name>
<Age>54</Age>
</Person>
<Person>
<Name>Daffy</Name>
<Age>30</Age>
</Person>
</People>
'
```
