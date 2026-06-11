---
title: "Last page/trailing page insert contention"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

means some statistics such as

are rarely useful. The following command can

be used to reset the wait statistics for this DMV:

The following scenarios have been observed to cause excessive latch contention.

A common OLTP practice is to create a clustered index on an identity or date column. This

helps maintain good physical organization of the index, which can greatly benefit performance

of both reads and writes to the index. This schema design can inadvertently lead to latch

contention however. This issue is most commonly seen with a large table, with small rows; and

inserts into an index containing a sequentially increasing leading key column such as ascending

integer or datetime key. In this scenario, the application rarely if ever performs updates or

deletes, the exception being for archiving operations.

In the following example, thread one and thread two both want to perform an insert of a

record that will be stored on page 299. From a logical locking perspective, there's no problem,

as row level locks are used, and exclusive locks on both records on the same page can be held

at the same time. However to ensure integrity of physical memory only one thread at a time

can acquire an exclusive latch so access to the page is serialized to prevent lost updates in

memory. In this case, thread 1 acquires the exclusive latch; and thread 2 waits, which registers a

wait for this resource in the wait statistics. This is displayed through the

value in the

DMV.

SQL Server latch contention scenarios

This contention is commonly referred to as "Last Page Insert" contention because it occurs on

the right-most edge of the B-tree as displayed in the following diagram:

This type of latch contention can be explained as follows. When a new row is inserted into an

index, SQL Server uses the following algorithm to execute the modification:

1. Traverse the B-tree to locate the correct page to hold the new record.

2. Latch the page with

, preventing others from modifying it, and acquire

shared latches (

) on all the non-leaf pages.

７

Note

In some cases, the SQL Engine requires

latches to be acquired on non-leaf B-tree

pages as well. For example, when a page-split occurs, any pages that are directly

affected need to be exclusively latched (

).

3. Record a log entry that the row has been modified.

4. Add the row to the page and mark the page as dirty.

5. Unlatch all pages.

If the table index is based upon a sequentially increasing key, each new insert goes to the same

page at the end of the B-tree, until that page is full. Under high-concurrency scenarios, this

might cause contention on the rightmost edge of the B-tree and can occur on clustered and

non-clustered indexes. Tables that are affected by this type of contention primarily accept

queries, and pages for the problematic indexes are normally relatively dense (for

example, a row size ~165 bytes (including row overhead) equals ~49 rows per page). In this

insert-heavy example, we expect

/

waits to occur, and this is the

typical observation. To examine Page Latch waits vs. Tree Page Latch waits, use the

DMV.

The following table summarizes the major factors observed with this type of latch contention:

This type of latch contention occurs mainly on 16+ CPU core systems and most

commonly on 32+ CPU core systems.

Uses a sequentially increasing identity value as a leading column in an index on a table

for transactional data.

The index has an increasing primary key with a high rate of inserts.

The index has at least one sequentially increasing column value.

Typically small row size with many rows per page.

Many threads contending for same resource with exclusive (

) or shared (

) latch

waits associated with the same resource_description in the

DMV as returned by the

Query sys.dm_os_waiting_tasks Ordered by Wait Duration

.

Consider changing the order of the index columns as described in the Non-sequential

index mitigation strategy if you can guarantee that inserts are distributed across the B-

tree uniformly all of the time.

If the Hash partition mitigation strategy is used, it removes the ability to use

partitioning for any other purposes such as sliding window archiving.

ﾉ

Expand table

`max_wait_time_ms`

`PAGELATCH_EX`

`wait_type`

`sys.dm_os_waiting_tasks`

```sql
DBCC SQLPERF ('sys.dm_os_latch_stats', CLEAR);
```

`PAGELATCH_EX`

`PAGELATCH_SH`

`EX`

`PAGELATCH_EX`

`INSERT`

`PAGELATCH_EX`

`PAGELATCH_SH`

`sys.dm_db_index_operational_stats`

`EX`

`SH`

`sys.dm_os_waiting_tasks`
