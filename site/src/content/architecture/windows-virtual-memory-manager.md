---
title: "Windows Virtual Memory Manager"
topic: "memory-management"
description: "Azure SQL Managed Instance"
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

The committed regions of address space are mapped to the available physical memory by the

Windows Virtual Memory Manager (VMM).

For more information on the amount of physical memory supported by different operating

systems, see the Windows documentation on

Memory Limits for Windows Releases

.

Virtual memory systems allow the over-commitment of physical memory, so that the ratio of

virtual-to-physical memory can exceed 1:1. As a result, larger programs can run on computers

with various physical memory configurations. However, using significantly more virtual memory

than the combined average working sets of all the processes can cause poor performance.

SQL Server dynamically acquires and frees memory as required. Typically, an administrator

doesn't have to specify how much memory should be allocated to SQL Server, although the

option still exists and is required in some environments.

One of the primary design goals of all database software is to minimize disk I/O because disk

reads and writes are among the most resource-intensive operations. SQL Server builds a buffer

pool in memory to hold pages read from the database. Much of the code in SQL Server is

dedicated to minimizing the number of physical reads and writes between the disk and the

buffer pool. SQL Server tries to reach a balance between two goals:

Keep the buffer pool from becoming so large that the entire system is low on memory.

Minimize physical I/O to the database files by maximizing the size of the buffer pool.

In a heavily loaded system, some large queries that require a large amount of memory to run

can't get the minimum amount of requested memory, and receive a time-out error while

waiting for memory resources. To resolve this, increase the

query wait Option

. For a parallel

query, consider reducing the

max degree of parallelism

value.

In a heavily loaded system under memory pressure, queries with merge join, sort, and bitmap

in the query plan can drop the bitmap when the queries don't get the minimum required

memory for the bitmap. This can affect the query performance and if the sorting process can't

fit in memory, it can increase the usage of worktables in

database, causing

to

SQL Server memory architecture

```sql
tempdb
```

```sql
tempdb
```
