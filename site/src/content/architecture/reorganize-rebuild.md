---
title: "Reorganize & rebuild"
topic: "filestream"
description: ""
tags: ["filestream","reorganize-rebuild"]
pubDate: 2025-12-01
---

Analytics Platform System (PDW)

This article helps you decide when and how to perform index maintenance. It covers concepts

such as index fragmentation and page density, and their impact on query performance and

resource consumption. It describes two index maintenance methods:

reorganizing an index

and

rebuilding an index. The article also suggests an index maintenance

strategy

that balances

potential performance improvements against resource consumption required for maintenance.

What is

and how it impacts performance:

In B-tree (rowstore) indexes, fragmentation exists when indexes have pages in which the

logical ordering within the index, based on the key values of the index, doesn't match the

physical ordering of index pages.

The Database Engine automatically modifies indexes whenever insert, update, or delete

operations are made to the underlying data. For example, the addition of rows in a table

can cause existing pages in

rowstore indexes

to split, making room for the insertion of

new rows. Over time these modifications can cause the data in the index to become

scattered in the database (fragmented).

７

Note

This article doesn't apply to a dedicated SQL pool in Azure Synapse Analytics. For

information on index maintenance for a dedicated SQL pool in Azure Synapse Analytics,

see.

７

Note

Documentation uses the term B-tree generally in reference to indexes. In rowstore

indexes, the Database Engine implements a B+ tree. This does not apply to

columnstore indexes or indexes on memory-optimized tables. For more information,

see the

and Azure SQL index architecture and design guide.
