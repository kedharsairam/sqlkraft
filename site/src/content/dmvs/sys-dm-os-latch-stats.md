---
name: 'sys.dm_os_latch_stats'
title: 'sys.dm_os_latch_stats'
category: 'execution'
description: 'permission on the database, or membership in the'
pubDate: 2026-05-29
---

either the

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

sys.dm_os_latch_stats can be used to identify the source of latch contention by examining the

relative wait numbers and wait times for the different latch classes. In some situations, you may

be able to resolve or reduce latch contention. However, there might be situations that will

require that you to contact Microsoft Customer Support Services.

You can reset the contents of sys.dm_os_latch_stats by using

as follows:

SQL

This resets all counters to 0.

A latch is an internal lightweight synchronization object similar to a lock, that is used by various

SQL Server components. A latch is primarily used to synchronize database pages during

operations such as buffer or file access. Each latch is associated with a single allocation unit.

A latch wait occurs when a latch request cannot be granted immediately, because the latch is

held by another thread in a conflicting mode. Unlike locks, a latch is released immediately after

the operation, even in write operations.

Latches are grouped into classes based on components and usage. Zero or more latches of a

particular class can exist at any point in time in an instance of SQL Server.

７

These statistics are not persisted if SQL Server is restarted. All data is cumulative since the

last time the statistics were reset, or since SQL Server was started.

The following table contains brief descriptions of the various latch classes.

ALLOC_CREATE_RINGBUF

Used internally by SQL Server to initialize the

synchronization of the creation of an

allocation ring buffer.

ALLOC_CREATE_FREESPACE_CACHE

Used to initialize the synchronization of

internal free space caches for heaps.

ALLOC_CACHE_MANAGER

Used to synchronize internal coherency tests.

ALLOC_FREESPACE_CACHE

Used to synchronize the access to a cache of

pages with available space for heaps and

binary large objects (BLOBs). Contention on

latches of this class can occur when multiple

connections try to insert rows into a heap or

BLOB at the same time. You can reduce this

contention by partitioning the object. Each

partition has its own latch. Partitioning will

distribute the inserts across multiple latches.

ALLOC_EXTENT_CACHE

Used to synchronize the access to a cache of

extents that contains pages that are not

allocated. Contention on latches of this class

can occur when multiple connections try to

allocate data pages in the same allocation unit

at the same time. This contention can be

reduced by partitioning the object of which

this allocation unit is a part.

ACCESS_METHODS_DATASET_PARENT

Used to synchronize child dataset access to

the parent dataset during parallel operations.

ACCESS_METHODS_HOBT_FACTORY

Used to synchronize access to an internal hash

table.

ACCESS_METHODS_HOBT

Used to synchronize access to the in-memory

representation of a HoBt.

７

does not track latch requests that were granted immediately, or

that failed without waiting.

ﾉ

ACCESS_METHODS_HOBT_COUNT

Used to synchronize access to a HoBt page

and row counters.

ACCESS_METHODS_HOBT_VIRTUAL_ROOT

Used to synchronize access to the root page

abstraction of an internal B-tree.

ACCESS_METHODS_CACHE_ONLY_HOBT_ALLOC

Used to synchronize worktable access.

ACCESS_METHODS_BULK_ALLOC

Used to synchronize access within bulk

allocators.

ACCESS_METHODS_SCAN_RANGE_GENERATOR

Used to synchronize access to a range

generator during parallel scans.

ACCESS_METHODS_KEY_RANGE_GENERATOR

Used to synchronize access to read-ahead

operations during key range parallel scans.

APPEND_ONLY_STORAGE_INSERT_POINT

Used to synchronize inserts in fast append-

only storage units.

APPEND_ONLY_STORAGE_FIRST_ALLOC

Used to synchronize the first allocation for an

append-only storage unit.

APPEND_ONLY_STORAGE_UNIT_MANAGER

Used for internal data structure access

synchronization within the fast append-only

storage unit manager.

APPEND_ONLY_STORAGE_MANAGER

Used to synchronize shrink operations in the

fast append-only storage unit manager.

BACKUP_RESULT_SET

Used to synchronize parallel backup result

sets.

BACKUP_TAPE_POOL

Used to synchronize backup tape pools.

BACKUP_LOG_REDO

Used to synchronize backup log redo

operations.

BACKUP_INSTANCE_ID

Used to synchronize the generation of

instance IDs for backup performance monitor

counters.

BACKUP_MANAGER

Used to synchronize the internal backup

manager.

BACKUP_MANAGER_DIFFERENTIAL

Used to synchronize differential backup

operations with DBCC.

BACKUP_OPERATION

Used for internal data structure

synchronization within a backup operation,

such as database, log, or file backup.

BACKUP_FILE_HANDLE

Used to synchronize file open operations

during a restore operation.

BUFFER

Used to synchronize short term access to

database pages. A buffer latch is required

before reading or modifying any database

page. Buffer latch contention can indicate

several issues, including hot pages and slow

I/Os.

This latch class covers all possible uses of page

latches. sys.dm_os_wait_stats makes a

difference between page latch waits that are

caused by I/O operations and read and write

operations on the page.

BUFFER_POOL_GROW

Used for internal buffer manager

synchronization during buffer pool grow

operations.

DATABASE_CHECKPOINT

Used to serialize checkpoints within a

database.

CLR_PROCEDURE_HASHTABLE

Internal use only.

CLR_UDX_STORE

Internal use only.

CLR_DATAT_ACCESS

Internal use only.

CLR_XVAR_PROXY_LIST

Internal use only.

DBCC_CHECK_AGGREGATE

Internal use only.

DBCC_CHECK_RESULTSET

Internal use only.

DBCC_CHECK_TABLE

Internal use only.

DBCC_CHECK_TABLE_INIT

Internal use only.

DBCC_CHECK_TRACE_LIST

Internal use only.

DBCC_FILE_CHECK_OBJECT

Internal use only.

DBCC_PERF

Used to synchronize internal performance

monitor counters.

DBCC_PFS_STATUS

Internal use only.

DBCC_OBJECT_METADATA

Internal use only.

DBCC_HASH_DLL

Internal use only.

EVENTING_CACHE

Internal use only.

FCB

Used to synchronize access to the file control

block.

FCB_REPLICA

Internal use only.

FGCB_ALLOC

Use to synchronize access to round robin

allocation information within a filegroup.

FGCB_ADD_REMOVE

Use to synchronize access to filegroups for

add, drop, grow, and shrink file operations.

FILEGROUP_MANAGER

Internal use only.

FILE_MANAGER

Internal use only.

FILESTREAM_FCB

Internal use only.

FILESTREAM_FILE_MANAGER

Internal use only.

FILESTREAM_GHOST_FILES

Internal use only.

FILESTREAM_DFS_ROOT

Internal use only.

LOG_MANAGER

Internal use only.

FULLTEXT_DOCUMENT_ID

Internal use only.

FULLTEXT_DOCUMENT_ID_TRANSACTION

Internal use only.

FULLTEXT_DOCUMENT_ID_NOTIFY

Internal use only.

FULLTEXT_LOGS

Internal use only.

FULLTEXT_CRAWL_LOG

Internal use only.

FULLTEXT_ADMIN

Internal use only.

FULLTEXT_AMDIN_COMMAND_CACHE

Internal use only.

FULLTEXT_LANGUAGE_TABLE

Internal use only.

FULLTEXT_CRAWL_DM_LIST

Internal use only.

FULLTEXT_CRAWL_CATALOG

Internal use only.

FULLTEXT_FILE_MANAGER

Internal use only.

DATABASE_MIRRORING_REDO

Internal use only.

DATABASE_MIRRORING_SERVER

Internal use only.

DATABASE_MIRRORING_CONNECTION

Internal use only.

DATABASE_MIRRORING_STREAM

Internal use only.

QUERY_OPTIMIZER_VD_MANAGER

Internal use only.

QUERY_OPTIMIZER_ID_MANAGER

Internal use only.

QUERY_OPTIMIZER_VIEW_REP

Internal use only.

RECOVERY_BAD_PAGE_TABLE

Internal use only.

RECOVERY_MANAGER

Internal use only.

SECURITY_OPERATION_RULE_TABLE

Internal use only.

SECURITY_OBJPERM_CACHE

Internal use only.

SECURITY_CRYPTO

Internal use only.

SECURITY_KEY_RING

Internal use only.

SECURITY_KEY_LIST

Internal use only.

SERVICE_BROKER_CONNECTION_RECEIVE

Internal use only.

SERVICE_BROKER_TRANSMISSION

Internal use only.

SERVICE_BROKER_TRANSMISSION_UPDATE

Internal use only.

SERVICE_BROKER_TRANSMISSION_STATE

Internal use only.

SERVICE_BROKER_TRANSMISSION_ERRORS

Internal use only.

SSBXmitWork

Internal use only.

SERVICE_BROKER_MESSAGE_TRANSMISSION

Internal use only.

SERVICE_BROKER_MAP_MANAGER

Internal use only.

SERVICE_BROKER_HOST_NAME

Internal use only.

SERVICE_BROKER_READ_CACHE

Internal use only.

SERVICE_BROKER_WAITFOR_MANAGER

Used to synchronize an instance level map of

wait queues. One queue exists per database

ID, Database Version, and Queue ID tuple.

Contention on latches of this class can occur

when many connections are: In a

WAITFOR(RECEIVE) wait state; calling

WAITFOR(RECEIVE); exceeding the WAITFOR

timeout; receiving a message; committing or

rolling back the transaction that contains the

WAITFOR(RECEIVE); You can reduce the

contention by reducing the number of threads

in a WAITFOR(RECEIVE) wait state.

SERVICE_BROKER_WAITFOR_TRANSACTION_DATA

Internal use only.

SERVICE_BROKER_TRANSMISSION_TRANSACTION_DATA

Internal use only.

SERVICE_BROKER_TRANSPORT

Internal use only.

SERVICE_BROKER_MIRROR_ROUTE

Internal use only.

TRACE_ID

Internal use only.

TRACE_AUDIT_ID

Internal use only.

TRACE

Internal use only.

TRACE_CONTROLLER

Internal use only.

TRACE_EVENT_QUEUE

Internal use only.

TRANSACTION_DISTRIBUTED_MARK

Internal use only.

TRANSACTION_OUTCOME

Internal use only.

NESTING_TRANSACTION_READONLY

Internal use only.

NESTING_TRANSACTION_FULL

Internal use only.

MSQL_TRANSACTION_MANAGER

Internal use only.

DATABASE_AUTONAME_MANAGER

Internal use only.

UTILITY_DYNAMIC_VECTOR

Internal use only.

UTILITY_SPARSE_BITMAP

Internal use only.

UTILITY_DATABASE_DROP

Internal use only.

UTILITY_DYNAMIC_MANAGER_VIEW

Internal use only.

UTILITY_DEBUG_FILESTREAM

Internal use only.

UTILITY_LOCK_INFORMATION

Internal use only.

## Server and Azure SQL index architecture and design guide

VERSIONING_TRANSACTION

Internal use only.

VERSIONING_TRANSACTION_LIST

Internal use only.

VERSIONING_TRANSACTION_CHAIN

Internal use only.

VERSIONING_STATE

Internal use only.

VERSIONING_STATE_CHANGE

Internal use only.

KTM_VIRTUAL_CLOCK

Internal use only.

DBCC SQLPERF (Transact-SQL)

SQL Server Operating System Related Dynamic Management Views (Transact-SQL)

SQL Server, Latches Object

Last updated on 11/18/2025

７

Documentation uses the term B-tree generally in reference to indexes. In rowstore

indexes, the Database Engine implements a B+ tree. This does not apply to columnstore

indexes or indexes on memory-optimized tables. For more information, see the

.

## sys.dm_pdw_nodes_os_loaded_modules

Article

•

02/28/2023

SQL Server

Analytics Platform System (PDW)


## Returns a row for each module loaded into the server address space.
Address of the module in the process.

Version of the file. Appears in the following format:

x.x:x.x

Version of the product. Appears in the following format:

x.x:x.x

1 = Module is a debug version of the loaded module.

1 = Module has been patched.

1 = Module is a pre-release version of the loaded module.

1 = Module is a private build of the loaded module.

1 = Module is a special build of the loaded module.

Language of version information of the module.

Name of company that created the module.


## Description of the module.
Name of module. Includes the full path of the module.

: Analytics Platform System (PDW)

The identifier for the node that this distribution is on.

７

To call this from Analytics Platform System (PDW), use the name

.

ﾉ

```sql
VIEW DATABASE STATE
```

```sql
##MS_ServerStateReader##
```

```sql
DBCC SQLPERF
```

```sql
DBCC SQLPERF ('sys.dm_os_latch_stats', CLEAR);
GO
```

```sql
sys.dm_os_latch_stats
```
