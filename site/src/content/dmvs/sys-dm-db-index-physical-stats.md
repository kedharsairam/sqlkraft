---
title: sys.dm_db_index_physical_stats
name: sys.dm_db_index_physical_stats
category: execution
description:
pubDate: 2026-05-29
---

representation of the global dictionary. This provides an inverse

look up of value to dictionary_id. Used for creating compressed

segments as part of Tuple Mover or Bulk Load.

COLUMN_SEGMENT_DELETE_BITMAP - A bitmap that tracks

segment deletes. There is one delete bitmap per partition.

int

Number of read or write accesses to this object.

bigint

Memory used by this object in the object pool.

datetime

Clock-time for when object_id was brought into the object pool.

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

,

, and

service objectives, and for databases in

, the

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

either the

permission on the database, or membership in the

server role is required.

Requires VIEW DATABASE PERFORMANCE STATE permission on the database.

Index Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_db_index_physical_stats (Transact-SQL)

sys.dm_db_index_operational_stats (Transact-SQL)

sys.indexes (Transact-SQL)

sys.objects (Transact-SQL)

Monitor and Tune for Performance

Columnstore indexes: Overview

Last updated on 11/18/2025

## Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

## Returns current row-level I/O, locking, and access method activity for compressed rowgroups

in a columnstore index. Use

to track the

length of time a user query must wait to read or write to a compressed rowgroup or partition

of a columnstore index, and identify rowgroups that are encountering significant I/O activity or

hot spots.

In-memory columnstore indexes don't appear in this DMV.

No

ID of the table with the columnstore index.

No

ID of the columnstore index.

No

1-based partition number within the index or heap.

No

ID of the rowgroup in the columnstore index. This is

unique within a partition.

No

Number of times the columnstore index partition

was scanned. This is the same for all rowgroups in

the partition.

No

Number of scans through the rowgroup since the

last SQL restart.

No

Number of times the delete buffer was used to

determine deleted rows in this rowgroup. This

includes accessing the in-memory hashtable and the

underlying B-tree.

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

ﾉ

## Note

## SQL

## Server and Azure SQL index architecture and design guide

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

No

Identified for informational purposes only. Not

supported. Future compatibility is not guaranteed.

N/A

Cumulative count of lock requests for this rowgroup

since the last SQL Server restart.

N/A

Cumulative number of times the database engine

waited on this rowgroup lock since the last SQL

Server restart.

N/A

Cumulative number of milliseconds the database

engine waited on this rowgroup lock since the last

SQL Server restart.

Requires the following permissions:

permission on the table specified by

.

permission to return information about all objects within the

database, by using the object wildcard

.

７

Documentation uses the term B-tree generally in reference to indexes. In rowstore

indexes, the Database Engine implements a B+ tree. This does not apply to columnstore

indexes or indexes on memory-optimized tables. For more information, see the

.

In SQL Server 2019 (15.x) and earlier versions, requires

permission to

return information about all objects within the database, by using the object wildcard

.

In SQL Server 2022 (16.x) and later versions, requires

permission on the database.

Granting

allows all objects in the database to be returned,

regardless of any

permissions denied on specific objects.

Denying

disallows all objects in the database to be

returned, regardless of any

permissions granted on specific objects. Also, when the

database wildcard

is specified, the database is omitted.

For more information, see

System dynamic management views

.

System dynamic management views

Index Related Dynamic Management Views and Functions (Transact-SQL)

Monitor and Tune for Performance

sys.dm_db_index_physical_stats (Transact-SQL)

sys.dm_db_index_usage_stats (Transact-SQL)

sys.dm_os_latch_stats (Transact-SQL)

sys.dm_db_partition_stats (Transact-SQL)

sys.allocation_units (Transact-SQL)

sys.indexes (Transact-SQL)

Last updated on 12/17/2025

## Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Provides current rowgroup-level information about all of the columnstore indexes in the

current database.

This DMV extends the catalog view

sys.column_store_row_groups

.

ID of the underlying table.

ID of this columnstore index on

table.

ID of the table partition that holds

.

You can use partition_number to join this DMV to

ID of this row group. For partitioned tables, value

is unique within the partition.

for an in-memory tail.

The hobt_id for a row group in the delta store.

if row group isn't in the delta store.

for tail of an in-memory table.

ID number associated

.

=

=

=

=

=

is the only state that applies to in-

memory tables.

Description of the row group state:

-

- A row group that is being built.

ﾉ

For example:

A row group in the columnstore is

while the data is being compressed. When the

compression finishes, a metadata switch changes

the state of the columnstore row group from

to

, and the state of the

deltastore row group from

to

.

-

- A deltastore row group that is

accepting new rows. An open row group is still in

rowstore format and hasn't been compressed to

columnstore format.

-

- A row group in the delta store that

contains the maximum number of rows, and is

waiting for the tuple mover process to compress

it into the columnstore.

-

- A row group that is compressed

with columnstore compression and stored in the

columnstore.

-

- A row group that was formerly in

the deltastore and is no longer used.

Number of rows physically stored in the row

group. For compressed row groups. Includes the

rows that are marked deleted.

Number of rows physically stored in a

compressed row group that are marked for

deletion.

for row groups that are in the delta store.

For nonclustered columnstore indexes, this value

doesn't include deleted rows stored in the delete

buffer. For more information, and to find the

number of deleted rows in the delete buffer, see

sys.internal_partitions

.

Combined size, in bytes, of all the pages in this

row group. This size doesn't include the size

required to store metadata or shared dictionaries.

Reason that triggered the

row group

to have less than the maximum number of rows.

-

-

-

-

-

-

-

-

-

-

Description of

.

-

:

Occurred when upgrading from the previous

version of SQL Server.

-

: The row group wasn't trimmed. The

row group was compressed with the maximum of

1,048,576 rows. The number of rows could be less

if a subset of rows was deleted after delta

rowgroup was closed

-

: The bulk-load batch size limited

the number of rows.

-

: Forced compression as part of

command.

-

: Dictionary size grew too

large to compress all of the rows together.

-

: Not enough available

memory to compress all the rows together.

-

: Closed as part of last

row group with rows < 1 million during index

build operation.

: A partition build with multiple cores can

result in more than one trim of this type.

-

: Only for columnstore on in-

memory table. If stats incorrectly indicated >= 1

million qualified rows in the tail but we found

fewer, the compressed rowgroup will have < 1

million rows

-

: Only for columnstore on in-

memory table. If tail has > 1 million qualified

rows, the last batch remaining rows are

compressed if the count is between 100,000 and

1 million

-

: A Tuple Mover merge operation

running in the background consolidated one or

more rowgroups into this rowgroup.

Shows how this rowgroup got moved from the

deltastore to a compressed state in the

columnstore.

-

-

-

-

-

-

-

-

- the operation doesn't apply

to the deltastore. Or, the rowgroup was

compressed before upgrading to SQL Server 2016

(13.x) in which case the history isn't preserved.

-

- An index create or index

rebuild compressed the rowgroup.

-

- The tuple mover running in the

background compressed the rowgroup. Tuple

mover happens after the rowgroup changes state

from

to

.

-

- The reorganization operation,

, moved the

rowgroup from the deltastore to the columnstore.

This occurred before the tuple-mover had time to

move the rowgroup.

-

- This rowgroup was open in

the deltastore and was forced into the

columnstore before it had a full number of rows.

-

- A bulk-load operation

compressed the rowgroup directly without using

the deltastore.

-

- A merge operation consolidated one

or more rowgroups into this rowgroup and then

performed the columnstore compression.

VertiPaq optimization improves columnstore

compression by rearranging the order of the rows

in the rowgroup to achieve higher compression.

This optimization occurs automatically in most

cases. There are two cases where VertiPaq

optimization isn't used:

a. when a delta rowgroup moves into the

columnstore and there are one or more

nonclustered indexes on the columnstore index -

in this case VertiPaq optimization is skipped to

minimize changes to the mapping index;

b. for columnstore indexes on memory-optimized

tables.

= No

= Yes

Row group generation associated with this row

group.

Clock time for when this rowgroup was created.

- for a columnstore index on an in-memory

table.

Clock time for when this rowgroup was closed.

- for a columnstore index on an in-memory

table.

## Returns one row for each rowgroup in the current database.

```sql
VIEW SERVER STATE
```

```sql
##MS_ServerStateReader##
```

```sql
VIEW DATABASE STATE
```

```sql
##MS_ServerStateReader##
```

```sql
sys.dm_db_column_store_row_group_operational_stats
```

```sql
object_id
```

```sql
index_id
```

```sql
partition_number
```

```sql
row_group_id
```

```sql
index_scan_count
```

```sql
scan_count
```

```sql
delete_buffer_scan_count
```

```sql
row_group_lock_count
```

```sql
row_group_lock_wait_count
```

```sql
row_group_lock_wait_in_ms
```

```sql
returned_row_count
```

```sql
returned_aggregate_count
```

```sql
returned_group_count
```

```sql
input_groupby_row_count
```

```sql
row_group_elimination_count
```

```sql
rowgroup_lock_count
```

```sql
rowgroup_lock_wait_count
```

```sql
rowgroup_lock_wait_in_ms
```

```sql
CONTROL
```

```sql
object_id
```

```sql
VIEW DATABASE STATE
```

```sql
@object_id = NULL
```

```sql
VIEW DATABASE STATE
```

```sql
@object_id = NULL
```

```sql
VIEW DATABASE PERFORMANCE STATE
```

```sql
VIEW DATABASE [PERFORMANCE] STATE
```

```sql
CONTROL
```

```sql
VIEW DATABASE [PERFORMANCE] STATE
```

```sql
CONTROL
```

```sql
@database_id = NULL
```

```sql
object_id
```

```sql
index_id
```

```sql
object_id
```

```sql
partition_number
```

```sql
row_group_id
```

```sql
sys.partitions
row_group_id
```

```sql
-1
```

```sql
delta_store_hobt_id
```

```sql
NULL
```

```sql
NULL
```

```sql
state
```

```sql
state_description
```

```sql
0
```

```sql
INVISIBLE
1
```

```sql
OPEN
2
```

```sql
CLOSED
3
```

```sql
COMPRESSED
4
```

```sql
TOMBSTONE
COMPRESSED
```

```sql
state_desc
```

```sql
0
```

```sql
INVISIBLE
```

```sql
INVISIBLE
```

```sql
INVISIBLE
```

```sql
COMPRESSED
```

```sql
CLOSED
```

```sql
TOMBSTONE
```

```sql
1
```

```sql
OPEN
```

```sql
2
```

```sql
CLOSED
```

```sql
3
```

```sql
COMPRESSED
```

```sql
4
```

```sql
TOMBSTONE
```

```sql
total_rows
```

```sql
deleted_rows
```

```sql
0
```

```sql
size_in_bytes
```

```sql
trim_reason
```

```sql
COMPRESSED
```

```sql
0
```

```sql
UNKNOWN_UPGRADED_FROM_PREVIOUS_VERSION
1
```

```sql
NO_TRIM
2
```

```sql
BULKLOAD
3
```

```sql
REORG
4
```

```sql
DICTIONARY_SIZE
5
```

```sql
MEMORY_LIMITATION
6
```

```sql
RESIDUAL_ROW_GROUP
7
```

```sql
STATS_MISMATCH
8
```

```sql
SPILLOVER
9
```

```sql
AUTO_MERGE
trim_reason_desc
```

```sql
trim_reason
```

```sql
0
```

```sql
UNKNOWN_UPGRADED_FROM_PREVIOUS_VERSION
```

```sql
1
```

```sql
NO_TRIM
```

```sql
2
```

```sql
BULKLOAD
```

```sql
3
```

```sql
REORG
```

```sql
REORG
```

```sql
4
```

```sql
DICTIONARY_SIZE
```

```sql
5
```

```sql
MEMORY_LIMITATION
```

```sql
6
```

```sql
RESIDUAL_ROW_GROUP
```

```sql
7
```

```sql
STATS_MISMATCH
```

```sql
8
```

```sql
SPILLOVER
```

```sql
9
```

```sql
AUTO_MERGE
```

```sql
transition_to_compressed_state
```

```sql
1
```

```sql
NOT_APPLICABLE
2
```

```sql
INDEX_BUILD
3
```

```sql
TUPLE_MOVER
4
```

```sql
REORG_NORMAL
5
```

```sql
REORG_FORCED
6
```

```sql
BULKLOAD
7
```

```sql
MERGE
transition_to_compressed_state_desc
```

```sql
1
```

```sql
NOT_APPLICABLE
```

```sql
2
```

```sql
INDEX_BUILD
```

```sql
3
```

```sql
TUPLE_MOVER
```

```sql
OPEN
```

```sql
CLOSED
```

```sql
4
```

```sql
REORG_NORMAL
```

```sql
ALTER INDEX ... REORG
```

```sql
CLOSED
```

```sql
5
```

```sql
REORG_FORCED
```

```sql
6
```

```sql
BULKLOAD
```

```sql
7
```

```sql
MERGE
```

```sql
has_vertipaq_optimization
```

```sql
0
```

```sql
1
```

```sql
generation
```

```sql
created_time
```

```sql
NULL
```

```sql
closed_time
```

```sql
NULL
```
