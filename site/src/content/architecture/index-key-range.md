---
title: "index key range"
topic: "index-architecture"
description: "pages can occur if you have relatively few data files in a filegroup and a large number of CPU"
tags: ["index-architecture","architecture"]
pubDate: 2026-05-29
---

pages can occur if you have relatively few data files in a filegroup and a large number of CPU

cores. A simple way to resolve this is to increase the number of files per filegroup.

If many

waits are observed for PFS or SGAM pages in

, complete these

steps to eliminate this bottleneck:

1. Add data files to

so that the number of tempdb data files is equal to the number

of processor cores in your server.

2. Enable SQL Server Trace Flag 1118.

For more information about allocation bottlenecks caused by contention on system pages, see

the blog post

What is allocation bottleneck?

There are other factors beyond allocation contention that can cause latch contention on

, such as heavy TVF use within queries.

The following sections describe techniques that can be used to address or work around

performance issues related to excessive latch contention.

One method for handling latch contention is to replace a sequential index key with a non-

sequential key to evenly distribute inserts across an index range.

Typically this is done by having a leading column in the index that distributes the workload

proportionally. There are a couple of options here:

２

Warning

Increasing the number of files per filegroup might adversely affect performance of certain

loads, such as loads with many large sort operations that spill memory to disk.

Evaluate your workload for a natural value that can be used to distribute inserts across the key

range. For example, consider an ATM banking scenario where

might be a good

candidate to distribute inserts into a transaction table for withdrawals since one customer can

only use one ATM at a time. Similarly in a point of sales system, perhaps

or a Store

ID would be a natural value that could be used to distribute inserts across a key range. This

technique requires creating a composite index key with the leading key column being either

the value of the column identified or some hash of that value combined with one or more extra

columns to provide uniqueness. In most cases, a hash of the value works best, because too

many distinct values result in poor physical organization. For example, in a point of sales

system, a hash can be created from the Store ID that is some modulo, which aligns with the

number of CPU cores. This technique would result in a relatively small number of ranges within

the table however it would be enough to distribute inserts in such a way to avoid latch

contention. The following image illustrates this technique.

）

Important

This pattern contradicts traditional indexing best practices. While this technique helps

ensure uniform distribution of inserts across the B-tree, it might also necessitate a schema

change at the application level. In addition, this pattern might negatively affect

performance of queries that require range scans that utilize the clustered index. Some

analysis of the workload patterns is required to determine if this design approach works

## Original table definition

## Reordered index definition

This pattern was implemented during a performance lab engagement and resolved latch

contention on a system with 32 physical CPU cores. The table was used to store the closing

balance at the end of a transaction; each business transaction performed a single insert into

the table.

When using the original table definition, excessive latch contention was observed to occur on

the clustered index pk_table1:

Reordering the key columns of the index with

as the leading column in the primary key

provided an almost random distribution of inserts across the pages. The resulting distribution

wasn't 100% random since not all users are online at the same time, but the distribution was

random enough to alleviate excessive latch contention. One caveat of reordering the index

definition is that any select queries against this table must be modified to use both

and

as equality predicates.

well. This pattern should be implemented if you're able to sacrifice some sequential scan

performance to gain insert throughput and scale.

７

Note

The object names in the table definition have been changed from their original values.

）

Important

## Using a hash value as the leading column in primary key

`PAGELATCH_UP`

`tempdb`

`tempdb`

`tempdb`

`ATM_ID`

`Checkout_ID`

`UserID`

`UserID`

`TransactionID`

```sql
CREATE
TABLE table1 (
TransactionID
BIGINT
NOT
NULL
,
UserID
INT
NOT
NULL
,
SomeInt
INT
NOT
NULL
);
GO
ALTER
TABLE table1
ADD
CONSTRAINT pk_table1 PRIMARY
KEY
CLUSTERED (TransactionID, UserID);
GO
```
