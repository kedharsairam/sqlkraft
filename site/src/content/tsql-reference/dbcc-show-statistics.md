---
name: "DBCC SHOW_STATISTICS"
title: "DBCC SHOW_STATISTICS"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

Displays current query optimization statistics for a table or indexed view. The query optimizer

uses statistics to estimate the cardinality or number of rows in the query result, which enables

the Query Optimizer to create a high quality query plan. For example, the Query Optimizer

could use cardinality estimates to choose the index seek operator instead of the index scan

operator in the query plan, improving query performance by avoiding a resource-intensive

index scan.

The Query Optimizer stores statistics for a table or indexed view in a statistics object. For a

table, the statistics object is created on either an index or a list of table columns. The statistics

object includes a header with metadata about the statistics, a histogram with the distribution

of values in the first key column of the statistics object, and a density vector to measure cross-

column correlation. The Database Engine can compute cardinality estimates with any of the

data in the statistics object. For more information, see

Statistics

and

Cardinality Estimation (SQL

Server).

displays the header, histogram, and density vector based on data stored

in the statistics object. The syntax lets you specify a table or indexed view along with a target

index name, statistics name, or column name.

Important updates in past versions of SQL Server:

Starting in SQL Server 2012 (11.x) Service Pack 1, the

sys.dm_db_stats_properties

dynamic

management view is available to programmatically retrieve header information contained

in the statistics object for non-incremental statistics.

Starting in SQL Server 2014 (12.x) Service Pack 2 and SQL Server 2012 (11.x) Service Pack

1, the

sys.dm_db_incremental_stats_properties

dynamic management view is available to

programmatically retrieve header information contained in the statistics object for

incremental statistics.

Starting in SQL Server 2016 (13.x) Service Pack 1 CU 2, the

sys.dm_db_stats_histogram

dynamic management view is available to programmatically retrieve histogram

information contained in the statistics object.

This syntax is not supported by serverless SQL pool in Azure Synapse Analytics.

For more information on statistics in Microsoft Fabric Data Warehouse, see

Statistics.

```sql
DBCC SHOW_STATISTICS
```
