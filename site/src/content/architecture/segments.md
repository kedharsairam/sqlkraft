---
title: "segments"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

When discussing columnstore indexes, we use the terms

rowstore

and

columnstore

to

emphasize the format for the data storage. Columnstore indexes use both types of storage.

A

is data that is logically organized as a table with rows and columns, and

physically stored in a column-wise data format.

A columnstore index physically stores most of the data in columnstore format. In

columnstore format, the data is compressed and uncompressed as columns. There's no

need to uncompress other values in each row that aren't requested by the query. This

makes it fast to scan an entire column of a large table.

A

is data that is logically organized as a table with rows and columns, and then

physically stored in a row-wise data format. This has been the traditional way to store

relational table data such as a clustered B+ tree index or a heap.

A columnstore index also physically stores some rows in a rowstore format called a. The deltastore, also called delta rowgroups, is a holding place for rows that

are too few in number to qualify for compression into the columnstore. Each delta

rowgroup is implemented as a clustered B+ tree index, which is a rowstore.

The columnstore index groups rows into manageable units. Each of these units is called a. For best performance, the number of rows in a rowgroup is large enough to

improve the compression ratio and small enough to benefit from in memory operations.

For example, the columnstore index performs these operations on rowgroups:

## delta rowgroups

## tuple-mover

## column

## segments

Compresses rowgroups into the columnstore. Compression is performed on each column

segment within a rowgroup.

Merges rowgroups during an

operation, including removal

of deleted data.

Recreates all rowgroups during an

operation.

Reports on rowgroup health and fragmentation in the dynamic management views

(DMVs).

The deltastore is comprised of one or more rowgroups called. Each delta

rowgroup is a clustered B+ tree index that stores small bulk loads and inserts until the

rowgroup contains 1,048,576 rows, at which time a process called the

automatically compresses a closed rowgroup into the columnstore.

For more information about rowgroup statuses, see

sys.dm_db_column_store_row_group_physical_stats.

In SQL Server 2019 (15.x) and later versions, the tuple-mover is helped by a background merge

task that automatically compresses smaller open delta rowgroups that have existed for some

time as determined by an internal threshold, or merges compressed rowgroups from which a

large number of rows has been deleted.

Each column has some of its values in each rowgroup. These values are called. Each rowgroup contains one column segment for every column in the table. Each

column has one column segment in each rowgroup.



Tip

Having too many small rowgroups decreases the columnstore index quality. A reorganize

operation merges smaller rowgroups, following an internal threshold policy that

determines how to remove deleted rows and combine the compressed rowgroups. After a

merge, the index quality is improved.

```sql
ALTER INDEX. REORGANIZE
```

```sql
ALTER INDEX. REBUILD
```
