---
name: 'sys.sp_xtp_checkpoint_force_garbage_colle'
title: 'sys.sp_xtp_checkpoint_force_garbage_colle'
category: 'general'
description: 'Marks source files used in the merge operation with the log sequence number (LSN) after'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

A returned row contains the following information:


## Description
Indicates the number of files that have been moved to FILESTREAM

garbage collection. The log sequence number (LSN) of these files is

less than the LSN of log truncation point.

Indicates the number of data/delta files whose LSN has been updated

with the log blockID of the end-of-log LSN.


## Returns the last corresponding LSN up to which the files have been
moved to FILESTREAM garbage collection.

You can manually trigger garbage collection with another system stored procedure,

. You can observe the reduction in memory cleanup in

sys.dm_xtp_system_memory_consumers

.

In SQL Server 2022 (16.x), the

sys.dm_xtp_system_memory_consumers

dynamic management

view has improved insights specific to

Memory-optimized TempDB metadata

.

Requires membership in the

fixed database role.

To mark unneeded source files for garbage collection in the

database, use the following

sample script:

SQL

System stored procedures (Transact-SQL)

sys.sp_xtp_force_gc (Transact-SQL)

ﾉ

Expand table

Related content

In-Memory OLTP overview and usage scenarios

sys.dm_xtp_system_memory_consumers (Transact-SQL)

```sql
num_collected_items
```

```sql
num_marked_for_collection_items
```

```sql
last_collected_xact_seqno
```

```sql
sys.sp_xtp_force_gc
```

```sql
tempdb
```

```sql
EXECUTE
sys.sp_xtp_checkpoint_force_garbage_collection N
'tempdb'
;
```
