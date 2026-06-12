---
title: "Dynamic partition of memory objects"
topic: "memory-management"
description: "page protection because it's affected by every byte of the page, however, it's moderately"
tags: ["memory-management","architecture"]
pubDate: "2026-05-29"
---

page protection because it's affected by every byte of the page, however, it's moderately

resource-intensive.

When checksum is enabled, errors caused by power failures and flawed hardware or firmware

can be detected any time the buffer manager reads a page from disk. For information on

setting checksum, see

ALTER DATABASE SET Options.

is non-uniform memory access (NUMA) aware, and performs well on NUMA

hardware without special configuration. As clock speed and the number of processors increase,

it becomes increasingly difficult to reduce the memory latency required to use this extra

processing power. To circumvent this, hardware vendors provide large L3 caches, but this is

only a limited solution. NUMA architecture provides a scalable solution to this problem.

is designed to take advantage of NUMA-based computers without requiring any

application changes. For more information, see

Soft-NUMA (SQL Server).

Heap allocators, known as

memory objects

in SQL Server, allow the Database Engine to allocate

memory from the heap. These can be tracked using the

sys.dm_os_memory_objects

DMV.

is a thread-safe memory object type that allows concurrent memory allocations

from multiple threads. For correct tracking,

objects rely on synchronization

constructs (a mutex) to ensure only a single thread is updating critical pieces of information at

a time.

）

Important

When a user or system database is upgraded to SQL Server 2005 (9.x) or later, the

value (

or

) is retained. We highly recommend that

you use.

might use fewer resources, but provides a

minimal subset of the

protection.

７

Note

The

object type is utilized throughout the Database Engine code base for

many different allocations, and can be partitioned globally, by node or by CPU.

However, the use of mutexes can lead to contention if many threads are allocating from the

same memory object in a highly concurrent fashion. Therefore, SQL Server has the concept of

partitioned memory objects (PMO) and each partition is represented by a single

object. The partitioning of a memory object is statically defined and can't be changed after

creation. As memory allocation patterns vary widely based on aspects like hardware and

memory usage, it's impossible to come up with the perfect partitioning pattern upfront.

In most cases, using a single partition suffices, but in some scenarios this can lead to

contention, which can be prevented only with a highly partitioned memory object. It isn't

desirable to partition each memory object as more partitions can result in other inefficiencies

and increase memory fragmentation.

Starting with SQL Server 2014 (12.x) SP2 and SQL Server 2016 (13.x), the Database Engine can

dynamically detect contention on a specific

object and promote the object to a

per-node or a per-CPU based implementation. Once promoted, the PMO remains promoted

until the SQL Server process is restarted.

contention can be detected by the

presence of high

waits in the

sys.dm_os_wait_stats

DMV, and by observing the

sys.dm_os_memory_objects

DMV columns

,

,

, and.

I/O fundamentals

Server memory configuration options

Read data pages in the Database Engine

Write pages in the Database Engine

Soft-NUMA (SQL Server)

Requirements for using memory-optimized tables

Troubleshoot out of memory or low memory issues in SQL Server

Resolve Out Of Memory issues

７

Note

Before SQL Server 2016 (13.x), trace flag 8048 could be used to force a node-based PMO

to become a CPU-based PMO. Starting with SQL Server 2014 (12.x) SP2 and SQL Server

2016 (13.x), this behavior is dynamic and controlled by the engine.
