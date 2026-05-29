---
title: sys.dm_xtp_gc_queue_stats
name: sys.dm_xtp_gc_queue_stats
category: execution
description:
pubDate: 2026-05-29
---

Article

•

05/19/2025

SQL Server

Azure SQL Database

Azure SQL Managed Instance

For more information, see

In-Memory OLTP overview and usage scenarios

.

The following dynamic management views (DMVs) are used with In-Memory OLTP:

sys.dm_xtp_gc_queue_stats

sys.dm_xtp_gc_stats

sys.dm_xtp_system_memory_consumers

sys.dm_xtp_transaction_stats

sys.dm_db_xtp_checkpoint_files

sys.dm_db_xtp_checkpoint_stats

sys.dm_db_xtp_gc_cycle_stats

sys.dm_db_xtp_hash_index_stats

sys.dm_db_xtp_index_stats

sys.dm_db_xtp_memory_consumers

sys.dm_db_xtp_merge_requests

sys.dm_db_xtp_nonclustered_index_stats

sys.dm_db_xtp_object_stats

sys.dm_db_xtp_table_memory_stats

sys.dm_db_xtp_transactions

sys.dm_db_xtp_undeploy_status

The following object catalog views are used with In-Memory OLTP.

sys.hash_indexes

sys.memory_optimized_tables_internal_attributes

There are additional DMVs that are intended for internal use only, and for which we provide no

direct documentation. In the area of memory-optimized tables, undocumented DMVs include

the following:

## Applies to:

Article

•

07/08/2024

SQL Server

Azure SQL Database

Azure SQL Managed Instance

## Returns statistics about the In-Memory OLTP checkpoint operations in the current database. If

the database has no In-Memory OLTP objects,

returns an

empty result set.

For more information, see

In-Memory OLTP (In-Memory Optimization)

.

SQL

SQL Server 2014 (12.x) is substantially different from more recent versions, and is discussed

separately.

The following table describes the columns in

, for SQL

Server 2016 (13.x) and later versions.

Last LSN seen by the controller.

The LSN of the end of log.

Log bytes unprocessed by the controller,

corresponding to the bytes between

and

.

Rate of transaction log consumption by the

controller (in KB/sec).

Time spent by the controller in actively

scanning the transaction log.

Cumulative wait time for the controller while

not scanning the log.

SQL Server 2016 and later versions

ﾉ

Number of waits for log IO incurred by the

controller thread.

Cumulative time spent waiting on log IO by

the controller thread.

Number of waits incurred by the controller

thread for a new log to be generated.

Cumulative time spent waiting on a new log

by the controller thread.

Number of times the controller transitioned

to an idle state.

Number of segments seen by the controller

and dispatched to the serializers. Segment is

a contiguous portion of log that forms a

unit of serialization. It is currently sized to 1

MB, but can change in future.

Total byte count of bytes dispatched by the

controller to serializers, since the database

restart.

Total count of bytes serialized since

database restart.

Time spent by serializers in user mode.

Time spent by serializers in kernel mode.

Total count of log bytes consumed since the

database restart.

Count of checkpoints closed since the

database restart.

Timestamp of the last closed checkpoint.

Recovery starts from this LSN.

GUID of the root file that hardened as a

result of the last completed checkpoint.

. Specifies how far it is valid to

read the root file up to (this is an internally

relevant type only - called BSN).

LSN of the truncation point.

Bytes from last close to the current end of

log.

Time since last close of the checkpoint.

Currently new segments are being assigned

to this checkpoint. The checkpoint system is

a pipeline. The current checkpoint is the one

which segments from the log are being

assigned to. Once it reaches a limit, the

controller releases the checkpoint, and a

new one created as current.

Count of segments in the current

checkpoint.

. Candidate to be picked as

recoverylsn when

closes.

Number of checkpoints in the pipeline

waiting to be closed.

ID of the closing checkpoint.

Serializers are working in parallel, so once

they finish, the checkpoint is a candidate for

closing by close thread. But the close thread

can only close one at a time and it must be

in order, so the closing checkpoint is the

one that the close thread is working on.

ID of the checkpoint to be used in recovery.

Time stamp of recovery checkpoint.

Recovery LSN for the bootstrap.

GUID of the root file for the bootstrap.

Error seen by any of the controller, serializer,

close, and merge threads.

Specifies the amount of data that was

serialized.

True if database is in in-memory OLTP

checkpoint-only mode.

SQL Server 2022 (16.x) and later

versions.

SQL Server 2019 (15.x) and earlier versions require

permission on the

database.

SQL Server 2022 (16.x) and later versions, require

permission

on the database.

Introduction to Memory-Optimized Tables

Memory-Optimized Table Dynamic Management Views (Transact-SQL)

In-Memory OLTP Overview and Usage Scenarios

Optimize performance by using in-memory technologies in Azure SQL Database

Optimize performance by using in-memory technologies in Azure SQL Managed Instance

## Applies to:

## SQL Server 2016 (13.x)

## Note

## CHECKPOINT (Transact-SQL)

Article

•

03/05/2024

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Displays information about In-Memory OLTP checkpoint files, including file size, physical

location and the transaction ID.

A memory-optimized file group internally uses append-only files to store inserted and deleted

rows for in-memory tables. There are two types of files. A data file contains inserted rows while

a delta file contains references to deleted rows.

SQL Server 2014 (12.x) is substantially different from more recent versions and is discussed in

SQL Server 2014

.

For more information, see

Creating and Managing Storage for Memory-Optimized Objects

.

The following table describes the columns for

, beginning with

.

container_id

The ID of the container (represented as a file with type

FILESTREAM in

) that the data or

delta file is part of. Joins with

in

sys.database_files (Transact-SQL)

.

container_guid

GUID of the Container, which the root, data or delta file

is part of. Joins with

in the

７

For the current checkpoint that has not closed, the state column of

will be UNDER CONSTRUCTION for new files. A

checkpoint closes automatically when there is sufficient transaction log growth since the

last checkpoint, or if you issue the

command. For more information, see

.

ﾉ

table.

checkpoint_file_id

GUID of the checkpoint file.

relative_file_path

Path of the file relative to container it is mapped to.

file_type

-1 for FREE

0 for DATA file.

1 for DELTA file.

2 for ROOT file

3 for LARGE DATA file

file_type_desc

FREE- All files maintained as FREE are available for

allocation. Free files can vary in size depending on

anticipated needs by the system. The maximum size is 1

GB.

DATA - Data files contain rows that have been inserted

into memory-optimized tables.

DELTA - Delta files contain references to rows in data

files that have been deleted.

ROOT - Root files contain system metadata for memory-

optimized and natively compiled objects.

LARGE DATA - Large data files contain values inserted in

(n)varchar(max) and varbinary(max) columns, as well as

the column segments that are part of columnstore

indexes on memory-optimized tables.

internal_storage_slot

The index of the file in the internal storage array.

for ROOT or for state other than

.

checkpoint_pair_file_id

Corresponding DATA or DELTA file.

for ROOT.

file_size_in_bytes

Size of the file on the disk.

file_size_used_in_bytes

For checkpoint file pairs that are still being populated,

this column will be updated after the next checkpoint.

logical_row_count

For Data, number of rows inserted.

For Delta, number of rows deleted after accounting for

drop table.

For Root, NULL.

state

0 - PRECREATED

1 - UNDER CONSTRUCTION

2 - ACTIVE

3 - MERGE TARGET

8 - WAITING FOR LOG TRUNCATION

state_desc

PRECREATED - A number of checkpoint files are

preallocated to minimize or eliminate any waits to

allocate new files as transactions are being executed.

These files can vary in size, and are created depending

on the estimated needs of the workload. They contain

no data. This is a storage overhead in databases with a

MEMORY_OPTIMIZED_DATA filegroup.

UNDER CONSTRUCTION - These checkpoint files are

under construction, meaning they are being populated

based on the log records generated by the database,

and are not yet part of a checkpoint.

ACTIVE - These contain the inserted/deleted rows from

previous closed checkpoints. They contain the contents

of the tables that area read into memory before

applying the active part of the transaction log at the

database restart. We expect that size of these checkpoint

files to be approximately 2x of the in-memory size of

memory-optimized tables, assuming the merge

operation is keeping up with the transactional workload.

MERGE TARGET - The target of merge operations - these

checkpoint files store the consolidated data rows from

the source files that were identified by the merge policy.

Once the merge is installed, the MERGE TARGET

transitions into ACTIVE state.

WAITING FOR LOG TRUNCATION - Once the merge has

been installed and the MERGE TARGET CFP is part of

durable checkpoint, the merge source checkpoint files

transition into this state. Files in this state are needed for

operational correctness of the database with memory-

optimized table. For example, to recover from a durable

checkpoint to go back in time.

## SQL Server

## 2014 (12.x)

lower_bound_tsn

Lower bound of the transaction in the file;

if state

not in (1, 3).

upper_bound_tsn

Upper bound of the transaction in the file;

if state

not in (1, 3).

begin_checkpoint_id

ID of the begin checkpoint.

end_checkpoint_id

ID of the end checkpoint.

last_updated_checkpoint_id

ID of the last checkpoint that updated this file.

encryption_status

0, 1, 2

encryption_status_desc

0 => UNENCRYPTED

1 => ENCRYPTED WITH KEY 1

2 => ENCRYPTED WITH KEY 2. Valid only for active files.

The following table describes the columns for

, for

.

container_id

The ID of the container (represented as a file with

type FILESTREAM in

) that the

data or delta file is part of. Joins with

in

sys.database_files (Transact-SQL)

.

container_guid

The GUID of the container that the data or delta file is

part of.

checkpoint_file_id

ID of the data or delta file.

relative_file_path

Path to the data or delta file, relative to the location

of the container.

file_type

0 for data file.

1 for delta file.

ﾉ

if the state column is set to 7.

file_type_desc

The type of file: DATA_FILE, DELTA_FILE, or

if the

state column is set to 7.

internal_storage_slot

The index of the file in the internal storage array.

if the state column is not 2 or 3.

checkpoint_pair_file_id

The corresponding data or delta file.

file_size_in_bytes

Size of the file that is used.

if the state column is

set to 5, 6, or 7.

file_size_used_in_bytes

Used size of the file that is used.

if the state

column is set to 5, 6, or 7.

For checkpoint file pairs that are still being

populated, this column will be updated after the next

checkpoint.

inserted_row_count

Number of rows in the data file.

deleted_row_count

Number of deleted rows in the delta file.

drop_table_deleted_row_count

The number of rows in the data files affected by a

drop table. Applies to data files when the state

column equals 1.

Shows deleted row counts from dropped table(s). The

drop_table_deleted_row_count statistics are compiled

after the memory garbage collection of the rows

from dropped table(s) is complete and a checkpoint

is taken. If you restart SQL Server before the drop

tables statistics are reflected in this column, the

statistics will be updated as part of recovery. The

recovery process does not load rows from dropped

tables. Statistics for dropped tables are compiled

during the load phase and reported in this column

when recovery completes.

state

0 - PRECREATED

1 - UNDER CONSTRUCTION

2 - ACTIVE

3 - MERGE TARGET

4 - MERGED SOURCE

5 - REQUIRED FOR BACKUP/HA

6 - IN TRANSITION TO TOMBSTONE

7 - TOMBSTONE

state_desc

PRECREATED - A small set of data and delta file pairs,

also known as checkpoint file pairs (CFPs) are kept

preallocated to minimize or eliminate any waits to

allocate new files as transactions are being executed.

They are created with a data file size of 128 MB and

delta file size of 8 MB, but contain no data. The

number of CFPs is computed as the number of logical

processors or schedulers (one per core, no maximum)

with a minimum of 8. This is a fixed storage overhead

in databases with memory-optimized tables.

UNDER CONSTRUCTION - Set of CFPs that store

newly inserted and possibly deleted data rows since

the last checkpoint.

ACTIVE - These contain the inserted and deleted rows

from previous closed checkpoints. These CFPs

contain all required inserted and deleted rows

required before applying the active part of the

transaction log at the database restart. The size of

these CFPs will be approximately two times the in-

memory size of memory-optimized tables, assuming

the merge operation is current with the transactional

workload.

MERGE TARGET - The CFP stores the consolidated

data rows from the CFP(s) that were identified by the

merge policy. Once the merge is installed, the MERGE

TARGET transitions into ACTIVE state.

MERGED SOURCE - Once the merge operation is

installed, the source CFPs are marked as MERGED

SOURCE. Note, the merge policy evaluator might

identify multiple merges but a CFP can only

participate in one merge operation.

REQUIRED FOR BACKUP/HA - Once the merge has

been installed and the MERGE TARGET CFP is part of

durable checkpoint, the merge source CFPs transition

into this state. CFPs in this state are needed for

```sql
sys.dm_xtp_threads
sys.dm_xtp_transaction_recent_rows
```

```sql
sys.dm_db_xtp_checkpoint_stats
```

```sql
sys.dm_db_xtp_checkpoint_stats
```

```sql
last_lsn_processed
```

```sql
end_of_log_lsn
```

```sql
bytes_to_end_of_log
```

```sql
last_lsn_processed
```

```sql
end_of_log_lsn
```

```sql
log_consumption_rate
```

```sql
active_scan_time_in_ms
```

```sql
total_wait_time_in_ms
```

```sql
USE
[In_Memory_db_name]
SELECT
*
FROM
sys.dm_db_xtp_checkpoint_stats;
```

```sql
waits_for_io
```

```sql
io_wait_time_in_ms
```

```sql
waits_for_new_log_count
```

```sql
new_log_wait_time_in_ms
```

```sql
idle_attempts_count
```

```sql
tx_segments_dispatched
```

```sql
segment_bytes_dispatched
```

```sql
bytes_serialized
```

```sql
serializer_user_time_in_ms
```

```sql
serializer_kernel_time_in_ms
```

```sql
xtp_log_bytes_consumed
```

```sql
checkpoints_closed
```

```sql
last_closed_checkpoint_ts
```

```sql
hardened_recovery_lsn
```

```sql
hardened_root_file_guid
```

```sql
hardened_root_file_watermark
```

```sql
hardened_truncation_lsn
```

```sql
log_bytes_since_last_close
```

```sql
time_since_last_close_in_ms
```

```sql
current_checkpoint_id
```

```sql
current_checkpoint_segment_count
```

```sql
recovery_lsn_candidate
```

```sql
current_checkpoint_id
```

```sql
outstanding_checkpoint_count
```

```sql
closing_checkpoint_id
```

```sql
recovery_checkpoint_id
```

```sql
recovery_checkpoint_ts
```

```sql
bootstrap_recovery_lsn
```

```sql
bootstrap_root_file_guid
```

```sql
internal_error_code
```

```sql
bytes_of_large_data_serialized
```

```sql
db_in_checkpoint_only_mode
```

```sql
VIEW DATABASE STATE
```

```sql
VIEW DATABASE PERFORMANCE STATE
```

```sql
sys.dm_db_xtp_checkpoint_files
```

```sql
sys.database_files
```

```sql
file_id
```

```sql
file_guid
```

```sql
sys.dm_db_xtp_checkpoint_files
```

```sql
CHECKPOINT
```

```sql
sys.database_files
```

```sql
NULL
```

```sql
1
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
sys.dm_db_xtp_checkpoint_files
```

```sql
sys.database_files
```

```sql
file_id
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```
