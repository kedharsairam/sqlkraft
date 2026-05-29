---
title: 'Supported features'
topic: 'query-processing'
description: 'For a detailed explanation of disk I/O in SQL Server, see'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

For a detailed explanation of disk I/O in SQL Server, see

SQL Server I/O fundamentals

.

A buffer is an 8-KB page in memory, the same size as a data or index page. Thus, the buffer

cache is divided into 8-KB pages. The buffer manager manages the functions for reading data

or index pages from the database disk files into the buffer cache, and writing modified pages

back to disk. A page remains in the buffer cache until the buffer manager needs the buffer area

to read in more data. Data is written back to disk only if it's modified. Data in the buffer cache

can be modified multiple times before being written back to disk. For more information, see

Read data pages in the Database Engine

and

Write pages in the Database Engine

.

When SQL Server starts, it computes the size of virtual address space for the buffer cache

based on several parameters such as the amount of physical memory on the system, the

configured number of maximum server threads, and various startup parameters. SQL Server

reserves this computed amount of its process virtual address space (called the memory target)

for the buffer cache, but it acquires (commits) only the required amount of physical memory

for the current load. You can query the

and

columns in the

sys.dm_os_sys_info

catalog view to return the number of pages reserved as the memory target

and the number of pages currently committed in the buffer cache, respectively.

The interval between SQL Server startup and when the buffer cache obtains its memory target

is called ramp-up. During this time, read requests fill the buffers as needed. For example, a

single 8-KB page read request fills a single buffer page. This means the ramp-up depends on

the number and type of client requests. Ramp-up is expedited by transforming single page

read requests into aligned eight page requests (making up one extent). This allows the ramp-

up to finish much faster, especially on machines with a lot of memory. For more information

about pages and extents, see

Page and extent architecture guide

.

Because the buffer manager uses most of the memory in the SQL Server process, it cooperates

with the memory manager to allow other components to use its buffers. The buffer manager

interacts primarily with the following components:

Resource Manager to control overall memory usage and, in 32-bit platforms, to control

address space usage.

Database Manager and the SQL Server Operating System (SQLOS) for low-level file I/O

operations.

Log Manager for write-ahead logging.

The buffer manager supports the following features:

### trace

### flag 834

```sql
committed_target_kb
```

```sql
committed_kb
```
