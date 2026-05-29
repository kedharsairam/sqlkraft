---
name: 'sys.stats_columns'
title: 'sys.stats_columns'
category: 'objects'
description: 'Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column that is part of ID of the object of which this column is part. ID of the statistics of which this column is part. If statistics correspond to an index, the 1-based ordinal within set of stats columns. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on'
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: 'HumanResources.Employee'
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column that is part of ID of the object of which this column is part. ID of the statistics of which this column is part. If statistics correspond to an index, the 1-based ordinal within set of stats columns. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see

## Syntax

```sql
HumanResources.Employee
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each column that is part of statistics. Description ID of the object of which this column is part. ID of the statistics of which this column is part. If statistics correspond to an index, the stats_id value is the same as the index_id value in the sys.indexes catalog view. 1-based ordinal within set of stats columns. ID of the column from . The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Querying the SQL Server System Catalog FAQ Statistics sys.dm_db_stats_properties (Transact-SQL) sys.dm_db_stats_histogram (Transact-SQL) sys.stats (Transact-SQL) Statistics in Microsoft Fabric Last updated on 11/18/2025 ﾉ Expand table See Also

## Examples

### Example 1

```sql
HumanResources.Employee
```

### Example 2

```sql
USE
AdventureWorks2022;
GO
SELECT
s.name
AS
statistics_name,
c.name
AS
column_name,
sc.stats_column_id
FROM
sys.stats
AS
s
INNER
JOIN
sys.stats_columns
AS
sc
ON
s.object_id = sc.object_id
AND
s.stats_id = sc.stats_id
INNER
JOIN
sys.columns
AS
c
ON
sc.object_id = c.object_id
AND
c.column_id = sc.column_id
WHERE
s.object_id = OBJECT_ID(
'HumanResources.Employee'
);
```
