---
name: "Examples: Rowstore indexes"
title: "Examples: Rowstore indexes"
category: "statements"
description: "This sample removes the archive compression, and only uses columnstore compression."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## A. Rebuild an index

## B. Rebuild all indexes on a table and specify options

This sample removes the archive compression, and only uses columnstore compression.

The following example rebuilds a single index on the

table in the

database.

The following example specifies the keyword. This rebuilds all indexes associated with the

table

in the

database. Three options are specified.

The following example adds the ONLINE option including the low priority lock option, and

adds the row compression option.

: SQL Server 2014 (12.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

## C. Reorganize an index with LOB compaction

## D. Set options on an index

## E. Disable an index

The following example reorganizes a single clustered index in the

database. Because the index contains a LOB data type in the leaf level, the statement also

compacts all pages that contain the large object data. Specifying the

option isn't required because the default value is ON.

The following example sets several options on the index

in the

database.

The following example disables a nonclustered index on the

table in the

database.

## F. Disable constraints

## G. Enable constraints

## H. Rebuild a partitioned index

The following example disables a

constraint by disabling the

index in

the

database. The

constraint on the underlying table is

automatically disabled and warning message is displayed.

The result set returns this warning message.

Output

The following example enables the

and

constraints that were

disabled in Example F.

The

constraint is enabled by rebuilding the

index.

The

constraint is then enabled.

### Applies to

### Applies to

## I. Change the compression setting of an index

## J. Change the setting of an index with XML compression

The following example rebuilds a single partition, partition number

, of the partitioned index

in the

database. Partition 5 is

rebuilt with

and the 10 minutes wait time for the low priority lock applies separately

to every lock acquired by index rebuild operation. If during this time the lock can't be obtained

to complete index rebuild, the rebuild operation statement itself is aborted, due to.

: SQL Server 2014 (12.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

The following example rebuilds an index on a nonpartitioned rowstore table.

: SQL Server 2022 (16.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance.

The following example rebuilds an index on a nonpartitioned rowstore table.

### Applies to

## K. Online resumable index rebuild

For more data compression examples, see

Data compression.

: SQL Server 2017 (14.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

The following examples show how to use online resumable index rebuild.

Execute an online index rebuild as resumable operation with. Executing the same

command again after an index operation was paused, automatically resumes the index rebuild

operation.

Execute an online index rebuild as resumable operation with

set to 240 minutes.

Pause a running resumable online index rebuild.

Resume an online index rebuild for an index rebuild that was executed as resumable operation

specifying a new value for

set to 4.

Resume an online index rebuild operation for an index online rebuild that was executed as

resumable. Set

to 2, set the execution time for the index being running as resumable to

240 minutes, and if an index is being blocked on the lock, wait 10 minutes and after that kill all

blockers.

Abort resumable index rebuild operation that is running or paused.

Index architecture and design guide

Perform index operations online

CREATE INDEX (Transact-SQL)

CREATE SPATIAL INDEX (Transact-SQL)

CREATE XML INDEX (Transact-SQL)

DROP INDEX (Transact-SQL)

Disable indexes and constraints

XML indexes (SQL Server)

Optimize index maintenance to improve query performance and reduce resource

consumption

sys.dm_db_index_physical_stats (Transact-SQL)

EVENTDATA (Transact-SQL)
