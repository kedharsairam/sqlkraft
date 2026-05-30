---
title: "How does SQL Server use latches?"
topic: "latch-contention"
description: "latch. Latches are also used to protect access to internal memory structures other than buffer"
tags: ["latch-contention", "architecture"]
pubDate: 2026-05-29
---

latch. Latches are also used to protect access to internal memory structures other than buffer

pool pages; these are known as Non-Buffer latches.

Contention on page latches is the most common scenario encountered on multi-CPU systems

and so most of this article focuses on these.

Latch contention occurs when multiple threads concurrently attempt to acquire incompatible

latches to the same in-memory structure. As a latch is an internal control mechanism; the SQL

engine automatically determines when to use them. Because the behavior of latches is

deterministic, application decisions including schema design can affect this behavior. This

article aims to provide the following information:

Background information on how latches are used by SQL Server.

Tools used to investigate latch contention.

How to determine if the amount of contention being observed is problematic.

We discuss some common scenarios and how best to handle them to alleviate contention.

A page in SQL Server is 8 KB and can store multiple rows. To increase concurrency and

performance, buffer latches are held only for the duration of the physical operation on the

page, unlike locks, which are held for the duration of the logical transaction.

Latches are internal to the SQL engine and are used to provide memory consistency, whereas

locks are used by SQL Server to provide logical transactional consistency. The following table

compares latches to locks:

Guarantee

consistency

of in-

memory

structures.

SQL Server

engine

only.

Performance cost is

low. To allow for

maximum

concurrency and

provide maximum

performance, latches

are held only for the

duration of the

physical operation on

the in-memory

structure, unlike

locks, which are held

sys.dm_os_wait_stats

- Provides

information on

,

, and

wait types

(

,

is used to group

all non-buffer latch waits).

sys.dm_os_latch_stats

– Provides

detailed information about non-buffer

latch waits.

sys.dm_db_index_operational_stats

-

This DMV provides aggregated waits

for each index, which is useful for

ﾉ

Expand table

for the duration of

the logical

transaction.

troubleshooting latch-related

performance issues.

Guarantee

consistency

of

transactions.

Can be

controlled

by user.

Performance cost is

high relative to

latches as locks must

be held for the

duration of the

transaction.

sys.dm_tran_locks

.

sys.dm_exec_sessions

.

Some latch contention is to be expected as a normal part of the operation of the SQL Server

engine. It's inevitable that multiple concurrent latch requests of varying compatibility occur on

a high concurrency system. SQL Server enforces latch compatibility by requiring the

incompatible latch requests to wait in a queue until outstanding latch requests are completed.

Latches are acquired in one of five different modes, which relate to level of access. SQL Server

latch modes can be summarized as follows:

: Keep latch. Ensures that the referenced structure can't be destroyed. Used when a

thread wants to look at a buffer structure. Because the KP latch is compatible with all

latches except for the destroy (DT) latch, the KP latch is considered to be

lightweight

,

meaning that the effect on performance when using it is minimal. Since the KP latch is

incompatible with the DT latch, it prevents any other thread from destroying the

referenced structure. For example, a KP latch prevents the structure it references from

being destroyed by the lazy writer process. For more information about how the lazy

writer process is used with SQL Server buffer page management, see

Write pages in the

Database Engine

.

: Shared latch. Required to read the referenced structure (for example, read a data

page). Multiple threads can simultaneously access a resource for reading under a shared

latch.

: Update latch. Compatible with

(Shared latch) and KP, but no others and therefore

doesn't allow an

latch to write to the referenced structure.

: Exclusive latch. Blocks other threads from writing to or reading from the referenced

structure. One example of use would be to modify contents of a page for torn page

protection.

SQL Server latch modes and compatibility

### Yes

### No

: Destroy latch. Must be acquired before destroying contents of referenced structure.

For example, a DT latch must be acquired by the lazy writer process to free up a clean

page before adding it to the list of free buffers available for use by other threads.

Latch modes have different levels of compatibility, for example, a shared latch (

) is

compatible with an update (UP) or keep (KP) latch but incompatible with a destroy latch (DT).

Multiple latches can be concurrently acquired on the same structure as long as the latches are

compatible. When a thread attempts to acquire a latch held in a mode that isn't compatible, it's

placed into a queue to wait for a signal indicating the resource is available. A spinlock of type

SOS_Task is used to protect the wait queue by enforcing serialized access to the queue. This

spinlock must be acquired to add items to the queue. The SOS_Task spinlock also signals

threads in the queue when incompatible latches are released, allowing the waiting threads to

acquire a compatible latch and continue working. The wait queue is processed on a first in, first

out (FIFO) basis as latch requests are released. Latches follow this FIFO system to ensure

fairness and to prevent thread starvation.

Latch mode compatibility is listed in the following table (

indicates compatibility and

indicates incompatibility):

Yes

Yes

Yes

Yes

No

Yes

Yes

Yes

No

No

Yes

Yes

No

No

No

Yes

No

No

No

No

No

No

No

No

No

With the increasing presence of NUMA based multiple socket / multi-core systems, SQL Server

2005 introduced Superlatches, also known as sublatches, which are effective only on systems

with 32 or more logical processors. Superlatches improve efficiency of the SQL engine for

certain usage patterns in highly concurrent OLTP workloads; for example, when certain pages

have a pattern of heavy read-only shared (

) access, but are written to rarely. An example of a

page with such an access pattern is a B-tree (that is, index) root page; the SQL engine requires

that a shared latch is held on the root page when a page-split occurs at any level in the B-tree.

In an insert-heavy and high-concurrency OLTP workload, the number of page splits increase

ﾉ

Expand table

SQL Server Superlatches and sublatches

### Server and Azure SQL index architecture and design guide

broadly in line with throughput, which can degrade performance. Superlatches can enable

increased performance for accessing shared pages where multiple concurrently running worker

threads require

latches. To accomplish this, the SQL Server Engine dynamically promotes a

latch on such a page to a Superlatch. A Superlatch partitions a single latch into an array of

sublatch structures, one sublatch per partition per CPU core, whereby the main latch becomes

a proxy redirector and global state synchronization isn't required for read-only latches. In

doing so, the worker, which is always assigned to a specific CPU, only needs to acquire the

shared (

) sublatch assigned to the local scheduler.

Acquisition of compatible latches, such as a shared Superlatch uses fewer resources and scales

access to hot pages better than a non-partitioned shared latch because removing the global

state synchronization requirement significantly improves performance by only accessing local

NUMA memory. Conversely, acquiring an exclusive (

) Superlatch is more expensive than

acquiring an

regular latch as SQL must signal across all sublatches. When a Superlatch is

observed to use a pattern of heavy

access, the SQL Engine can demote it after the page is

discarded from the buffer pool. The following diagram depicts a normal latch and a partitioned

Superlatch:

Use the

SQL Server:Latches

object and associated counters in Performance Monitor to gather

information about Superlatches, including the number of Superlatches, Superlatch promotions

７

Note

Documentation uses the term B-tree generally in reference to indexes. In rowstore

indexes, the Database Engine implements a B+ tree. This does not apply to columnstore

indexes or indexes on memory-optimized tables. For more information, see the

.



### Server:Latches

### Buffer (BUF) latch:

### Non-buffer (Non-BUF) latch:

### IO latch:

`PAGELATCH`

`PAGEIOLATCH`

`LATCH`

`LATCH_EX`

`LATCH_SH`

`KP`

`SH`

`UP`

`SH`

`EX`

`EX`

`DT`

`SH`

`KP`

`SH`

`UP`

`EX`

`DT`

`SH`

`SH`

`SH`

`EX`

`EX`

`EX`
