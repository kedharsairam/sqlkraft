---
name: "Aggregate functions"
title: "Aggregate functions"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

An aggregate function in the

Microsoft SQL Database Engine

performs a calculation on a set of

values, and returns a single value. Except for

, aggregate functions ignore

values.

Aggregate functions are often used with the

clause of the SELECT statement.

All aggregate functions are deterministic. In other words, aggregate functions return the same

value each time that they are called, when called with a specific set of input values. See

Deterministic and nondeterministic functions

for more information about function

determinism. The

OVER clause

might follow all aggregate functions, except the

,

, or

functions.

Use aggregate functions as expressions only in the following situations:

The select list of a

statement (either a subquery or an outer query).

A

clause.

Transact-SQL provides the following aggregate functions:

ANY_VALUE

APPROX_COUNT_DISTINCT

AVG

CHECKSUM_AGG

COUNT

COUNT_BIG

GROUPING

GROUPING_ID

MAX

MIN

STDEV

STDEVP

STRING_AGG

SUM

VAR

VARP
