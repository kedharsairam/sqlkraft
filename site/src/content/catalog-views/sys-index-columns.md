---
name: 'sys.index_columns'
title: 'sys.index_columns'
category: 'objects'
description: '= Column isn''t an included column.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
= Column isn't an included column.

Columns implicitly added because they're part of the clustering

key aren't listed in

.

Columns implicitly added because they're a partitioning column

are returned as

.

: Azure Synapse Analytics, SQL Server 2022 (16.x),

Azure SQL Database, and Azure SQL Managed Instance

Ordinal (1-based) within set of order columns in an ordered

columnstore index. For more on ordered columnstore indexes,

see

Performance tuning with ordered columnstore indexes

.

0 = Not a columnstore index & data clustering ordinal doesn't

apply

: SQL Server 2025 (17.x)

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following example returns all indexes and index columns for the table

.

SQL

AUTD

Here's the result set.

Output

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

sys.indexes (Transact-SQL)

sys.objects (Transact-SQL)

CREATE INDEX (Transact-SQL)

sys.columns (Transact-SQL)

Querying the SQL Server System Catalog FAQ

Last updated on 11/18/2025

Next steps

```sql
0
```

```sql
sys.index_columns
```

```sql
0
```

```sql
data_clustering_ordinal
```

```sql
Production.BillOfMaterials
```

```sql
USE
AdventureWorks2022;
GO
SELECT
i.name
AS
index_name
,COL_NAME(ic.object_id,ic.column_id)
AS
column_name
,ic.index_column_id
,ic.key_ordinal
,ic.is_included_column
FROM
sys.indexes
AS
i
INNER
JOIN
sys.index_columns
AS
ic
ON
i.object_id = ic.object_id
AND
i.index_id = ic.index_id
WHERE
i.object_id = OBJECT_ID(
'Production.BillOfMaterials'
);
```

```sql
index_name                                                 column_name
index_column_id key_ordinal is_included_column
---------------------------------------------------------- -----------------  ------
--------- ----------- -------------
AK_BillOfMaterials_ProductAssemblyID_ComponentID_StartDate ProductAssemblyID  1
1           0
AK_BillOfMaterials_ProductAssemblyID_ComponentID_StartDate ComponentID        2
2           0
AK_BillOfMaterials_ProductAssemblyID_ComponentID_StartDate StartDate          3
3           0
PK_BillOfMaterials_BillOfMaterialsID                       BillOfMaterialsID  1
1           0
IX_BillOfMaterials_UnitMeasureCode                         UnitMeasureCode    1
1           0
(5 row(s) affected)
```
