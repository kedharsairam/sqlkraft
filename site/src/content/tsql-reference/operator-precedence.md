---
name: "Operator precedence"
title: "Operator precedence"
category: "operators"
description: ""
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

#### Level

#### Operators

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

When a complex expression contains multiple operators, operator precedence determines the

sequence of operations. The order of execution can significantly affect the resulting value.

Operators have the precedence levels shown in the following table. An operator on a higher

level is evaluated before an operator on a lower level. In the following table, 1 is the highest

level and 8 is the lowest level.

1

(bitwise

)

2

(multiplication),

(division),

(modulus)

3

(positive),

(negative),

(addition),

(concatenation),

(subtraction),

(bitwise

),

(bitwise exclusive

),

(bitwise

),

(bitwise left shift),

(bitwise right shift)

4

,

,

,

,

,

,

,

,

(comparison operators)

5

6

7

,

,

,

,

,

,

8

(assignment)

When two operators in an expression have the same precedence level, the evaluation happens

from left to right based on their position in the expression. For example, in the expression used

in the following

statement, the subtraction operator is evaluated before the addition

operator.

Expand table

Use parentheses to override the defined precedence of the operators in an expression.

Everything within parentheses is evaluated to yield a single value. Any operator outside those

parentheses can use that value.

For example, in the expression used in the following

statement, the multiplication operator

has a higher precedence than the addition operator. The multiplication operation is evaluated

first. The expression result is.

In the expression used in the following

statement, the parentheses cause the addition to

be evaluated first. The expression result is.

If an expression has nested parentheses, the most deeply nested expression is evaluated first.

The following example contains nested parentheses, with the expression

in the most

deeply nested set of parentheses. This expression yields a value of. Then, the addition

operator (

) adds this result to

, which yields a value of. Finally, the

is multiplied by

to

yield an expression result of.

Logical operators (Transact-SQL)
