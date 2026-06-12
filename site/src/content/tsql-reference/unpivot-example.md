---
name: "UNPIVOT example"
title: "UNPIVOT example"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: 2026-05-29
---

carries out almost the reverse operation of

, by rotating columns into rows.

Suppose the table produced in the previous example is stored in the database as

, and you

want to rotate the column identifiers

,

,

,

, and

into row values that

correspond to a particular vendor. As such, you must identify two extra columns.

The column that contains the column values that you're rotating (

,

, and so on) is

called

, and the column that holds the values that currently exist under the columns

being rotated, is called. These columns correspond to the

pivot_column

and

value_column

, respectively, in the Transact-SQL definition. Here's the query.

When aggregate functions are used with

, the presence of any null values in the

value column aren't considered when computing an aggregation.

#### Output

### Object Explorer

### Views

### Script View

### as

Here's a partial result set.

isn't the exact reverse of.

carries out an aggregation and merges possible

multiple rows into a single row in the output.

doesn't reproduce the original table-

valued expression result, because rows have been merged. Also,

values in the input of

disappear in the output. When the values disappear, it shows that there might have

been original

values in the input before the

operation.

The

view in the

sample database

uses

to return the total sales for each salesperson, for each fiscal year. To script the view

in SQL Server Management Studio, in

, locate the view under the

folder

for the

database. Right-click the view name, and then select.

FROM clause (Transact-SQL)

CASE (Transact-SQL)
