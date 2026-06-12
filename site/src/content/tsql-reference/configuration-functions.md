---
name: "Configuration functions"
title: "Configuration functions"
category: "statements"
description: "T-SQL reference for Configuration functions syntax and usage."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

ﾃ

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

Learn about the categories of built-in functions you can use with SQL databases. You can use

the built-in functions or create your own user-defined functions.

Aggregate functions perform a calculation on a set of values and return a single value. They're

allowed in the select list or the

clause of a

statement. You can use an

aggregation in combination with the

clause to calculate the aggregation on

categories of rows. Use the

clause to calculate the aggregation on a specific range of

value. The

clause can't follow the

or

aggregations.

All aggregate functions are deterministic, which means they always return the same value when

they run on the same input values. For more information, see

Deterministic and

nondeterministic functions.

Analytic functions compute an aggregate value based on a group of rows. However, unlike

aggregate functions, analytic functions can return multiple rows for each group. You can use

analytic functions to compute moving averages, running totals, percentages, or top-N results

within a group.

2022 (16.x) and later versions, Azure SQL Managed Instance, Azure SQL

Database, SQL database in Microsoft Fabric

Bit manipulation functions allow you to process and store data more efficiently than with

individual bits. For more information, see

Bit manipulation functions.

#### Function category

`HAVING`

`SELECT`

```sql
GROUP BY
```

`OVER`

`OVER`

`GROUPING`

`GROUPING_ID`
