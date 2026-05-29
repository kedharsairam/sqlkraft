---
name: 'sys.column_store_row_groups'
title: 'sys.column_store_row_groups (Transact-'
category: 'objects'
description: 'The updatable columnstore first inserts new data into an open rowgroup, which is in rowstore'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

The updatable columnstore first inserts new data into an open rowgroup, which is in rowstore

format, and is also sometimes referred to as a delta table. Once an open rowgroup is full, its

state changes to

. A closed rowgroup is compressed into columnstore format by the

tuple mover and the state changes to

. The tuple mover is a background process

that periodically wakes up and checks whether there are any closed rowgroups that are ready

to compress into a columnstore rowgroup. The tuple mover also deallocates any rowgroups in

which every row is deleted. Deallocated rowgroups are marked as

. To run tuple

mover immediately, use the

clause of the

statement.

When a columnstore row group fills, it's compressed, and stops accepting new rows. When you

delete rows from a compressed group, they remain but are marked as deleted. Updates to a

compressed group are implemented as a delete from the compressed group, and an insert to

an open group.


## Returns information for a table if the user has
permission on the table.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

The following example joins the

view and other system views to

return information about clustered columnstore indexes. The

column is an

estimate of the efficiency of the row group.

SQL

For more information, see

Check the fragmentation of a columnstore index

.

Columnstore indexes: overview

sys.dm_db_column_store_row_group_physical_stats

sys.column_store_dictionaries [Transact-SQL]

sys.column_store_segments [Transact-SQL]

Querying the SQL Server System Catalog FAQ

Last updated on 01/06/2026

Related content

```sql
CLOSED
```

```sql
COMPRESSED
```

```sql
TOMBSTONE
```

```sql
REORGANIZE
```

```sql
ALTER INDEX
```

```sql
VIEW DEFINITION
```

```sql
sys.column_store_row_groups
```

```sql
percent_full
```

```sql
SELECT
i.object_id,
OBJECT_SCHEMA_NAME(i.object_id)
AS
schema_name,
OBJECT_NAME(i.object_id)
AS
table_name,
i.name
AS
index_name,
i.type_desc
AS
index_type_desc,
rg.partition_number,
rg.row_group_id,
rg.state_description,
rg.total_rows,
rg.deleted_rows,
rg.size_in_bytes,
100 * (rg.total_rows -
ISNULL
(rg.deleted_rows, 0)) / total_rows
AS
percent_full
FROM
sys.indexes
AS
i
```

```sql
INNER
JOIN
sys.column_store_row_groups
AS
rg
ON
i.object_id = rg.object_id
AND
i.index_id = rg.index_id
WHERE
INDEXPROPERTY(i.object_id, i.name,
'IsClustered'
) = 1
ORDER
BY
schema_name, table_name, index_name, row_group_id;
```
