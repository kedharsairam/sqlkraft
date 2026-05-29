---
name: "Trace flags"
title: "Trace flags"
category: "statements"
description: "The following table lists and describes the trace flags that are available in SQL Server."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The following table lists and describes the trace flags that are available in SQL Server.

Azure SQL Managed Instance supports the following global Trace flags: 460, 2301, 2389, 2390,

2453, 2467, 7471, 8207, 9389, 10316, and 11024. Session trace-flags aren't yet supported in SQL

Managed Instance.

Some trace flags were introduced in specific SQL Server versions. For more information on the

applicable version, see the Microsoft Support article associated with a specific trace flag.

Trace flag behavior might not be supported in future releases of SQL Server.

Тrace flags can be referenced directly in the table via a bookmark that you can add to the end of

the URL, using this format #tfNNNN. For example, to jump directly to trace flag 1118 in the table,

use

.

## Description

Increases the verboseness of the merge replication agent logging.

Important

: Trace flag 101 can only be enabled for the

Replication Merge Agent

using the

option

when executing

from the command prompt.

Warning

: Trace flag 101 isn't meant to be enabled continuously in a production environment, but

only for time-limited troubleshooting purposes. For more information, see

Find errors with the

Merge Agent

.

: Replication Merge Agent only.

Increases the verboseness of the merge replication agent logging and directs it to the

table.

Important

: Trace flag 102 can only be enabled for the

Replication Merge Agent

using the

option

when executing

from the command prompt.

Warning

: Trace flag 102 isn't meant to be enabled continuously in a production environment, but

ﾉ

Expand table

#### Trace

#### flag

#### Scope

#### 139

#### Applies to

#### Scope

#### 174

#### Scope

#### 176

#### Scope

#### 205

#### Scope

#### 260

#### Scope

#### 272

## Description

only for time-limited troubleshooting purposes. For more information, see

Find errors with the

Merge Agent

.

: Replication Merge Agent only.

Forces correct conversion semantics in the scope of

check commands like

DBCC CHECKDB

,

DBCC CHECKTABLE

and

DBCC CHECKCONSTRAINTS

, when analyzing the improved precision and

conversion logic introduced with compatibility level 130 for specific data types, on a database that

has a lower compatibility level. For more information, see

SQL Server and Azure SQL Database

improvements in handling some data types and uncommon operations

.

: SQL Server 2016 (13.x) RTM CU 3, SQL Server 2016 (13.x) Service Pack 1, and later

versions.

Warning

: Trace flag 139 isn't meant to be enabled continuously in a production environment, and

should be used for the sole purpose of performing database validation checks described in

SQL

Server and Azure SQL Database improvements in handling some data types and uncommon

operations

. It should be immediately disabled after validation checks are completed.

: Global only.

Increases the SQL Server Database Engine plan cache bucket count from 40,009 to 160,001 on 64-

bit systems. For more information, see

KB3026083

.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global only.

Addresses errors when rebuilding partitions online for tables that contain a computed partitioning

column. For more information, see

KB3213683

and

KB4541096

.

: Global or session.

Reports to the error log when a statistics-dependent stored procedure is being recompiled as a

result of autoupdate statistics. For more information, see an archived version of

KB195565

.

Note

: This trace flag requires enabling

trace flag 3605

.

: Global only.

Prints versioning information about extended stored procedure dynamic-link libraries (DLLs). For

more information about

, see

Programming Database Engine extended stored

procedures

.

: Global or session.

Disables identity preallocation to avoid gaps in the values of an identity column in cases where the

server restarts unexpectedly or fails over to a secondary server. Identity caching is used to improve

#### Trace

#### flag

#### Scope

#### 460

#### Applies to

#### Scope

#### 610

#### Scope

#### 634

#### Scope

## Description

performance on tables with identity columns.

Note

: Starting with SQL Server 2017 (14.x), to accomplish this at the database level, see the

option in

ALTER DATABASE SCOPED CONFIGURATION

.

: Global only.

Replaces data truncation message ID

8152

with message ID

2628

. For more information, see

KB4468101

.

Starting with SQL Server 2019 (15.x), to accomplish this at the database level, see the

option in

ALTER DATABASE SCOPED CONFIGURATION

.

: SQL Server 2016 (13.x) Service Pack 2 CU 6, SQL Server 2017 (14.x) CU 12, and later

versions.

Note

: Starting with database compatibility level 150, message ID 2628 is the default and this trace

flag has no effect. For database compatibility level 140 or lower, message ID 2628 remains an opt-

in error message that requires trace flag 460 to be enabled, and this database scoped configuration

has no effect.

: Global or session.

Controls minimally logged inserts into indexed tables. This trace flag isn't required starting with

SQL Server 2016 (13.x), as minimal logging is turned on by default for indexed tables. In SQL Server

2016 (13.x), when the bulk load operation causes a new page to be allocated, all of the rows

sequentially filling that new page are minimally logged if all the other prerequisites for minimal

logging are met. Rows inserted into existing pages (no new page allocation) to maintain index

order are still fully logged, as are rows that are moved as a result of page splits during the load.

It's also important to have

turned ON for indexes (which is ON by default) for

minimal logging operation to work as page locks are acquired during allocation and thereby only

page or extent allocations are logged. For more information, see

Data Loading Performance Guide

.

: Global or session.

Disables the background columnstore compression task. SQL Server periodically runs the Tuple

Mover background task that compresses columnstore index rowgroups with uncompressed data,

one such rowgroup at a time.

Columnstore compression improves query performance but also consumes system resources. You

can control the timing of columnstore compression manually, by disabling the background

compression task with trace flag 634, and then explicitly invoking

or

at the time of your choice.

: Global only.

#### Trace

#### flag

#### 652

#### Scope

#### 661

#### Scope

#### 692

#### Applies to

#### Scope

#### 715

#### Scope

#### 809

## Description

Disables page prefetching scans. If you turn on trace flag 652, SQL Server no longer brings

database pages into the buffer pool before these database pages are consumed by the scans. As a

result, queries that benefit from the page prefetching feature exhibit lower performance.

: Global or session.

Disables the ghost record removal process. Trace flag 661 disables the ghost record removal

process. A ghost record is the result of a delete operation. When you delete a record, the deleted

record is kept as a ghost record. Later, the deleted record is purged by the ghost record removal

process. When you disable this process, the deleted record isn't purged. Therefore, the space that

the deleted record consumes isn't freed. This behavior affects space consumption and the

performance of scan operations. For more information, review the

Ghost cleanup process guide

.

: Global only.

Disables fast inserts while bulk loading data into heap or clustered index. Starting with SQL Server

2016 (13.x), fast inserts are enabled by default, using minimal logging when database is in simple or

bulk logged recovery model to optimize insert performance for records inserted into new pages.

With fast inserts, each bulk load batch acquires new extents bypassing the allocation lookup for

existing extent with available free space to optimize insert performance.

With fast inserts, bulk loads with small batch sizes can lead to increased unused space consumed

by objects hence it's recommended to use large batchsize for each batch to fill the extent

completely. If increasing batchsize isn't feasible, this trace flag can help reduce unused space

reserved at the expense of performance.

: SQL Server 2016 (13.x) and later versions.

: Global or session.

Enables table lock for bulk load operations into a heap with no nonclustered indexes. When this

trace flag is enabled, bulk load operations acquire bulk update (BU) locks when bulk copying data

into a table. Bulk update (BU) locks allow multiple threads to bulk load data concurrently into the

same table, while preventing other processes that aren't bulk loading data from accessing the table.

The behavior is similar to when the user explicitly specifies

hint while performing bulk load,

or when the

table lock on bulk load is enabled for a given table. However, when

this trace flag is enabled, this behavior becomes default without any query or database changes.

: Global or session.

Enables what is referred to as

Direct Write

behavior for the

hybrid buffer pool

. This mode requires

that

persisted log buffer

is enabled in the same database as hybrid buffer pool.

Direct Write

allows

the hybrid buffer pool to serve as a cache for both dirty and clean pages, reducing the workload

demands on the DRAM buffer pools for OLAP and OLTP style workloads. This trace flag was

introduced in SQL Server 2022 (16.x) and the behavior is enabled by default in SQL Server 2022

(16.x) CU 1. If you're using SQL Server 2022 (16.x) CU 1 and later versions, the trace flag is ignored.

#### Trace

#### flag

#### 818

#### Scope

#### 830

#### Scope

#### 834

## Description

Enables extra I/O diagnostics to check for Lost Write or Stale Read conditions during file I/O

operations. Trace flag 818 enables an in-memory ring buffer that is used for tracking the last 2,048

successful write operations that are performed by SQL Server, not including sort and workfile I/Os.

When errors such as Error 605, 823, or 3448 occur, the incoming buffer's log sequence number

(LSN) value is compared to the recent write list. If the LSN that is retrieved is older than the one

specified during the write operation, a new error message is logged in the SQL Server error log. For

more information, see

SQL Server diagnostics detects unreported I/O problems due to stale reads

or lost writes

.

Note

: Starting with SQL Server 2017 (14.x), this trace flag has no effect.

: Global only.

Disables detection and reporting of I/O requests that take a very long time to complete. By default

SQL Server uses a mechanism to detect read and write I/O requests that take a long time (typically

longer than 15 seconds). This trace flag disables this detection. For more information, see

MSSQLSERVER_833

.

Note

: It isn't recommended that you enable this trace flag because you could decrease your ability

to detect I/O issues on the system.

: Global only.

Uses large-page allocations for all memory allocations within the SQL Server Operating System

(SQLOS) workspace. The large page size varies depending on the hardware platform and can be

from 2 MB to 16 MB. Large pages are allocated at startup and are kept throughout the lifetime of

the process.

In a certain narrow set of scenarios, trace flag 834 might improve performance by increasing the

efficiency of the translation look-aside buffer (TLB) in the CPU. In other words, trace flag 834

increases the efficiency of managing physical to virtual memory address translation that is

performed by the memory management hardware.

Before you enable trace flag 834, follow the recommendations for maximum server memory

configuration in

Server memory configuration options

.

Note

: Trace flag 834 applies only to 64-bit versions of SQL Server. You must have the Lock pages in

memory user right to turn on trace flag 834. You can turn on trace flag 834 only at startup. Trace

flag 834 can prevent the server from starting if memory is fragmented and if large pages can't be

allocated. Therefore, trace flag 834 is best suited for servers that are dedicated to SQL Server.

Note

: When enabled, the large-page memory model preallocates all SQLOS memory at instance

startup and doesn't return that memory to the OS.

Warning

: We don't recommend turning on trace flag 834 unless you thoroughly test it and

determine that it materially benefits your workload. Enabling this trace flag can substantially

increase the kernel CPU time and reduce performance. This occurs if memory becomes fragmented,

#### Trace

#### flag

#### Scope

#### 836

#### Scope

#### 845

#### Scope

#### 876

#### Applies to

#### Scope

#### 888

#### Applies to

#### Scope

## Description

requiring SQL Server to call Windows APIs to allocate and deallocate memory instead of reusing

memory cached in the SQLOS workspace. Trace flag 834 can also cause unnecessary memory

consumption because the unused part of committed memory blocks isn't released to the operating

system.

Note

: If you're using columnstore indexes, don't enable trace flag 834. For more information, see

Interoperability issues between batch mode processing and large page memory model

. Instead, if

using SQL Server 2019 (15.x) and later versions, use

trace flag 876

instead.

: Global only.

Use the max server memory option for the buffer pool. Trace flag 836 causes SQL Server to size the

buffer pool at startup based on the value of the max server memory option instead of based on the

total physical memory. You can use

trace flag 836

to reduce the number of buffer descriptors that

are allocated at startup in 32-bit Address Windowing Extensions (AWE) mode.

Note

: Trace flag 836 applies only to 32-bit versions of SQL Server that have the AWE allocation

enabled. You can turn on trace flag 836 only at startup.

: Global only.

Enables locked pages on Standard SKUs of SQL Server, when the service account for SQL Server has

the Lock Pages in Memory privilege enabled. For more information, see

KB970070

and

Server

Memory Server Configuration Options

.

Note

: Starting with SQL Server 2012 (11.x), this behavior is enabled by default for Standard SKUs,

and trace flag 845 must not be used.

: Global only.

Uses large-page allocations for columnstore.

Note

: Unlike trace flag 834, using trace flag 876 doesn't preallocate SQLOS memory at instance

startup, and unused memory can be released.

: SQL Server 2019 (15.x) and later versions.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global only.

Resolves performance degradation on PMEM devices with Hybrid Buffer Pool enabled in SQL Server

when PMEM devices run low on memory. For more information, see

KB4548103

.

: SQL Server 2019 (15.x) CU 4 and later versions.

: Global only.

#### Trace

#### flag

#### 890

#### Applies to

#### Scope

#### 898

#### Applies to

#### Scope

#### 902

#### Scope

#### 1117

#### Scope

#### 1118

## Description

Suppress long buffer pool scan complete messages (

error 898

) in the error log. For more

information on buffer pool scan and the message that is logged in the error log, see

Operations

that trigger a buffer pool scan may run slowly on large-memory computers

.

: SQL Server 2017 (14.x) and later versions.

: Global only.

Disables the

Direct Write

behavior of the

hybrid buffer pool

for troubleshooting or debugging

purposes. For more information, see

KB5022375

.

: SQL Server 2022 (16.x) CU 1 and later versions.

: Global only.

Bypasses execution of database upgrade script when installing a Cumulative Update or Service

Pack. If you encounter an error during script upgrade mode, it's recommended to contact Microsoft

SQL Customer Service and Support (CSS) for further guidance. For more information, see

KB2163980

.

Warning

: This trace flag is meant for troubleshooting of failed updates during script upgrade mode,

and it isn't supported to run it continuously in a production environment. Database upgrade scripts

need to execute successfully for a complete install of Cumulative Updates and Service Packs. Not

doing so can cause unexpected issues with your SQL Server instance.

: Global only.

When a file in the filegroup meets the autogrow threshold, all files in the filegroup grow. This trace

flag affects all databases. It's recommended only if in every database it's safe to grow all files in a

filegroup by the same amount.

Note

: Starting with SQL Server 2016 (13.x), this behavior is controlled by the

and

option of

, and trace flag 1117 has no effect. For more

information, see

ALTER DATABASE File and Filegroup Options

.

: Global only.

Forces page allocations on uniform extents instead of mixed extents, reducing contention on the

SGAM page. When a new object is created, by default, the first eight pages are allocated from

different extents (mixed extents). Afterwards, when more pages are needed, those are allocated

from that same extent (uniform extent). The SGAM page is used to track these mixed extents, so

can quickly become a bottleneck when numerous mixed page allocations are occurring. This trace

flag allocates all eight pages from the same extent when creating new objects, minimizing the need

to scan the SGAM page. For more information, see

KB328551

.

Note

: Starting with SQL Server 2016 (13.x) this behavior is controlled by the SET

MIXED_PAGE_ALLOCATION option of

, and trace flag 1118 has no effect. For more

#### Trace

#### flag

#### Scope

#### 1204

#### Scope

#### 1211

#### Scope

#### 1222

#### Scope

#### 1224

#### locks

#### locks

## Description

information, see

ALTER DATABASE SET options

.

: Global only.

## Returns the resources and types of locks participating in a deadlock and also the current command

affected. For more information about deadlocks, see the

Deadlocks guide

.

Note

: Avoid using trace flag 1204 on workload-intensive systems causing deadlocks. For more

information about other means of detecting deadlocks, see the

Deadlocks guide

.

: Global only.

Disables lock escalation based on memory pressure, or based on number of locks. The SQL Server

Database Engine doesn't escalate row or page locks to table locks.

Using this trace flag can generate excessive number of locks and if the lock memory grows large

enough, attempts to allocate additional locks for any query might fail. This can slow the

performance of the Database Engine, or cause error message 1204 (unable to allocate lock

resource) because of insufficient memory.

If both trace flags 1211 and 1224 are set, 1211 takes precedence over 1224. However, because trace

flag 1211 prevents escalation in every case, even under memory pressure, use

trace flag 1224

instead. This helps avoid "out-of-locks" errors when many locks are being used.

For more information on how to resolve blocking problems that are caused by lock escalation in

SQL Server, see

Resolve blocking problems caused by lock escalation in SQL Server

.

: Global or session.

## Returns the resources and types of locks that are participating in a deadlock and also the current

command affected, in an XML format that doesn't comply with any XSD schema. For more

information about deadlocks, see the

Deadlocks guide

.

Note

: Avoid using trace flag 1222 on workload-intensive systems causing deadlocks. For more

information about other means of detecting deadlocks, see the

Deadlocks guide

.

: Global only.

Disables lock escalation based on the number of locks. However, memory pressure can still activate

lock escalation. The Database Engine escalates row or page locks to table (or partition) locks if the

amount of memory used by lock objects exceeds one of the following conditions:

- 40 percent of the memory that is used by Database Engine. This is applicable only when the

parameter of

is set to 0.

- 40 percent of the lock memory that is configured by using the

parameter of

.

For more information, see

Server configuration options

.

#### Trace

#### flag

#### Scope

#### 1229

#### Scope

#### 1236

#### Scope

#### 1237

#### Scope

#### 1260

#### Scope

#### 1448

## Description

If both trace flags 1211 and 1224 are set, 1211 takes precedence over 1224. However, because trace

flag 1211 prevents escalation in every case, even under memory pressure, use

trace flag 1224

instead. This helps avoid "out-of-locks" errors when many locks are being used.

Note

: Lock escalation to the table-level or HoBT-level granularity can also be controlled by using

the

option of the

ALTER TABLE

statement.

For more information on how to resolve blocking problems that are caused by lock escalation in

SQL Server, see

Resolve blocking problems caused by lock escalation in SQL Server

.

: Global or session.

Disables all lock partitioning regardless of the number of CPUs. By default, SQL Server enables lock

partitioning when a server has 16 or more CPUs, to improve the scalability characteristics of larger

systems. For more information on lock partitioning, see the

Transaction Locking and Row

Versioning Guide

.

Warning

: Trace flag 1229 can cause spinlock contention and poor performance.

: Global only.

Enables database lock partitioning. For more information, see

KB2926217

.

Note

: Starting with SQL Server 2012 (11.x) Service Pack 3 and SQL Server 2014 (12.x) Service Pack 1,

this behavior is controlled by the Database Engine and trace flag 1236 has no effect.

: Global only.

Allows the

statement to honor the current user-defined session

deadlock priority instead of being the likely deadlock victim by default. For more information, see

KB4025261

.

Note

: Starting with SQL Server 2017 (14.x) and database

compatibility level

140 this is the default

behavior, and trace flag 1237 has no effect.

: Global or session or query (QUERYTRACEON).

Disable scheduler monitor dumps.

: Global only.

Enables the replication log reader to move forward even if the asynchronous secondaries haven't

acknowledged the reception of a change. Even with this trace flag enabled the log reader always

waits for the synchronous secondaries whose synchronization state is

. The log reader

doesn't go beyond the minimum acknowledged Log Sequence Number of the

secondaries. This trace flag applies to the instance of SQL Server, not just an availability group, an

availability database, or a log reader instance. This trace flag must be enabled on the publisher

#### Trace

#### flag

#### Scope

#### 1462

#### Scope

#### 1800

#### Applies to

#### Scope

#### 1802

#### Scope

#### 1819

#### Scope

#### 2301

#### Scope

#### 2312

## Description

instance. It takes effect immediately without a restart. This trace flag can be activated ahead of time

or when an asynchronous secondary replica fails.

: Global only.

Disables log stream compression for asynchronous availability groups. This feature is enabled by

default on asynchronous availability groups in order to optimize network bandwidth. For more

information, see

Tune compression for availability group

.

: Global only.

Enables SQL Server optimization when disks of different sector sizes are used for primary and

secondary replica log files, in SQL Server Always On and Log Shipping environments. This trace flag

is only required to be enabled on SQL Server instances with transaction log file residing on disk

with sector size of 512 bytes. Trace flag 1800 isn't required to be enabled on disk with sector sizes

larger than 4 KB. For more information, see

KB3009974

,

Microsoft support policy for 4K sector

hard drives in Windows

, and

Troubleshoot errors related to system disk sector size greater than 4

KB

.

: SQL Server 2012 (11.x) Service Pack 1 CU 13, SQL Server 2012 (11.x) Service Pack 2 CU 3,

SQL Server 2014 (12.x) RTM CU 5, and later versions.

: Global only.

Disables ACL change and impersonated access verification during database attach or detach

operations. This can be useful when attaching a database and encountering access permission

errors, such as error 5120.

: Global only.

Allows

backup to URL

to use a proxy server when accessing Azure block blobs. In addition to this

trace flag, you must set the WinHTTP proxy configuration on the server with the

netsh.exe

utility on

Windows Vista, Windows Server 2008, and later versions.

: Global or session or query (QUERYTRACEON).

Enable advanced decision support optimizations that are specific to decision support queries. This

option applies to decision support processing of large data sets.

: Global or session or query (QUERYTRACEON).

Sets the Query Optimizer cardinality estimation model to SQL Server 2014 (12.x) and later versions,

irrespective of the compatibility level of the database.

Note

: If the database compatibility level is lower than 120, enabling trace flag 2312 uses the

cardinality estimation model of SQL Server 2014 (12.x) (120). For more information, see

Query hints

.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

#### Trace

#### flag

#### Scope

#### 2335

#### Scope

#### 2338

#### Scope

#### 2340

#### Scope

#### 2371

#### Scope

## Description

query hint

instead of using this trace flag.

: Global or session or query (QUERYTRACEON).

Causes SQL Server to assume a fixed amount of memory is available during query optimization, for

a scenario where the

max server memory server configuration

is set too high, and causes SQL

Server to generate an inefficient plan for a specific query. It doesn't limit the memory SQL Server

grants to execute the query. The memory configured for SQL Server is still used by data cache,

query execution, and other consumers.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Causes SQL Server to use a narrow plan when executing an

statement to update indexes in

a table. When you do an

against a clustered index column, SQL Server updates not only the

clustered index itself, but also all the nonclustered indexes because the nonclustered indexes

contain the cluster key. A common way that the update occurs is to update the clustered index, and

then all nonclustered indexes at the same time. SQL Server would update one row, then move to

next row until all is complete. This is called narrow plan update or also called Per-Row Update. In

some cases, the Database Engine can choose to do a wide plan update. This trace flag forces a

narrow plan update.

: Global or session or query (QUERYTRACEON).

Causes SQL Server not to use a sort operation (batch sort) for optimized Nested Loops joins when

generating a plan. By default, SQL Server can use an optimized Nested Loops join instead of a full

scan or a Nested Loops join with an explicit Sort, when the Query Optimizer concludes that a sort is

most likely not required, but still a possibility if the cardinality or cost estimates are incorrect. For

more information, see

High CPU or memory grants may occur with queries that use optimized

nested loop or batch sort

.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Changes the fixed update statistics threshold to a linear update statistics threshold. For more

information, see this

AUTO_UPDATE_STATISTICS Option

.

Note

: Starting with SQL Server 2016 (13.x) and under the

database compatibility level

130 or above,

this behavior is controlled by the Database Engine and trace flag 2371 has no effect.

: Global only.

#### Trace

#### flag

#### 2389

#### Scope

#### 2390

#### Scope

#### 2422

#### Applies to

#### Scope

#### 2430

#### Scope

#### 2446

#### Applies to

## Description

Enable automatically generated quick statistics for ascending keys (histogram amendment). If trace

flag 2389 is set, and a leading statistics column is marked as ascending, then the histogram used to

estimate cardinality is adjusted at query compile time.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 120 or above. Use

trace flag 4139

instead.

: Global or session or query (QUERYTRACEON).

Enable automatically generated quick statistics for ascending or unknown keys (histogram

amendment). If trace flag 2390 is set, and a leading statistics column is marked as ascending or

unknown, then the histogram used to estimate cardinality is adjusted at query compile time. For

more information, see

Query hints

.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 120 or above. Use

trace flag 4139

instead.

: Global or session or query (QUERYTRACEON).

Enables the SQL Server Database Engine to abort a request when the maximum time set by

Resource Governor

configuration is exceeded. For more information, see

KB4038419

.

: SQL Server 2016 (13.x) Service Pack 2, SQL Server 2017 (14.x) CU 3, and later versions.

: Global only.

Enables alternate lock class cleanup. For more information, see

KB2754301

.

: Global only.

Causes SQL Server to generate a Showplan XML fragment with the

when

using the lightweight query execution statistics profiling infrastructure or executing the

DMV while troubleshooting long running queries.

: SQL Server 2017 (14.x) CU 31, SQL Server 2019 (15.x) CU 19, and SQL Server 2022 (16.x)

and later versions.

Warning

: Trace flag 2446 isn't meant to be enabled continuously in a production environment, but

only for time-limited troubleshooting purposes. Using this trace flag introduces additional and

possibly significant CPU and memory overhead as we create a Showplan XML fragment with

runtime parameter information, whether the

DMV is called or

not.

Note

: Starting with SQL Server 2022 (16.x), to accomplish this at the database level see the

#### Trace

#### flag

#### Scope

#### 2451

#### Applies to

#### Scope

#### 2453

#### Scope

#### 2467

#### Scope

#### 2469

#### Scope

#### 2528

## Description

option in

ALTER DATABASE SCOPED

CONFIGURATION

.

: Global only.

Enables the equivalent of the last actual execution plan in

.

: SQL Server 2019 (15.x) and later versions.

Note

: Starting with SQL Server 2019 (15.x) to accomplish this at the database level, see the

LAST_QUERY_PLAN_STATS option in

ALTER DATABASE SCOPED CONFIGURATION

.

: Global only.

Allows a table variable to trigger recompile when enough number of rows are changed. For more

information, see

KB2952444

.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Starting with SQL Server 2019 (15.x), this became

table variable deferred compilation

, and trace flag

2453 has no effect.

: Global or session or query (QUERYTRACEON).

Enables an alternate parallel worker thread allocation policy, based on which node has the least

allocated threads. For more information, see

Parallel Query Processing

. Refer to

Server

configuration: max worker threads

for information on configuring the max worker threads server

option.

Note

: Query degree of parallelism (DOP) has to fit into a single node for this alternate policy to be

used, or the default thread allocation policy is used instead. Using this trace flag, it isn't

recommended to execute queries specifying a DOP over the number of schedulers in a single node,

as this could interfere with queries specifying a DOP below or equal to the number of schedulers in

a single node.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global only.

Enables alternate exchange for

into a partitioned columnstore index. For

more information, see

KB3204769

.

: Global or session or query (QUERYTRACEON).

Disables parallel checking of objects by

,

, and

.

By default, the degree of parallelism is automatically determined by the query processor. The

maximum degree of parallelism is configured just like that of parallel queries. For more information,

see

Server configuration: max degree of parallelism

.

#### Trace

#### flag

#### Scope

#### 2544

#### Scope

#### 2549

## Description

Note

: Parallel DBCC checks should typically be enabled (default). The query processor reevaluates

and automatically adjusts parallelism for each table or batch of tables checked by

.

The typical use scenario is when a system administrator knows that server load might increase

before

completes, and so chooses to manually decrease or disable parallelism, in

order to increase concurrency with other user workload. However, disabling parallel checks in

can cause it to take longer to complete.

Note

: If

is executed using the

option and parallelism is disabled, tables

might be locked for longer periods of time.

Note

: Starting with SQL Server 2014 (12.x) Service Pack 2, a MAXDOP option is available to override

the max degree of parallelism configuration option of

for the DBCC statements.

: Global or session.

Causes a memory dump of SQL Server to become a full dump (default is mini dump). Full dumps

are a complete copy of the active target process memory. That would include all thread state, all

process allocated memory, and all loaded modules. Full dumps therefore have a size roughly the

amount of memory used by SQL Server process, which in turn can be almost as large as total

system RAM. On large servers dedicated to a single SQL Server instance, it could mean a file that's

several hundreds of gigabytes or more.

Warning

: Generating a full memory dump can suspend the SQL Server process for an extended

period of time (several seconds to several minutes) and can generate a very large dump file. Use

this with caution and only rarely if the situation requires it.

For more detailed information, see

Use the Sqldumper.exe tool to generate a dump file in SQL

Server

.

: Global only.

Forces the

command to assume each database file is on a unique disk drive but

treating different physical files as one logical file.

command builds an internal list of

pages to read per unique disk drive across all database files. This logic determines unique disk

drives based on the drive letter of the physical file name of each file.

Note

: Don't use this trace flag unless you know that each file is based on a unique physical disk.

Note

: Although this trace flag improves the performance of the

commands that

target usage of the

option, some users might not see any improvement in

performance. While this trace flag improves disk I/O resources usage, the underlying performance

of disk resources could limit the overall performance of the

command. For more

information, see

KB2634571

.

#### Trace

#### flag

#### Scope

#### 2551

#### Scope

#### 2562

#### Scope

#### 2566

#### Scope

#### 2592

## Description

: Global only.

Causes a memory dump of SQL Server to become a filtered dump (default is mini dump). This

captures a percentage of full memory, where large areas of memory structures pertaining to SQL

Server are purposefully filtered out and not serialized to disk as they bring no troubleshooting

added value (typically, data/index pages, some internal caches like In-Memory OLTP data pages

and Log Pool memory). This results in a file, which is smaller than a full memory dump while

retaining most of its usefulness as preferred option in most situations where mini dumps aren't

sufficient. For more detailed information, see

Use the Sqldumper.exe tool to generate a dump file in

SQL Server

.

: Global only.

Runs the

command in a single "batch" regardless of the number of indexes in the

database. By default, the

command tries to minimize

resources by limiting the

number of indexes or "facts" that it generates by using a "batches" concept. But this trace flag

forces all processing into one batch.

One effect of using this trace flag is that the space requirements for

might increase.

could grow to as much as 5 percent or more of the user database that's being processed by the

command.

Note

: Although this trace flag improves the performance of the

commands that

target usage of the

option, some users might not see any improvement in

performance. While this trace flag improves disk I/O resources usage, the underlying performance

of disk resources might limit the overall performance of the

command. For more

information, see

KB2634571

.

: Global or session.

Runs the

command without data purity check unless the

option is

specified.

Note

: Column-value integrity checks are enabled by default and don't require the DATA_PURITY

option. For databases upgraded from earlier versions of SQL Server, column-value checks aren't

enabled by default until

has been run error free on the database at

least once. After this,

checks column-value integrity by default. For more information,

see an archived version of

KB945770

.

: Global only.

Enables symbol resolution on stack dumps when the

Debugging Tools for Windows

are installed. For

example, using trace flag 3656 requires that trace flag 2592 is enabled.

Warning

: This is a debugging trace flag and not meant for production environment use.

#### Trace

#### flag

#### Applies to

#### Scope

#### 2610

#### Applies to

#### Scope

#### 2616

#### Applies to

#### Scope

#### 3015

#### Applies to

#### Scope

#### 3023

#### backup

#### checksum default

#### Scope

#### 3042

#### Scope

## Description

: SQL Server 2019 (15.x) and later versions.

: Global and session.

Enables memory dump compression and faster dump generation with

SQLDumper

and via

. For more information, see

Use the Sqldumper.exe utility to generate a dump file in SQL

Server

.

: SQL Server 2022 (16.x) CU 8, SQL Server 2019 (15.x) CU 23, and later versions.

: Global and session.

Enables the stack signature feature to make

Sqldumper.exe

generate a single dump per unique

stack signature per hour, which avoids potential dump flooding problems when the same issue

repeats frequently within one hour.

When this trace flag is enabled, the format of the dump file changes from

or

to

(for example,

).

: SQL Server 2022 (16.x) CU 12 and later versions.

: Global only.

Disables

writing backups to Azure immutable storage

.

: SQL Server 2025 (17.x) and later versions.

: Global only.

Enables

option as default for

command.

Note

: Starting with SQL Server 2014 (12.x), this behavior is controlled by setting the

configuration option. For more information, see

backup checksum default

and

Server configuration options

.

: Global and session.

Bypasses the default backup compression preallocation algorithm to allow the backup file to grow

only as needed to reach its final size. This trace flag is useful if you need to save on space by

allocating only the actual size required for the compressed backup. Using this trace flag might

cause a slight performance penalty (a possible increase in the duration of the backup operation).

For more information about the preallocation algorithm, see

Backup compression (SQL Server)

.

: Global only.

#### Trace

#### flag

#### 3051

#### Scope

#### 3205

#### Scope

#### 3226

#### Scope

#### 3261

#### Applies to

#### Scope

#### 3262

#### Applies to

#### Scope

#### 3427

#### Applies to

#### Scope

#### 3428

## Description

Enables SQL Server Backup to URL logging for page blobs in Azure Storage only. Logging writes to

a specific error log file. For more information, see

SQL Server Backup to URL Best Practices and

Troubleshooting

.

: Global only.

By default, if a tape drive supports hardware compression, either the

or

statement

uses it. With this trace flag, you can disable hardware compression for tape drivers. This is useful

when you want to exchange tapes with other sites or tape drives that don't support compression.

: Global or session.

By default, every successful backup and restore operation adds an entry in the SQL Server error log

and in the system event log. If you create frequent log backups, these success messages

accumulate quickly, resulting in huge error logs in which finding other messages becomes

problematic.

With this trace flag, you can suppress backup and restore log entries. This is useful if you're running

frequent log backups and if none of your scripts depend on those entries.

: Global only.

Disables differential database backups on secondary replica of an Always On availability group.

: SQL Server 2025 (17.x)

: Global only.

Disables full database backups on secondary replica of an Always On availability group.

: SQL Server 2025 (17.x)

: Global only.

Enables a fix for an issue when many consecutive transactions insert data into temp tables in SQL

Server 2016 (13.x) where this operation consumes more CPU than in SQL Server 2014 (12.x). For

more information, see

KB3216543

.

: SQL Server 2016 (13.x) Service Pack 1 CU 2 through SQL Server 2016 (13.x) Service Pack

2 CU 2. Starting with SQL Server 2016 (13.x) Service Pack 2 CU 3 and SQL Server 2017 (14.x), this

trace flag has no effect.

: Global only.

The Always On Redo Thread on a secondary replica can sometimes be blocked by T-SQL queries,

which can cause delays in synchronization. This trace flag terminates such blocking queries by

setting their lock timeout to 60 seconds. For more information on Redo thread latency, see

Redo

#### Trace

#### flag

#### Applies to

#### Scope

#### 3459

#### Applies to

#### Scope

#### 3468

#### Applies to

#### Scope

#### 3502

#### Applies to

#### Scope

#### 3605

#### Scope

#### 3608

#### Scope

## Description

thread falls behind due to resource contention

and

Troubleshooting REDO queue build-up (data

latency issues) on Always On Readable Secondary Replicas

.

Warning

: Be sure that you test and understand this option before deploying it in a production

environment as queries might be terminated.

: SQL Server 2019 (15.x)

: Global only.

Disables parallel redo. For more information, see

KB3200975

,

KB4101554

and this blog post,

Availability group secondary replica redo model and performance

.

: SQL Server 2016 (13.x), SQL Server 2017 (14.x), and later versions.

: Global only.

Disables

indirect checkpoints

on

.

: SQL Server 2016 (13.x) Service Pack 1 CU 5, SQL Server 2017 (14.x) CU 1, and later

versions.

: Global only.

Used to send checkpoint state changes to the error log.

: SQL Server 2012 (11.x) and later versions.

: Global or session.

Redirects tracing messages to the SQL Server error log. For example, using trace flags 205 and 8721

require trace flag 3605 to be enabled.

Warning

: This is a debugging trace flag and not meant to be enabled continuously in a production

environment.

: Global or session.

Prevents SQL Server from automatically starting and recovering any database except the

database. If activities that require

are initiated, then

is recovered and

is

created. Other databases are started and recovered when accessed. Some features, such as

snapshot isolation and read committed snapshot, might not work. Use for

Move system databases

and

Move user databases

.

Note

: Don't use during normal operation.

: Global only.

#### Trace

#### flag

#### 3625

#### sysadmin

#### Scope

#### 3656

#### Scope

#### 3880

#### Applies to

#### Scope

#### 3924

#### Scope

#### 3972

#### Scope

#### 4022

#### Scope

#### 4043

#### Scope

## Description

Limits the amount of information returned to users who aren't authenticated as members of the

fixed server role, by masking the parameters of some error messages using

.

This can help prevent disclosure of sensitive information.

: Global only.

Enables symbol resolution on stack dumps when the Debugging Tools for Windows are installed.

Warning

: This is a debugging trace flag and not meant for production environment use.

Note

: Starting with SQL Server 2019 (15.x),

trace flag 2592

must be enabled with trace flag 3656 to

enable symbol resolution.

: Global and session.

Disable the timer task that checks the state of a resumable index.

: SQL Server 2017 (14.x) and later versions and is intended for high-end systems with

high performance workloads.

: Global or session.

Enables automatic removal of orphaned DTC transactions with

, which is a problem for

some third party transaction monitors. For more information, see

KB4519668

and

KB4511816

.

: Global only.

Disables concurrent Page Free Space (PFS) updates feature. For more information on concurrent

PFS updates, see

Intelligent Performance

. For an issue where this trace flag is useful see Non-

yielding scheduler dumps during the recovery of a secondary availability database with a database

snapshot

KB5007794

.

: Global only.

Disables automatic execution of stored procedures when SQL Server starts. For more information

about automatic execution of startup stored procedures, see

sp_procoption

.

: Global only.

Fixes an error that occurs when you apply a security policy on PolyBase external table and use Row-

Level Security (RLS) in SQL Server 2019 (15.x). The error message resembles the following text:

"Security predicates can only be added to user tables and schema bound views" For more

information, see

KB4552159

.

: Global or session.

#### Trace

#### flag

#### 4136

#### Scope

#### 4137

#### Scope

#### 4138

#### Scope

#### 4139

## Description

Disables parameter sniffing unless

,

, or

is

used. For more information, see

KB980653

.

Starting with SQL Server 2016 (13.x), to accomplish this at the database level, see the

option in

ALTER DATABASE SCOPED CONFIGURATION

. To accomplish the same

result at the query level, add the

query hint

. The

hint

doesn't disable the parameter sniffing mechanism, but effectively bypasses it to achieve the same

intended result.

Starting with SQL Server 2016 (13.x) Service Pack 1, a second option to accomplish this at the query

level is to add the

query hint

instead of using this trace

flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session.

Causes SQL Server to generate a plan using minimum selectivity when estimating AND predicates

for filters to account for partial correlation instead of independence, under the query optimizer

cardinality estimation (CE) model of SQL Server 2012 (11.x) and earlier (70). For more information,

see

KB2658214

.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace flag

when using the CE 70.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 120 or above. Use

trace flag 9471

instead.

: Global or session or query (QUERYTRACEON).

Causes SQL Server to generate a plan that doesn't use row goal adjustments with queries that

contain

,

,

, or

keywords. For more information, see

KB2667211

.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Enable automatically generated quick statistics (histogram amendment) regardless of key column

status. If trace flag 4139 is set, regardless of the leading statistics column status (ascending,

descending, or stationary), the histogram used to estimate cardinality is adjusted at query compile

time. For more information, see

KB2952101

.

#### Trace

#### flag

#### Scope

#### 4199

#### QO changes from all previous database compatibility levels

#### QO changes for DE version post-RTM

#### Scope

#### 4610

#### Scope

## Description

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 70. Use trace flags 2389 and 2390 instead.

: Global or session or query (QUERYTRACEON).

Enables Query Optimizer (QO) fixes released in SQL Server Cumulative Updates and Service Packs.

QO changes that are made to previous releases of SQL Server are enabled by default under the

latest database

compatibility level

in a given product release, without trace flag 4199 being

enabled. For more information, see

KB974006

.

:

- If trace flag 4199 is enabled, query optimizer changes from all previous database compatibility

levels are also enabled.

- If trace flag 4199 is disabled or not set, query optimizer changes are enabled starting with

compatibility level 130. For compatibility levels below 130, query optimizer changes are disabled.

:

- If trace flag 4199 is enabled, query optimizer changes are enabled for the Database Engine

version post-RTM.

- If trace flag 4199 is disabled or not set, query optimizer changes are disabled for the Database

Engine version post-RTM.

Starting with SQL Server 2016 (13.x), to accomplish this at the database level, see the

option in

ALTER DATABASE SCOPED CONFIGURATION

.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace flag.

Important

: Query Optimizer fixes that address wrong results or access violation errors aren't

enabled by trace flag 4199. Those fixes aren't considered optional and become enabled by default

once the update package is installed.

: Global or session or query (

).

Increases the size of the hash table that stores the cache entries by a factor of 8. When used

together with trace flag 4618, increases the number of entries in the TokenAndPermUserStore cache

store to 8,192. For more information on troubleshooting TokenAndPermUserStore cache size issues,

see

Queries take longer to finish when the size of the TokenAndPermUserStore cache grows in SQL

Server

.

: Global only.

#### Trace

#### flag

#### 4616

#### Scope

#### 4618

#### Scope

#### 4621

#### Scope

#### 4631

#### Applies to

#### Scope

#### 4675

#### Scope

## Description

Makes server-level metadata visible to application roles. In SQL Server, an application role can't

access metadata outside its own database because application roles aren't associated with a server-

level principal. This is a change of behavior from earlier versions of SQL Server. Setting this global

flag disables the new restrictions, and allows for application roles to access server-level metadata.

: Global only.

Limits the number of entries in the TokenAndPermUserStore cache store to 1,024. When used

together with trace flag 4610, trace flag 4618 increases the number of entries in the

TokenAndPermUserStore cache store to 8,192. For more information on troubleshooting

TokenAndPermUserStore cache size issues, see

Queries take longer to finish when the size of the

TokenAndPermUserStore cache grows in SQL Server

.

: Global only.

Limits the number of entries in the TokenAndPermUserStore cache store to the number specified by

the user in a registry key. For more information, see

access check cache Server Configuration

Options

.

: Global only.

Disables SHA2_256/AES256 for hashing passwords that generate encryption keys. Starting in SQL

Server 2017 (14.x), SHA2 is used instead of SHA1. This means extra steps might be necessary to

have your SQL Server 2017 (14.x) installation decrypt items that were encrypted by SQL Server 2016

(13.x), as described in

Create identical symmetric keys on two servers

. For more information, see

KB4053407

.

: SQL Server 2017 (14.x) and later versions.

: Global only.

Enable checks on

create credential for managed identity

on a SQL Server on Azure VM if Microsoft

Entra authentication is enabled.

Enables diagnostics for the

statement. The

trace flag provides information about the primary managed identity and its setting for SQL Server

on Azure VM.

Note

: If the

statement was executed without trace flag 4675 enabled, no error

message is issued if the primary managed identity isn't set for the server. To troubleshoot this

scenario, the credential must be deleted and recreated again once the trace flag is enabled.

Warning

: Trace flag 4675 isn't meant to be enabled continuously in a production environment, and

only for time-limited troubleshooting sessions.

: Global or session.

#### Trace

#### flag

#### 5004

#### Scope

#### 6408

#### Applies to

#### Scope

#### 6498

#### Scope

#### 6527

#### Scope

#### 6531

#### Applies to

## Description

Pauses TDE encryption scan and causes encryption scan worker to exit without doing any work. The

database continues to be in encrypting state (encryption in progress). To resume re-encryption

scan, disable trace flag 5004 and run

.

: Global only.

Enables visibility of the estimated execution plan to see the remote query plan of PolyBase

pushdown computation.

: SQL Server 2019 (15.x) and later versions. For more information, see

How to tell if

external pushdown occurred

.

: Global or session or query (QUERYTRACEON).

Enables more than one large query compilation to gain access to the large gateway when there's

sufficient memory available. This trace flag can be used to keep memory usage for the compilation

of incoming queries under control, avoiding compilation waits for concurrent large queries. It's

based on a value of 80 percent of SQL Server Target Memory, and it allows for one large query

compilation per 25 GB of memory. For more information, see

KB3024815

.

Note

: Starting with SQL Server 2014 (12.x) Service Pack 2 and SQL Server 2016 (13.x), this behavior

is controlled by the Database Engine and trace flag 6498 has no effect.

: Global only.

Disables generation of a memory dump on the first occurrence of an out-of-memory exception in

CLR integration. By default, SQL Server generates a small memory dump on the first occurrence of

an out-of-memory exception in the CLR. The behavior of the trace flag is as follows:

- If this is used as a startup trace flag, a memory dump is never generated. However, a memory

dump might be generated if other trace flags are used.

- If this trace flag is enabled on a running server, a memory dump isn't automatically generated

from that point on. However, if a memory dump has already been generated due to an out-of-

memory exception in the CLR, this trace flag has no effect.

: Global only.

Disables preemptive scheduling protection for query operations with spatial data types. This can

reduce the CPU consumption and improve the overall performance for some spatial activities. For

more information, see

KB3005300

.

Note

: Only use this trace flag if the individual spatial method invocations (per row and column) take

less than ~4ms and result in frequent non-yielding scheduler errors.

: SQL Server 2012 (11.x) Service Pack 2 CU 4, SQL Server 2014 (12.x) CU 5, and later

versions.

#### Trace

#### flag

#### Scope

#### 6532

#### Scope

#### 6533

#### Scope

#### 6534

#### Scope

#### 6545

#### Applies to

#### Scope

#### 6559

#### Applies to

#### Scope

#### 7117

## Description

: Global and session.

Enables performance improvement of query operations with spatial data types in SQL Server 2012

(11.x) and SQL Server 2014 (12.x). The performance gain varies, depending on the configuration, the

types of queries, and the objects. For more information, see

KB3107399

.

Note

: Starting with SQL Server 2016 (13.x), this behavior is controlled by the Database Engine and

trace flag 6532 has no effect.

: Global and session.

Enables performance improvement of query operations with spatial data types in SQL Server 2012

(11.x) and SQL Server 2014 (12.x). The performance gain varies, depending on the configuration, the

types of queries, and the objects. For more information, see

KB3107399

.

Note

: Starting with SQL Server 2016 (13.x), this behavior is controlled by the Database Engine and

trace flag 6533 has no effect.

: Global and session.

Enables performance improvement of query operations with spatial data types beginning with SQL

Server 2012 (11.x). The performance gain varies, depending on the configuration, the types of

queries, and the objects. For more information, see

KB3107399

.

: Global only.

Enables CLR strict security. For more information, see

KB4018930

.

: SQL Server 2012 (11.x) Service Pack 3 CU 10, SQL Server 2014 (12.x) Service Pack 2 CU 6,

SQL Server 2016 (13.x) RTM CU 7, SQL Server 2016 (13.x) Service Pack 1 CU 4, and later versions.

Starting with SQL Server 2017 (14.x), this feature is enabled by default and trace flag 6545 has no

effect.

: Global only.

Enables fix that changes default CLR threading model logic. For more information, see

KB4517771

.

: SQL Server 2016 (13.x) Service Pack 2 CU 10, SQL Server 2017 (14.x) CU 18, SQL Server

2019 (15.x) CU 1, and later versions.

: Global only.

Mitigates an assertion failure that you might encounter when you have multiple nested inserts. This

trace flag enables the persistent version store (PVS) cleaner thread to proceed, if the PVS bit is set

for a row that might have been part of an aborted transaction. This trace flag allows the PVS

cleaner to ignore the bit and continue the cleaning operation.

#### Trace

#### flag

#### Applies to

#### Scope

#### 7314

#### Scope

#### 7412

#### Applies to

#### Scope

#### 7470

#### Applies to

#### Scope

#### 7471

#### Applies to

#### Scope

#### 7745

#### Scope

#### 7752

## Description

: SQL Server 2022 (16.x) CU 9 and later versions.

: Global only.

Forces

values with unknown precision/scale to be treated as double values with OLE DB

provider. For more information, see

KB3051993

.

: Global and session.

Enables the lightweight query execution statistics profiling infrastructure. For more information, see

KB3170113

.

: SQL Server 2016 (13.x) Service Pack 1 and later versions. Starting with SQL Server 2019

(15.x), this trace flag has no effect because lightweight profiling is enabled by default.

: Global only.

Enables additional computations for memory grants required for sort operations. For more

information, see

KB3088480

.

: SQL Server 2012 (11.x) Service Pack 2 CU 8, SQL Server 2014 (12.x) RTM CU 10, SQL

Server 2014 (12.x) Service Pack 1 CU 3, and later versions.

Warning

: Trace flag 7470 increases memory requirements for queries using sort operators, and

might affect memory availability for other concurrent queries.

: Global or session or query (QUERYTRACEON).

Enables running multiple

UPDATE STATISTICS

for different statistics on a single table concurrently.

For more information, see

KB3156157

.

: SQL Server 2014 (12.x) Service Pack 1 and later versions.

: Global only.

Forces Query Store to not flush data to disk on database shutdown.

Note

: Using this trace flag might cause Query Store data not previously flushed to disk to be lost if

the server shuts down. For a SQL Server shutdown, the command

can be

used instead of this trace flag to force an immediate shutdown.

: Global only.

Enables asynchronous load of Query Store.

Note

: Use this trace flag if SQL Server is experiencing high number of QDS_LOADDB waits related

to Query Store synchronous load (default behavior during database recovery).

#### Trace

#### flag

#### Scope

#### 7806

#### Scope

#### 8002

#### Scope

#### 8011

#### Scope

#### 8012

#### Scope

#### 8015

## Description

Note

: Starting with SQL Server 2019 (15.x), this behavior is controlled by the Database Engine and

trace flag 7752 has no effect.

: Global only.

Enables a dedicated administrator connection (DAC) on SQL Server Express. By default, no DAC

resources are reserved on SQL Server Express. For more information, see

Diagnostic connection for

database administrators

.

: Global only.

Enables soft processor affinity on SQL Server on Linux. By default, schedulers are bound to specific

CPUs defined in the affinity mask. With this trace flag enabled, schedulers can move across CPUs,

which generally improves performance while still respecting processor affinity and control group

(cgroup) v2 constraints. For more information, see

Control group (cgroup) v2 support

.

: Global only.

Disable the ring buffer for Resource Monitor. You can use the diagnostic information in this ring

buffer to diagnose out-of-memory conditions. Therefore, if you use this trace flag, the information

that's available to diagnose performance and functional problems with SQL Server is greatly

reduced. Trace flag 8011 always applies across the server and has global scope. You can turn on

trace flag 8011 at startup or in a user session.

: Global only.

Disable the ring buffer for schedulers. SQL Server records an event in the schedule ring buffer every

time that one of the following events occurs:

- A scheduler switches context to another worker

- A worker is suspended

- A worker is resumed

- A worker enters the preemptive mode or the non-preemptive mode.

You can use the diagnostic information in this ring buffer to analyze scheduling problems. For

example, you can use the information in this ring buffer to troubleshoot problems when SQL Server

stops responding. Trace flag 8012 disables recording of events for schedulers. You can turn on trace

flag 8012 only at startup.

Warning

: When you use this trace flag, the information that's available for you to diagnose

performance and functional problems with SQL Server is greatly reduced.

: Global only.

Disable autodetection and NUMA setup. For more information, see

KB2813214

.

#### Trace

#### flag

#### Scope

#### 8018

#### Scope

#### 8019

#### Scope

#### 8020

#### Scope

#### 8026

#### Scope

#### 8032

#### Scope

#### 8048

## Description

: Global only.

Disable the exception ring buffer. The exception ring buffer records the last 256 exceptions that are

raised on a node. Each record contains some information about the error and contains a stack

trace. A record is added to the ring buffer when an exception is raised. Trace flag 8018 disables the

creation of the ring buffer, and no exception information is recorded. Trace flag 8019 disables stack

collection during the record creation.

Warning

: When you use this trace flag, the information that's available for you to diagnose

performance and functional problems with SQL Server is greatly reduced.

: Global only.

Disable stack collection for the exception ring buffer. Trace flag 8019 has no effect if trace flag 8018

is turned on.

Warning

: When you use this trace flag, the information that's available for you to diagnose

performance and functional problems with SQL Server is greatly reduced.

: Global only.

Disable working set monitoring. SQL Server uses the size of the working set when it receives global

memory state signals from the operating system. Trace flag 8020 removes the size of the working

set memory from consideration when SQL Server interprets the global memory state signals. If you

use this trace flag incorrectly, heavy paging might occur, and the performance might be poor.

Therefore, contact Microsoft Support before you turn on trace flag 8020. You can turn on trace flag

8020 only at startup.

: Global only.

SQL Server clears a dump trigger after generating the dump once. If used with trace flag 2551 or

trace flag 2544, the option indicating the largest memory dump is honored. For more information,

see

Filtered dumps

.

: Global only.

Reverts the cache limit parameters to the SQL Server 2005 (9.x) setting, which in general allows

caches to be larger. Use this setting when frequently reused cache entries don't fit into the cache

and when the

optimize for ad hoc workloads Server Configuration Option

has failed to resolve the

problem with plan cache.

Warning

: Trace flag 8032 can cause poor performance if large caches make less memory available

for other memory consumers, such as the buffer pool.

: Global only.

Converts NUMA partitioned memory objects into CPU partitioned. For more information, see

KB2809338

.

#### Trace

#### flag

#### Scope

#### 8075

#### Applies to

#### Scope

#### 8079

#### Applies to

#### Scope

#### 8086

#### Applies to

#### Scope

#### 8089

#### Applies to

#### Scope

#### 8095

## Description

Note

: Starting with SQL Server 2014 (12.x) Service Pack 2 and SQL Server 2016 (13.x), this behavior

is dynamic and controlled by the Database Engine.

: Global only.

Reduces

VAS

fragmentation when you receive memory page allocation errors on a 64-bit SQL

Server 2012 (11.x) or SQL Server 2014 (12.x). For more information, see

KB3074434

.

: SQL Server 2012 (11.x), SQL Server 2014 (12.x) RTM CU 10, and SQL Server 2014 (12.x)

Service Pack 1 CU 3. Starting with SQL Server 2016 (13.x), this behavior is controlled by the

Database Engine and trace flag 8075 has no effect.

: Global only.

Allows SQL Server 2014 (12.x) Service Pack 2 to interrogate the hardware layout and automatically

configure Soft-NUMA on systems reporting 8 or more CPUs per NUMA node. The automatic Soft-

NUMA behavior is simultaneous multithreading (SMT/logical processor) aware. The partitioning

and creation of additional nodes scales background processing by increasing the number of

listeners, scaling, and network and encryption capabilities.

: SQL Server 2014 (12.x) Service Pack 2. Starting with SQL Server 2016 (13.x), this behavior

is controlled by the Database Engine and trace flag 8079 has no effect.

: Global only.

Disable NUMA locality check for memory commits.

: SQL Server 2019 (15.x) and later versions.

: Global.

In SQL Server 2017 (14.x) CU 16, you can enable the bitmap filtering for reducing the size of filtered

memory dumps. SQL Server allocates a bitmap that keeps track of memory pages to be excluded

from a filtered dump. Sqldumper.exe reads the bitmap and filters out pages without the need to

read any other memory manager metadata.

: SQL Server 2017 (14.x) CU 16 through CU 19 only. Starting with SQL Server 2017 (14.x)

CU 20 the bitmap filtering is enabled by default. Trace flag 8089 no longer applies, and is ignored if

turned on. The bitmap filtering can be disabled via trace flag 8095. For more information, see

KB4488943

.

: Global only.

Disables the bitmap filtering for filtered memory dumps. SQL Server allocates a bitmap that keeps

track of memory pages to be excluded from a filtered dump. Sqldumper.exe reads the bitmap and

filters out pages without the need to read any other memory manager metadata. This trace flag

applies to builds where bitmap filtering is enabled by default.

#### Trace

#### flag

#### Applies to

#### Scope

#### 8099

#### Applies to

#### Applies to

#### Scope

#### 8101

#### Applies to

#### Applies to

#### Scope

#### 8102

#### Applies to

#### Scope

#### 8121

#### Applies to

## Description

: SQL Server 2016 (13.x) CU 13 and later versions, SQL Server 2017 (14.x) CU 20 and later

versions, and SQL Server 2019 (15.x).

: Global only.

Enables a spinlock contention fix for high-end systems running SQL Server 2019 (15.x) serving many

concurrent users.

: SQL Server 2019 (15.x) CU 2 and CU 3 only. Starting with SQL Server 2019 (15.x) CU 4,

this behavior is enabled by default. For more information about spinlock contention, see

trace flag

8101

, and

KB4538688

.

: SQL Server 2019 (15.x)

: Global only.

Addresses high CPU usage on modern hardware, such as Intel Skylake processors, with a large

number of CPUs and a high number of concurrent users. To diagnose spinlock contention, see the

Diagnose and resolve spinlock contention on SQL Server

whitepaper.

: SQL Server 2019 (15.x) only, starting with CU 8, with further improvements introduced in

CU 14 and CU 16.

For more information, see

KB4538688

.

: SQL Server 2019 (15.x)

: Global only.

Addresses a high-CPU scenario caused by spinlock contention on the XVB_LIST spinlock. You can

observe this most commonly on high-end systems with a large number of newer generation

processors (CPUs). This trace flag can be enabled together with trace flag 8101. While trace flag

8101 changes the spin increment, trace flag 8102 staggers the spinlock backoffs. For more

information on backoffs, see

Diagnose and resolve spinlock contention on SQL Server

.

: SQL Server 2019 (15.x).

: Global only.

Fixes a system-wide low memory issue that occurs when SQL Server commits memory above the

maximum server memory under the memory model with the Lock Pages In Memory security policy

setting. This trace flag affords the memory that the Resource monitor system thread needs in order

to reduce SQL Server memory consumption. For more information, see

KB5008996

.

: SQL Server 2019 (15.x). For SQL Server 2022 (16.x) and later versions, this functionality is

enabled by default and this trace flag has no effect. If you'd like to disable this default behavior and

#### Trace

#### flag

#### Scope

#### 8134

#### Applies to

#### Scope

#### 8142

#### Applies to

#### Scope

#### 8145

#### Applies to

#### Scope

#### 8207

#### Scope

#### 8239

## Description

revert to the older behavior, you can use trace flag 8125. However, in most cases this choice isn't

recommended.

: Global only.

Enables the tracking of spinlock waits with the

wait type. You can enable this trace

flag when troubleshooting high CPU utilization, to confirm or rule out a

spinlock contention

problem. For more information, see

SPINLOCK_EXT

.

: SQL Server 2025 (17.x).

: Global only.

This trace flag partitions the specific spinlock-protected list by CPU, up to 64 partitions. This should

be used only on large-memory machines experiencing

spinlock

contention with elevated CPU utilization. See also

trace flag 8145

. For more information, see

KB5025808

.

: SQL Server 2019 (15.x) CU 21 and later versions.

: Global only.

Modifies the partitioning enabled by

trace flag 8142

to be per soft-NUMA node, instead of per

CPU. You must also enable

trace flag 8142

for this setting to take effect. For more information, see

KB5025808

.

: SQL Server 2019 (15.x) CU 21 and later versions.

: Global only.

Enables singleton updates for Transactional Replication and CDC. Updates to subscribers can be

replicated as a

and

pair. This might not meet business rules, such as firing an

trigger. With trace flag 8207, an update to a unique column that affects only one row (a

singleton update) is replicated as an

and not as a

or

pair. If the update

affects a column on which a unique constraint exists, or if the update affects multiple rows, the

update is still replicated as a

or

pair. For more information, see an archived version

of

KB302341

.

: Global only.

By default,

sys.sp_flush_commit_table_on_demand

computes a minimum of hardened cleanup

version and safe cleanup version, and proceeds with data deletion from the commit table. When

trace flag 8239 is set, a

value less than the cleanup point is ignored, and

cleanup runs after rerunning

. Incorrect use of this trace flag

can lead to data corruption. For more information, see

Troubleshoot change tracking auto cleanup

issues

.

#### Trace

#### flag

#### Applies to

#### Scope

#### 8273

#### Scope

#### 8284

#### Scope

#### 8285

#### Applies to

#### Scope

#### 8286

#### Applies to

#### Scope

#### 8287

#### Applies to

#### Scope

#### 8290

#### Applies to

#### Scope

## Description

: SQL Server 2022 (16.x) CU 3 and later versions.

: Global only.

Enabling trace flag 8273 disables

adaptive shallow cleanup for change tracking

.

Note

: This trace flag applies to SQL Server 2025 (17.x) and later versions.

: Global only.

Fixes a manual cleanup issue where the repeated lock escalations on the tables cause contention

and slowness in cleaning up the expired change tracking metadata.

Note

: This trace flag applies to SQL Server 2019 (15.x) CU 21 and later versions.

: Global only.

Converts an assertion failure (Expression:

) to an exception to prevent

a dump issue under certain circumstances, when you enable change tracking on a database that

has snapshot isolation turned on.

: SQL Server 2022 (16.x) CU 6, SQL Server 2019 (15.x) CU 21, and later versions.

: Global only.

Forces the cleanup query to use the

hint to improve performance. Can be used with

trace flag 8287

to use the

hint. For more information, see

KB5022375

.

: SQL Server 2019 (15.x) CU 19, SQL Server 2022 (16.x) CU 1, and later versions.

: Global only.

Forces the cleanup query to use the

hint to improve performance. Can be used with

trace flag 8286

to use the

hint. For more information, see

KB5022375

.

: SQL Server 2019 (15.x) CU 19, SQL Server 2022 (16.x) CU 1, and later versions.

: Global only.

After this trace flag is enabled, the change tracking (CT) auto cleanup process resets any invalid

cleanup version to a cleanup version based on the retention period. After you enable this trace flag,

you must let the auto cleanup process run. For more information, see

KB4538365

.

: SQL Server 2017 (14.x) CU 19, SQL Server 2019 (15.x) CU 4, SQL Server 2022 (16.x), and

later versions.

: Global or session.

#### Trace

#### flag

#### 8531

#### Applies to

#### Scope

#### 8558

#### Applies to

#### Scope

#### 8721

#### Scope

#### 8744

#### Scope

#### 8790

#### Scope

#### 8902

#### Applies to

#### Scope

## Description

Enables the fix for a contention issue with high

wait times that you might

encounter when running XA distributed transactions.

: SQL Server 2019 (15.x) CU 29, SQL Server 2022 (16.x) CU 16, and later versions.

: Global and startup only.

Enables a fix to ensure that you don't observe edge cases where when RCSI isolation level is

enabled then a transaction sometimes can't see the latest data from the tables that were modified

using DTC transactions even after xa_commit returned success for a short duration of time.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: SQL Server 2019 (15.x) CU 18, SQL Server 2022 (16.x), and later versions.

: Global only.

Reports to the error log when autoupdate statistics executes. For more information, see an archived

version of

KB195565

.

Note

: This trace flag requires enabling

trace flag 3605

.

: Global only.

Disable prefetching for the

Nested Loops

operator.

Warning

: Incorrect use of this trace flag might cause extra physical reads when SQL Server executes

plans that contain the Nested Loops operator.

: Global and session.

Causes SQL Server to use a wide query plan when executing an

statement to update

indexes in a table. When you do an

against a clustered index column, SQL Server updates

not only the clustered index itself, but also all the nonclustered indexes because the nonclustered

indexes contain the cluster index key. To optimize performance and reduce random I/O SQL Server

might choose to sort all nonclustered index data in memory, and then update all indexes by the

order. This is known as a wide plan, also called Per-Index Update, and can be forced using this trace

flag.

: Global, session, or query (QUERYTRACEON).

Disable locked pages for IO operations for high-end systems with high performance workloads.

: SQL Server 2019 (15.x) and later versions.

: Global.

#### Trace

#### flag

#### 8904

#### Applies to

#### Scope

#### 9024

#### Scope

#### 9109

#### Scope

#### 9135

#### Applies to

#### Scope

#### 9347

#### Scope

#### 9348

#### Scope

#### 9349

## Description

Enables a fix to address a parallel redo failure on a secondary replica by disabling inlined log IO,

limiting the contention possibility from many workers to the subset of background LogWriter

workers. For more information, see

KB5004649

and

Trace flag 8904 - Disable Inline Database Log

Flushes

.

: SQL Server 2019 (15.x) only, starting with CU 12.

: Global only.

Converts a global log pool memory object into NUMA node partitioned memory object. For more

information, see

KB2809338

.

Note

: Starting with SQL Server 2012 (11.x) Service Pack 3 and SQL Server 2014 (12.x) Service Pack 1,

this behavior is controlled by the Database Engine and trace flag 9024 has no effect.

: Global only.

Disables start of Query Notification functionality. For more information, see

Restore or recovery

may fail or take a long time if query notification is used in a database

.

Warning

: Use caution with this trace flag. This trace flag can be useful in a limited set of scenarios

primarily for troubleshooting or isolating a problem.

: Global and session.

Prevents the usage of indexed views. To accomplish this at the query level, add the

query hint instead of using this trace flag. For more information, see

Table Hints

.

: SQL Server 2019 (15.x) CU 23, SQL Server 2022 (16.x) CU 19, and later versions.

: Global only.

Disables batch mode for sort operator. SQL Server 2016 (13.x) introduced a new batch mode sort

operator that boosts performance for many analytical queries. For more information, see

KB3172787

.

: Global or session or query (QUERYTRACEON).

Enables the use of Query Optimizer cardinality estimates to decide whether BULK INSERT for a

clustered columnstore index should be initiated or not. If the estimated number of rows to insert is

less than 102,400, the Database Engine doesn't use

. If more than 102,400 rows are

estimated, a

is initiated. For more information, see

KB2998301

.

: Global or session or query (QUERYTRACEON).

Disables batch mode for top N sort operator. SQL Server 2016 (13.x) introduced a new batch mode

top sort operator that boosts performance for many analytical queries.

#### Trace

#### flag

#### Scope

#### 9358

#### Scope

#### 9389

#### Scope

#### 9398

#### Scope

#### 9410

#### Scope

#### 9440

#### Applies to

#### Scope

## Description

: Global or session or query (QUERYTRACEON).

Disables batch mode for sort operator. For more information, see

KB3171555

.

Note

: Starting with SQL Server 2017 (14.x), this behavior is enabled by default and this trace flag

has no effect.

: Global or session or query (QUERYTRACEON).

Enables additional dynamic memory grant for batch mode operators. If a query doesn't get the

memory it needs, it spills data to

, incurring additional I/O and potentially affecting query

performance. If the dynamic memory grant trace flag is enabled, a batch mode operator might ask

for additional memory and avoid spilling to

if additional memory is available. For more

information, see the

Effects of min memory per query

section of the

Memory Management

Architecture Guide

.

: Global or session.

Disables

Adaptive Join

operator that enables the choice of a

hash join or nested loops join

method

to be deferred until after the first input has been scanned, as introduced in SQL Server 2017 (14.x).

For more information, see

KB4099126

.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Enables a non-default fix for a query that uses a hash aggregate operator and spills. Enabling this

trace flag increases the available memory for distinct hash operations. For more information, see

KB3167159

.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Disables the fix for bug

2112485

and bug

2636294

. The bug fix doesn't apply when using the

legacy Cardinality Estimation (CE) model. When a database uses the default CE model, outer join

cardinality estimates might increase higher than the cardinality of the tables involved in the join

when the join predicates consist of primary keys from the tables (for example, primary key to

foreign key joins). A cap is applied that limits the amount of cardinality overestimation similar to

the overestimation limit that exists in the legacy CE for this scenario.

Note

: This trace flag only applies to databases with a compatibility level of 160 and lower.

: SQL Server 2019 (15.x) CU 20, SQL Server 2022 (16.x) CU 9, and later versions.

: Global or session or query (QUERYTRACEON).

#### Trace

#### flag

#### 9453

#### Scope

#### 9471

#### Scope

#### 9476

#### Scope

#### 9481

#### Scope

#### 9485

#### Scope

## Description

Disables batch mode execution. For more information, see

KB4016902

.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Causes SQL Server to generate a plan using minimum selectivity for single-table filters, under the

query optimizer cardinality estimation model of SQL Server 2014 (12.x) and later versions.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace

flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 70. Use

trace flag 4137

instead.

: Global or session or query (QUERYTRACEON).

Causes SQL Server to generate a plan using the Simple Containment assumption instead of the

default Base Containment assumption, under the query optimizer cardinality estimation model of

SQL Server 2014 (12.x) and later versions. For more information, see

Join containment assumption

in the New Cardinality Estimator degrades query performance

.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Sets the Query Optimizer cardinality estimation (CE) model to SQL Server 2012 (11.x) and earlier

(version 70), irrespective of the compatibility level of the database. For more information, see

Query

hints

.

Starting with SQL Server 2016 (13.x), to accomplish this at the database level, see the

option in

ALTER DATABASE SCOPED CONFIGURATION

.

Starting with SQL Server 2016 (13.x) Service Pack 1, to accomplish this at the query level, add the

query hint

instead of using this trace flag.

: Global or session or query (QUERYTRACEON).

Disables SELECT permission for

. For more information, see

KB2683304

.

: Global only.

#### Trace

#### flag

#### 9488

#### Scope

#### 9495

#### Scope

#### 9567

#### Scope

#### 9571

#### Scope

#### 9576

#### Scope

#### 9591

#### Scope

#### 9592

#### Scope

#### 9708

#### Applies to

## Description

Sets the fixed estimation for Table Valued Functions to the default of 1 (corresponding to the

default under the Query Optimizer cardinality estimation model of SQL Server 2008 R2 (10.50.x)

and earlier), when using the Query Optimizer cardinality estimation model of SQL Server 2012 (11.x)

and later versions.

: Global or session or query (QUERYTRACEON).

Disables parallelism during insertion for

operations and it applies to both user and

temporary tables. For more information, see

KB3180087

.

: Global or session.

Enables compression of the data stream for Always On Availability Groups during automatic

seeding. Compression can significantly reduce the transfer time during automatic seeding, and

increases the load on the processor. For more information, see

Use automatic seeding to initialize

an Always On availability group

and

Tune compression for availability group

.

: Global or session.

Disables Availability Groups Auto seeding to the default database path. For more information, see

Disk layout

.

: Global or session.

Disables the enhanced error collection for Availability Group failovers introduced in SQL Server

2016 (13.x) Service Pack 1 CU 10, SQL Server 2016 (13.x) Service Pack 2 CU 2, and SQL Server 2017

(14.x) CU 9. For more information, see

SQL Server Availability Groups – Enhanced Database Level

Failover

.

: Global only.

Disables log block compression in Always On Availability Groups. Log block compression is the

default behavior used with both synchronous and asynchronous replicas in SQL Server 2012 (11.x)

and SQL Server 2014 (12.x). In SQL Server 2016 (13.x), compression is only used with asynchronous

replica.

: Global or session.

Enables log stream compression for synchronous availability groups. This feature is disabled by

default on synchronous availability groups because compression adds latency. For more

information, see

Tune compression for availability group

.

: Global or session.

Enables collection of event publishing metrics for extended event sessions. For more information,

see

sys.dm_xe_session_events

.

: SQL Server 2022 (16.x) and later versions.

#### Trace

#### flag

#### Scope

#### 9714

#### Applies to

#### Scope

#### 9810

#### Applies to

#### Scope

#### 9898

#### Scope

#### 9929

#### Scope

#### 9939

#### Scope

#### 9944

#### Scope

## Description

: Global only.

Enables the SQL Server error log to record the start or stop of Extended Events (XEvents) sessions.

: SQL Server 2022 (16.x) CU 15 and later versions.

: Global only.

Disables the In-Memory OLTP engine from reclaiming Thread Local Storage (TLS) memory. In SQL

Server 2019 (15.x) and earlier versions, not reclaiming TLS memory is the default behavior. In SQL

Server 2022 (16.x), a new memory optimization was introduced that causes the In-Memory OLTP

engine to reclaim TLS memory, and to reduce the possibility of out-of-memory issues. This trace

flag reverts to the behavior before SQL Server 2022 (16.x).

: SQL Server 2022 (16.x) and later versions.

: Global only.

Changes the memory partitioning scheme for the In-Memory OLTP engine from per-CPU to per-

NUMA node. For existing In-Memory OLTP objects in a database, takes effect only after the server is

restarted or when a database is brought online. For more information, see

Memory fragmentation

: Global only.

Reduces the In-Memory checkpoint files to 1 MB each. For more information, see

KB3147012

.

: Global only.

Enables parallel plans and parallel scan of memory-optimized tables and table variables in DML

operations that reference memory-optimized tables or table variables, as long as they aren't the

target of the DML operation in SQL Server 2016 (13.x). For more information, see

KB4013877

.

Note

: Trace flag 9939 isn't needed if trace flag 4199 is also explicitly enabled.

: Global or session or query (QUERYTRACEON).

Enables a non-default fix for slow database recovery time when a database has a large number of

memory optimized tables or memory optimized table types, and blocking with

or

wait types might be observed. For more

information, see

KB4090789

and

KB4052338

.

For SQL Server on Linux, this trace flag only applies to SQL Server 2022 (16.x) CU 13 and later

versions.

: Global only.

#### Trace

#### flag

#### 9953

#### Applies to

#### Scope

#### 10054

#### Applies to

#### Scope

#### 10204

#### Scope

#### 10207

#### Scope

#### 10316

#### Scope

#### 10460

#### Applies to

## Description

Reuses the hidden schedulers used by the Memory Optimized tables.

: SQL Server 2019 (15.x) CU 20 and later versions, and SQL Server 2022 (16.x) CU 3 and

later versions.

: Global only.

Disables the SQL Server Query Optimizer rule that decorrelates subqueries in OR predicates into

outer joins.

: SQL Server 2019 (15.x) and later versions.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Disables merge/recompress during columnstore index reorganization. In SQL Server 2016 (13.x),

when a columnstore index is reorganized, there's new functionality to automatically merge any

small compressed rowgroups into larger compressed rowgroups, and recompressing any

rowgroups that have a large number of deleted rows.

Note

: Trace flag 10204 doesn't apply to columnstore indexes that are created on memory-

optimized tables.

: Global or session.

Allows clustered columnstore index (CCI) scans to skip corrupt segments or metadata, allowing data

retrieval from a corrupt CCI. For more information, see

KB3067257

.

: Global or session.

Enables creation of additional indexes on

internal memory-optimized staging temporal table

,

beside the default one. If you have specific query pattern that includes columns that aren't covered

by the default index, you might consider adding additional indexes.

Note

: System-versioned temporal tables for Memory-Optimized Tables are designed to provide

high transactional throughput. Creating additional indexes might introduce overhead for DML

operations that update or delete rows in the current table. With the additional indexes, you should

aim to find the right balance between performance of temporal queries and additional DML

overhead.

: Global or session.

Causes the SQL Server Stretch Database feature to provision a stretched table within the Azure SQL

Database Hyperscale service tier.

: SQL Server 2017 (14.x) CU 31, SQL Server 2019 (15.x) CU 18, and SQL Server 2022 (16.x)

#### Trace

#### flag

#### Scope

#### 11023

#### Scope

#### 11024

#### Applies to

#### Scope

#### 11047

#### Applies to

#### Scope

#### 11064

#### Applies to

#### Scope

#### 11068

## Description

and later versions.

Starting with SQL Server 2017 (14.x) CU 31, SQL Server 2019 (15.x) CU 18, and SQL Server 2022

(16.x), the default behavior of the Stretch Database feature provisions a stretched table within an

Azure SQL Database Standard service tier (S3).

: Global only.

Disables the use of the last persisted sample rate for all subsequent statistics update, where a

sample rate isn't specified explicitly as part of the

UPDATE STATISTICS

statement. For more

information, see

KB4039284

.

: Global only.

Enables triggering the auto update of statistics when the modification count of any partition

exceeds the local

threshold

. For more information, see

KB4041811

.

: SQL Server 2016 (13.x) Service Pack 2, SQL Server 2017 (14.x) CU 3, and later versions.

: Global only.

Applies the default timeout set by

or the Resource Governor

configuration to columnstore index build operations. For more

information, see

KB4480641

.

: SQL Server 2016 (13.x) Service Pack 2 CU 5, SQL Server 2017 (14.x) CU 14, and later

versions.

: Global only.

Improves the scalability of data loading operations into columnstore indexes, by optimizing

memory distribution between the

and

statements. For more information on loading

data into a columnstore index, see

Columnstore indexes - data loading guidance

.

: SQL Server 2019 (15.x) and later versions.

: Global only.

Uses the server, database, or resource pool configured max degree of parallelism (MAXDOP) value

for columnstore index insert operations. For more information on overriding degrees of parallelism,

see the

Query Processing Architecture Guide

.

Important

: This trace flag is only effective if trace flag 11064 is also enabled.

Important

: Use this trace flag when faster data loads are preferred over maintaining

columnstore

segment

quality. For example, using this trace flag when loading 1,048,577 rows into a columnstore

might result in more than one compressed rowgroup, if the insert operation is executing in parallel

#### Trace

#### flag

#### Applies to

#### Scope

#### 11561

#### Scope

#### 11631

#### Applies to

#### Scope

#### 11634

#### Applies to

#### Scope

#### 11953

#### Applies to

## Description

mode. Without this trace flag, the insert operation would result in one compressed rowgroup.

: SQL Server 2019 (15.x) and later versions.

: Global only.

Disables Microsoft Entra authentication for replication.

Note

: This trace flag applies to SQL Server 2022 (16.x) CU 6 and later versions.

: Global or session.

An

and the

background merge task

only clean up the deleted rows in

a columnstore index rowgroup when a certain threshold of rows has been deleted from that

rowgroup. The default threshold is 10 percent of the maximum row limit (1 million), or of 100,000

rows.

This trace flag changes the threshold to 10 percent of the total current rows in a columnstore

rowgroup. For example, if a rowgroup contains 20,000 rows, the threshold is 2,000 deleted rows

before this rowgroup is considered for cleanup. For more information, see

KB5000895

.

: SQL Server 2019 (15.x) CU 9 and later versions.

: Global only.

An

and the

background merge task

clean up the deleted rows in a

columnstore index rowgroup only when a certain threshold of rows has been deleted from that

rowgroup. The default threshold is 10 percent of the maximum row limit (1 million), or of 100,000

rows.

This trace flag changes the threshold to 1 percent of the total current rows in a columnstore

rowgroup. If enabled together with trace flag 11631, then it's 1 percent of the current number of

rows in a rowgroup, instead of 1 percent of 1 million rows. For more information, see

KB5000895

.

: SQL Server 2019 (15.x) CU 9 and later versions.

: Global only.

Enables you to add Microsoft Entra ID users via the

## syntax in the

statement.

Note

: Customers must validate Microsoft Entra ID users, because SQL Server doesn't perform this

validation. So, SQL Server doesn't require any

Microsoft Graph permissions

. For more information,

see

CREATE USER

.

: SQL Server 2022 (16.x) CU 20 and later versions.

#### Trace

#### flag

#### Scope

#### 12310

#### Applies to

#### Scope

#### 12324

#### Applies to

#### Scope

#### 12348

#### Applies to

#### Scope

#### 12481

#### Applies to

#### Scope

#### 12502

#### Applies to

#### Scope

#### 12618

#### Applies to

## Description

: Global only.

Increases the flow control limits for the number of messages that each availability group gate

allows. These limits are the new default values in SQL Server 2022 (16.x) and therefore the trace flag

has no effect in this version. For more information, see

Flow control gates

.

: SQL Server 2019 (15.x) CU 9, SQL Server 2017 (14.x) CU 18, SQL Server 2016 (13.x) SP 1

CU 16, and later versions.

: Global only.

Resolves an issue introduced with changes to the link feature for Azure SQL Managed Instance,

which prevents availability groups from synchronizing when replicas are running on different

cumulative updates. For more information, see

KB5024276

.

: SQL Server 2019 (15.x) CU 20 and later versions.

: Global only.

Disables the

asynchronous page request dispatching feature

that improves failover when

encountering undo-of-redo delays from network latency. Enabling the trace flag reverts the

mechanism to the default behavior.

: SQL Server 2025 (17.x)

: Global only.

Disables logging auditing information for external permissions in the

field of audit records. For more information, see

KB5022375

.

: SQL Server 2022 (16.x) CU 1 and later versions.

: Global only.

Disables external authorization policies for on-premises SQL Server instances.

: SQL Server 2022 (16.x) CU 5 and later versions.

: Global only.

Enables the automatic plan correction (APC) model of the automatic tuning feature to perform

multiple consecutive plan regression checks over the same plan, which allows for the accumulation

of additional statistics for evaluation by the new model. For more information, see

KB5026717

.

: SQL Server 2022 (16.x) CU 4 and later versions.

#### Trace

#### flag

#### Scope

#### 12656

#### Applies to

#### Scope

#### 13116

#### Applies to

#### Scope

#### 13127

#### Applies to

#### Scope

#### 13156

#### Scope

#### 13702

#### Applies to

#### Scope

#### 15005

#### Applies to

#### Scope

## Description

: Global only.

Enables the automatic plan correction (APC) model of the automatic tuning feature to use a time-

based plan regression check that occurs five minutes after a plan change is detected, which avoids

biasing the regression checks by queries that execute quickly. This allows APC to take into account

query executions that might run longer, or are prone to timing out because of a plan change. For

more information, see

KB5026717

.

: SQL Server 2022 (16.x) CU 4 and later versions.

: Global only.

Disables the fix for bug

13685819

. Use this trace flag if after you apply SQL Server 2016 (13.x)

Service Pack 2 CU 16, you encounter an issue in which DML (insert/update/delete) queries that use

parallel plans can't complete any execution and encounter HP_SPOOL_BARRIER waits.

: SQL Server 2016 (13.x) Service Pack 2 CU 16.

: Global only.

Enables additional string pattern matching optimizations.

: SQL Server 2019 (15.x) and later versions and is intended for high-end systems with

high performance workloads.

: Global or session.

Disables the fix for the "UDF invocation with a large number of scalar expression re-evaluations can

cause a non-yielding scheduler error" issue. This original fix might sometimes cause a performance

regression. For more information, see

KB4538581

.

: Global only.

Enables PolyBase capabilities for SQL Server on Linux. This trace flag also enables other trace flags

required to support the PolyBase feature.

: SQL Server 2022 (16.x) on Linux.

: Global only.

Enables a replication subscriber to use a nondefault port for transactional replication in an

availability group or other scenarios.

: SQL Server 2022 (16.x) CU 20 and later versions.

: Global only.

#### Trace

#### flag

#### 15025

#### Applies to

#### Scope

#### 15096

#### Applies to

#### Scope

#### 15097

#### Applies to

#### Scope

#### 15212

#### Applies to

#### Scope

#### 15608

#### Applies to

#### Scope

#### 15915

## Description

Disables the Azure Key Vault access that is required for a newly created Virtual Log File (VLF), which

allows high-volume customer workloads to continue without interruption. Once this trace flag is

enabled, SQL Server uses Extensible Key Management for encryption and key generation, and

doesn't contact Azure Key Vault during the creation of the VLF. For more information, see

FIX:

Database accessibility issues with high-volume customer workloads that use EKM for encryption

and key generation

.

: SQL Server 2019 (15.x) CU 19, SQL Server 2022 (16.x) CU 1, and later versions.

: Global only.

Disable population count (popcnt) operations with AVX-512 instruction sets.

: SQL Server 2022 (16.x) and later versions.

: Global or session.

Enables AVX-512 support for SQL Server 2022 (16.x) and later versions.

Important

: Enable AVX-512 support for the following CPUs:

- Intel Ice Lake and later

- AMD EYPC Genoa and later

: SQL Server 2022 (16.x) and later versions.

: Global or session.

Disables Service Broker timer messages that are acting as a verbose notification on the timeout

event. Messages affected with this trace flag are:

in Service Broker Dialog Cleanup sequence, and

in

Service Broker Dialog Close sequence. Once this trace flag is enabled, the print-out of these

informal messages is skipped.

: SQL Server 2022 (16.x) and later versions.

: Global only.

Disables

Persisted statistics for readable secondary replicas

feature. To fully disable the feature,

apply this trace flag to the primary replica and all secondary replicas.

: SQL Server 2025 (17.x) and later versions.

: Startup only.

Enables a fix for a performance issue that you might encounter when

is called frequently

from multiple connections, which could cause a memory leak. The memory isn't cleaned up until

#### Trace

#### flag

#### Applies to

#### Scope

#### 16268

#### Applies to

#### Scope

#### 16301

#### Applies to

#### Scope

#### 17600

#### Applies to

#### Scope

## Description

you restart the SQL Server service.

: SQL Server 2019 (15.x) CU 29 and later versions.

: Global only.

Disables automatic feedback behavior for cardinality estimation (CE) feedback when you use

REGEXP_LIKE

.

: SQL Server 2025 (17.x) and later versions.

: Global only.

Skips the blocking I/O operation in the

stored procedure. After you turn on

this trace flag, the

stored procedure limits I/O statistics collection, which

helps the availability group avoid restart and failover when there's a long delay in the I/O system.

: SQL Server 2019 (15.x) CU 26, SQL Server 2022 (16.x) CU 12, and later versions.

: Global only.

Changes the default driver version of the MSOLEDBSQL provider used by linked servers from v19 to

v18. This trace flag provides an alternative for environments that don't support the new

options of the OLE DB 19 driver. In SQL Server 2025 (17.x), MSOLEDBSQL is set to OLE DB v19.

Using this trace flag sets MSOLEDBSQL to OLE DB v18. For information, see

Release notes for the

Microsoft OLE DB Driver for SQL Server

.

: SQL Server 2025 (17.x) and later versions.

: Global or session.

Data types (Transact-SQL)

DBCC TRACEOFF (Transact-SQL)

DBCC TRACEON (Transact-SQL)

DBCC TRACESTATUS (Transact-SQL)

DBCC INPUTBUFFER (Transact-SQL)

DBCC OUTPUTBUFFER (Transact-SQL)

EXECUTE (Transact-SQL)

SELECT (Transact-SQL)

SET NOCOUNT (Transact-SQL)

Query hints (Transact-SQL)

Related content

SQL Server diagnostics detects unreported I/O problems due to stale reads or lost writes

ALTER DATABASE SET options (Transact-SQL)

ALTER DATABASE SCOPED CONFIGURATION (Transact-SQL)

Last updated on 04/20/2026

```sql
dbcc-traceon-trace-flags-transact-sql#tf1118
```

```sql
-T
```

```sql
<Distribution server>..msmerge_history
```

```sql
-T
```

```sql
SELECT
x
FROM
correlated
WHERE
f1 = 0
AND
f2 = 1
OPTION
(QUERYTRACEON 4199, QUERYTRACEON 4137);
```

```sql
DBCC
```

```sql
GetXpVersion()
```

```sql
INSERT
```

```sql
IDENTITY_CACHE
```

```sql
VERBOSE_TRUNCATION_WARNINGS
```

```sql
ALLOW_PAGE_LOCKS
```

```sql
ALTER INDEX...REORGANIZE
```

```sql
ALTER INDEX...REBUILD
```

```sql
TABLOCK
```

```sql
sp_tableoption
```

```sql
AUTOGROW_SINGLE_FILE
```

```sql
AUTOGROW_ALL_FILES
```

```sql
ALTER DATABASE
```

```sql
ALTER DATABASE
```

```sql
sp_configure
```

```sql
sp_configure
```

```sql
LOCK_ESCALATION
```

```sql
ALTER PARTITION FUNCTION
```

```sql
SYNCHRONIZED
```

```sql
SYNCHRONIZED
```

```sql
USE HINT 'FORCE_DEFAULT_CARDINALITY_ESTIMATION'
```

```sql
UPDATE
```

```sql
UPDATE
```

```sql
USE HINT 'DISABLE_OPTIMIZED_NESTED_LOOP'
```

```sql
REQUEST_MAX_CPU_TIME_SEC
```

```sql
ParameterRuntimeValue
```

```sql
sys.dm_exec_query_statistics_xml
```

```sql
sys.dm_exec_query_statistics_xml
```

```sql
FORCE_SHOWPLAN_RUNTIME_PARAMETER_COLLECTION
```

```sql
sys.dm_exec_query_plan_stats
```

```sql
INSERT INTO ... SELECT
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKFILEGROUP
```

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
DBCC
CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
TABLOCK
```

```sql
sp_configure
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
PHYSICAL_ONLY
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
tempdb
```

```sql
tempdb
```

```sql
tempdb
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
PHYSICAL_ONLY
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
DATA_PURITY
```

```sql
DBCC CHECKDB WITH DATA_PURITY
```

```sql
DBCC CHECKDB
```

```sql
DBCC
STACKDUMP
```

```sql
SQLDump<xxxx>.mdmp
```

```sql
SQLDmpr<xxxx>.mdmp
```

```sql
SQLDmpr<xxxx>.P<xxxxx.xxxxxxxx>.T<xxxxxxxxxxxxxx>.{<xxxxxxxx-xxxx-xxxx-
xxxx-xxxxxxxxxxxx>}.dmp
```

```sql
SQLDmpr0024.P26900.66D498FA.T20240117034050.{eec59a9e-
d615-4ac4-a46a-f650fee23787}.dmp
```

```sql
CHECKSUM
```

```sql
BACKUP
```

```sql
DUMP
```

```sql
BACKUP
```

```sql
tempdb
```

```sql
master
```

```sql
tempdb
```

```sql
model
```

```sql
tempdb
```

```sql
'******'
```

```sql
SPID = -2
```

```sql
OPTION(RECOMPILE)
```

```sql
WITH RECOMPILE
```

```sql
OPTIMIZE FOR <value>
```

```sql
PARAMETER_SNIFFING
```

```sql
OPTIMIZE FOR UNKNOWN
```

```sql
OPTIMIZE FOR UNKNOWN
```

```sql
USE HINT 'DISABLE_PARAMETER_SNIFFING'
```

```sql
USE HINT 'ASSUME_MIN_SELECTIVITY_FOR_FILTER_ESTIMATES'
```

```sql
TOP
```

```sql
OPTION (FAST <n>)
```

```sql
IN
```

```sql
EXISTS
```

```sql
USE HINT 'DISABLE_OPTIMIZER_ROWGOAL'
```

```sql
USE HINT 'ENABLE_HIST_AMENDMENT_FOR_ASC_KEYS'
```

```sql
QUERY_OPTIMIZER_HOTFIXES
```

```sql
USE HINT 'ENABLE_QUERY_OPTIMIZER_HOTFIXES'
```

```sql
QUERYTRACEON
```

```sql
CREATE CREDENTAIL WITH IDENTITY = 'Managed Identity'
```

```sql
CREATE CREDENTIAL
```

```sql
ALTER DATABASE <database_name> SET ENCRYPTION ON
```

```sql
NUMBER
```

```sql
SHUTDOWN WITH NOWAIT
```

```sql
SPINLOCK_EXT
```

```sql
SOS_BLOCKALLOCPARTIALLIST
```

```sql
DELETE
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
INSERT
```

```sql
DELETE
```

```sql
INSERT
```

```sql
safe_cleanup_version()
```

```sql
sys.sp_flush_commit_table_on_demand
```

```sql
m_versionStatus.IsVisible ()
```

```sql
FORCE ORDER
```

```sql
FORCESEEK
```

```sql
FORCESEEK
```

```sql
FORCE ORDER
```

```sql
KTM_RECOVERY_MANAGER
```

```sql
UPDATE
```

```sql
UPDATE
```

```sql
USE HINT
'EXPAND VIEWS'
```

```sql
BULK INSERT
```

```sql
BULK INSERT
```

```sql
tempdb
```

```sql
tempdb
```

```sql
USE HINT 'ASSUME_MIN_SELECTIVITY_FOR_FILTER_ESTIMATES'
```

```sql
USE HINT 'ASSUME_JOIN_PREDICATE_DEPENDS_ON_FILTERS'
```

```sql
LEGACY_CARDINALITY_ESTIMATION
```

```sql
USE HINT 'FORCE_LEGACY_CARDINALITY_ESTIMATION'
```

```sql
DBCC SHOW_STATISTICS
```

```sql
INSERT...SELECT
```

```sql
PREMPTIVE_OS_FINDFILE
```

```sql
PREEMPTIVE_OS_CREATEDIRECTORY
```

```sql
query wait (s)
```

```sql
REQUEST_MEMORY_GRANT_TIMEOUT_SEC
```

```sql
SELECT
```

```sql
INSERT
```

```sql
ALTER INDEX ... REORGANIZE
```

```sql
ALTER INDEX ... REORGANIZE
```

```sql
WITH SID = <sid>, TYPE = [E|X]
```

```sql
CREATE USER
```

```sql
external_policy_permission_checked
```

```sql
SSBDT: Dialog timer delete during registration
```

```sql
SSBDT: Dialog timer delete during dispatch
```

```sql
sp_lock
```

```sql
sp_server_diagnostics
```

```sql
sp_server_diagnostics
```

```sql
Encrypt
```
