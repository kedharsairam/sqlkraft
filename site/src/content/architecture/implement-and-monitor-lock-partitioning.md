---
title: "Implement and monitor lock partitioning"
topic: "locking"
description: "executed, based on the characteristics of the schema and query."
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

executed, based on the characteristics of the schema and query. For example, to reduce the

overhead of locking, the optimizer might choose page locks in an index when performing an

index scan.

For large computer systems, locks on frequently referenced objects can become a performance

bottleneck as acquiring and releasing locks place contention on internal synchronization

resources. Lock partitioning enhances locking performance by splitting a single lock resource into

multiple lock resources. Only object locks can be partitioned. Object locks that have a subtype

aren't partitioned. For more information, see

sys.dm_tran_locks (Transact-SQL).

Locking tasks access internal resources, two of which are optimized by lock partitioning:

Spinlocks provide internal access synchronization for a lock resource, such as a row or a

table.

Without lock partitioning, one spinlock manages all lock requests for a single lock resource.

On systems that experience a large volume of activity, contention can occur as lock requests

wait for the spinlock to become available. In this situation, acquiring locks can become a

bottleneck and can negatively impact performance.

To reduce contention on a single lock resource, lock partitioning splits a single lock resource

into multiple lock resources to distribute the load across multiple spinlocks.

Memory is used to store the lock resource structures.

Once the spinlock is acquired, lock structures are stored in memory and then accessed and

possibly modified. Distributing lock access across multiple memory resources, each specific

to a CPU, helps eliminate the overhead of memory block transfer between CPUs, which

improves performance.
