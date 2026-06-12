---
title: "inline)"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

This might involve comparing any user-defined code construct that is stored in the

database (such as stored procedures, user-defined functions, or views) with system tables

that hold information on data types used in underlying tables (such as

sys.columns

).

2. If unable to traverse all code to the previous point, then for the same purpose, change

the data type on the table to match any variable/parameter declaration.

3. Reason out the usefulness of the following constructs:

Functions being used as predicates;

Wildcard searches;

Complex expressions based on columnar data - evaluate the need to instead create

persisted computed columns, which can be indexed;

Foreign platform (such as Oracle, DB2, MySQL, and Sybase) and SQL Server to SQL

Server migration.

Table Valued Functions return a table data type that can be an alternative to views. While views

are limited to a single

statement, user-defined functions can contain additional

statements that allow more logic than is possible in views.

Since the output table of a multi-statement table valued function (MSTVF) isn't created at

compile time, the SQL Server Query Optimizer relies on heuristics, and not actual statistics, to

determine row estimations.

Even if indexes are added to the base tables, this isn't going to help.

For MSTVFs, SQL Server uses a fixed estimation of 1 for the number of rows expected to be

returned by an MSTVF (starting with SQL Server 2014 (12.x) that fixed estimation is 100 rows).

７

Note

All of these steps can be done programmatically.

７

Note

For SQL Server to SQL Server migrations, if this issue existed in the source SQL Server,

migrating to a newer version of SQL Server as-is doesn't address this scenario.

`SELECT`
