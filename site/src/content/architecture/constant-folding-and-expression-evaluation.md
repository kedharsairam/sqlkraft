---
title: "Constant folding and expression evaluation"
topic: "io-fundamentals"
description: "The basic steps that SQL Server uses to process a single SELECT statement include the"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

The basic steps that SQL Server uses to process a single SELECT statement include the

following:

1. The parser scans the

statement and breaks it into logical units such as keywords,

expressions, operators, and identifiers.

2. A query tree, sometimes referred to as a sequence tree, is built describing the logical

steps needed to transform the source data into the format required by the result set.

3. The Query Optimizer analyzes different ways the source tables can be accessed. It then

selects the series of steps that return the results fastest while using fewer resources. The

query tree is updated to record this exact series of steps. The final, optimized version of

the query tree is called the execution plan.

4. The relational engine starts executing the execution plan. As the steps that require data

from the base tables are processed, the relational engine requests that the storage engine

pass up data from the rowsets requested from the relational engine.

5. The relational engine processes the data returned from the storage engine into the

format defined for the result set and returns the result set to the client.

SQL Server evaluates some constant expressions early to improve query performance. This

optimization technique used by the query optimizer aims to simplify expressions at compile

time rather than at runtime. It involves evaluating constant expressions during query

７

Note

SQL Server Management Studio has three options to display execution plans:

The

, which is the compiled plan, as produced by the Query

Optimizer.

The

, which is the same as the compiled plan plus its execution

context. This includes runtime information available after the execution completes,

such as execution warnings, or in newer versions of the Database Engine, the elapsed

and CPU time used during execution.

The

, which is the same as the compiled plan plus its execution

context. This includes runtime information during execution progress, and is updated

every second. Runtime information includes for example the actual number of rows

flowing through the operators.

`SELECT`
