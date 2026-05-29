---
name: 'sys.sp_xtp_force_gc'
title: 'sys.sp_xtp_force_gc'
category: 'general'
description: 'Causes the in-memory engine to release memory related to deleted rows of in-memory data'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

When the

@dname

parameter provided is a user database, the memory structures related

memory-optimized tables are affected.

Therefore, you might expect to see different results when executing

:

without a parameter, with

, or with

a user database name.

for success. Nonzero for failure.

Requires membership in the

fixed database role.

Memory-optimized garbage collection happens normally and automatically in response to

memory pressure. You can manually trigger garbage collection with

. You

can observe the reduction in memory cleanup in

sys.dm_xtp_system_memory_consumers

. In

SQL Server 2022 (16.x), the

dynamic management view

has improved insights specific to

Memory-optimized TempDB metadata

.

Contrast with

sys.sp_xtp_checkpoint_force_garbage_collection

, which marks checkpoint files

used in the merge operation with the log sequence number (LSN) after which they aren't

needed and can be garbage collected. Also,

moves the files whose associated LSN is lower than the log truncation point to FILESTREAM

garbage collection.

Prior to SQL Server 2022 (16.x), execute this stored procedure twice.

To execute garbage cleanup on system-level memory structures and memory-optimized

TempDB metadata in SQL Server 2022 (16.x):

SQL

To execute garbage cleanup on system-level memory structures and memory-optimized

TempDB metadata prior to SQL Server 2022 (16.x):

SQL

System stored procedures (Transact-SQL)

sys.sp_xtp_checkpoint_force_garbage_collection (Transact-SQL)

sys.dm_xtp_system_memory_consumers (Transact-SQL)

In-Memory OLTP overview and usage scenarios

Memory-optimized TempDB metadata

Memory-optimized tempdb metadata (HkTempDB) out of memory errors

Related content

```sql
sys.sp_xtp_force_gc
```

```sql
@dbname = N'tempdb'
```

```sql
@dbname =
```

```sql
0
```

```sql
sys.sp_xtp_force_gc
```

```sql
sys.dm_xtp_system_memory_consumers
```

```sql
sys.sp_xtp_checkpoint_force_garbage_collection
```

```sql
EXECUTE
sys.sp_xtp_force_gc N
'tempdb'
;
GO
```

```sql
EXECUTE
sys.sp_xtp_force_gc;
GO
EXECUTE
sys.sp_xtp_force_gc N
'tempdb'
;
GO
EXECUTE
sys.sp_xtp_force_gc N
'tempdb'
;
GO
EXECUTE
sys.sp_xtp_force_gc;
GO
EXECUTE
sys.sp_xtp_force_gc;
GO
```
