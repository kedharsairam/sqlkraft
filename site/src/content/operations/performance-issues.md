---
title: "Performance issues"
topic: "ssms"
description: |
  Article

  •

  11/22/2024

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  When you analyze the T-SQL code in your database project, one or more
tags:
  - "ssms"
  - "performance-issues"
pubDate: 2025-12-01
---

Article

•

11/22/2024

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

When you analyze the T-SQL code in your database project, one or more warnings might be

categorized as performance issues. You should address a performance issue to avoid the

following situation:

A table scan occurs when the code is executed.

In general, you might suppress a performance issue if the table contains so little data that a

scan won't cause performance to drop significantly.

The provided rules identify the following performance issues:

SR0004: Avoid using columns that don't have indexes as test expressions in IN predicates

SR0005: Avoid using patterns that start with "%" in LIKE predicates

SR0006: Move a column reference to one side of a comparison operator to use a column

index

SR0007: Use ISNULL(column, default_value) on nullable columns in expressions

SR0015: Extract deterministic function calls from WHERE predicates

You cause a table scan if you use a WHERE clause that references one or more columns that

aren't indexed as part of an IN predicate. The table scan reduces performance.

To resolve this issue, you must make one of the following changes:

Change the IN predicate to reference only those columns that have an index.

Add an index to any column that the IN predicate references and that doesn't already

have an index.

In this example, a simple SELECT statement references a column, [c1], that didn't have an index.

The second statement defines an index that you can add to resolve this warning.
