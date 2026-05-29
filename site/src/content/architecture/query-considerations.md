---
title: 'Query considerations'
topic: 'query-processing'
description: '### sys.dm_db_index_usage_stats'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

### sys.dm_db_index_usage_stats

### sys.dm_db_index_operational_stats

You can have more indexes on tables that have few data modifications but large

volumes of data. For such tables, a variety of indexes can help query performance

while the index update overhead remains acceptable. However, don't create indexes

speculatively. Monitor index usage, and remove unused indexes over time.

Indexing small tables might not be optimal because it can take the Database Engine

longer to traverse the index searching for data than to perform a base table scan.

Therefore, indexes on small tables might never be used, but must still be updated as the

data in the table is updated.

Indexes on views can provide significant performance gains when the view contains

aggregations and/or joins. For more information, see

Create indexed views

.

Databases on primary replicas in Azure SQL Database automatically generate

database

advisor performance recommendations

for indexes. You can optionally

enable automatic

index tuning

.

Query Store helps identify queries with suboptimal performance

and provides a history of

query execution plans

that let you see the indexes selected by the optimizer. You can use

this data to make your index tuning changes most impactful by focusing on the most

frequent and resource consuming queries.

When you design an index, consider the following query guidelines:

Create nonclustered indexes on the columns that are frequently used in

predicates

and

join expressions in queries. These are your

SARGable

columns. However, you should avoid

adding unnecessary column to indexes. Adding too many index columns can adversely

affect disk space and index update performance.

The term

SARGable

in relational databases refers to a

earch

ument

predicate

that can use an index to speed up the execution of the query. For more information, see

SQL Server and Azure SQL index architecture and design guide

.



Tip

Always make sure that the indexes you create are actually used by the query

workload. Drop unused indexes.

Index usage statistics are available in

and

.

### ntext

### text

### image

### varchar(max)

### nvarchar(max)

### varbinary(max)

### json

### vector

### nonclustered index
