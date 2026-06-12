---
name: "Use PIVOT and UNPIVOT"
title: "Use PIVOT and UNPIVOT"
category: "statements"
description: "can include table-valued functions, but it can't contain"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

function. The

left_table_source

can include table-valued functions, but it can't contain

## arguments that are columns from the

right_table_source.

The APPLY operator works in the following way to produce the table source for the FROM

clause:

1. Evaluates

right_table_source

against each row of the

left_table_source

to produce rowsets.

The values in the

right_table_source

depend on

left_table_source.

right_table_source

can be

represented approximately this way:

, where

is a table-

valued function.

2. Combines the result sets that are produced for each row in the evaluation of

right_table_source

with the

left_table_source

by performing a UNION ALL operation.

The list of columns produced by the result of the APPLY operator is the set of columns

from the

left_table_source

that is combined with the list of columns from the

right_table_source.

The

pivot_column

and

value_column

are grouping columns that are used by the PIVOT

operator. PIVOT follows the following process to obtain the output result set:

1. Performs a GROUP BY on its

input_table

against the grouping columns and produces one

output row for each group.

The grouping columns in the output row obtain the corresponding column values for that

group in the

input_table.

2. Generates values for the columns in the column list for each output row by performing

the following:

a. Grouping additionally the rows generated in the GROUP BY in the previous step

against the

pivot_column.

For each output column in the

column_list

, selecting a subgroup that satisfies the

condition:

b.

aggregate_function

is evaluated against the

value_column

on this subgroup and its

result is returned as the value of the corresponding

output_column. If the subgroup is

empty, SQL Server generates a null value for that

output_column. If the aggregate

function is COUNT and the subgroup is empty, zero (0) is returned.

`TVF(left_table_source.row)`

`TVF`

```sql
pivot_column = CONVERT(<data type of pivot_column>, 'output_column')
```
