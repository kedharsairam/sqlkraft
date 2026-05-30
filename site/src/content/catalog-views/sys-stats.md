---
name: "sys.stats"
title: "sys.stats"
category: "compatibility"
description: "filtered index, the number of rows might be less than the number of rows in the table. Total number of rows sampled for statistics calculations. Number of steps in the histogram. For more information, see DBCC SHOW_STATISTICS (Transact-SQL) unfiltered_rows Total number of rows in the table before applying the filter expression (for filtered statistics). If statistics are not filtered, unfiltered_r"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "HumanResources.Employee"
---

## Description

filtered index, the number of rows might be less than the number of rows in the table. Total number of rows sampled for statistics calculations. Number of steps in the histogram. For more information, see DBCC SHOW_STATISTICS (Transact-SQL) unfiltered_rows Total number of rows in the table before applying the filter expression (for filtered statistics). If statistics are not filtered, unfiltered_rows is equal to the value returns in the rows column. modification_counter Total number of modifications for the leading statistics column (the column on which the histogram is built) since the last time statistics were updated. Memory-optimized tables: starting SQL Server 2016 (13.x) and in Azure SQL Database this column contains: total number of modifications for the table since the last time statistics were

## Syntax

`HumanResources.Employee`

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each column that is part of statistics. Description ID of the object of which this column is part. ID of the statistics of which this column is part. If statistics correspond to an index, the stats_id value is the same as the index_id value in the sys.indexes catalog view. 1-based ordinal within set of stats columns. ID of the column from . The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Querying the SQL Server System Catalog FAQ Statistics sys.dm_db_stats_properties (Transact-SQL) sys.dm_db_stats_histogram (Transact-SQL) sys.stats (Transact-SQL) Statistics in Microsoft Fabric Last updated on 11/18/2025 ﾉ Expand table See Also

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

Azure SQL Database this column contains: total number of

modifications for the table since the last time statistics were

updated or the database was restarted.

persisted_sample_percent

Persisted sample percentage used for statistic updates that do

not explicitly specify a sampling percentage. If value is zero, then

no persisted sample percentage is set for this statistic.

SQL Server 2016 (13.x) SP1 CU4

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
