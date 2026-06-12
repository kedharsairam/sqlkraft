---
title: "Walkthrough: Diagnose a latch contention"
topic: "io-fundamentals"
description: "Allows the use of other partitioning features, such as archiving data using a sliding"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Allows the use of other partitioning features, such as archiving data using a sliding

window scheme and partition switch functionality.

Possible challenges when choosing a key/index to ensure 'close enough to' uniform

distribution of inserts all of the time.

GUID as a leading column can be used to guarantee uniform distribution with the caveat

that it can result in excessive page-split operations.

Random inserts across B-Tree can result in too many page-split operations and lead to

latch contention on non-leaf pages.

Transparent for inserts.

Partitioning can't be used for intended management features such as archiving data using

partition switch options.

Can cause partition elimination issues for queries including individual and range-based

select/update, and queries that perform a join.

Adding a persisted computed column is an offline operation.

The following walkthrough demonstrates the tools and techniques described in

Diagnosing

Latch Contention

and

Handling Latch Contention for Different Table Patterns

to

resolve a problem in a real world scenario. This scenario describes a customer engagement to

perform load testing of a point of sales system, which simulated approximately 8,000 stores

performing transactions against a SQL Server application running on an 8 socket, 32 physical

core system with 256 GB of memory.



Tip

For more techniques, see the blog post.
