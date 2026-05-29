---
title: "Each partition can have multiple delta rowgroups"
topic: "io-fundamentals"
description: "state. A background process named the tuple-mover"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

transitions from an

to

state. A background process named the tuple-mover

checks for closed row groups. If the process finds a closed rowgroup, it compresses the

rowgroup and stores it into the columnstore.

When a delta rowgroup has been compressed, the existing delta rowgroup transitions into

state to be removed later by the tuple-mover when there's no reference to it, and

the new compressed rowgroup is marked as

.

For more information about rowgroup statuses, see

sys.dm_db_column_store_row_group_physical_stats

.

You can force delta rowgroups into the columnstore by using

ALTER INDEX

to rebuild or

reorganize the index. If there's memory pressure during compression, the columnstore index

might reduce the number of rows in the compressed rowgroup.

The concept of partitioning is the same in a clustered index, a heap, and a columnstore index.

Partitioning a table divides the table into smaller groups of rows according to a range of

column values. It's often used for managing the data. For example, you could create a partition

for each year of data, and then use partition switching to archive old data to less expensive

storage.

Rowgroups are always defined within a table partition. When a columnstore index is

partitioned, each partition has its own compressed rowgroups and delta rowgroups. A

nonpartitioned table contains one partition.

Each partition can have more than one delta rowgroups. When the columnstore index needs to

add data to a delta rowgroup and the delta rowgroup is locked by another transaction, the

columnstore index tries to obtain a lock on a different delta rowgroup. If there are no delta

rowgroups available, the columnstore index creates a new delta rowgroup. For example, a table

with 10 partitions could easily have 20 or more delta rowgroups.



Tip

Consider using table partitioning if there's a need to remove data from the columnstore.

Switching out and truncating partitions that aren't needed anymore is an efficient strategy

to delete data without introducing fragmentation in the columnstore.

```sql
OPEN
```

```sql
CLOSED
```

```sql
TOMBSTONE
```

```sql
COMPRESSED
```
