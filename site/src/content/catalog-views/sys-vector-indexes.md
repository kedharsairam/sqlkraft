---
name: 'sys.vector_indexes'
title: 'sys.vector_indexes'
category: 'indexes'
description: 'SQL Server 2025 (17.x)'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2025 (17.x)

Contains a row per vector index.


## Description
Inherits columns from

sys.indexes

.

varchar(20)

Type of vector index (DiskANN only for now)

varchar(20)

Metric used to create the vector index

nvarchar(max)

Internal usage only

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following example returns all indexes for the table

used in the

DiskANN sample

available in the

GitHub sample repo

.

SQL

ﾉ

Expand table

Related content

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

sys.indexes (Transact-SQL)

CREATE VECTOR INDEX (Transact-SQL)

sys.dm_db_vector_indexes (Transact-SQL)

Last updated on 03/18/2026

```sql
[dbo].[wikipedia_articles_embeddings]
```

```sql
SELECT
object_id,
index_id,
vector_index_type,
distance_metric,
build_parameters
FROM
sys.vector_indexes
AS
vi
WHERE
object_id = OBJECT_ID(
'[dbo].[wikipedia_articles_embeddings]'
)
```
