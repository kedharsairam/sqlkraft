---
title: "Space used by the persistent version store (PVS)"
topic: "io-fundamentals"
description: "Each database row might use up to 14 bytes at the end of the row for row versioning"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Each database row might use up to 14 bytes at the end of the row for row versioning

information. The row versioning information contains the transaction sequence number of the

transaction that committed the version and the pointer to the versioned row. These 14 bytes are

added the first time the row is modified, or when a new row is inserted, under any of these

conditions:

or

options are set to.

The table has a trigger.

Multiple Active Results Sets (MARS) is being used.

Online index build operations are currently running on the table.

Accelerated database recovery (ADR)

is enabled.

These 14 bytes are removed from the database row the first time the row is modified under all of

these conditions:

and

options are set to.

The trigger no longer exists on the table.

MARS isn't being used.

Online index build operations aren't currently running.

Accelerated database recovery (ADR)

is disabled.

If you use any of the row versioning features, you might need to allocate additional disk space for

the database to accommodate the 14 bytes per database row. Adding the row versioning

information can cause index page splits or the allocation of a new data page if there isn't enough

space available on the current page. For example, if the average row length is 100 bytes, the

additional 14 bytes cause an existing table to grow up to 14 percent.

Decreasing the

fill factor

might help to prevent or decrease fragmentation of index pages. To

view current page density information for the data and indexes of a table or view, you can use

sys.dm_db_index_physical_stats.

When ADR is enabled, row versions can be stored in persistent version store (PVS) in one of the

following ways, depending on the size of the row prior to modification:

If the size is small, the entire old row version is stored as a part of the modified row.

If the size is intermediate, the difference between the old row version and the modified row

is stored as a part of the modified row. The difference is constructed in a way that lets the

database engine reconstruct the entire old row version if needed.

### in-row

### off-row

`READ_COMMITTED_SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`READ_COMMITTED_SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

`OFF`
