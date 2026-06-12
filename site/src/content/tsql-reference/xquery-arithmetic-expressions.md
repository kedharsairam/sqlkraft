---
name: "xquery-arithmetic-expressions"
title: "XQuery - Arithmetic Expressions"
category: "xquery"
description: "XQuery Language Reference: Arithmetic Expressions"
syntax: |
  DECLARE @x xml
  SET @x=''
  SELECT @x.query('2 div 2')
  SELECT @x.query('2 * 2')
  DECLARE @x xml
  SET @x=''
  -- Following will not work
  -- SELECT @x.query('2 idiv 2')
  -- Workaround
  SELECT @x.query('xs:integer(2 div 3)')
tags:
  - "xquery"
  - "arithmetic-expressions"
pubDate: 2025-12-01
---

Article

•

04/03/2023

SQL Server

All arithmetic operators are supported, except for. The following examples illustrate the

basic use of arithmetic operators:

Because

is not supported, a solution is to use the

constructor:

The resulting type from an arithmetic operator is based on the types of the input values. If the

operands are different types, either one or both when required will be cast to a common

primitive base type according to the type hierarchy. For information about type hierarchy, see

Type Casting Rules in XQuery.

Numeric type promotion occurs if the two operations are different numeric base types. For

example, adding an

to an

would first change the decimal value to a

double. Next, addition would be performed that would result in a double value.

Untyped atomic values are cast to the other operand's numeric base type, or to

if

the other operand is also untyped.

These are the limitations:

Arguments for the arithmetic operators must be of numeric type or.

Operations on

values result in a value of type

instead of.

```sql
DECLARE @x xml
SET @x=''
SELECT @x.query('2 div 2')
SELECT @x.query('2 * 2')
DECLARE @x xml
SET @x=''
-- Following will not work
-- SELECT @x.query('2 idiv 2')
-- Workaround
SELECT @x.query('xs:integer(2 div 3)')
```
