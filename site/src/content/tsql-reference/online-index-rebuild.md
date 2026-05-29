---
name: 'Online index rebuild'
title: 'Online index rebuild'
category: 'queries'
description: 'Dropping a clustered index requires temporary disk space that''s equal to the size of the existing'
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

Dropping a clustered index requires temporary disk space that's equal to the size of the existing

clustered index. This operation releases the additional space as soon as it completes.

When you run

on a published table at a SQL Server Publisher, the change

propagates to all SQL Server Subscribers by default. This functionality has some restrictions. You

can disable it. For more information, see

Make Schema Changes on Publication Databases

.

You can't enable compression for system tables. If the table is a heap, the rebuild operation for

mode is single-threaded. Use

mode for a multithreaded heap rebuild operation.

For more information about data compression, see

Data compression

.

To evaluate how changing the compression state affects a table, an index, or a partition, use the

sp_estimate_data_compression_savings

system stored procedure.

The following restrictions apply to partitioned tables:

You can't change the compression setting of a single partition if the table has nonaligned

indexes.

The

... syntax rebuilds the specified partition.

The

... syntax rebuilds all partitions.

When you drop columns that use the deprecated

data type, the cleanup of the deleted

data occurs as a serialized operation on all rows. The cleanup can require a large amount of time.

When you drop an

column in a table with lots of rows, update the

column to

value first, and then drop the column. You can run this option with parallel operations and make

it much faster.

７

Note

The options listed under

apply to clustered indexes on

tables. You can't apply these options to clustered indexes on views or nonclustered indexes.

```sql
ALTER TABLE
```

```sql
ONLINE
```

```sql
OFFLINE
```

```sql
ALTER TABLE <table> REBUILD PARTITION
```

```sql
ALTER TABLE <table> REBUILD WITH
```

```sql
NULL
```

```sql
<drop_clustered_constraint_option>
```
