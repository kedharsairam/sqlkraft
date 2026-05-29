---
name: 'sys.stats'
title: 'sys.stats'
category: 'objects'
description: ': SQL Server 2025 (17.x) and later versions,'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
: SQL Server 2025 (17.x) and later versions,

Azure SQL Database, Azure SQL Managed Instance

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

The following examples return all the statistics and statistics columns for the

table.

SQL

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

sys.dm_db_stats_properties (Transact-SQL)

sys.dm_db_stats_histogram (Transact-SQL)

sys.stats_columns (Transact-SQL)

Statistics

sp_updatestats (Transact-SQL)

CREATE STATISTICS (Transact-SQL)

Related content

Create statistics

Last updated on 11/18/2025

```sql
HumanResources.Employee
```

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
