---
title: "Buffer management"
topic: "memory-management"
description: ", the initial memory grant can't be exceeded under any condition. If"
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

For

row mode execution

, the initial memory grant can't be exceeded under any condition. If

more memory than the initial grant is needed to execute

hash

or

sort

operations, then the

operations spill to disk. A hash operation that spills is supported by a Workfile in

, while

a sort operation that spills is supported by a

Worktable

.

A spill that occurs during a Sort operation is known as a

Sort Warnings Event Class

. Sort

warnings indicate that sort operations don't fit into memory. This doesn't include sort

operations involving the creation of indexes, only sort operations within a query (such as an

clause used in a

statement).

A spill that occurs during a hash operation is known as a

Hash Warning Event Class

. These

occur when a hash recursion or cessation of hashing (hash bailout) has occurred during a

hashing operation.

Hash recursion occurs when the build input doesn't fit into available memory, resulting in

the split of input into multiple partitions that are processed separately. If any of these

partitions still don't fit into available memory, it's split into subpartitions, which are also

processed separately. This splitting process continues until each partition fits into

available memory or until the maximum recursion level is reached.

Hash bailout occurs when a hashing operation reaches its maximum recursion level and

shifts to an alternate plan to process the remaining partitioned data. These events can

cause reduced performance in your server.

For

batch mode execution

, the initial memory grant can dynamically increase up to a certain

internal threshold by default. This dynamic memory grant mechanism is designed to allow

memory-resident execution of

hash

or

sort

operations running in batch mode. If these

operations still don't fit into memory, then the operations spill to disk.

For more information on execution modes, see the

Query Processing Architecture Guide

.

The primary purpose of a SQL Server database is to store and retrieve data, so intensive disk

I/O is a core characteristic of the Database Engine. And because disk I/O operations can

consume many resources and take a relatively long time to finish, SQL Server focuses on

making I/O highly efficient. Buffer management is a key component in achieving this efficiency.

The buffer management component consists of two mechanisms: the

buffer manager

to access

and update database pages, and the

buffer cache

(also called the

buffer pool

), to reduce

database file I/O.

```sql
tempdb
```

```sql
ORDER BY
```

```sql
SELECT
```
