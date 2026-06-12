---
name: "Histogram"
title: "Histogram"
category: "statements"
description: "(4, 4, 6), (4, 5, 6), (4, 5, 7). Using the prefix (A, B) the same column values have these distinct"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

## Description

(4, 4, 6), (4, 5, 6), (4, 5, 7). Using the prefix (A, B) the same column values have these distinct

value lists: (3, 5), (4, 4), and (4, 5)

Average

Length

Average length, in bytes, to store a list of the column values for the column prefix. For

example, if the values in the list (3, 5, 6) each require 4 bytes the length is 12 bytes.

Columns

Names of columns in the prefix for which All density and Average length are displayed.

option is specified.

## Description

Upper bound column value for a histogram step. The column value is also called a

key value.

Estimated number of rows whose column value falls within a histogram step,

excluding the upper bound.

histogram step.

Estimated number of rows with a distinct column value within a histogram step,

excluding the upper bound.

Average number of rows with duplicate column values within a histogram step,

excluding the upper bound. When

is greater than 0,

is calculated by dividing

by.

When

is 0,

## returns 1 for the histogram step.

Statistics update date is stored in the

statistics blob object

together with the

histogram

and

density vector

, not in the metadata. When no data is read to generate statistics data, the

statistics blob isn't created, the date isn't available, and the

column is. This is the

case for filtered statistics for which the predicate doesn't return any rows, or for new empty

tables.

Expand table

A histogram measures the frequency of occurrence for each distinct value in a data set. The

query optimizer computes a histogram on the column values in the first key column of the

statistics object, selecting the column values by statistically sampling the rows or by performing

a full scan of all rows in the table or view. If the histogram is created from a sampled set of

rows, the stored totals for number of rows and number of distinct values are estimates and

don't need to be whole integers.

To create the histogram, the query optimizer sorts the column values, computes the number of

values that match each distinct column value and then aggregates the column values into a

maximum of 200 contiguous histogram steps. Each step includes a range of column values

followed by an upper bound column value. The range includes all possible column values

between boundary values, excluding the boundary values themselves. The lowest of the sorted

column values is the upper boundary value for the first histogram step.

The following diagram shows a histogram with six steps. The area to the left of the first upper

boundary value is the first step.

For each histogram step:

Bold line represents the upper boundary value (RANGE_HI_KEY) and the number of times

it occurs (EQ_ROWS)

Solid area left of RANGE_HI_KEY represents the range of column values and the average

number of times each column value occurs (AVG_RANGE_ROWS). The AVG_RANGE_ROWS

for the first histogram step is always 0.

Dotted lines represent the sampled values used to estimate total number of distinct

values in the range (DISTINCT_RANGE_ROWS) and total number of values in the range

(RANGE_ROWS). The query optimizer uses RANGE_ROWS and DISTINCT_RANGE_ROWS to

compute AVG_RANGE_ROWS and doesn't store the sampled values.

#### Column prefix

#### Density calculated on

`HISTOGRAM`

`RANGE_HI_KEY`

`RANGE_ROWS`

`EQ_ROWS`

`DISTINCT_RANGE_ROWS`

`AVG_RANGE_ROWS`

`DISTINCT_RANGE_ROWS`

`AVG_RANGE_ROWS`

`RANGE_ROWS`

`DISTINCT_RANGE_ROWS`

`DISTINCT_RANGE_ROWS`

`AVG_RANGE_ROWS`

`updated`

`NULL`
