---
title: "and random inserts (queue table)"
topic: "query-processing"
description: "Use of the Hash partition mitigation strategy can lead to partition elimination"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Use of the Hash partition mitigation strategy can lead to partition elimination

problems for

queries used by the application.

This scenario is typically seen when a SQL table is used as a temporary queue (for example, in

an asynchronous messaging system).

In this scenario exclusive (

) and shared (

) latch contention can occur under the following

conditions:

Insert, select, update, or delete operations occur under high concurrency.

Row size is relatively small (leading to dense pages).

The number of rows in the table is relatively small; leading to a shallow B-tree, defined by

having an index depth of two or three.

Latch contention can occur even if access is random across the B-tree such as when a non-

sequential column is the leading key in a clustered index. The following screenshot is from a

system experiencing this type of latch contention. In this example, contention is due to the

density of the pages caused by small row size and a relatively shallow B-tree. As concurrency

increases, latch contention on pages occurs even though inserts are random across the B-tree

since a GUID was the leading column in the index.

In the following screenshot, the waits occur on both buffer data pages and pages free space

(PFS) pages. Even when the number of data files was increased, latch contention was prevalent

on buffer data pages.

７

Note

Even B-trees with a greater depth than this can experience contention with this type of

access pattern, if the frequency of data manipulation language (DML) and concurrency of

the system is high enough. The level of latch contention might become pronounced as

concurrency increases when 16 or more CPU cores are available to the system.

The following table summarizes the major factors observed with this type of latch contention:

Latch contention occurs mainly on computers with 16+ CPU cores.

High rate of insert/select/update/delete access patterns against small tables.

Shallow B-tree (index depth of two or three).

Small row size (many records per page).

Latch contention occurs only under high levels of concurrent requests from the

application tier.

Observe waits on buffer (

and

) and non-buffer latch

due to root splits. Also

waits on PFS

pages. For more information about non-buffer latch waits, see

sys.dm_os_latch_stats

in SQL Server help.

ﾉ

Expand table

`SELECT`

`EX`

`SH`

`PAGELATCH_EX`

`PAGELATCH_SH`

`ACCESS_METHODS_HOBT_VIRTUAL_ROOT`

`PAGELATCH_UP`
