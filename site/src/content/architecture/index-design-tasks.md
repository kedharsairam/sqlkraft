---
title: "Index design tasks"
topic: "index-architecture"
description: ""
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

Server Management Studio, on the

menu, select

or.

Don't always equate index usage with good performance, and good performance with efficient

index use. If using an index always helped produce the best performance, the job of the query

optimizer would be simple. In reality, an incorrect index choice can cause less than optimal

performance. Therefore, the task of the query optimizer is to select an index, or a combination

of indexes, only when it improves performance, and to avoid indexed retrieval when it hinders

performance.

A common design mistake is to create many indexes speculatively to "give the optimizer

choices". The resulting overindexing slows down data modifications and can cause concurrency

problems.

Rowstore has been the traditional way to store relational table data.

Rowstore

refers to a table

where the underlying data storage format is a heap, a B+ tree (

clustered index

), or a memory-

optimized table.

Disk-based rowstore

excludes memory-optimized tables.

The following tasks make up our recommended strategy for designing indexes:

1.

For example, in an online transaction processing (OLTP) database with frequent data

modifications that must sustain a high throughput, a few narrow rowstore indexes

targeted for the most critical queries would be a good initial index design. For extremely

high throughput, consider memory-optimized tables and indexes, which provide a lock

and latch-free design. For more information, see

Memory-optimized nonclustered index

design guidelines

and

Hash index design guidelines

in this guide.

Conversely, for an analytics or data warehousing (OLAP) database that must process very

large data sets quickly, using clustered columnstore indexes would be especially

appropriate. For more information, see

Columnstore indexes: overview

or

Columnstore

index architecture

in this guide.

2.

For example, knowing that a frequently used query joins two or more tables helps you

determine the set of indexes for these tables.

3.

1

### Determine which index options can enhance performance

### Examine existing indexes on the table to prevent creating duplicate or very similar

### indexes
