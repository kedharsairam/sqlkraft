---
name: "Use APPLY"
title: "Use APPLY"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Same as above in the

## description, except it

includes rows that became active on the upper boundary defined by the <end_date_time>

endpoint.

: SQL Server 2016 (13.x) and later versions, and SQL Database.

## Returns a table with the values for all record versions that were opened and closed within the

specified time range defined by the two datetime values for the CONTAINED IN argument.

Rows that became active exactly on the lower boundary or ceased being active exactly on the

upper boundary are included.

## Returns a table with the values from all rows from both the current table and the history table.

The FROM clause supports the SQL-92 syntax for joined tables and derived tables. SQL-92

## syntax provides the INNER, LEFT OUTER, RIGHT OUTER, FULL OUTER, and CROSS join

operators.

UNION and JOIN within a FROM clause are supported within views and in derived tables and

subqueries.

A self-join is a table that is joined to itself. Insert or update operations that are based on a self-

join follow the order in the FROM clause.

Because SQL Server considers distribution and cardinality statistics from linked servers that

provide column distribution statistics, the REMOTE join hint isn't required to force evaluating a

join remotely. The SQL Server query processor considers remote statistics and determines

whether a remote-join strategy is appropriate. REMOTE join hint is useful for providers that

don't provide column distribution statistics.

Both the left and right operands of the APPLY operator are table expressions. The main

difference between these operands is that the

right_table_source

can use a table-valued

function that takes a column from the

left_table_source

as one of the arguments of the
