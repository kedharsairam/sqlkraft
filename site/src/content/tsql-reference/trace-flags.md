---
name: "Trace flags"
title: "Trace flags"
category: "statements"
description: "The following table lists and describes the trace flags that are available in SQL Server."
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

The following table lists and describes the trace flags that are available in SQL Server.

supports the following global Trace flags: 460, 2301, 2389, 2390,

2453, 2467, 7471, 8207, 9389, 10316, and 11024. Session trace-flags aren't yet supported in SQL

Managed Instance.

Some trace flags were introduced in specific SQL Server versions. For more information on the

applicable version, see the Microsoft Support article associated with a specific trace flag.

Trace flag behavior might not be supported in future releases of SQL Server.

Тrace flags can be referenced directly in the table via a bookmark that you can add to the end of

the URL, using this format #tfNNNN. For example, to jump directly to trace flag 1118 in the table,

use.

## Description

Increases the verboseness of the merge replication agent logging.

Important

Replication Merge Agent

option

when executing

from the command prompt.

Warning

only for time-limited troubleshooting purposes.

Merge Agent.

: Replication Merge Agent only.

table.

Important

Replication Merge Agent

option

when executing

from the command prompt.

Warning

#### Trace

#### Scope

#### 139

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

only for time-limited troubleshooting purposes.

Merge Agent.

: Replication Merge Agent only.

DBCC CHECKDB

,

DBCC CHECKTABLE

and

DBCC CHECKCONSTRAINTS

has a lower compatibility level.

and Azure SQL Database

improvements in handling some data types and uncommon operations.

versions.

Warning

Server and Azure SQL Database improvements in handling some data types and uncommon

operations. It should be immediately disabled after validation checks are completed.

: Global only.

Increases the SQL Server Database Engine plan cache bucket count from 40,009 to 160,001 on 64-

bit systems.

KB3026083.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global only.

Addresses errors when rebuilding partitions online for tables that contain a computed partitioning

column.

KB3213683

and

KB4541096.

: Global or session.

Reports to the error log when a statistics-dependent stored procedure is being recompiled as a

result of autoupdate statistics.

KB195565.

Note

: This trace flag requires enabling

trace flag 3605.

: Global only.

Prints versioning information about extended stored procedure dynamic-link libraries (DLLs). For

Programming Database Engine extended stored

procedures.

: Global or session.

server restarts unexpectedly or fails over to a secondary server. Identity caching is used to improve

#### Trace

#### Scope

#### 460

#### Scope

#### 610

#### Scope

#### 634

#### Scope

## Description

performance on tables with identity columns.

Note

ALTER DATABASE SCOPED CONFIGURATION.

: Global only.

Replaces data truncation message ID

8152

with message ID

2628.

KB4468101.

ALTER DATABASE SCOPED CONFIGURATION.

versions.

Note

flag has no effect. For database compatibility level 140 or lower, message ID 2628 remains an opt-

in error message that requires trace flag 460 to be enabled, and this database scoped configuration

has no effect.

: Global or session.

Controls minimally logged inserts into indexed tables.

2016 (13.x), as minimal logging is turned on by default for indexed tables. In SQL Server

sequentially filling that new page are minimally logged if all the other prerequisites for minimal

logging are met.

order are still fully logged, as are rows that are moved as a result of page splits during the load.

page or extent allocations are logged.

Data Loading Performance Guide.

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

#### 652

#### Scope

#### 661

#### Scope

#### 692

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

process. When you disable this process, the deleted record isn't purged.

the deleted record consumes isn't freed.

performance of scan operations.

Ghost cleanup process guide.

: Global only.

Disables fast inserts while bulk loading data into heap or clustered index. Starting with SQL Server

bulk logged recovery model to optimize insert performance for records inserted into new pages.

existing extent with available free space to optimize insert performance.

With fast inserts, bulk loads with small batch sizes can lead to increased unused space consumed

by objects hence it's recommended to use large batchsize for each batch to fill the extent

completely.

reserved at the expense of performance.

: SQL Server 2016 (13.x) and later versions.

: Global or session.

Enables table lock for bulk load operations into a heap with no nonclustered indexes.

into a table.

same table, while preventing other processes that aren't bulk loading data from accessing the table.

The behavior is similar to when the user explicitly specifies

hint while performing bulk load,

table lock on bulk load is enabled for a given table.

this trace flag is enabled, this behavior becomes default without any query or database changes.

: Global or session.

Direct Write

hybrid buffer pool. This mode requires

that

persisted log buffer

is enabled in the same database as hybrid buffer pool.

Direct Write

allows

the hybrid buffer pool to serve as a cache for both dirty and clean pages, reducing the workload

demands on the DRAM buffer pools for OLAP and OLTP style workloads.

introduced in SQL Server 2022 (16.x) and the behavior is enabled by default in SQL Server 2022

(16.x) CU 1. If you're using SQL Server 2022 (16.x) CU 1 and later versions, the trace flag is ignored.

#### Trace

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

(LSN) value is compared to the recent write list.

specified during the write operation, a new error message is logged in the SQL Server error log. For

or lost writes.

Note

: Starting with SQL Server 2017 (14.x), this trace flag has no effect.

: Global only.

Disables detection and reporting of I/O requests that take a very long time to complete. By default

uses a mechanism to detect read and write I/O requests that take a long time (typically

longer than 15 seconds). This trace flag disables this detection.

MSSQLSERVER_833.

Note

: It isn't recommended that you enable this trace flag because you could decrease your ability

to detect I/O issues on the system.

: Global only.

Uses large-page allocations for all memory allocations within the SQL Server Operating System

(SQLOS) workspace.

from 2 MB to 16 MB.

the process.

efficiency of the translation look-aside buffer (TLB) in the CPU. In other words, trace flag 834

performed by the memory management hardware.

Before you enable trace flag 834, follow the recommendations for maximum server memory

Server memory configuration options.

Note

: Trace flag 834 applies only to 64-bit versions of SQL Server.

memory user right to turn on trace flag 834. You can turn on trace flag 834 only at startup. Trace

allocated. Therefore, trace flag 834 is best suited for servers that are dedicated to SQL Server.

Note

: When enabled, the large-page memory model preallocates all SQLOS memory at instance

startup and doesn't return that memory to the OS.

Warning

determine that it materially benefits your workload. Enabling this trace flag can substantially

increase the kernel CPU time and reduce performance. This occurs if memory becomes fragmented,

#### Trace

#### Scope

#### 836

#### Scope

#### 845

#### Scope

#### 876

#### Scope

#### 888

#### Scope

## Description

requiring SQL Server to call Windows APIs to allocate and deallocate memory instead of reusing

memory cached in the SQLOS workspace. Trace flag 834 can also cause unnecessary memory

consumption because the unused part of committed memory blocks isn't released to the operating

system.

Note

: If you're using columnstore indexes, don't enable trace flag 834.

Interoperability issues between batch mode processing and large page memory model.

trace flag 876

instead.

: Global only.

Use the max server memory option for the buffer pool.

total physical memory.

trace flag 836

are allocated at startup in 32-bit Address Windowing Extensions (AWE) mode.

Note

: Trace flag 836 applies only to 32-bit versions of SQL Server that have the AWE allocation

enabled. You can turn on trace flag 836 only at startup.

: Global only.

the Lock Pages in Memory privilege enabled.

KB970070

and

Server

Memory Server Configuration Options.

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

when PMEM devices run low on memory.

KB4548103.

: SQL Server 2019 (15.x) CU 4 and later versions.

: Global only.

#### Trace

#### 890

#### Scope

#### 898

#### Scope

#### 902

#### Scope

#### 1117

#### Scope

#### 1118

## Description

Suppress long buffer pool scan complete messages (

error 898

) in the error log.

Operations

that trigger a buffer pool scan may run slowly on large-memory computers.

: SQL Server 2017 (14.x) and later versions.

: Global only.

Direct Write

for troubleshooting or debugging

purposes.

KB5022375.

: SQL Server 2022 (16.x) CU 1 and later versions.

: Global only.

Bypasses execution of database upgrade script when installing a Cumulative Update or Service

Pack. If you encounter an error during script upgrade mode, it's recommended to contact Microsoft

SQL Customer Service and Support (CSS) for further guidance.

KB2163980.

Warning

: This trace flag is meant for troubleshooting of failed updates during script upgrade mode,

and it isn't supported to run it continuously in a production environment. Database upgrade scripts

need to execute successfully for a complete install of Cumulative Updates and Service Packs. Not

doing so can cause unexpected issues with your SQL Server instance.

: Global only.

When a file in the filegroup meets the autogrow threshold, all files in the filegroup grow.

flag affects all databases. It's recommended only if in every database it's safe to grow all files in a

filegroup by the same amount.

Note

and

, and trace flag 1117 has no effect.

ALTER DATABASE File and Filegroup Options.

: Global only.

SGAM page.

different extents (mixed extents). Afterwards, when more pages are needed, those are allocated

from that same extent (uniform extent).

can quickly become a bottleneck when numerous mixed page allocations are occurring.

to scan the SGAM page.

KB328551.

Note

: Starting with SQL Server 2016 (13.x) this behavior is controlled by the SET

, and trace flag 1118 has no effect.

#### Trace

#### Scope

#### 1204

#### Scope

#### 1211

#### Scope

#### 1222

#### Scope

#### 1224

## Description

ALTER DATABASE SET options.

: Global only.

## Returns the resources and types of locks participating in a deadlock and also the current command

affected. For more information about deadlocks, see the

Deadlocks guide.

Note

: Avoid using trace flag 1204 on workload-intensive systems causing deadlocks. For more

information about other means of detecting deadlocks, see the

Deadlocks guide.

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

, see

Resolve blocking problems caused by lock escalation in SQL Server.

: Global or session.

## Returns the resources and types of locks that are participating in a deadlock and also the current

command affected, in an XML format that doesn't comply with any XSD schema. For more

information about deadlocks, see the

Deadlocks guide.

Note

: Avoid using trace flag 1222 on workload-intensive systems causing deadlocks. For more

information about other means of detecting deadlocks, see the

Deadlocks guide.

: Global only.

Disables lock escalation based on the number of locks. However, memory pressure can still activate

lock escalation. The Database Engine escalates row or page locks to table (or partition) locks if the

amount of memory used by lock objects exceeds one of the following conditions:

- 40 percent of the memory that is used by Database Engine. This is applicable only when the

parameter of

is set to 0.

- 40 percent of the lock memory that is configured by using the

parameter of.

For more information, see

Server configuration options.

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

If both trace flags 1211 and 1224 are set, 1211 takes precedence over 1224.

trace flag 1224

instead. This helps avoid "out-of-locks" errors when many locks are being used.

Note

the

ALTER TABLE

statement.

Resolve blocking problems caused by lock escalation in SQL Server.

: Global or session.

Disables all lock partitioning regardless of the number of CPUs.

partitioning when a server has 16 or more CPUs, to improve the scalability characteristics of larger

systems.

Transaction Locking and Row

Versioning Guide.

Warning

: Trace flag 1229 can cause spinlock contention and poor performance.

: Global only.

Enables database lock partitioning.

KB2926217.

Note

: Starting with SQL Server 2012 (11.x) Service Pack 3 and SQL Server 2014 (12.x) Service Pack 1,

this behavior is controlled by the Database Engine and trace flag 1236 has no effect.

: Global only.

statement to honor the current user-defined session

deadlock priority instead of being the likely deadlock victim by default.

KB4025261.

Note

: Starting with SQL Server 2017 (14.x) and database

140 this is the default

behavior, and trace flag 1237 has no effect.

: Global or session or query (QUERYTRACEON).

Disable scheduler monitor dumps.

: Global only.

Enables the replication log reader to move forward even if the asynchronous secondaries haven't

acknowledged the reception of a change. Even with this trace flag enabled the log reader always

waits for the synchronous secondaries whose synchronization state is. The log reader

secondaries.

availability database, or a log reader instance. This trace flag must be enabled on the publisher

#### Trace

#### Scope

#### 1462

#### Scope

#### 1800

#### Scope

#### 1802

#### Scope

#### 1819

#### Scope

#### 2301

#### Scope

#### 2312

## Description

instance. It takes effect immediately without a restart.

or when an asynchronous secondary replica fails.

: Global only.

Disables log stream compression for asynchronous availability groups.

default on asynchronous availability groups in order to optimize network bandwidth.

Tune compression for availability group.

: Global only.

secondary replica log files, in SQL Server Always On and Log Shipping environments.

with sector size of 512 bytes.

larger than 4 KB.

KB3009974

,

Microsoft support policy for 4K sector

hard drives in Windows

Troubleshoot errors related to system disk sector size greater than 4

KB.

: SQL Server 2012 (11.x) Service Pack 1 CU 13, SQL Server 2012 (11.x) Service Pack 2 CU 3,

2014 (12.x) RTM CU 5, and later versions.

: Global only.

Disables ACL change and impersonated access verification during database attach or detach

operations. This can be useful when attaching a database and encountering access permission

errors, such as error 5120.

: Global only.

Allows

backup to URL

to use a proxy server when accessing Azure block blobs.

netsh.exe

Windows Vista, Windows Server 2008, and later versions.

: Global or session or query (QUERYTRACEON).

Enable advanced decision support optimizations that are specific to decision support queries. This

option applies to decision support processing of large data sets.

: Global or session or query (QUERYTRACEON).

Sets the Query Optimizer cardinality estimation model to SQL Server 2014 (12.x) and later versions,

irrespective of the compatibility level of the database.

Note

cardinality estimation model of SQL Server 2014 (12.x) (120).

Query hints.

#### Trace

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

instead of using this trace flag.

: Global or session or query (QUERYTRACEON).

max server memory server configuration

is set too high, and causes SQL

Server to generate an inefficient plan for a specific query. It doesn't limit the memory SQL Server

grants to execute the query. The memory configured for SQL Server is still used by data cache,

query execution, and other consumers.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

a table.

clustered index itself, but also all the nonclustered indexes because the nonclustered indexes

contain the cluster key.

then all nonclustered indexes at the same time.

next row until all is complete. This is called narrow plan update or also called Per-Row Update. In

some cases, the Database Engine can choose to do a wide plan update. This trace flag forces a

narrow plan update.

: Global or session or query (QUERYTRACEON).

generating a plan.

most likely not required, but still a possibility if the cardinality or cost estimates are incorrect. For

High CPU or memory grants may occur with queries that use optimized

nested loop or batch sort.

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Changes the fixed update statistics threshold to a linear update statistics threshold.

AUTO_UPDATE_STATISTICS Option.

Note

130 or above,

this behavior is controlled by the Database Engine and trace flag 2371 has no effect.

: Global only.

#### Trace

#### 2389

#### Scope

#### 2390

#### Scope

#### 2422

#### Scope

#### 2430

#### Scope

#### 2446

## Description

Enable automatically generated quick statistics for ascending keys (histogram amendment).

estimate cardinality is adjusted at query compile time.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 120 or above. Use

trace flag 4139

instead.

: Global or session or query (QUERYTRACEON).

Enable automatically generated quick statistics for ascending or unknown keys (histogram

amendment).

unknown, then the histogram used to estimate cardinality is adjusted at query compile time. For

Query hints.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 120 or above. Use

trace flag 4139

instead.

: Global or session or query (QUERYTRACEON).

Resource Governor

configuration is exceeded.

KB4038419.

: SQL Server 2016 (13.x) Service Pack 2, SQL Server 2017 (14.x) CU 3, and later versions.

: Global only.

Enables alternate lock class cleanup.

KB2754301.

: Global only.

when

DMV while troubleshooting long running queries.

: SQL Server 2017 (14.x) CU 31, SQL Server 2019 (15.x) CU 19, and SQL Server 2022 (16.x)

and later versions.

Warning

only for time-limited troubleshooting purposes.

not.

Note

#### Trace

#### Scope

#### 2451

#### Scope

#### 2453

#### Scope

#### 2467

#### Scope

#### 2469

#### Scope

#### 2528

## Description

ALTER DATABASE SCOPED

CONFIGURATION.

: Global only.

Enables the equivalent of the last actual execution plan in.

: SQL Server 2019 (15.x) and later versions.

Note

ALTER DATABASE SCOPED CONFIGURATION.

: Global only.

Allows a table variable to trigger recompile when enough number of rows are changed.

KB2952444.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Starting with SQL Server 2019 (15.x), this became

table variable deferred compilation

2453 has no effect.

: Global or session or query (QUERYTRACEON).

allocated threads.

Parallel Query Processing.

Server

configuration: max worker threads

for information on configuring the max worker threads server

option.

Note

used, or the default thread allocation policy is used instead. Using this trace flag, it isn't

recommended to execute queries specifying a DOP over the number of schedulers in a single node,

a single node.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global only.

into a partitioned columnstore index. For

KB3204769.

: Global or session or query (QUERYTRACEON).

,

, and.

By default, the degree of parallelism is automatically determined by the query processor. The

maximum degree of parallelism is configured just like that of parallel queries. For more information,

see

Server configuration: max degree of parallelism.

#### Trace

#### Scope

#### 2544

#### Scope

#### 2549

## Description

Note

: Parallel DBCC checks should typically be enabled (default). The query processor reevaluates

and automatically adjusts parallelism for each table or batch of tables checked by.

The typical use scenario is when a system administrator knows that server load might increase

before

order to increase concurrency with other user workload.

can cause it to take longer to complete.

Note

: If

option and parallelism is disabled, tables

might be locked for longer periods of time.

Note

: Starting with SQL Server 2014 (12.x) Service Pack 2, a MAXDOP option is available to override

for the DBCC statements.

: Global or session.

Causes a memory dump of SQL Server to become a full dump (default is mini dump).

are a complete copy of the active target process memory.

process allocated memory, and all loaded modules.

system RAM. On large servers dedicated to a single SQL Server instance, it could mean a file that's

several hundreds of gigabytes or more.

Warning

: Generating a full memory dump can suspend the SQL Server process for an extended

period of time (several seconds to several minutes) and can generate a very large dump file. Use

this with caution and only rarely if the situation requires it.

Use the Sqldumper.exe tool to generate a dump file in SQL

Server.

: Global only.

treating different physical files as one logical file.

pages to read per unique disk drive across all database files.

drives based on the drive letter of the physical file name of each file.

Note

: Don't use this trace flag unless you know that each file is based on a unique physical disk.

Note

performance. While this trace flag improves disk I/O resources usage, the underlying performance

command.

KB2634571.

#### Trace

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

and Log Pool memory).

retaining most of its usefulness as preferred option in most situations where mini dumps aren't

sufficient..

: Global only.

database.

command tries to minimize

number of indexes or "facts" that it generates by using a "batches" concept.

forces all processing into one batch.

might increase.

command.

Note

performance. While this trace flag improves disk I/O resources usage, the underlying performance

command.

KB2634571.

: Global or session.

specified.

Note

: Column-value integrity checks are enabled by default and don't require the DATA_PURITY

option. For databases upgraded from earlier versions of SQL Server, column-value checks aren't

least once. After this,

checks column-value integrity by default. For more information,

KB945770.

: Global only.

Debugging Tools for Windows

are installed. For

example, using trace flag 3656 requires that trace flag 2592 is enabled.

Warning

: This is a debugging trace flag and not meant for production environment use.

#### Trace

#### Scope

#### 2610

#### Scope

#### 2616

#### Scope

#### 3015

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

SQLDumper

and via.

Use the Sqldumper.exe utility to generate a dump file in SQL

Server.

: SQL Server 2022 (16.x) CU 8, SQL Server 2019 (15.x) CU 23, and later versions.

: Global and session.

Sqldumper.exe

generate a single dump per unique

repeats frequently within one hour.

or

to

(for example,

).

: SQL Server 2022 (16.x) CU 12 and later versions.

: Global only.

Disables

writing backups to Azure immutable storage.

: SQL Server 2025 (17.x) and later versions.

: Global only.

Enables

command.

Note

configuration option.

backup checksum default

and

Server configuration options.

: Global and session.

only as needed to reach its final size.

allocating only the actual size required for the compressed backup.

cause a slight performance penalty (a possible increase in the duration of the backup operation).

Backup compression (SQL Server).

: Global only.

#### Trace

#### 3051

#### Scope

#### 3205

#### Scope

#### 3226

#### Scope

#### 3261

#### Scope

#### 3262

#### Scope

#### 3427

#### Scope

#### 3428

## Description

Enables SQL Server Backup to URL logging for page blobs in Azure Storage only.

a specific error log file.

Troubleshooting.

: Global only.

or

statement

uses it. With this trace flag, you can disable hardware compression for tape drivers. This is useful

when you want to exchange tapes with other sites or tape drives that don't support compression.

: Global or session.

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

KB3216543.

: SQL Server 2016 (13.x) Service Pack 1 CU 2 through SQL Server 2016 (13.x) Service Pack

2 CU 2.

trace flag has no effect.

: Global only.

The Always On Redo Thread on a secondary replica can sometimes be blocked by T-SQL queries,

which can cause delays in synchronization.

setting their lock timeout to 60 seconds.

Redo

#### Trace

#### Scope

#### 3459

#### Scope

#### 3468

#### Scope

#### 3502

#### Scope

#### 3605

#### Scope

#### 3608

#### Scope

## Description

thread falls behind due to resource contention

and

Troubleshooting REDO queue build-up (data

latency issues) on Always On Readable Secondary Replicas.

Warning

: Be sure that you test and understand this option before deploying it in a production

environment as queries might be terminated.

: SQL Server 2019 (15.x)

: Global only.

Disables parallel redo.

KB3200975

,

KB4101554

and this blog post,

Availability group secondary replica redo model and performance.

: SQL Server 2016 (13.x), SQL Server 2017 (14.x), and later versions.

: Global only.

Disables

indirect checkpoints

on.

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

database. If activities that require

is

created. Other databases are started and recovered when accessed.

snapshot isolation and read committed snapshot, might not work.

Move system databases

and

Move user databases.

Note

: Don't use during normal operation.

: Global only.

#### Trace

#### 3625

#### sysadmin

#### Scope

#### 3656

#### Scope

#### 3880

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

fixed server role, by masking the parameters of some error messages using.

This can help prevent disclosure of sensitive information.

: Global only.

Enables symbol resolution on stack dumps when the Debugging Tools for Windows are installed.

Warning

: This is a debugging trace flag and not meant for production environment use.

Note

: Starting with SQL Server 2019 (15.x),

trace flag 2592

enable symbol resolution.

: Global and session.

Disable the timer task that checks the state of a resumable index.

high performance workloads.

: Global or session.

some third party transaction monitors.

KB4519668

and

KB4511816.

: Global only.

Disables concurrent Page Free Space (PFS) updates feature. For more information on concurrent

Intelligent Performance. For an issue where this trace flag is useful see Non-

yielding scheduler dumps during the recovery of a secondary availability database with a database

snapshot

KB5007794.

: Global only.

Disables automatic execution of stored procedures when SQL Server starts. For more information

sp_procoption.

: Global only.

Fixes an error that occurs when you apply a security policy on PolyBase external table and use Row-

Level Security (RLS) in SQL Server 2019 (15.x). The error message resembles the following text:

KB4552159.

: Global or session.

#### Trace

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

is

used.

KB980653.

ALTER DATABASE SCOPED CONFIGURATION.

query hint. The

hint

intended result.

flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session.

Causes SQL Server to generate a plan using minimum selectivity when estimating AND predicates

for filters to account for partial correlation instead of independence, under the query optimizer

cardinality estimation (CE) model of SQL Server 2012 (11.x) and earlier (70). For more information,

see

KB2658214.

when using the CE 70.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 120 or above. Use

trace flag 9471

instead.

: Global or session or query (QUERYTRACEON).

contain

,

,

keywords.

KB2667211.

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Enable automatically generated quick statistics (histogram amendment) regardless of key column

status. If trace flag 4139 is set, regardless of the leading statistics column status (ascending,

descending, or stationary), the histogram used to estimate cardinality is adjusted at query compile

time.

KB2952101.

#### Trace

#### Scope

#### 4199

#### QO changes from all previous database compatibility levels

#### QO changes for DE version post-RTM

#### Scope

#### 4610

#### Scope

## Description

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 70. Use trace flags 2389 and 2390 instead.

: Global or session or query (QUERYTRACEON).

Enables Query Optimizer (QO) fixes released in SQL Server Cumulative Updates and Service Packs.

latest database

enabled.

KB974006.

:

- If trace flag 4199 is enabled, query optimizer changes from all previous database compatibility

levels are also enabled.

compatibility level 130. For compatibility levels below 130, query optimizer changes are disabled.

:

- If trace flag 4199 is enabled, query optimizer changes are enabled for the Database Engine

version post-RTM.

- If trace flag 4199 is disabled or not set, query optimizer changes are disabled for the Database

Engine version post-RTM.

ALTER DATABASE SCOPED CONFIGURATION.

instead of using this trace flag.

Important

: Query Optimizer fixes that address wrong results or access violation errors aren't

enabled by trace flag 4199. Those fixes aren't considered optional and become enabled by default

once the update package is installed.

: Global or session or query (

).

Increases the size of the hash table that stores the cache entries by a factor of 8.

store to 8,192. For more information on troubleshooting TokenAndPermUserStore cache size issues,

see

Queries take longer to finish when the size of the TokenAndPermUserStore cache grows in SQL

Server.

: Global only.

#### Trace

#### 4616

#### Scope

#### 4618

#### Scope

#### 4621

#### Scope

#### 4631

#### Scope

#### 4675

#### Scope

## Description

Makes server-level metadata visible to application roles. In SQL Server, an application role can't

access metadata outside its own database because application roles aren't associated with a server-

level principal. This is a change of behavior from earlier versions of SQL Server. Setting this global

flag disables the new restrictions, and allows for application roles to access server-level metadata.

: Global only.

Limits the number of entries in the TokenAndPermUserStore cache store to 1,024.

TokenAndPermUserStore cache store to 8,192. For more information on troubleshooting

TokenAndPermUserStore cache grows in SQL Server.

: Global only.

the user in a registry key.

access check cache Server Configuration

Options.

: Global only.

Disables SHA2_256/AES256 for hashing passwords that generate encryption keys. Starting in SQL

Server 2017 (14.x), SHA2 is used instead of SHA1.

have your SQL Server 2017 (14.x) installation decrypt items that were encrypted by SQL Server 2016

Create identical symmetric keys on two servers.

KB4053407.

: SQL Server 2017 (14.x) and later versions.

: Global only.

create credential for managed identity

on a SQL Server on Azure VM if Microsoft

Entra authentication is enabled.

statement. The

trace flag provides information about the primary managed identity and its setting for SQL Server

on Azure VM.

Note

message is issued if the primary managed identity isn't set for the server.

scenario, the credential must be deleted and recreated again once the trace flag is enabled.

Warning

only for time-limited troubleshooting sessions.

: Global or session.

#### Trace

#### 5004

#### Scope

#### 6408

#### Scope

#### 6498

#### Scope

#### 6527

#### Scope

#### 6531

## Description

Pauses TDE encryption scan and causes encryption scan worker to exit without doing any work. The

database continues to be in encrypting state (encryption in progress). To resume re-encryption

scan, disable trace flag 5004 and run.

: Global only.

Enables visibility of the estimated execution plan to see the remote query plan of PolyBase

pushdown computation.

: SQL Server 2019 (15.x) and later versions.

external pushdown occurred.

: Global or session or query (QUERYTRACEON).

Enables more than one large query compilation to gain access to the large gateway when there's

sufficient memory available. This trace flag can be used to keep memory usage for the compilation

of incoming queries under control, avoiding compilation waits for concurrent large queries. It's

compilation per 25 GB of memory.

KB3024815.

Note

: Starting with SQL Server 2014 (12.x) Service Pack 2 and SQL Server 2016 (13.x), this behavior

is controlled by the Database Engine and trace flag 6498 has no effect.

: Global only.

CLR integration.

an out-of-memory exception in the CLR. The behavior of the trace flag is as follows:

- If this is used as a startup trace flag, a memory dump is never generated. However, a memory

dump might be generated if other trace flags are used.

- If this trace flag is enabled on a running server, a memory dump isn't automatically generated

from that point on. However, if a memory dump has already been generated due to an out-of-

memory exception in the CLR, this trace flag has no effect.

: Global only.

Disables preemptive scheduling protection for query operations with spatial data types.

reduce the CPU consumption and improve the overall performance for some spatial activities. For

KB3005300.

Note

less than ~4ms and result in frequent non-yielding scheduler errors.

versions.

#### Trace

#### Scope

#### 6532

#### Scope

#### 6533

#### Scope

#### 6534

#### Scope

#### 6545

#### Scope

#### 6559

#### Scope

#### 7117

## Description

: Global and session.

Enables performance improvement of query operations with spatial data types in SQL Server 2012

(11.x) and SQL Server 2014 (12.x).

types of queries, and the objects.

KB3107399.

Note

trace flag 6532 has no effect.

: Global and session.

Enables performance improvement of query operations with spatial data types in SQL Server 2012

(11.x) and SQL Server 2014 (12.x).

types of queries, and the objects.

KB3107399.

Note

trace flag 6533 has no effect.

: Global and session.

Enables performance improvement of query operations with spatial data types beginning with SQL

Server 2012 (11.x).

queries, and the objects.

KB3107399.

: Global only.

Enables CLR strict security.

KB4018930.

: SQL Server 2012 (11.x) Service Pack 3 CU 10, SQL Server 2014 (12.x) Service Pack 2 CU 6,

2016 (13.x) RTM CU 7, SQL Server 2016 (13.x) Service Pack 1 CU 4, and later versions.

effect.

: Global only.

Enables fix that changes default CLR threading model logic.

KB4517771.

: SQL Server 2016 (13.x) Service Pack 2 CU 10, SQL Server 2017 (14.x) CU 18, SQL Server

2019 (15.x) CU 1, and later versions.

: Global only.

Mitigates an assertion failure that you might encounter when you have multiple nested inserts. This

for a row that might have been part of an aborted transaction. This trace flag allows the PVS

cleaner to ignore the bit and continue the cleaning operation.

#### Trace

#### Scope

#### 7314

#### Scope

#### 7412

#### Scope

#### 7470

#### Scope

#### 7471

#### Scope

#### 7745

#### Scope

#### 7752

## Description

: SQL Server 2022 (16.x) CU 9 and later versions.

: Global only.

Forces

values with unknown precision/scale to be treated as double values with OLE DB

provider.

KB3051993.

: Global and session.

Enables the lightweight query execution statistics profiling infrastructure.

KB3170113.

: SQL Server 2016 (13.x) Service Pack 1 and later versions. Starting with SQL Server 2019

(15.x), this trace flag has no effect because lightweight profiling is enabled by default.

: Global only.

Enables additional computations for memory grants required for sort operations.

KB3088480.

: SQL Server 2012 (11.x) Service Pack 2 CU 8, SQL Server 2014 (12.x) RTM CU 10, SQL

Server 2014 (12.x) Service Pack 1 CU 3, and later versions.

Warning

might affect memory availability for other concurrent queries.

: Global or session or query (QUERYTRACEON).

Enables running multiple

UPDATE STATISTICS

for different statistics on a single table concurrently.

KB3156157.

: SQL Server 2014 (12.x) Service Pack 1 and later versions.

: Global only.

Forces Query Store to not flush data to disk on database shutdown.

Note

the server shuts down. For a SQL Server shutdown, the command

used instead of this trace flag to force an immediate shutdown.

Enables asynchronous load of Query Store.

: Use this trace flag if SQL Server is experiencing high number of QDS_LOADDB waits related

to Query Store synchronous load (default behavior during database recovery).

## Description

Note

trace flag 7752 has no effect.

: Global only.

Enables a dedicated administrator connection (DAC) on SQL Server Express. By default, no DAC

resources are reserved on SQL Server Express.

database administrators.

: Global only.

Enables soft processor affinity on SQL Server on Linux. By default, schedulers are bound to specific

CPUs defined in the affinity mask. With this trace flag enabled, schedulers can move across CPUs,

(cgroup) v2 constraints.

Control group (cgroup) v2 support.

: Global only.

Disable the ring buffer for Resource Monitor.

buffer to diagnose out-of-memory conditions. Therefore, if you use this trace flag, the information

that's available to diagnose performance and functional problems with SQL Server is greatly

reduced. Trace flag 8011 always applies across the server and has global scope.

trace flag 8011 at startup or in a user session.

: Global only.

Disable the ring buffer for schedulers.

time that one of the following events occurs:

- A scheduler switches context to another worker

- A worker is suspended

- A worker is resumed

- A worker enters the preemptive mode or the non-preemptive mode.

You can use the diagnostic information in this ring buffer to analyze scheduling problems. For

example, you can use the information in this ring buffer to troubleshoot problems when SQL Server

stops responding. Trace flag 8012 disables recording of events for schedulers.

flag 8012 only at startup.

Warning

: When you use this trace flag, the information that's available for you to diagnose

performance and functional problems with SQL Server is greatly reduced.

: Global only.

Disable autodetection and NUMA setup.

KB2813214.

#### Trace

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

Disable the exception ring buffer.

raised on a node.

trace. A record is added to the ring buffer when an exception is raised.

creation of the ring buffer, and no exception information is recorded.

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

set memory from consideration when SQL Server interprets the global memory state signals.

use this trace flag incorrectly, heavy paging might occur, and the performance might be poor.

Therefore, contact Microsoft Support before you turn on trace flag 8020.

8020 only at startup.

: Global only.

clears a dump trigger after generating the dump once.

trace flag 2544, the option indicating the largest memory dump is honored. For more information,

see

Filtered dumps.

: Global only.

Reverts the cache limit parameters to the SQL Server 2005 (9.x) setting, which in general allows

caches to be larger.

optimize for ad hoc workloads Server Configuration Option

problem with plan cache.

Warning

: Trace flag 8032 can cause poor performance if large caches make less memory available

for other memory consumers, such as the buffer pool.

: Global only.

Converts NUMA partitioned memory objects into CPU partitioned.

KB2809338.

#### Trace

#### Scope

#### 8075

#### Scope

#### 8079

#### Scope

#### 8086

#### Scope

#### 8089

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

Server 2012 (11.x) or SQL Server 2014 (12.x).

KB3074434.

: SQL Server 2012 (11.x), SQL Server 2014 (12.x) RTM CU 10, and SQL Server 2014 (12.x)

Service Pack 1 CU 3.

Database Engine and trace flag 8075 has no effect.

: Global only.

Allows SQL Server 2014 (12.x) Service Pack 2 to interrogate the hardware layout and automatically

configure Soft-NUMA on systems reporting 8 or more CPUs per NUMA node. The automatic Soft-

NUMA behavior is simultaneous multithreading (SMT/logical processor) aware. The partitioning

listeners, scaling, and network and encryption capabilities.

: SQL Server 2014 (12.x) Service Pack 2. Starting with SQL Server 2016 (13.x), this behavior

is controlled by the Database Engine and trace flag 8079 has no effect.

: Global only.

Disable NUMA locality check for memory commits.

: SQL Server 2019 (15.x) and later versions.

: Global.

In SQL Server 2017 (14.x) CU 16, you can enable the bitmap filtering for reducing the size of filtered

memory dumps. SQL Server allocates a bitmap that keeps track of memory pages to be excluded

from a filtered dump.

read any other memory manager metadata.

: SQL Server 2017 (14.x) CU 16 through CU 19 only. Starting with SQL Server 2017 (14.x)

CU 20 the bitmap filtering is enabled by default.

turned on. The bitmap filtering can be disabled via trace flag 8095.

KB4488943.

: Global only.

Disables the bitmap filtering for filtered memory dumps.

track of memory pages to be excluded from a filtered dump.

filters out pages without the need to read any other memory manager metadata.

applies to builds where bitmap filtering is enabled by default.

#### Trace

#### Scope

#### 8099

#### Scope

#### 8101

#### Scope

#### 8102

#### Scope

#### 8121

## Description

versions, and SQL Server 2019 (15.x).

: Global only.

concurrent users.

: SQL Server 2019 (15.x) CU 2 and CU 3 only. Starting with SQL Server 2019 (15.x) CU 4,

this behavior is enabled by default.

8101

KB4538688.

: SQL Server 2019 (15.x)

: Global only.

number of CPUs and a high number of concurrent users.

Diagnose and resolve spinlock contention on SQL Server

whitepaper.

CU 14 and CU 16.

KB4538688.

: SQL Server 2019 (15.x)

: Global only.

Addresses a high-CPU scenario caused by spinlock contention on the XVB_LIST spinlock.

observe this most commonly on high-end systems with a large number of newer generation

processors (CPUs). This trace flag can be enabled together with trace flag 8101.

8101 changes the spin increment, trace flag 8102 staggers the spinlock backoffs.

Diagnose and resolve spinlock contention on SQL Server.

: SQL Server 2019 (15.x).

: Global only.

maximum server memory under the memory model with the Lock Pages In Memory security policy

setting.

to reduce SQL Server memory consumption.

KB5008996.

: SQL Server 2019 (15.x).

enabled by default and this trace flag has no effect.

#### Trace

#### Scope

#### 8134

#### Scope

#### 8142

#### Scope

#### 8145

#### Scope

#### 8207

#### Scope

#### 8239

## Description

revert to the older behavior, you can use trace flag 8125. However, in most cases this choice isn't

recommended.

: Global only.

wait type.

flag when troubleshooting high CPU utilization, to confirm or rule out a

spinlock contention

problem.

SPINLOCK_EXT.

: SQL Server 2025 (17.x).

: Global only.

This trace flag partitions the specific spinlock-protected list by CPU, up to 64 partitions. This should

be used only on large-memory machines experiencing

spinlock

contention with elevated CPU utilization.

trace flag 8145.

KB5025808.

: SQL Server 2019 (15.x) CU 21 and later versions.

: Global only.

trace flag 8142

CPU. You must also enable

trace flag 8142

for this setting to take effect.

KB5025808.

: SQL Server 2019 (15.x) CU 21 and later versions.

: Global only.

Enables singleton updates for Transactional Replication and CDC.

replicated as a

and

pair.

trigger. With trace flag 8207, an update to a unique column that affects only one row (a

and not as a

or

pair. If the update

update is still replicated as a

or

pair. For more information, see an archived version

of

KB302341.

: Global only.

By default,

sys.sp_flush_commit_table_on_demand

computes a minimum of hardened cleanup

version and safe cleanup version, and proceeds with data deletion from the commit table. When

trace flag 8239 is set, a

cleanup runs after rerunning.

can lead to data corruption.

Troubleshoot change tracking auto cleanup

issues.

#### Trace

#### Scope

#### 8273

#### Scope

#### 8284

#### Scope

#### 8285

#### Scope

#### 8286

#### Scope

#### 8287

#### Scope

#### 8290

#### Scope

## Description

: SQL Server 2022 (16.x) CU 3 and later versions.

: Global only.

Enabling trace flag 8273 disables

adaptive shallow cleanup for change tracking.

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

has snapshot isolation turned on.

: SQL Server 2022 (16.x) CU 6, SQL Server 2019 (15.x) CU 21, and later versions.

: Global only.

hint to improve performance.

trace flag 8287

hint.

KB5022375.

: SQL Server 2019 (15.x) CU 19, SQL Server 2022 (16.x) CU 1, and later versions.

: Global only.

hint to improve performance.

trace flag 8286

hint.

KB5022375.

: SQL Server 2019 (15.x) CU 19, SQL Server 2022 (16.x) CU 1, and later versions.

: Global only.

After this trace flag is enabled, the change tracking (CT) auto cleanup process resets any invalid

cleanup version to a cleanup version based on the retention period. After you enable this trace flag,

you must let the auto cleanup process run.

KB4538365.

later versions.

: Global or session.

#### Trace

#### 8531

#### Scope

#### 8558

#### Scope

#### 8721

#### Scope

#### 8744

#### Scope

#### 8790

#### Scope

#### 8902

#### Scope

## Description

encounter when running XA distributed transactions.

: SQL Server 2019 (15.x) CU 29, SQL Server 2022 (16.x) CU 16, and later versions.

: Global and startup only.

enabled then a transaction sometimes can't see the latest data from the tables that were modified

using DTC transactions even after xa_commit returned success for a short duration of time.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: SQL Server 2019 (15.x) CU 18, SQL Server 2022 (16.x), and later versions.

: Global only.

Reports to the error log when autoupdate statistics executes. For more information, see an archived

KB195565.

Note

: This trace flag requires enabling

trace flag 3605.

: Global only.

Nested Loops

operator.

Warning

: Incorrect use of this trace flag might cause extra physical reads when SQL Server executes

plans that contain the Nested Loops operator.

: Global and session.

statement to update

indexes in a table.

against a clustered index column, SQL Server updates

not only the clustered index itself, but also all the nonclustered indexes because the nonclustered

indexes contain the cluster index key. To optimize performance and reduce random I/O SQL Server

order.

flag.

: Global, session, or query (QUERYTRACEON).

Disable locked pages for IO operations for high-end systems with high performance workloads.

: SQL Server 2019 (15.x) and later versions.

: Global.

#### Trace

#### 8904

#### Scope

#### 9024

#### Scope

#### 9109

#### Scope

#### 9135

#### Scope

#### 9347

#### Scope

#### 9348

#### Scope

#### 9349

## Description

Enables a fix to address a parallel redo failure on a secondary replica by disabling inlined log IO,

limiting the contention possibility from many workers to the subset of background LogWriter

workers.

KB5004649

and

Trace flag 8904 - Disable Inline Database Log

Flushes.

: SQL Server 2019 (15.x) only, starting with CU 12.

: Global only.

Converts a global log pool memory object into NUMA node partitioned memory object.

KB2809338.

Note

: Starting with SQL Server 2012 (11.x) Service Pack 3 and SQL Server 2014 (12.x) Service Pack 1,

this behavior is controlled by the Database Engine and trace flag 9024 has no effect.

: Global only.

Disables start of Query Notification functionality.

Restore or recovery

may fail or take a long time if query notification is used in a database.

Warning

: Use caution with this trace flag. This trace flag can be useful in a limited set of scenarios

primarily for troubleshooting or isolating a problem.

: Global and session.

Prevents the usage of indexed views.

query hint instead of using this trace flag.

Table Hints.

: SQL Server 2019 (15.x) CU 23, SQL Server 2022 (16.x) CU 19, and later versions.

: Global only.

Disables batch mode for sort operator.

operator that boosts performance for many analytical queries.

KB3172787.

: Global or session or query (QUERYTRACEON).

Enables the use of Query Optimizer cardinality estimates to decide whether BULK INSERT for a

clustered columnstore index should be initiated or not.

less than 102,400, the Database Engine doesn't use.

estimated, a

is initiated.

KB2998301.

: Global or session or query (QUERYTRACEON).

Disables batch mode for top N sort operator.

top sort operator that boosts performance for many analytical queries.

#### Trace

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

#### Scope

## Description

: Global or session or query (QUERYTRACEON).

Disables batch mode for sort operator.

KB3171555.

Note

has no effect.

: Global or session or query (QUERYTRACEON).

Enables additional dynamic memory grant for batch mode operators.

performance.

if additional memory is available.

Memory Management

Architecture Guide.

: Global or session.

Disables

Adaptive Join

operator that enables the choice of a

method

to be deferred until after the first input has been scanned, as introduced in SQL Server 2017 (14.x).

KB4099126.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Enables a non-default fix for a query that uses a hash aggregate operator and spills.

trace flag increases the available memory for distinct hash operations.

KB3167159.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

2112485

2636294.

legacy Cardinality Estimation (CE) model.

foreign key joins).

the overestimation limit that exists in the legacy CE for this scenario.

Note

: This trace flag only applies to databases with a compatibility level of 160 and lower.

: SQL Server 2019 (15.x) CU 20, SQL Server 2022 (16.x) CU 9, and later versions.

: Global or session or query (QUERYTRACEON).

#### Trace

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

Disables batch mode execution.

KB4016902.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

query optimizer cardinality estimation model of SQL Server 2014 (12.x) and later versions.

flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

Note

: This trace flag doesn't apply to CE version 70. Use

trace flag 4137

instead.

: Global or session or query (QUERYTRACEON).

2014 (12.x) and later versions.

Join containment assumption

in the New Cardinality Estimator degrades query performance.

instead of using this trace flag.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Sets the Query Optimizer cardinality estimation (CE) model to SQL Server 2012 (11.x) and earlier

(version 70), irrespective of the compatibility level of the database.

Query

hints.

ALTER DATABASE SCOPED CONFIGURATION.

instead of using this trace flag.

: Global or session or query (QUERYTRACEON).

Disables SELECT permission for.

KB2683304.

: Global only.

#### Trace

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

## Description

default under the Query Optimizer cardinality estimation model of SQL Server 2008 R2 (10.50.x)

and earlier), when using the Query Optimizer cardinality estimation model of SQL Server 2012 (11.x)

and later versions.

: Global or session or query (QUERYTRACEON).

temporary tables.

KB3180087.

: Global or session.

Enables compression of the data stream for Always On Availability Groups during automatic

seeding.

increases the load on the processor.

Use automatic seeding to initialize

and

Tune compression for availability group.

: Global or session.

Disables Availability Groups Auto seeding to the default database path.

Disk layout.

: Global or session.

Disables the enhanced error collection for Availability Group failovers introduced in SQL Server

2016 (13.x) Service Pack 1 CU 10, SQL Server 2016 (13.x) Service Pack 2 CU 2, and SQL Server 2017

(14.x) CU 9.

Availability Groups – Enhanced Database Level

Failover.

: Global only.

Disables log block compression in Always On Availability Groups.

default behavior used with both synchronous and asynchronous replicas in SQL Server 2012 (11.x)

and SQL Server 2014 (12.x). In SQL Server 2016 (13.x), compression is only used with asynchronous

replica.

: Global or session.

Enables log stream compression for synchronous availability groups.

default on synchronous availability groups because compression adds latency.

Tune compression for availability group.

: Global or session.

Enables collection of event publishing metrics for extended event sessions. For more information,

see

sys.dm_xe_session_events.

: SQL Server 2022 (16.x) and later versions.

#### Trace

#### Scope

#### 9714

#### Scope

#### 9810

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

engine to reclaim TLS memory, and to reduce the possibility of out-of-memory issues.

flag reverts to the behavior before SQL Server 2022 (16.x).

: SQL Server 2022 (16.x) and later versions.

: Global only.

Changes the memory partitioning scheme for the In-Memory OLTP engine from per-CPU to per-

NUMA node.

restarted or when a database is brought online.

Memory fragmentation

: Global only.

Reduces the In-Memory checkpoint files to 1 MB each.

KB3147012.

: Global only.

Enables parallel plans and parallel scan of memory-optimized tables and table variables in DML

target of the DML operation in SQL Server 2016 (13.x).

KB4013877.

Note

: Trace flag 9939 isn't needed if trace flag 4199 is also explicitly enabled.

: Global or session or query (QUERYTRACEON).

or

wait types might be observed.

KB4090789

and

KB4052338.

versions.

: Global only.

#### Trace

#### 9953

#### Scope

#### 10054

#### Scope

#### 10204

#### Scope

#### 10207

#### Scope

#### 10316

#### Scope

#### 10460

## Description

Reuses the hidden schedulers used by the Memory Optimized tables.

later versions.

: Global only.

outer joins.

: SQL Server 2019 (15.x) and later versions.

Note

: Ensure that you thoroughly test this option, before rolling it into a production environment.

: Global or session or query (QUERYTRACEON).

Disables merge/recompress during columnstore index reorganization. In SQL Server 2016 (13.x),

rowgroups that have a large number of deleted rows.

Note

: Trace flag 10204 doesn't apply to columnstore indexes that are created on memory-

optimized tables.

: Global or session.

retrieval from a corrupt CCI.

KB3067257.

: Global or session.

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

#### Scope

#### 11023

#### Scope

#### 11024

#### Scope

#### 11047

#### Scope

#### 11064

#### Scope

#### 11068

## Description

and later versions.

Starting with SQL Server 2017 (14.x) CU 31, SQL Server 2019 (15.x) CU 18, and SQL Server 2022

Standard service tier (S3).

: Global only.

Disables the use of the last persisted sample rate for all subsequent statistics update, where a

UPDATE STATISTICS

statement.

KB4039284.

: Global only.

Enables triggering the auto update of statistics when the modification count of any partition

threshold.

KB4041811.

: SQL Server 2016 (13.x) Service Pack 2, SQL Server 2017 (14.x) CU 3, and later versions.

: Global only.

or the Resource Governor

configuration to columnstore index build operations.

KB4480641.

versions.

: Global only.

Improves the scalability of data loading operations into columnstore indexes, by optimizing

and

statements. For more information on loading

Columnstore indexes - data loading guidance.

: SQL Server 2019 (15.x) and later versions.

: Global only.

for columnstore index insert operations. For more information on overriding degrees of parallelism,

Query Processing Architecture Guide.

Important

: This trace flag is only effective if trace flag 11064 is also enabled.

Important

: Use this trace flag when faster data loads are preferred over maintaining

columnstore

segment

quality. For example, using this trace flag when loading 1,048,577 rows into a columnstore

might result in more than one compressed rowgroup, if the insert operation is executing in parallel

#### Trace

#### Scope

#### 11561

#### Scope

#### 11631

#### Scope

#### 11634

#### Scope

#### 11953

## Description

mode. Without this trace flag, the insert operation would result in one compressed rowgroup.

: SQL Server 2019 (15.x) and later versions.

: Global only.

Disables Microsoft Entra authentication for replication.

Note

: This trace flag applies to SQL Server 2022 (16.x) CU 6 and later versions.

: Global or session.

An

rowgroup. The default threshold is 10 percent of the maximum row limit (1 million), or of 100,000

rows.

This trace flag changes the threshold to 10 percent of the total current rows in a columnstore

rowgroup.

before this rowgroup is considered for cleanup.

KB5000895.

: SQL Server 2019 (15.x) CU 9 and later versions.

: Global only.

An

clean up the deleted rows in a

rowgroup. The default threshold is 10 percent of the maximum row limit (1 million), or of 100,000

rows.

This trace flag changes the threshold to 1 percent of the total current rows in a columnstore

rowgroup.

rows in a rowgroup, instead of 1 percent of 1 million rows.

KB5000895.

: SQL Server 2019 (15.x) CU 9 and later versions.

: Global only.

## syntax in the

statement.

Note

: Customers must validate Microsoft Entra ID users, because SQL Server doesn't perform this

validation. So, SQL Server doesn't require any

Microsoft Graph permissions. For more information,

see

CREATE USER.

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

allows.

has no effect in this version.

Flow control gates.

: SQL Server 2019 (15.x) CU 9, SQL Server 2017 (14.x) CU 18, SQL Server 2016 (13.x) SP 1

CU 16, and later versions.

: Global only.

Resolves an issue introduced with changes to the link feature for Azure SQL Managed Instance,

which prevents availability groups from synchronizing when replicas are running on different

cumulative updates.

KB5024276.

: SQL Server 2019 (15.x) CU 20 and later versions.

: Global only.

asynchronous page request dispatching feature

encountering undo-of-redo delays from network latency.

mechanism to the default behavior.

: SQL Server 2025 (17.x)

: Global only.

field of audit records.

KB5022375.

: SQL Server 2022 (16.x) CU 1 and later versions.

: Global only.

Disables external authorization policies for on-premises SQL Server instances.

: SQL Server 2022 (16.x) CU 5 and later versions.

: Global only.

Enables the automatic plan correction (APC) model of the automatic tuning feature to perform

multiple consecutive plan regression checks over the same plan, which allows for the accumulation

of additional statistics for evaluation by the new model.

KB5026717.

: SQL Server 2022 (16.x) CU 4 and later versions.

#### Trace

#### Scope

#### 12656

#### Scope

#### 13116

#### Scope

#### 13127

#### Scope

#### 13156

#### Scope

#### 13702

#### Scope

#### 15005

#### Scope

## Description

: Global only.

Enables the automatic plan correction (APC) model of the automatic tuning feature to use a time-

based plan regression check that occurs five minutes after a plan change is detected, which avoids

biasing the regression checks by queries that execute quickly. This allows APC to take into account

query executions that might run longer, or are prone to timing out because of a plan change. For

KB5026717.

: SQL Server 2022 (16.x) CU 4 and later versions.

: Global only.

13685819. Use this trace flag if after you apply SQL Server 2016 (13.x)

parallel plans can't complete any execution and encounter HP_SPOOL_BARRIER waits.

: SQL Server 2016 (13.x) Service Pack 2 CU 16.

: Global only.

Enables additional string pattern matching optimizations.

high performance workloads.

: Global or session.

cause a non-yielding scheduler error" issue. This original fix might sometimes cause a performance

regression.

KB4538581.

: Global only.

Enables PolyBase capabilities for SQL Server on Linux.

required to support the PolyBase feature.

: SQL Server 2022 (16.x) on Linux.

: Global only.

availability group or other scenarios.

: SQL Server 2022 (16.x) CU 20 and later versions.

: Global only.

#### Trace

#### 15025

#### Scope

#### 15096

#### Scope

#### 15097

#### Scope

#### 15212

#### Scope

#### 15608

#### Scope

#### 15915

## Description

allows high-volume customer workloads to continue without interruption.

doesn't contact Azure Key Vault during the creation of the VLF.

FIX:

Database accessibility issues with high-volume customer workloads that use EKM for encryption

and key generation.

: SQL Server 2019 (15.x) CU 19, SQL Server 2022 (16.x) CU 1, and later versions.

: Global only.

Disable population count (popcnt) operations with AVX-512 instruction sets.

: SQL Server 2022 (16.x) and later versions.

: Global or session.

Enables AVX-512 support for SQL Server 2022 (16.x) and later versions.

Important

: Enable AVX-512 support for the following CPUs:

: SQL Server 2022 (16.x) and later versions.

: Global or session.

Disables Service Broker timer messages that are acting as a verbose notification on the timeout

event. Messages affected with this trace flag are:

in

Service Broker Dialog Close sequence.

informal messages is skipped.

: SQL Server 2022 (16.x) and later versions.

: Global only.

Disables

Persisted statistics for readable secondary replicas

feature. To fully disable the feature,

apply this trace flag to the primary replica and all secondary replicas.

: SQL Server 2025 (17.x) and later versions.

: Startup only.

is called frequently

from multiple connections, which could cause a memory leak.

#### Trace

#### Scope

#### 16268

#### Scope

#### 16301

#### Scope

#### 17600

#### Scope

## Description

you restart the SQL Server service.

: SQL Server 2019 (15.x) CU 29 and later versions.

: Global only.

REGEXP_LIKE.

: SQL Server 2025 (17.x) and later versions.

: Global only.

stored procedure.

helps the availability group avoid restart and failover when there's a long delay in the I/O system.

: SQL Server 2019 (15.x) CU 26, SQL Server 2022 (16.x) CU 12, and later versions.

: Global only.

v18.

options of the OLE DB 19 driver. In SQL Server 2025 (17.x), MSOLEDBSQL is set to OLE DB v19.

Using this trace flag sets MSOLEDBSQL to OLE DB v18.

Microsoft OLE DB Driver for SQL Server.

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
