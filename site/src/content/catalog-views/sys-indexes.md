---
name: 'sys.indexes'
title: 'sys.indexes'
category: 'indexes'
description: 'indexes are supported only on memory-optimized tables. The'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

indexes are supported only on memory-optimized tables. The

view shows the current hash indexes and the hash properties. For more

information, see

sys.hash_indexes

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

The following example returns all indexes for the table

in the

AdventureWorks2025 database.

SQL

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

sys.index_columns

sys.xml_indexes

8

Related content

sys.objects

sys.key_constraints

sys.filegroups

sys.partition_schemes

Querying the SQL Server System Catalog FAQ

In-Memory OLTP overview and usage scenarios

Last updated on 11/24/2025

```sql
NONCLUSTERED HASH
```

```sql
sys.hash_indexes
```

```sql
Production.Product
```

```sql
SELECT
i.name
AS
index_name,
i.type_desc,
is_unique,
ds.type_desc
AS
filegroup_or_partition_scheme,
ds.name
AS
filegroup_or_partition_scheme_name,
ignore_dup_key,
is_primary_key,
is_unique_constraint,
fill_factor,
is_padded,
is_disabled,
allow_row_locks,
allow_page_locks
FROM
sys.indexes
AS
i
INNER
JOIN
sys.data_spaces
AS
ds
ON
i.data_space_id = ds.data_space_id
WHERE
is_hypothetical = 0
AND
i.index_id <> 0
AND
i.object_id = OBJECT_ID(
'Production.Product'
);
GO
```
