---
title: 'Use hash partitioning with a computed column'
topic: 'io-fundamentals'
description: 'the index key approach enables use of partitioning for other features, this technique can also'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

the index key approach enables use of partitioning for other features, this technique can also

introduce potential downsides of more page-splits, poor physical organization and low page

densities.

Table partitioning within SQL Server can be used to mitigate excessive latch contention.

Creating a hash partitioning scheme with a computed column on a partitioned table is a

common approach that can be accomplished with these steps:

1. Create a new filegroup or use an existing filegroup to hold the partitions.

2. If using a new filegroup, equally balance individual files over the LUN, taking care to use

an optimal layout. If the access pattern involves a high rate of inserts, make sure to create

the same number of files as there are physical CPU cores on the SQL Server computer.

3. Use the

command to partition the tables into

X

partitions,

where

X

is the number of physical CPU cores on the SQL Server computer. (at least up to

32 partitions)

4. Use the

command:

Bind the partition function to the filegroups.

Add a hash column of type tinyint or smallint to the table.

Calculate a good hash distribution. For example, use

with modulo or

.

７

Note

The use of GUIDs as leading key columns of indexes is a highly debated subject. An in-

depth discussion of the pros and cons of this method falls outside the scope of this article.

７

Note

A 1:1 alignment of the number of partitions to the number of CPU cores isn't always

necessary. In many cases, this can be some value less than the number of CPU cores.

Having more partitions can result in more overhead for queries that have to search

all partitions, and in these cases fewer partitions can help. In SQLCAT testing on 64

and 128 logical CPU systems with real customer workloads 32 partitions has been

sufficient to resolve excessive latch contention and reach scale targets. Ultimately the

ideal number of partitions should be determined through testing.

```sql
CREATE PARTITION FUNCTION
```

```sql
CREATE PARTITION SCHEME
```

```sql
HASHBYTES
```

```sql
BINARY_CHECKSUM
```
