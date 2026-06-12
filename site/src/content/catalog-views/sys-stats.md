---
name: "sys.stats"
title: "sys.stats"
category: "compatibility"
description: "filtered index, the number of rows might be less than the number of rows in the table. Total number of rows sampled for statistics calculations. Number of steps in the histogram. For more information, see DBCC SHOW_STATISTICS (Transact-SQL) unfiltered_rows Total number of rows in the table before applying the filter expression (for filtered statistics). If statistics are not filtered, unfiltered_r"
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: "HumanResources.Employee"
---

## Description

filtered index, the number of rows might be less than the number of rows in the table. Total number of rows sampled for statistics calculations. Number of steps in the histogram. For more information, see DBCC SHOW_STATISTICS (Transact-SQL) unfiltered_rows Total number of rows in the table before applying the filter expression (for filtered statistics). If statistics are not filtered, unfiltered_rows is equal to the value returns in the rows column. modification_counter Total number of modifications for the leading statistics column (the column on which the histogram is built) since the last time statistics were updated.

## Syntax

`HumanResources.Employee`

## Permissions

## Remarks

filtered index, the number of rows might be less than the

number of rows in the table.

rows_sampled

Total number of rows sampled for statistics calculations.

Number of steps in the histogram. For more information, see

DBCC SHOW_STATISTICS (Transact-SQL)

unfiltered_rows

Total number of rows in the table before applying the filter

expression (for filtered statistics). If statistics are not filtered,

unfiltered_rows is equal to the value returns in the rows column.

modification_counter

Total number of modifications for the leading statistics column

(the column on which the histogram is built) since the last time

statistics were updated.

Memory-optimized tables: starting SQL Server 2016 (13.x) and in

this column contains: total number of

modifications for the table since the last time statistics were

updated or the database was restarted.

persisted_sample_percent

Persisted sample percentage used for statistic updates that do

not explicitly specify a sampling percentage. If value is zero, then

no persisted sample percentage is set for this statistic.

2016 (13.x) SP1 CU4

returns an empty rowset under any of the following conditions:

The specified object is not found or does not correspond to a table or indexed view.

The specified statistics ID does not correspond to existing statistics for the specified

The current user does not have permissions to view the statistics object.

This behavior allows for the safe usage of

when cross applied to

rows in views such as

Statistics update date is stored in the

statistics blob object

together with the

density vector

, not in the metadata. When no data is read to generate statistics data, the

statistics blob is not created, the date is not available, and the

last_updated

column is NULL.

This is the case for filtered statistics for which the predicate does not return any rows, or for

new empty tables.

## Examples

### Example 1

`HumanResources.Employee`

### Example 2

```sql
USE
AdventureWorks2022;
GO
SELECT s.name
AS statistics_name,
c.name
AS column_name,
sc.stats_column_id
FROM sys.stats
AS s
INNER
JOIN sys.stats_columns
AS sc
ON s.object_id = sc.object_id
AND s.stats_id = sc.stats_id
INNER
JOIN sys.columns
AS c
ON sc.object_id = c.object_id
AND c.column_id = sc.column_id
WHERE s.object_id = OBJECT_ID(
'HumanResources.Employee'
);
```
