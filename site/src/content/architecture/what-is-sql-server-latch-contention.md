---
title: "What is SQL Server latch contention?"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

This guide describes how to identify and resolve latch contention issues observed when

running SQL Server applications on high concurrency systems with certain workloads.

As the number of CPU cores on servers continues to increase, the associated increase in

concurrency can introduce contention points on data structures that must be accessed in a

serial fashion within the database engine. This is especially true for high throughput/high

concurrency transaction processing (OLTP) workloads. There are several tools, techniques, and

ways to approach these challenges as well as practices that can be followed in designing

applications that might help to avoid them altogether. This article discusses a particular type of

contention on data structures that use spinlocks to serialize access to these data structures.

Latches are lightweight synchronization primitives that are used by the SQL Server engine to

guarantee consistency of in-memory structures including; index, data pages, and internal

structures, such as non-leaf pages in a B-Tree. SQL Server uses buffer latches to protect pages

in the buffer pool and I/O latches to protect pages not yet loaded into the buffer pool.

Whenever data is written to or read from a page in the SQL Server buffer pool a worker thread

must first acquire a buffer latch for the page. There are various buffer latch types available for

accessing pages in the buffer pool including exclusive latch (

) and shared latch

(

). When SQL Server attempts to access a page that isn't already present in the

buffer pool, an asynchronous I/O is posted to load the page into the buffer pool. If SQL Server

needs to wait for the I/O subsystem to respond, it waits on an exclusive (

) or

shared (

) I/O latch depending on the type of request; this is done to prevent

another worker thread from loading the same page into the buffer pool with an incompatible

７

Note

This content was written by the Microsoft SQL Server Customer Advisory Team (SQLCAT)

team based on their process for identifying and resolving issues related to page latch

contention in SQL Server applications on high-concurrency systems. The

recommendations and best practices documented here are based on real-world

experience during the development and deployment of real-world OLTP systems.

`PAGELATCH_EX`

`PAGELATCH_SH`

`PAGEIOLATCH_EX`

`PAGEIOLATCH_SH`
