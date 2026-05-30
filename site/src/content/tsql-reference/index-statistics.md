---
name: "Index statistics"
title: "Index statistics"
category: "hints"
description: "To evaluate how changing the compression state affects the space usage by a table, an index,"
tags: ["tsql", "hints"]
pubDate: 2026-05-29
---

To evaluate how changing the compression state affects the space usage by a table, an index,

or a partition, use the

sp_estimate_data_compression_savings

stored procedure.

: SQL Server 2022 (16.x) and later versions, Azure SQL Database, SQL database in

Microsoft Fabric, and Azure SQL Managed Instance.

Many of the data compression considerations apply to XML compression. You should also be

aware of the following considerations:

When a list of partitions is specified, XML compression can be enabled on individual

partitions. If the list of partitions isn't specified, all partitions are set to use XML

compression. When a table or index is created, XML data compression is disabled unless

otherwise specified. When a table is modified, the existing compression is preserved

unless otherwise specified.

If you specify a list of partitions or a partition that is out of range, an error is generated.

When a clustered index is created on a heap, the clustered index inherits the XML

compression state of the heap unless an alternative compression option is specified.

Changing the XML compression setting of a heap requires all nonclustered indexes on the

table to be rebuilt so that they have pointers to the new row locations in the heap.

You can enable or disable XML compression online or offline. Enabling compression on a

heap is single threaded for an online operation.

To determine the XML compression state of partitions in a partitioned table, use the

column of the

catalog view.

When a rowstore index is created, the Database Engine also creates

statistics

on the key

columns of the index. The name of the statistics object in the

sys.stats

catalog view matches

the name of the index. For a non-partitioned index, the statistics are built using a full scan of

the data. For a partitioned index, statistics are build using the default sampling algorithm.

When a columnstore index is created, the Database Engine creates a statistics object in

sys.stats

as well. This statistics object doesn't contain statistics data such as the histogram and

the density vector. It is used when creating a database clone by scripting the database. At that

time, the

and

commands are

used to obtain columnstore metadata such as segment, dictionary, and delta store size and

add it to the statistics on the columnstore index. This metadata is obtained dynamically at

query compilation time for a regular database, but is provided by the statistics object for a

`xml_compression`

`sys.partitions`

```sql
DBCC SHOW_STATISTICS
```

```sql
UPDATE STATISTICS ... WITH STATS_STREAM
```
