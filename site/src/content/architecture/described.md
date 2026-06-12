---
title: "Described"
topic: "filestream"
description: ""
tags: ["filestream","described"]
pubDate: 2025-12-01
---

An index is an on-disk structure associated with a table or view that speeds retrieval of rows

from the table or view. An index contains keys built from one or more columns in the table or

view. These keys are stored in a structure (B-tree) that enables SQL Server to find the row or

rows associated with the key values quickly and efficiently.

A table or view can contain the following types of indexes:

Clustered

Clustered indexes sort and store the data rows in the table or view based on their key

values. These key values are the columns included in the index definition. There can be

only one clustered index per table, because the data rows themselves can be stored in

only one order.

The only time the data rows in a table are stored in sorted order is when the table

contains a clustered index. When a table has a clustered index, the table is called a

clustered table. If a table has no clustered index, its data rows are stored in an

unordered structure called a heap.

Nonclustered

Nonclustered indexes have a structure separate from the data rows. A nonclustered

index contains the nonclustered index key values and each key value entry has a

pointer to the data row that contains the key value.

The pointer from an index row in a nonclustered index to a data row is called a row

locator. The structure of the row locator depends on whether the data pages are

stored in a heap or a clustered table. For a heap, a row locator is a pointer to the row.

For a clustered table, the row locator is the clustered index key.

You can add nonkey columns to the leaf level of the nonclustered index to bypass

existing index key limits, and execute fully covered queries. For more information, see

７

Note

Documentation uses the term B-tree generally in reference to indexes. In rowstore

indexes, the Database Engine implements a B+ tree. This does not apply to columnstore

indexes or indexes on memory-optimized tables. For more information, see the.
