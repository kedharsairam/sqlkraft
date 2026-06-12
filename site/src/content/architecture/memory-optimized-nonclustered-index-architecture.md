---
title: "Memory-optimized nonclustered index architecture"
topic: "index-architecture"
description: "read the older version of the row, and so avoid the performance slowdown associated with a"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

read the older version of the row, and so avoid the performance slowdown associated with a

row lock.

The hash index could also have different versions of its entries to accommodate the update.

Later when the older versions are no longer needed, a garbage collection (GC) thread traverses

the buckets and their link lists to clean away old entries. The GC thread performs better if the

link list chain lengths are short. For more information, see

In-Memory OLTP Garbage Collection.

Besides hash indexes, nonclustered indexes are the other possible index types in a memory-

optimized table. For more information, see

Indexes on Memory-Optimized Tables.

Nonclustered indexes on memory-optimized tables are implemented using a data structure

called a Bw-tree, originally envisioned and described by Microsoft Research in 2011. A Bw-tree

is a lock and latch-free variation of a B-tree. For more information, see

The Bw-tree: A B-tree

for New Hardware Platforms.

At a high level, the Bw-tree can be understood as a map of pages organized by page ID

(PidMap), a facility to allocate and reuse page IDs (PidAlloc) and a set of pages linked in the

page map and to each other. These three high level subcomponents make up the basic internal

structure of a Bw-tree.

The structure is similar to a normal B-tree in the sense that each page has a set of key values

that are ordered and there are levels in the index each pointing to a lower level and the leaf

levels point to a data row. However there are several differences.

Just like with hash indexes, multiple data rows can be linked together to support versioning.

The page pointers between the levels are logical page IDs, which are offsets into a page

mapping table, that in turn has the physical address for each page.

There are no in-place updates of index pages. New delta pages are introduced for this purpose.

No latching or locking is required for page updates.

Index pages aren't a fixed size.

The key value in each nonleaf level page is the highest value that the child that it points to

contains, and each row also contains that page logical page ID. On the leaf-level pages, along

with the key value, it contains the physical address of the data row.
