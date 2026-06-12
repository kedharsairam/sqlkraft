---
title: "Partitioned indexes"
topic: "index-architecture"
description: "Hash or nonclustered for memory-optimized tables"
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

Hash or nonclustered for memory-optimized tables

As you develop your index design strategy, you should consider the placement of the indexes

on the filegroups associated with the database.

By default, indexes are stored in the same filegroup as the base table (clustered index or heap)

on which the index is created. Other configurations are possible, including:

Create nonclustered indexes on a filegroup other than the filegroup of the base table.

Partition clustered and nonclustered indexes to span multiple filegroups.

For nonpartitioned tables, the simplest approach is usually the best: create all tables on the

same filegroup, and add as many data files to the filegroup as necessary to utilize all available

physical storage.

More advanced index placement approaches can be considered when tiered storage is

available. For example, you could create a filegroup for frequently accessed tables with files on

faster disks, and a filegroup for archive tables on slower disks.

You can move a table with a clustered index from one filegroup to another by dropping the

clustered index and specifying a new filegroup or partition scheme in the

clause of the

statement or by using the

statement with the

clause.

You can also consider partitioning disk-based heaps, clustered, and nonclustered indexes

across multiple filegroups. Partitioned indexes are partitioned horizontally (by row), based on a

partition function. The partition function defines how each row is mapped to a partition based

on the values of a certain column you designate, called the partitioning column. A partition

scheme specifies the mapping of a set of partitions to a filegroup.

Partitioning an index can provide the following benefits:

Make large databases more manageable. OLAP systems, for example, can implement

partition-aware ETL that greatly simplifies adding and removing data in bulk.

Make certain types of queries, such as long-running analytical queries, run faster. When

queries use a partitioned index, the Database Engine can process multiple partitions at

the same time and skip (eliminate) partitions that aren't needed by the query.

### Sort

### Sort

```sql
MOVE TO
```

```sql
DROP INDEX
```

```sql
CREATE INDEX
```

`DROP_EXISTING`
