---
name: "xquery-comparison-expressions"
title: "XQuery - Comparison Expressions"
category: "xquery"
description: "XQuery Language Reference: Comparison Expressions"
syntax: |
  declare @x xml
            set @x=''
tags: ["xquery","comparison-expressions"]
pubDate: 2025-12-01
---

XQuery provides the following types of comparison operators:

General comparison operators

Value comparison operators

Node comparison operators

Node order comparison operators

General comparison operators can be used to compare atomic values, sequences, or any

combination of the two.

The general operators are defined in the following table.

Description

=

Equal

!=

Not equal

<

Less than

>

Greater than

<=

Less than or equal to

> =

Greater than or equal to

When you are comparing two sequences by using general comparison operators and a value

exists in the second sequence that compares True to a value in the first sequence, the overall

result is True. Otherwise, it is False. For example, (1, 2, 3) = (3, 4) is True, because the value 3

appears in both sequences.

Expand table

```sql
declare @x xml set @x=''
```
