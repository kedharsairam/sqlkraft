---
name: "level 140"
title: "level 140"
category: "statements"
description: "consecutive executions. For more information,"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

consecutive executions. For more information,

see

row mode memory grant feedback

.

Queries referencing T-SQL scalar UDFs will use

iterative invocation, lack costing and force serial

execution.

T-SQL scalar UDFs are transformed into

equivalent relational expressions that are

"inlined" into the calling query, often resulting in

significant performance gains. For more

information, see

T-SQL scalar UDF inlining.

Table variables use a fixed guess for the cardinality

estimate. If the actual number of rows is much higher

than the guessed value, performance of downstream

operations can suffer.

New plans will use the actual cardinality of the

table variable encountered on first compilation

instead of a fixed guess. For more information,

see

table variable deferred compilation.

For more information on query processing features enabled in database compatibility level

150, refer to

What's new in SQL Server 2019

and

Intelligent query processing in SQL databases

.

This section describes new behaviors introduced with compatibility level 140.

Cardinality estimates for statements referencing

multi-statement table-valued functions use a fixed

row guess.

Cardinality estimates for eligible statements

referencing multi-statement table-valued functions

will use the actual cardinality of the function

output. This is enabled via

for multi-statement table-valued functions.

Batch-mode queries that request insufficient

memory grant sizes that result in spills to disk

might continue to have issues on consecutive

executions.

Batch-mode queries that request insufficient

memory grant sizes that result in spills to disk

might have improved performance on consecutive

executions. This is enabled via

which will update the

memory grant size of a cached plan if spills have

occurred for batch mode operators.

Batch-mode queries that request an excessive

memory grant size that results in concurrency

issues might continue to have issues on

consecutive executions.

Batch-mode queries that request an excessive

memory grant size that results in concurrency

issues might have improved concurrency on

consecutive executions. This is enabled via

which will update

ﾉ

Expand table

#### Compatibility level setting of 130 or lower

#### Compatibility level setting of 140

#### adaptive

#### join

#### Compatibility level setting of 120 or lower

#### Compatibility level setting of 130

#### CardinalityEstimationModelVersion="130"
