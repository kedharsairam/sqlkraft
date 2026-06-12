---
title: "Index metadata"
topic: "index-architecture"
description: "The performance of a nonclustered index is better than with hash indexes when querying a"
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

The performance of a nonclustered index is better than with hash indexes when querying a

memory-optimized table with inequality predicates.

A column in a memory-optimized table can be part of both a hash index and a nonclustered

index.

When a key column in a nonclustered index has many duplicate values, performance can

degrade for updates, inserts, and deletes. One way to improve performance in this situation is

to add a column that has better selectivity in the index key.

To examine index metadata such as index definitions, properties, and data statistics, use the

following system views:

sys.objects

sys.indexes

sys.index_columns

sys.columns

sys.types

sys.partitions

sys.internal_partitions

sys.dm_db_index_usage_stats

sys.dm_db_partition_stats

sys.dm_db_index_operational_stats

The previous views apply to all index types. For columnstore indexes, additionally use the

following views:

sys.column_store_row_groups

sys.column_store_segments

sys.column_store_dictionaries

sys.dm_column_store_object_pool

sys.dm_db_column_store_row_group_operational_stats

sys.dm_db_column_store_row_group_physical_stats

For columnstore indexes, all columns are stored in the metadata as included columns. The

columnstore index doesn't have key columns.

For indexes on memory-optimized tables, additionally use the following views:

sys.hash_indexes

sys.dm_db_xtp_hash_index_stats

sys.dm_db_xtp_index_stats

sys.dm_db_xtp_nonclustered_index_stats

sys.dm_db_xtp_object_stats

sys.dm_db_xtp_table_memory_stats

sys.memory_optimized_tables_internal_attributes

CREATE INDEX (Transact-SQL)

Optimize index maintenance to improve query performance and reduce resource

consumption

Partitioned tables and indexes

Indexes on Memory-Optimized Tables

Columnstore indexes: overview

Indexes on computed columns

Tune nonclustered indexes with missing index suggestions
